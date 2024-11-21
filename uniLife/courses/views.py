from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Keyword
from .forms import CourseForm, KeywordForm

# Ana sayfa: Tüm derslerin listesi
def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

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
    courses = Course.objects.all()
    course_id = request.GET.get('course')
    if course_id:
        keywords = keywords.filter(course_id=course_id)
    return render(request, 'courses/keyword_list.html', {'keywords': keywords, 'courses': courses})

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
