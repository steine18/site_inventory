from django.db import models

class Site(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Equipment_type(models.Model):
    eq_type = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.eq_type

class Equipment_model(models.Model):
    eq_type = models.ForeignKey(Equipment_type, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.eq_type} - {self.brand} {self.model}'

    class Meta:
        unique_together = ('brand', 'model')

class Equipment(models.Model):
    equipment_model = models.ForeignKey(Equipment_model, on_delete=models.CASCADE)
    sn = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.equipment_model} SN:{self.sn}'

    class Meta:
        unique_together = ('equipment_model', 'sn')

class Site_equipment(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    eq_type = models.ForeignKey(Equipment_type, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)



class Deployment(models.Model):
    site_eq = models.ForeignKey(Site_equipment, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.site_eq.site.id} SN:{self.instrument.sn}'

    @property
    def is_active(self):
        if self.check_out == None:
            return True
        else:
            return False

class Shop_log(models.Model):
    instrument = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.instrument}'

    @property
    def in_stock(self):
        if self.check_out == None:
            return True
        else:
            return False

class Equipment_test(models.Model):
    instrument = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    test_type = models.CharField(
        max_length=1,
        choices=[('B', 'Bench'), ('F', 'Field')],
        default='B',
    )
    result = models.CharField(
        max_length=1,
        choices=[('P', 'Pass'), ('F', 'Fail'), ('O', 'Other')],
    )
    test_date = models.DateTimeField()
    notes = models.TextField(blank=True)

