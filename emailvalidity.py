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