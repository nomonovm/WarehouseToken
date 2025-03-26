from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError


class MahsulotSerializer(ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = "__all__"


class SotuvSerializer(ModelSerializer):
    class Meta:
        model = Sotuv
        fields = "__all__"

    def validate(self, data):
        mijoz = data.get('mijoz')
        if mijoz.qarz > 500000:
            raise ValidationError({"qarz": "Mahsulot olib ketishingiz mumkin emas, qarzingiz 500,000 so'mdan ko'p."})
        return data


class SotuvchiSerializer(ModelSerializer):
    class Meta:
        model = Sotuvchi
        fields = "__all__"


class MijozSerializer(ModelSerializer):
    class Meta:
        model = Mijoz
        fields = "__all__"


class BolimSerializer(ModelSerializer):
    class Meta:
        model = Bolim
        fields = "__all__"
