import requests
import grpc

# Keycloak settings
KEYCLOAK_URL = 'http://localhost:8080'
CLIENT_ID = 'myclient'
CLIENT_SECRET = 'CM5J5Cy0Jeqx1lgYAZGIMVOl1B8XaSFC'
REALM_NAME = 'myrealm'

# Function to validate token with Keycloak
def validate_token(access_token):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'token': access_token
    }

    response = requests.post(
        f'{KEYCLOAK_URL}/realms/{REALM_NAME}/protocol/openid-connect/token/introspect', headers=headers, data=data)
    
    return response.json()["active"]



def authenticate(context):
    # Extract access token from metadata
    metadata = dict(context.invocation_metadata())
    access_token = metadata.get('authorization').split(" ")[1]
    # Validate token with Keycloak
    if not validate_token(access_token):
        context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Invalid token')
