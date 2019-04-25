"""Defines the controller for generating refresh tokens"""
import json
from uuid import uuid4

from pylons import app_globals as g
from pylons import request

from r2.controllers import add_controller
from r2.controllers.reddit_base import MinimalController
from r2.controllers.oauth2 import OAuth2AccessController
from r2.lib.db.thing import NotFound
from r2.models.account import (
    Account,
    register,
)
from r2.models.subreddit import Subreddit
from r2.models.token import (
    OAuth2Client,
    OAuth2AccessToken,
    OAuth2RefreshToken,
    OAuth2Scope,
)


@add_controller
class RefreshTokenController(MinimalController):
    """The controller for generating refresh tokens"""
    def GET_refresh_token(self, *args, **kwargs):  # pylint: disable=unused-argument
        """Generate a refresh token given a username"""
        username = request.GET['username']
        try:
            account = Account._by_name(username)
        except NotFound:
            account = register(username, uuid4().hex, '127.0.0.1')

        # subscribe the user now because reddit does not have consistency across
        # its APIs on what it considers the user to be subscribed to
        if not account.has_subscribed:
            Subreddit.subscribe_defaults(account)
            account.has_subscribed = True
            account._commit()

        client_id = g.secrets['generate_refresh_token_client_id']
        client = OAuth2Client.get_token(client_id)
        scope = OAuth2Scope(OAuth2Scope.FULL_ACCESS)
        user_id = account._id36
        refresh_token = OAuth2RefreshToken._new(
            client_id=client._id,
            user_id=user_id,
            scope=scope,
        )
        access_token = OAuth2AccessToken._new(
            client_id=client._id,
            user_id=user_id,
            scope=scope,
            device_id='device',
        )
        return json.dumps(OAuth2AccessController._make_new_token_response(access_token, refresh_token))
