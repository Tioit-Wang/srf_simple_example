from srf import fields
from srf.serializers import ModelSerializer, Serializer

from models import UserModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        read_only_fields = ('id',)


class CoverNameUserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        read_only_fields = ('id',)

    # async or sync depend on you
    async def output_name(self, value, data):
        print(value, data)
        return 'This new name'

    def output_id(self, value, data):
        print(value, data)
        return 'i am id'


class SimpleSerializer(Serializer):
    name = fields.CharField()
    age = fields.IntegerField()
    gender = fields.ChoiceField(choices=((1, 'man'), (2, 'woman')))

    # don't need MetaClass, unlike DRF
    # you can use more field

    # ('empty', 'SkipField', 'Field', 'CharField', 'IntegerField', 'FloatField', 'DecimalField', 'BooleanField',
    # 'DateTimeField', 'DateField', 'TimeField', 'ChoiceField', 'EnumChoiceField', 'SerializerMethodField')
