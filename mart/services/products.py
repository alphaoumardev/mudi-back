from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from mart.serializers import *


# Here are just for the products
@api_view(['GET', 'POST'])
def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductsModel(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        seriliazer = ProductsModel(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        return Response(seriliazer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def get_one_product(request, pk):
    if request.method == "GET":
        article = Product.objects.get(id=pk)
        seriliazer = ProductsModel(article, many=False)
        return Response(seriliazer.data)
    if request.method == 'PUT':
        article = Product.objects.get(id=pk)
        seriliazer = ProductsModel(instance=article, data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
        return Response(seriliazer.data)
    if request.method == 'DELETE':
        article = Product.objects.get(id=pk)
        article.delete()
        return Response("The note is deleted")


@api_view(["GET"])
def get_pro_by_category(request, pk):
    if request.method == "GET":
        category = Category.objects.get(id=pk)
        variant = Product.objects.filter(category=category).order_by('-id')
        serializer = ProductsModel(variant, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_genre(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreModel(genres, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_one_genre(request, pk):
    if request.method == "GET":
        genres = Genre.objects.get(id=pk)
        serializer = GenreModel(genres, many=False)
        return Response(serializer.data)


@api_view(["GET"])
def get_types(request):
    if request.method == "GET":
        types = Types.objects.all()
        serializer = TypesModel(types, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_one_type(request, pk):
    if request.method == "GET":
        types = Types.objects.get(id=pk)
        serializer = TypesModel(types, many=False)
        return Response(serializer.data)


@api_view(["GET"])
def get_category(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategoryModel(categories, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_one_category(request, pk):
    if request.method == "GET":
        categories = Category.objects.get(id=pk)
        serializer = CategoryModel(categories, many=False)
        return Response(serializer.data)


@api_view(["GET"])
def get_by_genre(request, pk):
    if request.method == "GET":
        categories = Category.objects.filter(genre__id=pk)
        serializer = CategoryModel(categories, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_by_type(request, pk):
    if request.method == "GET":
        categories = Category.objects.filter(type__id=pk)
        serializer = CategoryModel(categories, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_variants(request):
    if request.method == "GET":
        variant = Variant.objects.all()
        serializer = VariantModel(variant, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_one_variant(request, pk):
    if request.method == "GET":
        variant = Variant.objects.filter(product__id=pk)
        serializer = VariantModel(variant, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_futured_images(request, pk):
    if request.method == "GET":
        images = FuturedImages.objects.filter(product__id=pk)
        serializer = FuturedImagesModel(images, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_categories(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreModel(genres, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_category_by_name(request, query=None):
    if request.method == "GET":
        category = Category.objects.filter(genre__genre_name=query)
        serializer = CategoryModel(category, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def get_pro_by_category(request, query=None, name=None):
    if request.method == "GET":
        genre = Category.objects.filter(genre__genre_name=query).filter(type__type_name=name)
        items = Product.objects.filter(category__genre__category__in=genre).filter(category__type__category__in=genre)
        serializer = ProductsModel(items, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_sliders(request):
    if request.method == "GET":
        slide = Sliders.objects.all().order_by("-id")
        items = SlidersModel(slide, many=True)
        return Response(items.data)
