
def email():
    email = input("What's your email? ").strip()
    
    username, domain = email.split("@")
    
    if username and domain.endswith(".edu"):
        print("Valid email!")
    else:
        print("Invalid email!")
    

if __name__ == "__main__":
    email()