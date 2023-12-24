import re

def format_1():
    name = input("What's your name? ").strip()
    
    parttent_1 = r"^(.+), (.+)$"
    parttent_2 = r"^(.+), ?(.+)$"
    parttent_3 = r"^(.+), *(.+)$"
    
    matches = re.search(parttent_3, name)
    
    #:= is help me like belown
    if matches := re.search(parttent_3, name):
        #first, last = matches.groups()
        #name = f"{first} {last}"
        
        name = matches.group(1) + " " + matches.group(2)
    
    print(f"Hello, world! {name}")
    
    
if __name__ == "__main__":
    format_1()