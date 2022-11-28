from django.db import models

# Create your models here.
class Bird(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    

class Feeding(models.Model):

    MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
    )

    date = models.DateField()
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])


    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    # To order the data by desc date
    class Meta:
        ordering = ['-date']