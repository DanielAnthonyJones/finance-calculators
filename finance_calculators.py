"""
When trying to ask for an input again if the wrong thing is inputted i learned about
try and except instead of trying to if an variable is not equal to a data type and then breaking the loop 
since i tried many different things but they didnt seem to work how i thought they would.

I learned about being able to call upon functions that have been written before which is used to exit the program

What took me the most time was getting things to loop properly since i wrote out the entire code and the basics
of what the task wanted me to do and include quickly then had ideas on how to improve it such as printing out 
all the information in a neat way.

I learned how to do a countdown when i had the idea for an end sequence type thing


"""

# allows the use of functions such as math.pow or math.lower and time.sleep

import math
import time

# an exit function called upon later to end the program

def exit_time(seconds):

    # countdown before exiting program

    while (seconds > 0):
        

         print(f"\nThe program will close in {seconds} seconds.")
         
         time.sleep(1)

         seconds -= 1

    
    print("\nThank you for using this service.")

    time.sleep(2)

    exit()



while True:

        while True:

            # shows the user a menu and asks them to choose either investment or bond

            user_selection = input("\ninvestment - to calculate the amount of interest you'll earn on your investment\nbond       - to calculate the amoount you'll have to pay on a home loan\n\nEnter either \'investment\' or \'bond\' from the menu above to proceed: ").lower()

            # when option is investment, asks user to input the deposit amount

            if (user_selection == 'investment'):
            
                while True:
                    
                    time.sleep(1)

                    try:

                        money_deposit = float(input("\nEnter the amount of money you are depositing: "))

                        break
                    
                    # if the user inputs anything that isnt a number it displays a message and asks for an input again

                    except:

                        pass

                    time.sleep(1)

                    print ("\nPlease enter only numbers and do not include currency signs ")

                # asks user for the interest rate of investment and if numbers arent inputted it asks again

                while True:

                    time.sleep(1)

                    try:

                        investement_interest_rate = float(input("\nEnter the interest rate in %: "))
            
                        break

                    except:
                        
                        pass

                    time.sleep(1)

                    print ("\nPlease enter only numbers and do not include a \'%\' sign ")

                # asks user for the investment number of years and if numbers arent inputted it asks again

                while True:

                    time.sleep(1)

                    try:

                        number_of_years = float(input("\nEnter the number of years you plan on investing for: "))

                        break
                    
                    except:

                        pass

                    time.sleep(1)

                    print("\nPlease enter only numbers")

                # asks user if the interest is simple or compound and will do calculations based on which is chosen, repeats if one of the options isnt chosen
                        
                while True:
            
                    time.sleep(1)

                    interest = input("\nEnter an interest type: \'simple\' or \'compound\': ").lower()

                    # create new variables for the purpose of calculations

                    r = (investement_interest_rate / 100)
                    p = money_deposit
                    t = math.floor(number_of_years)

                    # simple interest calculations, and prints the answer along with prior information inputted

                    if (interest == 'simple'):

                        total_amount = p *(1 + r*t)

                        time.sleep(1)

                        print(f"\n________________________________________\n\nOriginal deposit:\t{round(money_deposit, 2)}\n\nInterest type:\t\tSimple\n\nInterest rate:\t\t{investement_interest_rate}%\n\nYears:\t\t\t{t}\n\nNew amount:\t\t{round(total_amount, 2)}\n________________________________________ ")
                        
                        break

                    # compound interest calculations, and prints the answer along with prior information inputted

                    elif (interest == 'compound'):

                        total_amount = p * math.pow((1+r),t)

                        time.sleep(1)

                        print(f"\n________________________________________\n\nOriginal deposit:\t{round(money_deposit, 2)}\n\nInterest type:\t\tCompound\n\nInterest rate:\t\t{investement_interest_rate}%\n\nYears:\t\t\t{t}\n\nNew amount:\t\t{round(total_amount, 2)}\n________________________________________ ")

                        break

                    else:

                        time.sleep(1)

                        print ("\nPlease enter one of the aforementioned options ")   


                break
                

            # when option chosen is bond, asks user to enter current value of house

            elif (user_selection == 'bond'):
                
                while True:
                    
                    time.sleep(1)

                    try:
                    
                        current_house_value = float(input("\nEnter the current value of the house: "))

                        break

                    # if the user inputs anything that isnt a number it displays a message and asks the user for an input again    
                        
                    except:
                        
                        pass

                    time.sleep(1)

                    print("\nPlease enter only numbers and do not include currency signs ")
                
                # asks the user for bond interest rate

                while True:

                    time.sleep(1)

                    try:

                        bond_interest_rate = float(input("\nEnter the interest rate in %: "))

                        break
                
                    except:

                        pass

                    time.sleep(1)
                        
                    print ("\nPlease enter only numbers and do not include a \'%\' sign ") 

                # asks the user for the number of months they plan to repay for
                
                while True:
                    
                    time.sleep(1)

                    try:

                        number_of_months = float(input("\nEnter the number of months you plan to repay the bond for: "))

                        p = current_house_value
                        i = ((bond_interest_rate/100)/12)
                        n = math.floor(number_of_months)

                        repayment = (i * p)/(1 - (1 + i)**(-n))

                        time.sleep(1)

                        # bond interest calculations, and prints the repayment per month along with prior information inputted

                        print(f"\n________________________________________\n\nCurrent house value:\t{round(current_house_value, 2)}\n\nInterest rate:\t\t{bond_interest_rate}%\n\nMonths:\t\t\t{n}\n\nRepayment plan:\t\t{round(repayment, 2)} per month\n________________________________________ ")

                        break
                    
                    except:

                        pass

                    time.sleep(1)
                    
                    print("\nPlease enter only numbers")
                                
                break

            else:
                print ("\nPlease enter one of the aforementioned options ")

                time.sleep(1)

        time.sleep(1)

        # asks user if they want to use the service again

        while True:

            time.sleep(1)

            restart_service = input("\nWould you like to do another calculation: Enter \'Y\' for Yes or \'N\' for No: ").upper()

            # if they want to use the service again it loops back to the investment and bond selection menu

            if (restart_service == 'Y'):

                time.sleep(1)

                break

            # if they dont want to use the service again it exits the program after a displayed countdown

            elif (restart_service == 'N'):

                time.sleep(1)

                seconds = 5

                # exit function defined at the start of the code

                exit_time(seconds)
                
                break
                
             
            else:

                print ("\nPlease enter one of the aforementioned options ")

  




        
    


