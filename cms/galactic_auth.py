from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import PBKDF2PasswordHasher

from cms.models import GalacticUser


class FixedPBKDF2Hasher(PBKDF2PasswordHasher):
    """
    Override PBKDF2PasswordHasher to use a fixed salt value.
    """

    iterations = 100000
    _fixed_salt = "saltsaltsaltsalt"

    def encode(self, password, salt=None, iterations=None):
        return super().encode(password, self._fixed_salt, self.iterations)


class GalacticAuthBackend(BaseBackend):
    """
    Authenticate using `GalacticUser.galactic_id`
    """

    def authenticate(self, request, token=None):
        if token is None:
            return None

        hashed_galactic_id = FixedPBKDF2Hasher().encode(token, salt=None)
        try:
            return GalacticUser.objects.get(galactic_id=hashed_galactic_id)
        except GalacticUser.DoesNotExist:
            return None

    def get_user(self, galactic_id):
        hashed_galactic_id = FixedPBKDF2Hasher().encode(galactic_id, salt=None)
        try:
            return GalacticUser.objects.get(galactic_id=hashed_galactic_id)
        except GalacticUser.DoesNotExist:
            return None
