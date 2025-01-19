from django.db import models

# Create your models here.
class StatesInfo(models.Model):
      state_name = models.CharField(max_length=150)
      city_name = models.CharField(max_length=150)
      population_no  = models.CharField(max_length=150)

      def __str__(self):
          return f"{self.state_name}, {self.city_name} - Population: {self.population_no}"