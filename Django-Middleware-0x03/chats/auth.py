from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    """
    Custom JWT Authentication class that can be extended for additional functionality.
    Currently, it inherits from JWTAuthentication without modifications.
    """
    pass    