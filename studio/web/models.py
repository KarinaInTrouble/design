from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Common Models
class DesignCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Категории дизайна'

class Feedback(models.Model):
    fullname = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.subject}"
    
    class Meta:
        verbose_name_plural = 'Обратная связь'
    

# Client

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.ForeignKey(DesignCategory, on_delete=models.CASCADE)
    project_description = models.TextField()
    attachment = models.FileField(upload_to='attachments/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.category.name} Request"
    
    class Meta:
        verbose_name_plural = 'Заявки'

# Manager

class Executor(models.Model):
    fullname = models.CharField(max_length=100)
    photo = models.FileField(upload_to='photo/')
    bio = models.TextField()
    skills = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name_plural = 'Исполнитель'

class ClientOrder(models.Model):
    client = models.ForeignKey(Request, on_delete=models.CASCADE)
    assigned_executor = models.ForeignKey(Executor, on_delete=models.CASCADE, null=True, blank=True)
    status_choices = [
        ('assigned', 'Назначен'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='assigned')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.client.fullname} - {self.status}"
    
    class Meta:
        verbose_name_plural = 'Обработка заявок'


