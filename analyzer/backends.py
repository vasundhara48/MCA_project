from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(email=username).first()
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None