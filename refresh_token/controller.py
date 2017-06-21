import json
import os
from uuid import uuid4

from pylons import app_globals as g
from pylons import tmpl_context as c
from pylons import request

from r2.controllers import add_controller
from r2.controllers.reddit_base import MinimalController
from r2.controllers.oauth2 import OAuth2AccessController
from r2.lib.db.thing import NotFound
from r2.models.account import (
    Account,
    register,
)
from r2.models.token import (
    OAuth2Client, OAuth2AuthorizationCode, OAuth2AccessToken,
    OAuth2RefreshToken, OAuth2Scope)


@add_controller
class RefreshTokenController(MinimalController):
    def GET_refresh_token(self, *args):
        username = request.GET['username']
        try:
            account = Account._by_name(username)
        except NotFound:
            account = register(username, uuid4().hex, '127.0.0.1')

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
