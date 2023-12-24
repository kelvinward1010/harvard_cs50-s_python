import re



def email_1():
    email = input("What's your email? ").strip()
    
    username, domain = email.split("@")
    
    if username and domain.endswith(".edu"):
        print("Valid email!")
    else:
        print("Invalid email!")
        
def email_2():
    email = input("What's your email? ").strip()
    
    pattern_0 = r"^.+@.+\.edu$"                             #any characters
    pattern_1 = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|edu)$"   #ok@harvard.edu
    pattern_2 = r"^\w+@\w+\.edu$"                           #ok@harvard.edu
    pattern_3 = r"^(\w|\s)+@\w+\.edu$"                      #ok @harvard.edu
    pattern_4 = r"^\w+@\w+\.\w+\.edu$"                      #ok@cs50.harvard.edu
    pattern_5 = r"^\w+@(\w+\.)?\w+\.edu$"                   #ok@cs50.harvard.edu or ok@harvard.edu
    pattern_6 = r"^(\w|\.)+@(\w+\.)?\w+\.edu$"              #ok@cs50.harvard.edu or ok@harvard.edu or ok.123@harvard.edu
    
    if re.search(pattern_6, email, re.IGNORECASE):
        print("Valid email!")
    else:
        print("Invalid email!")
    

if __name__ == "__main__":
    email_2()