from django.db import models

class Player(models.Model):

	POSITIONS = (
		('PG', 'Point Guard'),
		('SG', 'Shooting Guard'),
		('SF', 'Small Forward'),
		('PF', 'Power Forward'),
		('C', 'Center'),
	)

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	position = models.CharField(max_length=2, choices=POSITIONS)
