from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Keyword, Category, Tag
from .forms import CourseForm, KeywordForm
from .filters import KeywordFilter

# Ana sayfa: Tüm derslerin listesi
# views.py

from django.shortcuts import render
from .models import Course, Category, Tag

def index(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    # Filtreleme
    category_id = request.GET.get('category')
    tag_id = request.GET.get('tag')

    if category_id:
        courses = courses.filter(categories__id=category_id)
    if tag_id:
        courses = courses.filter(tags__id=tag_id)

    return render(request, 'courses/index.html', {'courses': courses, 'categories': categories, 'tags': tags})


# Ders ekleme
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})

# Ders detay sayfası
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

# Ders düzenleme
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form})

# Ders silme
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('index')
    return render(request, 'courses/course_delete.html', {'course': course})

# Anahtar kelime ekleme
def keyword_create(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('keyword_list')
    else:
        form = KeywordForm()
    return render(request, 'courses/keyword_form.html', {'form': form})

# Anahtar kelime listesi
def keyword_list(request):
    keywords = Keyword.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    # Filtreleme
    tag_id = request.GET.get('tag')
    
    if tag_id:
        keywords = keywords.filter(tags__id=tag_id)

    return render(request, 'courses/keyword_list.html', {'keywords': keywords, 'tags': tags})

# Anahtar kelime düzenleme
def keyword_edit(request, pk):
    keyword = get_object_or_404(Keyword, pk=pk)
    if request.method == 'POST':
        form = KeywordForm(request.POST, request.FILES, instance=keyword)
        if form.is_valid():
            form.save()
            return redirect('keyword_list')
    else:
        form = KeywordForm(instance=keyword)
    return render(request, 'courses/keyword_form.html', {'form': form})

# Anahtar kelime silme
def keyword_delete(request, pk):
    keyword = get_object_or_404(Keyword, pk=pk)
    if request.method == 'POST':
        keyword.delete()
        return redirect('keyword_list')
    return render(request, 'courses/keyword_delete.html', {'keyword': keyword})

def keyword_image_detail(request, pk):
    keyword = get_object_or_404(Keyword, pk=pk)
    return render(request, 'courses/keyword_image_detail.html', {'keyword': keyword})

def keyword_detail(request, pk):
    keyword = get_object_or_404(Keyword, pk=pk)
    return render(request, 'courses/keyword_detail.html', {'keyword': keyword})
