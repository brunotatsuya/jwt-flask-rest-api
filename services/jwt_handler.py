import os
import jwt
from datetime import datetime, timedelta

def generate_jwt(payload, lifetime=None):
    # Generates a new JWT token, wrapping information provided by payload (dict)
    # Lifetime describes (in minutes) how much time the token will be valid
    if lifetime:
        payload['exp'] = (datetime.now() + timedelta(minutes=lifetime)).timestamp()
    return jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm="HS256")

def decode_jwt(token):
    # Tries to retrieve payload information inside of a existent JWT token (string)
    # Will throw an error if the token is invalid (expired or inconsistent)
    return jwt.decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])