from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers, generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def create(self, validated_data):
        user = User()
        user.username = validated_data['username']
        user.email = validated_data['email']
        user.password = make_password(validated_data['password'])
        user.is_active = True
        user.save()
        authenticate(username=validated_data['username'], password=validated_data['password'])
        return validated_data

class LoginSerialize(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_email(self, email, password):
        user = None
        if email and password:
            user = self.authenticate(email=email, password=password)
        else:
            msg = _('user name dan password harus cocok')
            raise exception.ValidateError(msg)

        return user

    def _validate_username(self, username, password):
        user = None

        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)
        return user

class ListUserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


# apiView

class RegisterApiView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

class LoginApiView(generics.CreateAPIView):
    serializer_class = LoginSerialize
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        if user:
            token = RefreshToken.for_user(user)
            response = {}
            response['username'] = user.username
            response['access_token'] = str(token.access_token)
            response['refresh_token'] = str(token)
            return Response(response)
        else:
            response = {}
            response['error'] = "username dan password salah"
            return Response(response)

class ListUserApiiew(generics.ListAPIView):
    serializer_class = ListUserSerialize
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    