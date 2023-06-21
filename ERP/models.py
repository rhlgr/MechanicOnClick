from django.db import models
import uuid
from account.models import Customer , Employee
from Franchise.models import Center
import datetime
# Create your models here.

class Vehical(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    number = models.CharField(max_length=20 , unique= True , blank=False , null= False)
    type = models.CharField(max_length=20)
    def save(self,*args , **kwargs):
        self.number = self.number.upper()
        return super().save(*args , **kwargs)
    def __str__(self) -> str:
        return self.number
class ProvidedService():
    pass
class CenterServices(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400, default="Diam dolor diam ipsum sit amet diam et eos erat ipsum")
    price = models.IntegerField(default=500)
    center = models.ForeignKey(Center,on_delete= models.CASCADE)
    tax = models.FloatField(default=5)
    def __str__(self) -> str:
        return str(self.name) + ' - ' + str(self.center) + '- ' + str(self.price)
    
class CenterProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400, default="Diam dolor diam ipsum sit amet diam et eos erat ipsum")
    purchase_price = models.IntegerField(default=300)
    price = models.IntegerField(default=500)
    center = models.ForeignKey(Center,on_delete= models.CASCADE)
    serial_number = models.CharField(max_length=50 , unique=True)
    tax = models.FloatField(default=5)
    stock = models.IntegerField(default=0)
    def __str__(self) -> str:
        return str(self.name) + ' - '  + str(self.price)
    
    def save(self, *args , **kwargs):
       if self.serial_number is None:

            if CenterProduct.objects.filter(center = self.center).exists():
                
                last = CenterProduct.objects.filter(center = self.center).latest('id')
                n=  int(last.serial_number[:-(len(str(self.center.code))+1)])
                n +=1
                self.serial_number = str(n) +'-' + str(self.center.code)

            else :
                self.serial_number = '1-' + str(self.center.code)
            




    

       return super(CenterProduct, self).save(*args, **kwargs)

class Service(models.Model):
    class Progress(models.TextChoices):
        WAITING = 'WAITING' , 'Waiting'
        DOING = 'DOING' , 'Doing'
    vehical = models.ForeignKey(Vehical , on_delete=models.SET_NULL, blank=True , null= True)   
    center = models.ForeignKey(Center , on_delete=models.SET_NULL , null=True , blank= True)
    services = models.ManyToManyField(CenterServices)
    products = models.ManyToManyField(CenterProduct)
    progress = models.CharField(max_length=20 , choices=Progress.choices , default= Progress.WAITING)
    date = models.DateTimeField(auto_now_add=True)
    # Customer Already in vehical
    additional_services = models.CharField(max_length=200 ,null=True , blank=True)
    additional_services_cost = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)
    #customer = models.ForeignKey(Customer , on_delete=models.SET_NULL, blank=True , null= True)

    def __str__(self) -> str:
        return str(self.vehical.number) + ' - ' + str(self.date.date())

class Estimate(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    serial_number = models.CharField(max_length=50)
    service = models.OneToOneField(Service , on_delete= models.CASCADE)
    price = models.FloatField()
    report = models.FileField(null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True , editable=False)
    def save(self, *args, **kwargs):
        
        self.serial_number = str(self.service.id) +'-ES-'+ str(self.service.center)  
        
        services = list(self.service.services.all())
        self.price = 0
        for service in services:
            self.price += service.price * (1 + service.tax/100)
        self.price += self.service.additional_services_cost
        super(Estimate, self).save(*args, **kwargs)
    def __str__(self) -> str:
        return str(self.service) + '-' +str(self.created_at)

class Update(models.Model):
    update_image = models.ImageField(upload_to='media/updateimg' , blank= True , null= True)
    update_title = models.CharField(max_length=50 , blank= True , null= True)
    update_description = models.CharField(max_length=200 , blank= True , null= True)
    service = models.ForeignKey(Service , on_delete=models.CASCADE)
    def __str__(self):
        return self.update_title

class PaySlip(models.Model):
    employee = models.ForeignKey(Employee , null=True , blank= True ,  on_delete= models.SET_NULL)
    amount = models.FloatField()
    date = models.DateField(default= datetime.date.today)
    slip = models.FileField(upload_to='media/payslips')
    #proof = models.FileField(null=True , blank=True)
    txnid = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.employee) + ' - ' + str(self.date)

class Attendance(models.Model):
    class AttendanceStatus(models.TextChoices):
        NOT_MARKED = 'NOT MARKED' , 'NOT MARKED'
        PRESENT = 'PRESENT' , 'PRESENT'
        ABSENT = 'ABSENT' , 'ABSENT'
    employee = models.ForeignKey(Employee , null=True , blank=True , on_delete=models.SET_NULL)
    status =  models.CharField(max_length=50 , choices=AttendanceStatus.choices ,default= AttendanceStatus.NOT_MARKED)
    date = models.DateField()
    def __str__(self) -> str:
        return str(self.employee) + " - " + str(self.date)
    class Meta:
        unique_together = ('employee' , 'date')

class Task(models.Model):
    title = models.CharField(max_length=50 )
    description = models.CharField(max_length=200)
    services = models.ForeignKey(Service , null=True , blank= True , on_delete=models.SET_NULL)
    employee = models.ForeignKey(Employee , null=True , blank=True , on_delete=models.SET_NULL)
    date = models.DateField(default= datetime.date.today)
    center = models.ForeignKey(Center , on_delete=models.CASCADE)
    class TaskStatus(models.TextChoices):
        NA = 'NA' , 'NA'
        ACCEPTED = 'ACCEPTED' , 'ACCEPTED'
        REJECTED = 'REJECTED' , 'REJECTED'
        DONE = 'DONE' , 'DONE'
        PENDING = 'PENDING' , 'PENDING'
        FAILED = 'FAILED' , 'FAILED'
    status = models.CharField(max_length=50 , choices=TaskStatus.choices ,default= TaskStatus.NA)
    def __str__(self) -> str:
        return str(self.employee) + ' - ' + str(self.title)
    

class ProductSale(models.Model):
    service = models.ForeignKey(Service , on_delete=models.CASCADE)
    product = models.ForeignKey(CenterProduct , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    amount = models.FloatField(default=0)
    def save(self, *args , **kwargs):
        if self.id is None:
            pro = CenterProduct.objects.get(id = self.product.id)
            if pro.stock < self.quantity:
                raise ValueError
            pro.stock = pro.stock - self.quantity
            self.amount = self.quantity * pro.price*((100+pro.tax)/100)
            pro.save()
            self.service.products.add(pro)
        return super().save(*args , **kwargs)
    def __str__(self) -> str:
        return str(self.product) + ' - ' + str(self.quantity)
    class Meta:
        unique_together = ('service' ,  'product')