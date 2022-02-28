def getdate():
    import datetime
    return datetime.datetime.now()
r=str(getdate())



print("Enter your code")
x=int(input())
if x==1:
    print("1 for Retrieve OR 2 for Log")
    y=int(input())
    if y==2:
        print("diet or excerise")
        z=int(input())
        if z==1:
        
            print("enter your diet")
            d=input()
            f=open("aakash diet.txt","a")
            
            f.write(r)
            f.write(d)
    
            f.close() 
        elif z==2:
            print("enter your excerise")
            e=input()
            f=open("aakash ex.txt","w")
            f.write(r)
            f.write(e)
            f.close()
        else:
            print("Invalid code")    
    elif y==1:
        print("which file you want to retrive")
        k=int(input())
        if k==1:
            f=open("aakash diet.txt","r")
            print(f.read())
        else:
            g=open("aakash ex.txt","r")
            print(g.read())                    
elif x==2:
    print("r OR l")
    y=int(input())
    if y==2:
        print("diet or excerise")
        z=int(input())
        if z==1:
        
            print("enter your diet")
            d=input()
            f=open("Ankur diet.txt","a")
            
            f.write(r)
            f.write(d)
            f.close() 
        elif z==2:
            print("enter your excerise")
            e=input()
            f=open("Ankur ex.txt","w")
            f.write(r)
            f.write(e)
            f.close()
        else:
            print("Invalid code")    
    elif y==1:
        print("which file you want to retrive")
        k=int(input())
        if k==1:
            f=open("Ankur diet.txt","r")
            print(f.read())
        else:
            g=open("Ankur ex.txt","r")
            print(g.read())                    
elif x==3:
    print("r OR l")
    y=int(input())
    if y==2:
        print("diet or excerise")
        z=int(input())
        if z==1:
        
            print("enter your diet")
            d=input()
            f=open("jwala diet.txt","a")
            
            f.write(r)
            f.write(d)
            f.close() 
        elif z==2:
            print("enter your excerise")
            e=input()
            f=open("jwala ex.txt","w")
            f.write(r)
            f.write(e)
            f.close()
        else:
            print("Invalid code")    
    elif y==1:
        print("which file you want to retrive")
        k=int(input())
        if k==1:
            f=open("jwala diet.txt","r")
            print(f.read())
        else:
            g=open("jwala ex.txt","r")
            print(g.read())               
else:
    print("User id not created")