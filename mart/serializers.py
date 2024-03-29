from rest_framework import serializers
from .entity.orders_entity import *
from .entity.products_entity import *
from .entity.customers_entity import *


class CustomerModel(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'


class GenreModel(serializers.ModelSerializer):
    class Meta:
        model = Genre
        # fields = ['genre_name']
        fields = '__all__'

class TypesModel(serializers.ModelSerializer):
    class Meta:
        model = Types
        # fields = ['type_name']
        fields = '__all__'

class CategoryModel(serializers.ModelSerializer):
    genre = GenreModel(many=False, read_only=True)
    type = TypesModel(many=False, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'genre', 'type']
        # fields = '__all__'

class ProductsModel(serializers.ModelSerializer):
    category = CategoryModel(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "sku", "category", "image", "image_hover",
                  "description", "brand", "price", "status", "stock", "quantity",
                  "onsale", "created_at", "updated_at", "deleted_at",]
        # fields  = '__all__'

class ColorsOptionModel(serializers.ModelSerializer):
    class Meta:
        model = ColorsOption
        fields = '__all__'

class TagModel(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

class SizesOptionModel(serializers.ModelSerializer):
    class Meta:
        model = SizesOption
        fields = '__all__'

class FuturedImagesModel(serializers.ModelSerializer):
    product = ProductsModel(many=False, read_only=True)
    class Meta:
        model = FuturedImages
        fields = ['id', 'image_url', 'product']

class VariantModel(serializers.ModelSerializer):
    product = ProductsModel(many=False, read_only=True)
    color = ColorsOptionModel(many=False, read_only=True)
    size = SizesOptionModel(many=False, read_only=True)

    class Meta:
        model = Variant
        fields = ['id', 'product', 'color','size']

class WishListModel(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

class SlidersModel(serializers.ModelSerializer):
    product = ProductsModel(many=False, read_only=True)
    class Meta:
        model = Sliders
        fields = ['product']

class CommentsModel(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class CartItemModel(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class OrderDetailsModel(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'


class PaymentDetailsModel(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'


class UserPayModel(serializers.ModelSerializer):
    class Meta:
        model = UserPay
        fields = '__all__'












