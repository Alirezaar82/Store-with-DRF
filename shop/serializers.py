from rest_framework import serializers

from .models import CategoryModel, CommentModel, ProductModel

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
    status = serializers.SerializerMethodField()
    class Meta:
        model = CommentModel
        fields = ['id', 'title','body','status',]

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