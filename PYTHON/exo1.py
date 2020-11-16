from datetime import datetime
name = input("Bạn tên gì ? ")
age = int(input("Nhập năm sinh của bạn: "))
currentYear = datetime.now().year 
yearOld = currentYear - age
nameAge = "{greeting} \nTôi tên là : {name}\nTôi năm nay : {yearOld} tuổi".format(greeting = "Xin chào bạn !",name =name,yearOld =str(yearOld))
print(nameAge)