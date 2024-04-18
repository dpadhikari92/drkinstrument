from .forms import BlogPostForm
from .models import BlogPost
from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactMessage
from .forms import ContactForm
from .forms import ContactForm  # Import your ContactForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from math import ceil
from django.shortcuts import redirect, render
from .models import ContactMessage, Product
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def index(request):
    current_user = request.user
    print(current_user)
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4)-(n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}

    return render(request, "index.html", params)


# views.py


# views.py


# views.py


def contact_us(request):
    thank_you_message = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            thank_you_message = "Thank you for contacting us! We'll get back to you soon."

    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form, 'thank_you_message': thank_you_message})


def about_us(request):
    return render(request, 'about_us.html')


def product_list(request):
    return render(request, 'product_list.html')


# blog/views.py


def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})


def view_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'view_blog_post.html', {'post': post})
