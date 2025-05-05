def linear_search(roll_nos,target):
    for i in range(len(roll_nos)):
        if roll_nos[i] == target:
            return True
    return False
    
def sentinel_search(roll_nos,target):
    roll_nos.append(target)
    
    i=0
    while roll_nos[i] != target:
        i +=1
    roll_nos.pop()
    return i<len(roll_nos)- 1
    
def main():
    roll_nos=[20,30,40,50]
    target=int(input("enter the roll number to be searched"))
     
    if linear_search(roll_nos,target):
        print(f"{target}" " attended the program(linear search)")
    else:
        print(f"{target}" " not attended the program(linear search)")

    if sentinel_search(roll_nos,target):
        print(f"{target}" " attended the program(sentinel search)")
    else:
        print(f"{target}" " not attended the program(sentinel search)")

if __name__=="__main__":
    main()
     

    