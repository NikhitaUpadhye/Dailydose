# Application (Static)
import time
print('Welcome to J-Store..')
print()
pro1 = float(input('Enter pro1 cost : '))
pro2 = float(input('Enter pro2 cost : '))
pro3 = float(input('Enter pro3 cost : '))
gst = float(input('Enter GST value : '))
print()
pro_Cost = pro1+pro2+pro3

gst_Value  = pro_Cost*gst

total_Amount = pro_Cost+gst_Value

print()
print('Product -1 Cost is : ',pro1)
time.sleep(1)
print('Product -2 Cost is : ',pro2)
time.sleep(1)
print('Product -3 Cost is : ',pro3)
time.sleep(1)
print('-'*30)
time.sleep(1)
print('Amount Without Tax : ',pro_Cost)
print('-'*30)
time.sleep(1)
print('Total Amount with Tax : ',total_Amount)

