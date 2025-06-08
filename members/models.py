from django.db import models

class member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    


