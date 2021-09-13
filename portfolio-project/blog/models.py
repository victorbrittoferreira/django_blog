from django.db import models

## try again 

class Blog(models.Model):
    title = models.CharField(max_length= 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    

    # teste
    
    # title name edit
    def __str__(self):
        return self.title
        
    #text body rate
    def summary(self):
        return self.body[:100]
    
    #time format
    def pub_date_pretty(self):
        return self.pub_date.strftime('%I:%M %P %d %b %Y')
    
      



