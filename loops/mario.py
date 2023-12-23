def main():
    # print_collumn(3)
    # print_row(4)
    print_square(5)
    
def print_collumn(height):
    for _ in range(height):
        print("#\n" * height, end="")

def print_row(width):
    print("#" * width)  
    
def print_square(size):
    
    #for each row in square
    for i in range(size - 2):
        print_row(size)
        #for each brick in square
        for j in range(size):
            print("#", end="")
        print()
        
main()