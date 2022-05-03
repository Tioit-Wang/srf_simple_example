from srf import ModelViewSet

from models import UserModel
from serializers import UserSerializer


class TestView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel
    search_fields = ('@question',)
