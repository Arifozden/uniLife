from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.ManyToManyField(Category, blank=True)  # Kategorileri ilişkilendirdik
    tags = models.ManyToManyField(Tag, blank=True)  # Etiketleri ilişkilendirdik
    learned = models.TextField(blank=True, null=True)
    images = models.ImageField(upload_to='course_images/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Keyword(models.Model):
    word = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='keywords')
    english = models.CharField(max_length=100)
    turkish = models.CharField(max_length=100)
    norwegian = models.CharField(max_length=100)
    image = models.ImageField(upload_to='keyword_images/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)  # Anahtar kelimelere etiketleri ilişkilendirdik
    

    def __str__(self):
        return f"{self.english} ({self.course.name})"
