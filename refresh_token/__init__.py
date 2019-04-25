"""Plugin for generating refresh tokens on reddit"""

from r2.lib.plugin import Plugin


__version__ = "0.0.5"


class RefreshToken(Plugin):
    """Plugin for generating refresh tokens on reddit"""
    needs_static_build = False

    def add_routes(self, mc):
        """Add the refresh token endpoint to the list of reddit endpoints"""
        mc('/api/v1/generate_refresh_token', controller='refreshtoken', action='refresh_token')

    def load_controllers(self):
        """
        Add the controller referenced by the route. reddit uses locals() to get these values
        """
        from refresh_token.controller import RefreshTokenController  # pylint: disable=unused-variable
