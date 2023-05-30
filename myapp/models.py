from django.db import models

# Create your models here.
class BotUser(models.Model):
    name  = models.CharField(max_length=150,verbose_name="Name",help_text="Enter name",null=True,blank=True)
    telegram_id = models.CharField(max_length=30,verbose_name="Telegram ID",help_text="Enter telegram ID",unique=True)
    language = models.CharField(max_length=4,default='uz',verbose_name="Language",help_text="Enter language")
    phone  = models.CharField(max_length=20,verbose_name="Phone number",help_text="Enter phone number",null=True,blank=True)
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        if self.name:
            return self.name
        else:
            return f"{self.telegram_id} ID foydalanuvchi"
    class Meta:
        db_table = "BotUser"
        verbose_name  =  "BotUser"
        verbose_name_plural = "BotUser"
from main import manzil
class Location(models.Model):
    user = models.ForeignKey(BotUser,on_delete=models.CASCADE,verbose_name="Bot User",to_field='telegram_id')
    latitude = models.CharField(max_length=50,verbose_name="Latitude",null=True,blank=True)
    longitude = models.CharField(max_length=50,verbose_name="Longitude",null=True,blank=True)
    def __str__(self) -> str:
        if self.latitude and self.longitude:
           return manzil(latitude=self.latitude,longitude=self.longitude)
        else:
            return "Manzil"
    class Meta:
        db_table = "Location"
        verbose_name  =  "Location"
        verbose_name_plural = "Locations"
class Category(models.Model):
    name  = models.CharField(max_length=150,verbose_name="Category",help_text="Enter category")
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Category"
        verbose_name  =  "Category"
        verbose_name_plural = "Categories"
class SubCategory(models.Model):
    name = models.CharField(max_length=150,verbose_name="Subcategory",help_text="Enter subcategory")  
    category  = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Category",help_text="Choose category",null=True,blank=True,related_name='subcategory')
    def __str__(self):
        return self.name
    class Meta:
        db_table = "SubCategory"
        verbose_name  =  "SubCategory"
        verbose_name_plural = "SubCategories"
   
from django.utils.html import format_html 

class Product(models.Model):
    name = models.CharField(max_length=150,verbose_name="Product",help_text="Enter product name",null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Category",help_text="Choose category",related_name='products')
    subcategory  = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Subcategory',related_name='products')
    image = models.ImageField(upload_to='my-images',verbose_name="Image",help_text='Upload image',null=True,blank=True)
    about = models.TextField(verbose_name="About",null=True,blank=True)
    price = models.IntegerField(verbose_name="Price",help_text="Enter price",null=True,blank=True)
    discount = models.IntegerField(verbose_name="Discount",help_text="Enter discount",null=True,blank=True)     
    def __str__(self):
        
        if self.name:
            return self.name
        else:
            return 'Mahsulot'
    @property
    def picture(self):
       
          return format_html('<img src="{}" width="50" height="50" style="border-radius:50%"'.format(self.image.url))
    class Meta:
        db_table = "Product"
        verbose_name  =  "Product"
        verbose_name_plural = "Products"
class Order(models.Model):
    user = models.ForeignKey(BotUser,on_delete=models.CASCADE,verbose_name="Bot User",to_field='telegram_id')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        if self.user.name:
           return self.user.name
        else:
            return "Buyurtma"
    @property
    def all_products(self):
        return sum([item.quantity for item in self.items.all()])
    @property
    def all_shop(self):
        return sum([item.shop for item in self.items.all()])
    class Meta:
        db_table = "Order"
        verbose_name  =  "Order"
        verbose_name_plural = "Order"
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="Order",related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="Product")
    quantity = models.IntegerField(default=1,verbose_name="Quantity")
    def __str__(self):
        return 'Xarid'
    @property
    def shop(self):
        if self.product.discount:
          return (self.product.price-self.product.discount) * self.quantity
        else:
            return self.product.price * self.quantity
    @property
    def product_id(self):
        return self.product.id
    class Meta:
        db_table = "OrderItem"
        verbose_name  =  "OrderItem"
        verbose_name_plural = "OrderItems"