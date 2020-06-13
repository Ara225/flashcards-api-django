from django.db import models
class FlashCard(models.Model):
    front = models.TextField()
    back = models.TextField() 
    flashCard_type = models.CharField(
        max_length=4,
        choices=[
            ("CODE", 'Code'),
            ("TEXT", 'Text')
        ],
        default="TEXT",
    )
    
    def __str__(self):
        return self.name
