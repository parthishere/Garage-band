from django.db import models

# Create your models here.
# TAG_CHOICES = [
#     ('EN', 'Entertainment'), 
#     ('EN2', 'Entertaintment 2'),
#     ('EN3', 'Entertaintment 3'),
#     ('EN4', 'Entertaintment 4'),
#     ('EN5', 'Entertaintment 5'),
# ]

class Tag(models.Model):
    tag_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.tag_name)