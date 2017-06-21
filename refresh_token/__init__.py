__version__ = "0.0.3"

from r2.lib.plugin import Plugin
from r2.lib.configparse import ConfigValue
from r2.lib.js import Module
from r2.config.routing import not_in_sr


class RefreshToken(Plugin):
    needs_static_build = False

    def add_routes(self, mc):
        mc('/api/v1/generate_refresh_token', controller='refreshtoken', action='refresh_token')

    def load_controllers(self):
        from refresh_token.controller import RefreshTokenController
