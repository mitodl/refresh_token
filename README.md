# refresh_token
Plugin for reddit to generate OAuth refresh tokens for a particular user given a username.
If the user does not exist a new user is created. Essentially this lets anonymous users log in as anyone they want,
with no scope limitations.

**Warning**: This plugin opens a giant security hole. Please do not use it unless you know what you are doing.

## Installation
TBD

## Usage
The plugin exposes an endpoint at `/api/v1/generate_refresh_token?username=<user>`. It returns a JSON dict like this:

    {
        "access_token": "52-pq61YqdqakZaKbYwl8TsADma2HU",
        "expires_in": 3600,
        "token_type": "bearer",
        "scope": "*",
        "refresh_token": "52-3S5VMvq39W4qrueZbl_yCpMzqWg",
        "device_id": "device"
    }

Each time the endpoint is accessed it will create a new refresh token and a new access token.
