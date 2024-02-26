from tkinter import CASCADE
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_hairdresser = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HairdresserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salon_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField()
    services_offered = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class vendor_profiles (models.Model):
  user_id=models.ForeignKey(User,on_delete=models.CASCADE)
  shop_name=models.CharField
  shop_description=models.TextField
  # shop_logo varchar
  address=models.CharField(max_length=255)
  phone_number= models.CharField(max_length=255)
  # website varchar
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class payment_method (models.Model):
  user_id=models.ForeignKey(User,on_delete=models.CASCADE)
  payment_type=models.CharField(max_length=20,choices=[('Mpesa', 'Mpesa'), ('PayPal', 'PayPal'), ('Bank transfer', 'Bank transfer')])
  # // PayPal
  # // Mpesa
  details=models.CharField
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

class products(models.Model):
  vendor_profiles_id=models.ForeignKey(vendor_profiles,on_delete=models.CASCADE)
  name=models.CharField
  description=models.TextField
  price=models.CharField(max_length=100)
  quantity_available=models.CharField(max_length=100)
  # // also stock
  # // PositiveIntegerField
  # image varchar
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

class categories (models.Model):
  product_id=models.ForeignKey(products,on_delete=models.CASCADE)
  name=models.CharField(max_length=100)
  description=models.TextField
  # image varchar
  created_at= models.DateTimeField(auto_now_add=True)
  updated_at= models.DateTimeField(auto_now=True)

class cart (models.Model):
  user_id=models.ForeignKey(User,on_delete=models.CASCADE)
  # // oneToOne relationship
  created_at= models.DateTimeField(auto_now_add=True)
  updated_at= models.DateTimeField(auto_now=True)

class cartItem(models.Model):
  cart_id=models.ForeignKey(cart, on_delete=models.CASCADE)
  product_id=models.ForeignKey(products,on_delete=models.CASCADE)
  quantity=models.CharField(max_length=100)
  created_at= models.DateTimeField(auto_now_add=True)
  updated_at= models.DateTimeField(auto_now=True)

class Service(models.Model):
    hairdresser_profile = models.ForeignKey(HairdresserProfile, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hairdresser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings_as_hairdresser')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cancellation(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    refund_amount = models.CharField(max_length=100)
    refund_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class reviews (models.Model):
  user_id=models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
  hairdresser_id=models.ForeignKey(HairdresserProfile, on_delete=models.CASCADE)
  service_id=models.ForeignKey(Service, on_delete=models.CASCADE)
 # rating=models.IntegerField
  review_text=models.TextField
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

#   class posts(models.Model):
#   author_id int [ref: > users.id]
#   content  varchar
#   image_url varchar
#   video_url varchar
#   video_length varchar
#   is_booking boolean
#   is_purchasing boolean
#   // DurationField
#   created_at timestamp
#   updated_at timestamp
  
class payment(models.Model):
  amount=models.IntegerField
  payment_method=models.CharField(max_length=20,choices=[('Mpesa', 'Mpesa'), ('PayPal', 'PayPal'), ('Bank transfer', 'Bank transfer')], default='Mpesa')
#Mpesa, PayPal, bank transfer
  transaction_id=models.CharField(max_length=255)
#"TXN123456789"
  status=status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed')])
 #pending, confirmed, cancelleed
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

class orderItems(models.Model):
  product_id=models.ForeignKey(products, on_delete=models.CASCADE) 
  quantity=models.CharField(max_length=100)
  item_price=models.CharField(max_length=100)
  # accessing all products in an order
  # It is an association proxy for a MANY TO MANY FIELD 
  # total_price varchar
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

class transaction(models.Model):
  order_id=models.ForeignKey(orderItems, on_delete=models.CASCADE) 
  payment_method_id=models.ForeignKey(payment, on_delete=models.CASCADE) 
  status=models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed')])
  amount=models.CharField(max_length=100)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

