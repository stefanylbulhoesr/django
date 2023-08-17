from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name  #faz mostrar o nome da categoria ao inves do indice


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165) #caracteres
    slug = models.SlugField() #
    preparation_time = models.IntegerField() #numero inteiro
    preparation_time_unit = models.CharField(max_length=165)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=165)
    preparation_steps = models.TextField() #campo de texto livre
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) #campo dia e hora o auto_now_add no momento da criação gera uma data
    updated_at = models.DateTimeField(auto_now=True) #o auto_now atualiza o campo
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None) #precisa do paremetro para onde vai (category) e o on delete define o que vai acontecer caso a categoria seja deletada, nesse caso, será nula e, para isso, precisamos do null=True
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #aqui está usando o import de User para adicionar os usuários ao banco 


    def __str__(self):
        return self.title