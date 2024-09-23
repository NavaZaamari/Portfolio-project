from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from . import serializers
from ...models import User, Profile
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from mail_templated import EmailMessage
from .utils import MyThread
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.conf import settings
from rest_framework.views import APIView


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = serializers.RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            data = {"email": email}
            user_obj = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage(
                "email/activation.tpl", {"token": token}, "nava@gmail.com", to=[email]
            )
            MyThread(email_obj).start()
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {"access": str(refresh.access_token)}


class ChangePasswordAPIView(generics.GenericAPIView):
    model = User
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, request):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.obj = self.get_object(request)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.obj.set_password(serializer.data.get("new_password"))
            self.obj.save()
            return Response(
                {"detail": "Password has been updated successfully."},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(self.queryset, user=self.request.user)


class ActivationView(APIView):
    def get(self, request, token):
        try:
            token = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"])
            user_id = token.get("user_id")
        except jwt.ExpiredSignatureError:
            return Response(
                {"error": "Token expired"}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.InvalidSignatureError:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )
        user_obj = User.objects.get(pk=user_id)
        user_obj.is_verified = True
        user_obj.is_active = True
        user_obj.save()
        return Response(
            {"detail": "Account activated successfully."}, status=status.HTTP_200_OK
        )


class ActivationResendView(generics.GenericAPIView):
    serializer_class = serializers.ActivationResendSerializer

    def post(self, request):
        serializer = serializers.ActivationResendSerializer(data=request.data)
        if serializer.is_valid():
            user_obj = serializer.validated_data["user"]
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage(
                "email/activation.tpl",
                {"token": token},
                "nava@gmail.com",
                to=[user_obj.email],
            )
            MyThread(email_obj).start()
            return Response(
                {"details": "email has been sent succesfully!"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {"access": str(refresh.access_token)}
