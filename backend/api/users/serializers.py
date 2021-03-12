from django.db.utils import IntegrityError
from rest_framework import serializers

from users.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "is_active",
            "is_staff",
            "date_joined",
            "last_login",
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }
    
    def validate_username(self, value):
        if len(value.split(" ")) > 1:
            raise serializers.ValidationError("Invalid username")
        return value.lower()


    def save(self):
        username = self.validated_data.get("username", None)
        email = self.validated_data.get("email", None)
        password = self.validated_data.get("password", None)
        password2 = self.validated_data.get("password2", None)

        if username and email:
            try:
                user = User.objects.create(username=username, email=email)
                if password == password2:
                    user.set_password(password2)
                    user.save()
            except IntegrityError:
                raise serializers.ValidationError("username or email is already exist")
        return serializers.ValidationError("username and email are required.")
