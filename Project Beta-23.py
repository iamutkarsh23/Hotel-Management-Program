########################################################################################################################

import pickle
import os
#from datetime import date

def detailsOfTheRoom():
    
            
            print "===============================Select Desired Room Type From Below :============================================-\n  "
            print "_______________________________________________________________________________________________________________"
            print "\n                                                  Guest Rooms"
            print "_______________________________________________________________________________________________________________"
            print """\n1. Deluxe City View Room                                                                 USD 790 per night
    Bed Options - One King Bed/Two Queen Beds
    Location - 1st & 2nd floors"""
            print "_______________________________________________________________________________________________________________"
            print """\n2. Premier Skyline Room                                                                  USD 939 per night
    Bed Options - One King Bed/Two Queen Beds
    Location - 3rd,4th & 5th floors"""
            print "_______________________________________________________________________________________________________________"
            print """\n3. Deluxe Parial Sea-View Room                                                           USD 1,123 per night
    Bed Options - One King Bed
    Location - 1st & 2nd floors"""
            print "_______________________________________________________________________________________________________________"
            print """\n4. Premier Sea-View Room                                                                 USD 1,271 per night
    Bed Options - One King Bed/Two Queen Beds
    Location - 2nd to 5th floors"""
            print "_______________________________________________________________________________________________________________"
            print "\n                                               Special Suites"
            print "_______________________________________________________________________________________________________________"
            print """\n5. Imperial Suite                                                                        USD 4,220 per night
    Bed Options - Two King Beds/Two Queen Beds
    Location - 1nd to 4th floors"""
            print "_______________________________________________________________________________________________________________"
            print """\n6. Penthouse Suite                                                                       USD 5,323 per night
    Bed Options - Two King Bed/Three Queen Beds
    Location - 5th floor"""
            print "_______________________________________________________________________________________________________________"
            print """\n7. Presidential Suite                                                                    USD 5,550 per night
    Bed Options - Two King Bed/Three Queen Beds
    Location - 5th floor"""
            print "_______________________________________________________________________________________________________________"
            print """\n8. Royal Suite                                                                           USD 7,823 per night
    Bed Options - Two King Bed/Two Queen Beds
    Location - 5th floor"""
            print "_______________________________________________________________________________________________________________"



#customer's class
class customer(object):
    def __init__(self):
        self.cname=""        
        self.mno=0
        self.mail=""
        self.password=0
    def acquire(self):
        self.cname=raw_input("Enter your full name --> ")
        
        self.mno=raw_input("\nEnter your mobile number (should contain 14 digits) --> ")
        while len(self.mno)<>14:
            print"The mobile number you have entered is incorrect .\n It should contain 14 digits.\n"
            self.mno=raw_input("Enter your mobile number (should contain 14 digits)--> ")
        else :
            print "Mobile number successfully registered.\n"
        self.mail=raw_input ("Enter your email id (abc@xyz.com) --> ")
        while self.mail[-4:]<>".com":
            print "Your email id could not be recognised .Make sure you have written it in the form abc@xyz.com"
            self.mail=raw_input ("Enter your email id (abc@xyz.com) --> ")
        else:
            print "Your email has been verified.\n"
        self.password=raw_input("Please enter a password for your account (6-12 characters)--> ")
        while len(self.password)<6 or len(self.password)>12:
            print "Please enter a password between 6 and 12 characters.\n"
            self.password=raw_input("Please enter a password for your account again (6-12 characters)--> ")
        else:
            print" Password has been saved.\n"

    #for modification take new entries
    def modify_cust(cust):
        print"""Choose the details of the reservations you want to change :- \n
    1. Check in date\n
    2. Check out date\n
    3. Destination\n
    4. Room\n
    5. Number of people\n

    """
        choice=input("Enter your choice :- ")
        
        if choice==1:
            year1 = int(input('Enter check in  year --> '))
            month1 = int(input('\nEnter check in  month --> '))
            day1=int(input("\nEnter check in day --> "))
            cust.cid = date(year1,month1,day1)
            while cust.cid>cust.cod:
                print "Your check in date is after your check out date "
                print "Please try again"
                year1 = int(input('\nEnter check in year --> '))
                
                month1 = int(input('\nEnter check in  month --> '))
                day1 = int(input('\nEnter check in day --> '))
                cust.cid = date(year1,month1,day1)
                year = int(input('\nEnter check out year --> '))
                month = int(input('\nEnter check out month --> '))
                day = int(input('\nEnter check out day --> '))
                cust.cod = date(year,month,day)            
            cust.days=abs(cust.cod-cust.cid).days
            
        elif choice==2:
            year = int(input('\nEnter check out year --> '))
            month = int(input('\nEnter check out month --> '))
            day = int(input('\nEnter check out day --> '))
            cust.cod = date(year,month,day)
            
            while cust.cid>cust.cod:
                print "Your check in date is after your check out date!"
                print "Please try again!\n"
                year1 = int(input('\nEnter check in  year --> '))
                
                month1 = int(input('\nEnter check in  month --> '))
                
                day1 = int(input('\nEnter check in day --> '))
                
                cust.cid = date(year1,month1,day1)
                year = int(input('\nEnter check out year --> '))
                
                month = int(input('\nEnter check out month --> '))
                
                day = int(input('\nEnter check out day --> '))
                
                cust.cod = date(year,month,day)            
            cust.days=abs(self.cod-self.cid).days
            
        elif choice==3:
            a="""=================Select a destination======================== \n
                 \t \t 1  Atlanta
                 \t \t 2  Chicago
                 \t \t 3  Dallas
                 \t \t 4  Hawaii
                 \t \t 5  Los Angeles
                 \t \t 6  Las Vegas
                 \t \t 7  New York
                 \t \t 8  San Diego
                 \t \t 9  Toronto
                 \t \t 10 Vancover
                 \t \t 11 Washington"""
            print a
            c=int(raw_input("\nPlease Enter your choice --> "))
            if c==1:
                cust.dest="Atlanta"
            elif c==2:
                cust.dest="Chicago"
            elif c==3:
                cust.dest="Dallas"
            elif c==4:
                cust.dest="Hawaii"
            elif c==5:
                cust.dest="Las Vegas"
            elif c==6:
                cust.dest="Los Angeles"
            elif c==7:
                cust.dest="New York"
            elif c==8:
                cust.dest="San Diego"
            elif c==9:
                cust.dest="Toronto"
            elif c==10:
                cust.dest="Vancouver"
            elif c==11:
                cust.dest="Washington,DC"
            else:
                print "Wrong Input!"
                c=int(raw_input("\nPlease Enter your choice --> "))
        
                 
        elif choice==4:

            detailsOfTheRoom()
            
            c=int(raw_input("Please Enter your choice (1-8)--> "))
            if c==1:
                cust.room="Deluxe City View Room"
                cust.cost_per_night=790
            elif c==2:
                cust.room="Premier Skyline Room"
                cust.cost_per_night=939
            elif c==3:
                cust.room="Deluxe Partial Sea-View Room"
                cust.cost_per_night=1123
            elif c==4:
                cust.room="Premier Sea-View Room"
                cust.cost_per_night=1271
            elif c==5:
                cust.room="Imperial Suite"
                cust.cost_per_night=4220
            elif c==6:
                cust.room="Penthouse Suite"
                cust.cost_per_night=5323
            elif c==7:
                cust.room="Presidential Suite"
                cust.cost_per_night=5550
            elif c==8:
                cust.room="Royal Suite"
                cust.cost_per_night=7823
            else :
                print "Wrong Input!"
                c=int(raw_input("Please Enter your choice (1-8)--> "))
                
        elif abcd==5:
            cust.noa=input("Enter number of members travelling with you --> ")

        cust.display()
        return cust


        
class reservation( customer):
    def __init__(self):
        super(reservation,self).__init__()       
        self.cname=""
        self.password=0
        
        self.dest=""
        self.cid=""
        self.cod=""
        self.noa=0
        self.noc=0
        self.room=""
        self.cost_per_night=0
        self.days=0
        
    def reserve(self):
        self.cname=raw_input("\nEnter your full name --> ")
        self.password=raw_input("\nPlease enter a password for your account --> ")
        year1 = int(input('\nEnter check in  year -->  '))
        month1 = int(input('\nEnter check in  month --> '))
        day1=int(input("\nEnter check in day --> "))
        self.cid = date(year1,month1,day1)
        year = int(input('\nEnter check out year --> '))
        month = int(input('\nEnter check out month --> '))
        day = int(input('\nEnter check out day --> '))
        self.cod = date(year,month,day)
        while self.cid>self.cod:
            print "Your check in date is after your check out date!"
            print "Please try again!\n"
            year1 = int(input('\nEnter check in  year --> '))
            month1 = int(input('\nEnter check in  month --> '))
            day1 = int(input('\nEnter check in day --> '))
            self.cid = date(year1,month1,day1)
            year = int(input('\nEnter check out year --> '))
            month = int(input('\nEnter check out month --> '))
            day = int(input('\nEnter check out day --> '))
            self.cod = date(year,month,day)
            
        self.days=abs(self.cod-self.cid).days
        a="""=================Select a destination======================== \n
         \t \t 1  Atlanta
         \t \t 2  Chicago
         \t \t 3  Dallas
         \t \t 4  Hawaii
         \t \t 5  Los Angeles
         \t \t 6  Las Vegas
         \t \t 7  New York
         \t \t 8  San Diego
         \t \t 9  Toronto
         \t \t 10 Vancover
         \t \t 11 Washington"""
        print a
        c=int(raw_input("\nPlease Enter your choice --> "))
        if c==1:
            self.dest="Atlanta"
        elif c==2:
            self.dest="Chicago"
        elif c==3:
            self.dest="Dallas"
        elif c==4:
            self.dest="Hawaii"
        elif c==5:
            self.dest="Las Vegas"
        elif c==6:
            self.dest="Los Angeles"
        elif c==7:
            self.dest="New York"
        elif c==8:
            self.dest="San Diego"
        elif c==9:
            self.dest="Toronto"
        elif c==10:
            self.dest="Vancouver"
        elif c==11:
            self.dest="Washington,DC"
        else:
            print "Wrong Input!"
            c=int(raw_input("\nPlease Enter your choice --> "))
    

        print "===============================Select Desired Room Type From Below :============================================-\n  "
        print "_______________________________________________________________________________________________________________"
        print "\n                                                  Guest Rooms"
        print "_______________________________________________________________________________________________________________"
        print """\n1. Deluxe City View Room                                                                 USD 790 per night
Bed Options - One King Bed/Two Queen Beds
Location - 1st & 2nd floors"""
        print "_______________________________________________________________________________________________________________"
        print """\n2. Premier Skyline Room                                                                  USD 939 per night
Bed Options - One King Bed/Two Queen Beds
Location - 3rd,4th & 5th floors"""
        print "_______________________________________________________________________________________________________________"
        print """\n3. Deluxe Parial Sea-View Room                                                           USD 1,123 per night
Bed Options - One King Bed
Location - 1st & 2nd floors"""
        print "_______________________________________________________________________________________________________________"
        print """\n4. Premier Sea-View Room                                                                 USD 1,271 per night
Bed Options - One King Bed/Two Queen Beds
Location - 2nd to 5th floors"""
        print "_______________________________________________________________________________________________________________"
        print "\n                                               Special Suites"
        print "_______________________________________________________________________________________________________________"
        print """\n5. Imperial Suite                                                                        USD 4,220 per night
Bed Options - Two King Beds/Two Queen Beds
Location - 1nd to 4th floors"""
        print "_______________________________________________________________________________________________________________"
        print """\n6. Penthouse Suite                                                                       USD 5,323 per night
Bed Options - Two King Bed/Three Queen Beds
Location - 5th floor"""
        print "_______________________________________________________________________________________________________________"
        print """\n7. Presidential Suite                                                                    USD 5,550 per night
Bed Options - Two King Bed/Three Queen Beds
Location - 5th floor"""
        print "_______________________________________________________________________________________________________________"
        print """\n8. Royal Suite                                                                           USD 7,823 per night
Bed Options - Two King Bed/Two Queen Beds
Location - 5th floor"""
        print "_______________________________________________________________________________________________________________"


        c=int(raw_input("Please Enter your choice (1-8)--> "))
        if c==1:
            self.room="Deluxe City View Room"
            self.cost_per_night=790
        elif c==2:
            self.room="Premier Skyline Room"
            self.cost_per_night=939
        elif c==3:
            self.room="Deluxe Partial Sea-View Room"
            self.cost_per_night=1123
        elif c==4:
            self.room="Premier Sea-View Room"
            self.cost_per_night=1271
        elif c==5:
            self.room="Imperial Suite"
            self.cost_per_night=4220
        elif c==6:
            self.room="Penthouse Suite"
            self.cost_per_night=5323
        elif c==7:
            self.room="Presidential Suite"
            self.cost_per_night=5550
        elif c==8:
            self.room="Royal Suite"
            self.cost_per_night=7823
        else :
            print "Wrong Input!"
            c=int(raw_input("Please Enter your choice (1-8)--> "))
        self.noa=input("Enter number of members travelling with you --> ")
        
    def display(self):
        print "Your name is --> ", self.cname
        print "\nYour destination is --> ", self.dest
        print "\nYour check in date is--> ", self.cid
        print "\nYour check out date is--> ", self.cod
        print "\nThe number of days you are going to say with us--> ", self.days
        print "\nThe room you have selected --> ", self.room
        print "\nThe total cost for your trip is $",1.1*(self.cost_per_night*self.days)
        print "\nThank you for choosing us as your hotel choice."
        print "         Hope to see you again soon!"
        


##Main program##

print   """\n                                                           WELCOME TO FIVE POINTS HOTEL AND RESORTS



                                                Book hotels and resorts directly with FIVE POINTS to make your next
                                                        business trip or vacation more relaxing and affordable"""

c='y'
while (c=='y'or c=='Y'):
    
    print "1 Reservation                                                                    "
    print "2 About us                                                                         "
    print "3 Exit                                                                            "
    choice=input("Enter your Choice :- ")
    
    if choice==1:
        print"Are you already a registered member?"
        print "\n"
        print "If yes, please press Y to continue- "
        print "If you are not a registered member, press N to continue- "
        b=raw_input("Enter your choice --> ")
        if b=="n" or b=="N":
            print "\nPlease register with us for booking a room."
            #entering customer info
            cust=customer()
            cust.acquire()
            file1=open("hotelcu.dat","ab+")
            pickle.dump(cust,file1)#dumping in hotelcu file            
            file1.close()
            print"\nThankyou for registring with us."
            print "\nNow let us reserve a room for you."
            print "Please enter the following details carefully!"
            res=reservation()
            res.reserve()
            res.display()
            #checking if reservation is being done under the correct name
            cust=customer()
            f=True
            file2=open("hotelres.dat","ab+")
            file1=open("hotelcu.dat","ab+")
            while True:
                try:
                    cust=pickle.load(file1)
                    if str.upper(cust.cname)==str.upper(res.cname) and str.upper(cust.password)==str.upper(res.password):
                        pickle.dump(res,file2)
                        f=False
                        print "\nYou have now successfully reserved a room."
                        break               
                    
                except:
                    break
            if f==True:
                print "\nYou haven't registered properly!"           
            file1.close()
            file2.close()
                        
            
        elif b=="y" or b=="Y":
            cust=reservation()
            res=customer()
            
            flag=True
            un=raw_input("Enter your full name --> ")
            p=raw_input("Enter password --> ")
            
            file1=open("hotelres.dat","rb")
            file2=open("hotelcu.dat","rb")
            file3=open("temp.dat","wb")
            
            while True:
                try:
                    cust=pickle.load(file1)
                    cust1=customer()
                    
                    res=pickle.load(file2)
                    
                    if str.upper(cust.cname)==str.upper(un)==str.upper(res.cname) and str.upper(cust.password)==str.upper(p)==str.upper(res.password):
                        print" We have a reservation made under your name."
                        cust.display()
                        print "\nDo you want to modify your reservation?"
                        abc=input("If yes press 1 , if no then press 2 --> ")     
                        if abc==1:
                            
                            cust1=modify_cust(cust)
                            print "\nModified!\n"
                            pickle.dump(cust1,file3)
                            flag=False
                        elif abc ==2:
                            break
                            pickle.dump(cust,file3)
                        else:
                            print "Wrong input!"
                            abc=input("If yes press 1 , if no then press 2 --> ")
                            pickle.dump(cust.file3)
                    else:
                        print "\nYou are not a registered member!"
                        pickle.dump(cust,file3)
                        #break
                except:
                    break
            
            file1.close()
            file2.close()
            file3.close()
            
            if flag==True:
           
                print "\nYou are not registered!"
            else:
                os.remove("hotelres.dat")
                os.rename("temp.dat","hotelres.dat")
            
        else:
            print "Wrong input!"
            print "Please try again!"
            b=raw_input("\nEnter your choice --> ")
        
       
    elif choice==2:
        print"""                             \"Times change, but our dedication to perfecting the travel experience never will."\

Our highly personalized 24-hour service, combined with authentic, elegant surroundings of the highest quality, embodies a home away from home for those who know

and appreciate the best. As the company has grown from a single hotel to 101 in 42 countries, our deeply instilled culture, personified by our employees, continues

to get stronger. Over more than 50 years, our people have built an unrivalled depth of reliability, trust and connection with our guests – a connection we will

steadfastly uphold, now and always.

                                                                   Service Culture

        Much admired, and not easily replicated, the Five points culture is firmly grounded in our people – in who we are, what we believe and how we behave. Our goals, beliefs and principles are described in the Five points corporate mission statement.
        
        
                                                                  Five points History
Beginning with the launch of the company in 1960, this timeline illustrates milestones in the story of Five points Hotels and Resorts.
 

                                                                    Corporate Bios

Five points senior executives have more combined experience than any other team in our industry. Their stories speak for themselves.

                                                                     Living Values
   
Guided by our shared values, Five points has identified high-priority areas where we believe we can make a difference. This clear vision allows us to work together
most effectively, as individuals, as a company and as a partner.

                                                             COMMITMENT TO AN ETHICAL CULTURE

Five points is committed to conducting business in a manner that complies with applicable laws and is – and is perceived to be – consistent with the highest ethical
standards, including standards intended to prevent bribery and corruption.

 Five points is committed to understanding the risks that may compromise these standards and using all reasonable efforts to ensure that those who provide services to and for Four Seasons – including employees, contractors and agents – are aware of and share our commitment to an ethical and anti-bribery culture.
"""        
        
    elif choice==3:
        break
    else:
        print "Wrong input!"
        print "Please try again!"
        choice=input("\nEnter your Choice --> ")


        
        

        
        
        
            
            
            
        
           
