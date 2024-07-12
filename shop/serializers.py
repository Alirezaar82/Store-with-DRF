from rest_framework import serializers

from accounts.models import CustomUser

from .models import CategoryModel, CommentModel, ProductModel

class ShopUserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id','full_name']
    def get_full_name(self,user):
        return user.user_profile.get_fullname()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id','name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = ProductModel
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    customer = ShopUserSerializer(read_only=True)
    status = serializers.SerializerMethodField()
    class Meta:
        model = CommentModel
        fields = ['id','customer', 'title','body','status',]

    def create(self, validated_data):
        product_id = self.context['product_pk']
        customer_id = self.context['customer_pk']
        
        new_comment =  CommentModel.objects.create(
            product_id = product_id,
            customer_id = customer_id,
            **validated_data
        )
        self.instance = new_comment
        return new_comment

    def get_status(self,comment):
        return comment.get_status().get('label')