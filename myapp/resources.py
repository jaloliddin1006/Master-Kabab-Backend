from import_export.resources import ModelResource
from .models import Category,Product
class CategoryResource(ModelResource):
    class Meta:
        model = Category
class ProductResource(ModelResource):
    class Meta:
        model = Product