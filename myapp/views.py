from django.shortcuts import render
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    images = Image.objects.all()
    return render(request, 'myapp/home.html', {'images': images, 'form': form})