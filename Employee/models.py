from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=30)
    employee_photo_id = models.CharField(max_length=100,default='abc')
    employee_salary = models.DecimalField(max_digits=18, decimal_places=2)
    employee_gender = models.CharField(max_length=10)
    employee_department = models.CharField(max_length=30,default='')
    city_id = models.ForeignKey('City.CityModel',db_column='city_id', on_delete=models.CASCADE,default='')

    class Meta:
        db_table = 'tbl_employee'

    @property
    def hra(self):
        return str(self.employee_salary * 2 /100) + '/-'
    @property
    def da(self):
        return str(self.employee_salary * 3 /100) + '/-'
    @property
    def pf(self):   
        return str(self.employee_salary * 14 /100) + '/-'
    @property
    def net_salary(self):
        hra = self.employee_salary * 2 /100
        da = self.employee_salary * 3 /100
        pf = self.employee_salary * 14 /100
        total = self.employee_salary + hra + da - pf 
        return str(total) + '/-' 
    @property
    def employee_main_salery(self):
        return str(self.employee_salary ) + '/-'