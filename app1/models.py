# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
'''

class Barcode(models.Model):
    id = models.BigAutoField(primary_key=True)
    barcode = models.CharField(max_length=45)
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'barcode'


class Brand(models.Model):
    id = models.BigAutoField(primary_key=True)
    brandname = models.CharField(db_column='brandName', max_length=45)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'brand'
0

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    categoryname = models.CharField(db_column='categoryName', max_length=45)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    cityname = models.CharField(db_column='cityName', max_length=45)  # Field name made lowercase.
    districtid = models.ForeignKey('District', models.DO_NOTHING, db_column='districtId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class Color(models.Model):
    id = models.BigAutoField(primary_key=True)
    color = models.CharField(max_length=45)
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'color'


class Counter(models.Model):
    id = models.BigAutoField(primary_key=True)
    counterno = models.CharField(db_column='counterNo', max_length=45)  # Field name made lowercase.
    systemmacaddress = models.CharField(db_column='systemMACAddress', max_length=45)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.
    statusid = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'counter'


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    countryname = models.CharField(db_column='countryName', max_length=45)  # Field name made lowercase.
    countrycode = models.CharField(db_column='countryCode', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(db_column='fullName', max_length=45)  # Field name made lowercase.
    address = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45)
    mobileno = models.CharField(db_column='mobileNo', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    departmentname = models.CharField(db_column='departmentName', max_length=45)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'


class District(models.Model):
    id = models.BigAutoField(primary_key=True)
    districtname = models.CharField(db_column='districtName', max_length=45)  # Field name made lowercase.
    stateid = models.ForeignKey('State', models.DO_NOTHING, db_column='stateId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'district'


class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='cityId')  # Field name made lowercase.
    districtid = models.ForeignKey(District, models.DO_NOTHING, db_column='districtId')  # Field name made lowercase.
    stateid = models.ForeignKey('State', models.DO_NOTHING, db_column='stateId')  # Field name made lowercase.
    countryid = models.ForeignKey(Country, models.DO_NOTHING, db_column='countryId')  # Field name made lowercase.
    email = models.CharField(max_length=45)
    mobileno = models.CharField(db_column='mobileNo', max_length=45)  # Field name made lowercase.
    photo = models.CharField(max_length=45)
    adharcardphoto = models.CharField(db_column='adharCardPhoto', max_length=45)  # Field name made lowercase.
    pancardphoto = models.CharField(db_column='panCardPhoto', max_length=45)  # Field name made lowercase.
    dob = models.DateField()
    joiningdate = models.DateField(db_column='joiningDate')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Employeedetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    employeid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employeId')  # Field name made lowercase.
    relivingdate = models.DateField(db_column='relivingDate')  # Field name made lowercase.
    salary = models.FloatField()
    designation = models.CharField(max_length=45)
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employeedetails'


class Garbage(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemrateid = models.ForeignKey('Itemrates', models.DO_NOTHING, db_column='itemRateId')  # Field name made lowercase.
    quantity = models.PositiveIntegerField()
    unitid = models.ForeignKey('Unit', models.DO_NOTHING, db_column='unitId')  # Field name made lowercase.
    damageduring = models.CharField(db_column='damageDuring', max_length=45)  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'garbage'


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemname = models.CharField(db_column='itemName', max_length=45)  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='categoryId')  # Field name made lowercase.
    subcategoryid = models.ForeignKey('Subcategory', models.DO_NOTHING, db_column='subCategoryId')  # Field name made lowercase.
    colorid = models.ForeignKey(Color, models.DO_NOTHING, db_column='colorId')  # Field name made lowercase.
    brandid = models.ForeignKey(Brand, models.DO_NOTHING, db_column='brandId')  # Field name made lowercase.
    sizeid = models.ForeignKey('Size', models.DO_NOTHING, db_column='sizeId')  # Field name made lowercase.
    departmentid = models.ForeignKey(Department, models.DO_NOTHING, db_column='departmentId')  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.
    isgoodsconversionitem = models.CharField(db_column='isGoodsConversionItem', max_length=45)  # Field name made lowercase.
    itemimg = models.CharField(db_column='itemImg', max_length=45)  # Field name made lowercase.
    rackid = models.ForeignKey('Rack', models.DO_NOTHING, db_column='rackId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item'


class Itemrates(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemid = models.ForeignKey(Item, models.DO_NOTHING, db_column='itemId')  # Field name made lowercase.
    mrp = models.FloatField()
    retailrate = models.FloatField(db_column='retailRate')  # Field name made lowercase.
    purchaserate = models.FloatField(db_column='purchaseRate')  # Field name made lowercase.
    quantity = models.PositiveIntegerField()
    unitid = models.ForeignKey('Unit', models.DO_NOTHING, db_column='unitId')  # Field name made lowercase.
    taxid = models.ForeignKey('Tax', models.DO_NOTHING, db_column='taxId')  # Field name made lowercase.
    date = models.CharField(max_length=45)
    barcode = models.BigIntegerField()
    effectiverate = models.FloatField(db_column='effectiveRate')  # Field name made lowercase.
    wholesalerate = models.FloatField(db_column='wholeSaleRate')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemrates'


class Itemreturntype(models.Model):
    id = models.BigAutoField(primary_key=True)
    returntype = models.CharField(db_column='returnType', max_length=100)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemreturntype'


class Itemsuplimentory(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemrateid = models.ForeignKey(Itemrates, models.DO_NOTHING, db_column='itemRateId')  # Field name made lowercase.
    suplimentoryitemid = models.ForeignKey(Itemrates, models.DO_NOTHING, db_column='suplimentoryItemId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemsuplimentory'


class Loyalitypoint(models.Model):
    id = models.BigAutoField(primary_key=True)
    loyalitypoint = models.FloatField(db_column='loyalityPoint')  # Field name made lowercase.
    loyalityamounts = models.FloatField(db_column='loyalityAmounts')  # Field name made lowercase.
    redemptionpoint = models.FloatField(db_column='redemptionPoint')  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loyalitypoint'


class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    menuname = models.CharField(db_column='menuName', max_length=45)  # Field name made lowercase.
    menuurl = models.CharField(db_column='menuURL', max_length=45)  # Field name made lowercase.
    menudescription = models.CharField(db_column='menuDescription', max_length=100)  # Field name made lowercase.
    menulevel = models.PositiveIntegerField(db_column='menuLevel')  # Field name made lowercase.
    menusequencenumber = models.PositiveIntegerField(db_column='menuSequenceNumber')  # Field name made lowercase.
    numberofchilds = models.PositiveIntegerField(db_column='numberOfChilds')  # Field name made lowercase.
    parentmenuid = models.BigIntegerField(db_column='parentMenuId')  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='updatedOn')  # Field name made lowercase.
    ismenuactive = models.PositiveIntegerField(db_column='isMenuActive')  # Field name made lowercase.
    menuicon = models.CharField(db_column='menuIcon', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu'


class Menurole(models.Model):
    id = models.BigAutoField(primary_key=True)
    menuid = models.ForeignKey(Menu, models.DO_NOTHING, db_column='menuId')  # Field name made lowercase.
    roleid = models.ForeignKey('Role', models.DO_NOTHING, db_column='roleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menurole'


class Paymentmode(models.Model):
    id = models.BigAutoField(primary_key=True)
    transactiontype = models.CharField(db_column='transactionType', max_length=45)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymentmode'


class Purchase(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.PositiveIntegerField()
    mrp = models.FloatField()
    retailrate = models.FloatField(db_column='retailRate')  # Field name made lowercase.
    purchaserate = models.FloatField(db_column='purchaseRate')  # Field name made lowercase.
    itemrateid = models.ForeignKey(Itemrates, models.DO_NOTHING, db_column='itemRateId')  # Field name made lowercase.
    purchasesupplierid = models.ForeignKey('Purchasesupplier', models.DO_NOTHING, db_column='purchaseSupplierId')  # Field name made lowercase.
    itemsuplimentoryid = models.ForeignKey(Itemsuplimentory, models.DO_NOTHING, db_column='ItemSuplimentoryId')  # Field name made lowercase.
    unitid = models.ForeignKey('Unit', models.DO_NOTHING, db_column='unitId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchase'


class Purchasebill(models.Model):
    id = models.BigAutoField(primary_key=True)
    purchasesupplierid = models.ForeignKey('Purchasesupplier', models.DO_NOTHING, db_column='purchaseSupplierId')  # Field name made lowercase.
    paymentmodeid = models.ForeignKey(Paymentmode, models.DO_NOTHING, db_column='paymentModeId')  # Field name made lowercase.
    billdate = models.DateField(db_column='billDate')  # Field name made lowercase.
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'purchasebill'


class Purchasereturn(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemrateid = models.ForeignKey(Itemrates, models.DO_NOTHING, db_column='itemRateId')  # Field name made lowercase.
    quantity = models.PositiveIntegerField()
    unitid = models.ForeignKey('Unit', models.DO_NOTHING, db_column='unitId')  # Field name made lowercase.
    returndate = models.DateField(db_column='returnDate')  # Field name made lowercase.
    supplierid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='supplierId')  # Field name made lowercase.
    itemreturntypeid = models.ForeignKey(Itemreturntype, models.DO_NOTHING, db_column='itemReturnTypeId')  # Field name made lowercase.
    returnamount = models.FloatField(db_column='returnAmount')  # Field name made lowercase.
    purchasebillid = models.ForeignKey(Purchasebill, models.DO_NOTHING, db_column='purchaseBillId')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchasereturn'


class Purchasesupplier(models.Model):
    id = models.BigAutoField(primary_key=True)
    supplierid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='supplierId')  # Field name made lowercase.
    purchasedate = models.DateField(db_column='purchaseDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchasesupplier'


class Rack(models.Model):
    id = models.BigAutoField(primary_key=True)
    rackno = models.CharField(db_column='rackNo', max_length=45)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rack'


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    rolename = models.CharField(db_column='roleName', max_length=45)  # Field name made lowercase.
    hasrole = models.CharField(db_column='hasRole', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role'


class Sales(models.Model):
    id = models.BigAutoField(primary_key=True)
    salesorderid = models.ForeignKey('Salesorder', models.DO_NOTHING, db_column='salesOrderId')  # Field name made lowercase.
    itemrateid = models.ForeignKey(Itemrates, models.DO_NOTHING, db_column='itemRateId')  # Field name made lowercase.
    quantity = models.PositiveIntegerField()
    unitid = models.ForeignKey('Unit', models.DO_NOTHING, db_column='unitId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sales'


class Salesbill(models.Model):
    id = models.BigAutoField(primary_key=True)
    salesorderid = models.ForeignKey('Salesorder', models.DO_NOTHING, db_column='salesOrderId')  # Field name made lowercase.
    paymentmodeid = models.ForeignKey(Paymentmode, models.DO_NOTHING, db_column='paymentModeId')  # Field name made lowercase.
    billdate = models.DateTimeField(db_column='billDate')  # Field name made lowercase.
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'salesbill'


class Salesorder(models.Model):
    id = models.BigAutoField(primary_key=True)
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customerId')  # Field name made lowercase.
    salesdate = models.DateTimeField(db_column='salesDate')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    counterid = models.ForeignKey(Counter, models.DO_NOTHING, db_column='counterId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesorder'


class Salesreturn(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemrateid = models.ForeignKey(Itemrates, models.DO_NOTHING, db_column='itemRateId')  # Field name made lowercase.
    salesbillid = models.ForeignKey(Salesbill, models.DO_NOTHING, db_column='salesBillId')  # Field name made lowercase.
    quantity = models.PositiveIntegerField()
    unitid = models.ForeignKey('Unit', models.DO_NOTHING, db_column='unitId')  # Field name made lowercase.
    returndate = models.DateField(db_column='returnDate')  # Field name made lowercase.
    reason = models.CharField(max_length=45)
    itemreturntypeid = models.ForeignKey(Itemreturntype, models.DO_NOTHING, db_column='itemReturnTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesreturn'


class Salesreturntype(models.Model):
    id = models.BigAutoField(primary_key=True)
    returntype = models.CharField(db_column='returnType', max_length=100)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesreturntype'


class Size(models.Model):
    id = models.BigAutoField(primary_key=True)
    size = models.CharField(max_length=45)
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'size'


class State(models.Model):
    id = models.BigAutoField(primary_key=True)
    statename = models.CharField(db_column='stateName', max_length=45)  # Field name made lowercase.
    countryid = models.ForeignKey(Country, models.DO_NOTHING, db_column='countryId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'state'


class Status(models.Model):
    id = models.BigAutoField(primary_key=True)
    statusname = models.CharField(db_column='statusName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'status'


class Subcategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    subcategoryname = models.CharField(db_column='subCategoryName', max_length=45)  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='categoryId')  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subcategory'


class Supplier(models.Model):
    id = models.BigAutoField(primary_key=True)
    suppliername = models.CharField(db_column='supplierName', max_length=45)  # Field name made lowercase.
    address = models.CharField(max_length=45)
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='cityId')  # Field name made lowercase.
    districtid = models.ForeignKey(District, models.DO_NOTHING, db_column='districtId')  # Field name made lowercase.
    stateid = models.ForeignKey(State, models.DO_NOTHING, db_column='stateId')  # Field name made lowercase.
    countryid = models.ForeignKey(Country, models.DO_NOTHING, db_column='countryId')  # Field name made lowercase.
    email = models.CharField(max_length=45)
    mobileno = models.CharField(db_column='mobileNo', max_length=10)  # Field name made lowercase.
    landlineno = models.CharField(db_column='landlineNo', max_length=11)  # Field name made lowercase.
    faxno = models.CharField(db_column='faxNo', max_length=45)  # Field name made lowercase.
    panno = models.CharField(db_column='panNo', max_length=10)  # Field name made lowercase.
    tanno = models.CharField(db_column='tanNo', max_length=45)  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier'


class Tax(models.Model):
    id = models.BigAutoField(primary_key=True)
    cgsttax = models.FloatField(db_column='CGSTtax')  # Field name made lowercase.
    sgsttax = models.FloatField(db_column='SGSTtax')  # Field name made lowercase.
    igsttax = models.FloatField(db_column='IGSTtax')  # Field name made lowercase.
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tax'


class Unit(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit = models.CharField(max_length=45)
    updatedby = models.BigIntegerField(db_column='updatedBy')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    deleteflag = models.PositiveIntegerField(db_column='deleteFlag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unit'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(db_column='userName', max_length=45)  # Field name made lowercase.
    password = models.CharField(max_length=200)
    registrationdate = models.DateField(db_column='registrationDate')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.
    statusid = models.ForeignKey(Status, models.DO_NOTHING, db_column='statusId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class Usercounterlogin(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    counterid = models.ForeignKey(Counter, models.DO_NOTHING, db_column='counterId')  # Field name made lowercase.
    logindate = models.DateTimeField(db_column='loginDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usercounterlogin'


class Userrole(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    roleid = models.ForeignKey(Role, models.DO_NOTHING, db_column='roleId')  # Field name made lowercase.
    updatedon = models.DateField(db_column='updatedOn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userrole'

'''

# class Origin(models.Model):
#     name = models.CharField(max_length=100)
#
#     def save(self, *args, **kwargs):
#         if self.__class__.objects.count():
#             self.pk = self.__class__.objects.first().pk
#         super().save(*args, **kwargs)
