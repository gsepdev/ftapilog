from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE, null=True, blank=True)
    expenses = models.ManyToManyField('Expense', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'
    def __str__(self):
       return self.name

METHOD = (
    (0,"Card"),
    (1,"Cash")
)

class Expense(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=200)

    owner = models.ForeignKey('auth.User', related_name='expenses', on_delete=models.CASCADE,blank=True)
    amount= models.FloatField()
    payment_date= models.DateTimeField(blank=True, null=True)
    last_modified= models.DateTimeField(auto_now=True)
    method= models.IntegerField(choices=METHOD, default=0)


    def __str__(self):
        return self.description

    class Meta:
        ordering = ['created']
