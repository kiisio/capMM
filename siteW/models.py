# -*- coding: utf-8 -*-

from django.db import models

class stihl(models.Model):
	marque = models.CharField(max_length= 10)
	type = models.CharField(max_length = 30)
	modele = models.CharField(max_length = 20)

class marque(models.Model):
	marque = models.CharField(max_length = 10)
	adresseURL = models.CharField(max_length = 500)
	
	
