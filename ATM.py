class account: #تعریف کلاس
    
    def __init__(self,inventory): #تعریف متد سازنده و پارامتری  که موجودی حساب را تعیین می کند
        
        self.inventory=cash #صفتی ساخته و موجودی دریافتی از کاربر را در آن می ریزیم
        
        if inventory<0: #اگر مقدار کمتر از صفر وارد شود
            
            self.inventory=0 #صفت سازنده موجودی را برابر صفر قرار می دهد
            
            print("invalid!") #نمایش پیغام خطا
            
    def credit(self,deposit): #تعریف متد افزودن به موجودی و قرار دادن پارامتر ورودی
        
        self.deposit=plus #مقدار را از ورودی دریافت می کند
        
        self.inventory=self.deposit+self.inventory #مقدار دریافتی را به موجودی کاربر اضافه می کند
        
    def debit(self,withdraw): #متد برداشت را تعریف و پارامتری را به آن اضافه می کنیم
        
        self.withdraw=minus #مقدار را دریافت می کند
        
        if self.withdraw<self.inventory: #اگر مقدار درخواستی برای برداشت از موجودی کاربر کمتر باشد
            
            self.inventory=self.inventory-self.withdraw #مقدار درخواستی را از موجودی کم کرده و موجودی فعلی را نمایش می دهد
            
        else: #در غیر این صورت پیغام موجودی ناکافی را نمایش بده
            
            print("insufficient inventory!")
            
    def getbalance(self): #تعریف  متد
        
        print("current inventory =",self.inventory) #دستور نمایش موجودی

ps1=1234

ps2=int(input("enter your password:"))

if ps1==ps2:
    cash=int(input("inventory="))
    acc=account(cash)
    while  True : #حلقه تکرار برای فراخوانی مجدد توابع

        print("1.deposit:","\n") #گزینه های مورد نظر
    
        print("2.withdraw:","\n")
    
        print("3.inventory:","\n")
    
        print("4.exit:","\n")
    
        z=int(input("enter:")) #انتخاب گزینه مورد نظر از فهرست
    
        if z==1: #اگر گزینه 1 انتخاب شود 
        
            plus=int(input("deposit=")) #مبلغ مورد نظر جهت افزودن به موجودی را وارد کنید
        
            acc.credit(plus) #فراخوانی متد
        
        elif z==2:
        
            minus=int(input("withdraw=")) #مبلغ جهت برداشت
        
            acc.debit(minus) #فراخوانی متد
        
        elif z==3:
        
            acc.getbalance() #فراخوانی متد
        
        elif z==4:
        
            break #دستور خروج از حلقه
            
        else: #در غیر این صورت نمایش بده : عدد وارد شده صحیح نیست
        
            print("invalid order")
else :

    print("wrong password!")
 
