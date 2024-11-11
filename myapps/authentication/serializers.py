from myapps.authentication.models import UserCustomize
from rest_framework import serializers
# from .models import

class UserCustomizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomize
        fields = ["id", "email", "password"]
    # username = serializers.CharField(
    #     required=True,
    #     error_messages={
    #         'blank': "El nombre de usuario no puede estar vacío.",
    #         'required': "El nombre de usuario es obligatorio."
    #     }
    # )
    email = serializers.CharField(
        required=True,
        error_messages={
            'blank': "El email del usuario no puede estar vacío.",
            'required': "El email del usuario es obligatorio."
        }
    )
    password = serializers.CharField(
        write_only=True,
        required = True,
        error_messages = {
            'blank': "El campo contraseña no puede estar vacío.",
            'required': "La contraseña es obligatoria."
        }
    )

        # }

    def create(self, validated_data):
        # print(validated_data)
        user = UserCustomize.objects.create_user(validated_data['email'], validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    # def validate_username(self, value):
    #     if UserCustomize.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("Este nombre de usuario ya se encuentra registrado.")
    #     return value
    # def validate(self, data):
    #     if not data.get('email') or data.get('email').strip() == '':
    #         raise serializers.ValidationError({"email": "El email no puede estar en blanco."})
    #     if not data.get('username') or data.get('username').strip() == '':
    #         raise serializers.ValidationError({"username": "El nombre de usuario no puede estar en blanco."})
    #     if not data.get('password') or data.get('password').strip() == '':
    #         raise serializers.ValidationError({"password": "La contraseña no puede estar en blanco."})
    #     return data

    # def validate_email(self, value):
    #     if UserCustomize.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("El email ya se encuentra registrado")
    #     return value

    # def validate_username(self, value):
    #     if User.objects.filter(username=value).exists():
    #         raise serializers.ValidationError("Este nombre de usuario ya se encuentra registrado.")
    #     return value
        # extra_kwargs = {"password": {"max_length": 20, "min_length": 5}}
        #
        # def create(self, validated_data):
        #     user = User.objects.create_user(
        #         email=validated_data["email"],
        #         password=validated_data["password"],
        #         username=validated_data["username"]
        #     )
        #     return user
