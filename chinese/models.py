from django.db import models


class Product (models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()

    image = models.ImageField(upload_to="shop/images", default=" ")

    def __str__(self):
        return self.product_name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    phone_no = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
