from djoser.serializers import UserSerializer as DjoserUserSerializer
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer


class UserSerializer(DjoserUserSerializer):
    class Meta(DjoserUserSerializer):
        fields = ['id','phone_number','email']


class UserCreateSerializer(DjoserUserCreateSerializer):
    class Meta(DjoserUserCreateSerializer):
        fields = ['id','phone_number','password','email']


    
