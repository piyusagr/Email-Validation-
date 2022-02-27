# Email-Validation-
<!-- # using  regex    and string function in phyton -->



# using regex function

if re.search(email_codition,user_email):

    print(" Right Email ")
    
else:

    print(" Wrong Email ")



# using string function

email=input("Enter the Email: ")

k,d,j=0,0,0

if len(email)>=6:

   if email[0].isalpha():
     
       if ("@"in email) and (email.count("@")==1):
            
            if (email[-4]==".")^(email[-3]=="."):
                
                for i in email:
                    
                    if i==i.isspace():
                        
                        k=1
                    
                    elif i.isalpha():
                         
                         if i==i.upper():
                            
                            j=1
                    
                    elif i.isdigit():
                        
                        k=0
                    
                    elif i=="_"  or i=="." or i=="@":
                        
                        j=0
                    
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print(" Wrong Email ")
                elif k==0 or j==0 or d==0:
                    print(" Right Email")
            else:
                print(" Wrong Eamil ")
        else:
            print(" Wrong Eamil ")
    else:
        print(" Wrong Email ")
else:

    print(" Wrong Email ")
    
    
![image](https://user-images.githubusercontent.com/85010286/155887485-d5d39bf8-6868-444f-8185-647ffb4ae5ee.png)
    
![image](https://user-images.githubusercontent.com/85010286/155887491-9e0e6ec5-90f6-4d98-8c3b-60e2f23f07df.png)

