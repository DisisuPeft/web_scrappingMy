from myapps.scrapping.models import URLs
from myapps.scrapping.models import PriceProduct
from rest_framework import serializers
# from .models import

class URLsSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLs
        fields = ["url", "article"]
    # username = serializers.CharField(
    #     required=True,
    #     error_messages={
    #         'blank': "El nombre de usuario no puede estar vacío.",
    #         'required': "El nombre de usuario es obligatorio."
    #     }
    # )

        # }

    def create(self, validated_data):
        # print(validated_data)
        article = URLs.objects.create(
            url=validated_data['url'],
            article=validated_data['article']
        )
        article.save()
        return article


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


class PriceProductSerializer(serializers.ModelSerializer):

    url_id = serializers.PrimaryKeyRelatedField(queryset=URLs.objects.all(), source='URLs_id')

    class Meta:
        model = PriceProduct
        fields = ["price"]

    def create(self, validated_data):
        instance = validated_data.pop('url_id')
        price = PriceProduct.objects.create(price=validated_data['price'],
                                            URLs_id=instance)
        return price