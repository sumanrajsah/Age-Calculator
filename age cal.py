x=(input("Enter your Date of birth in the form of DD/MM/YYYY= "))
b=(input("Enter your present Date in the form of DD/MM/YYYY= "))
dob=list(map(int,x.split('/')))
p=list(map(int,b.split('/')))
q=abs(dob[1]-p[1])
r=(p[2]-dob[2])
if 1 <= dob[0]  <= 31 and 1 <= dob[1] <= 12 and p[2] > dob[2]:
    if 1 <= p[0] <=31 and 1 <= p[1] <= 12:
            d=abs(dob[0]-p[0])
            m=(abs(dob[1]-p[1])*30)
            y=0
            for i in range(dob[2],p[2]):
                if ((i%4 == 0) and (i%100 != 0)) or (i%400 == 0):
                        y+=366
                else:
                        y+=365
            print("You survived",(d+m+y),"days in this world")
            
            o=1
            while o>0:
                print("---------------","Choose any option from the following given below:","Enter 0 to Exit from terminal","Enter 1 to  Get your Birth Date","Enter 2 to Get Present date your entered early","Enter 3 To Know how many years you spent in this world","Enter 4 To Know how many months you spent in this world","Enter 5 To Know how many Hours you spent in this world","Enter 6 To Know how many Minutes you spent in this world","Enter 7 To Know how many Seconds you spent in this world","Enter 8 to Re-Print Output",sep="\n")
                a=int(input("Enter your Option Here: "))
                if a<9:
                   if a==1:
                       print("Your Birth date is: ",x)
                       print("-------------")
                   elif a==2:
                       print("Present date you entered early: ",b)
                   elif a==3:
                       print("you spent",r,"Years",q,"Months and",d,"Days")
                   elif a==4:
                       print("You spent",(q+(r*12))," Months in this world")                       
                  
                   elif a==5:
                       print("You survived ",((y+d+m)*24),"Hours in this world")
                   elif a==6:
                       print("You survived ",((y+d+m)*24*60),"Minutes in this world")
                   elif a==7:
                       print("You survived",((y+d+m)*24*60*60),"Seconds in this world")
                   elif a==8:
                       print("You survived",(d+m+y),"Days in this world")
                   elif a==0:
                       print("*** Terminal Terminated ***","*****Thank You*****",sep="\n")
                       break
                else: 
                    print("------------------ **Please choose Valid Option** --------------")
                o+=1
    else:
        print("Enter Valid present date")
else:
    print("Enter Valid Date of birth")
