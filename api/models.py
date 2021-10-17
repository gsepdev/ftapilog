from django.db import models

# Create your models here.




class Category1(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Expense(models.Model):
    METHOD_PAYMENT = (
    ('CD',"Card"),
    ('CH', "Cash")
)

    description=models.CharField(max_length=200)
    amount= models.FloatField()
    category = models.ForeignKey(Category1, on_delete=models.CASCADE,null=True)

    payment_date= models.DateTimeField(blank=True, null=True)
    created_on= models.DateTimeField(auto_now_add=True)
    last_modified= models.DateTimeField(auto_now=True)
    method_payment= models.CharField(max_length=9, choices=METHOD_PAYMENT, default="CD")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.description
