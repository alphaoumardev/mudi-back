from django.urls import path
from .services import products

urlpatterns = [
    # The product
    path('all/', products.get_products, name='product'),
    path('one/<str:pk>', products.get_one_product, name='one'),
    path('probycategory/<str:query>', products.get_pro_by_category, name='pro'),

    # The categories
    path('genres/', products.get_genre, name='genres'),
    path('genre/<str:pk>', products.get_one_genre, name='one_genre'),

    path('types/', products.get_types, name='types'),
    path('type/<str:pk>', products.get_one_type, name='one_type'),

    path('category/', products.get_category, name='cate'),
    path('category/<str:pk>', products.get_one_category, name='one_cate'),
    path('bygenre/<str:pk>', products.get_by_genre, name='bygenre'),
    path('bytype/<str:pk>', products.get_by_type, name='bytype'),

    # The variants
    path('variants/', products.get_variants, name='variants'),
    path('byvariant/<str:pk>', products.get_one_variant, name='byvariant'),

    path('catename/', products.get_categories, name='categories_list'),
    path('catename/<str:query>', products.get_category_by_name, name='details'),
    path('catename/<str:query>/<str:name>', products.get_pro_by_category, name='pro'),

    path('images/<str:pk>', products.get_futured_images, name="images"),

    path('sliders/', products.get_sliders, name="sliders"),

]
