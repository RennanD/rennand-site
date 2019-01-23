from django.db import models

# Create your models here.

class Person(models.Model):
	nome = models.CharField(max_length=200)
	skills = models.CharField(max_length=200)
	bio = models.TextField()
	face = models.CharField(max_length=250)
	insta = models.CharField(max_length=250)
	foto = models.ImageField(blank = True)
	email = models.CharField(max_length=250, default = '')
	fone = models.CharField(max_length=250, default = '')

	def __str__(self):
		return self.nome

class Project(models.Model):
	titulo = models.CharField(max_length=200)
	desc = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	capa = models.ImageField()
	
	def __str__(self):
		return self.titulo	