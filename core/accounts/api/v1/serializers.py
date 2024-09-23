from ...models import User, Profile
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=225)

    class Meta:
        model = User
        fields = ["email", "password", "password1"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password1"]:
            raise serializers.ValidationError({"detail": "Passwords must match."})

        try:
            validate_password(attrs.get("password"))
        except ValidationError as e:
            raise serializers.ValidationError({"detail": list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1", None)
        return User.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(max_length=225)
    new_password = serializers.CharField(max_length=225)
    confirm_password = serializers.CharField(max_length=225)

    class Meta:
        model = User
        fields = ["old_password", "new_password", "confirm_password"]

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"detail": "Passwords must match."})

        try:
            validate_password(attrs.get("new_password"))
        except serializers.ValidationError as e:
            raise serializers.ValidationError({"detail": list(e.messages)})

        user = self.context["request"].user
        if not user.check_password(attrs["old_password"]):
            raise serializers.ValidationError({"detail": "Old password is incorrect."})

        return super().validate(attrs)


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "email", "first_name", "last_name", "bio", "image"]


class ActivationResendSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs["email"]
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"detail": "User with this email does not exist."}
            )
        attrs["user"] = user_obj
        return super().validiate(attrs)
