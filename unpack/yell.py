def main():
    yell("This", "is", "CS50")
    
def yell(*words):
    #way 1
    # uppercased = []
    # for word in words:
    #     uppercased.append(word.upper())
    
    #way 2
    # uppercased = map(str.upper, words)
    
    #way 3
    uppercased = [word.upper() for word in words]
    
    print(*uppercased)
        
    
if __name__ == '__main__':
    main()