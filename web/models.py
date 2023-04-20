from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
    
class Subscribe(models.Model):
    first_name= models.CharField(max_length=20)   
    last_name= models.CharField(max_length=20) 
    email= models.EmailField()
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
