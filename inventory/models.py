from django.db import models

# Create your models here.
class phone(models.Model):
    idno = models.IntegerField()
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    ram = models.IntegerField()
    storage = models.IntegerField()
    price = models.IntegerField()
    # stock_qty = models.IntegerField()
    choice = (
    ('AVAILABLE ','Item Ready to be Sold'),
    ('SOLD','Item Soldout'),
    ('RESTOCKING','Item will be Restocked in a few Days')
    )
    availibility = models.CharField(choices=choice,default="AVAILABLE",max_length=50)

    # class Meta:
    #     abstract = True 
    def __str__(self):
        return 'Name : {0} Brand : {1} Price: {2}'.format(self.name,self.brand,self.price) 
