import random


def main():

    userInput()
    writingfile()

result = []

def userInput():
        
    try:
        userValue = int(input("Enter Number Of Password, You Need At a Time "))
    except:
        print("\n \t Enter Valid Number or Integer No \n ")

    creating(userValue)


def creating(value):

    if value != None:

        for _ in range(value):

            lower = "abcdefghijklmnopqrstuvwxyz"
            upper = lower.upper()
            number = "0123456789"
            symbol = "!@#$%^&*()"
            All = lower + upper + number + symbol
            length = 16
            passwd = ''.join(random.sample(All, length))  # Generate a stronger password for a user
            passwd = str(passwd)
            result.append(passwd)
            
            print("\tPassword  ", _ + 1, " = ", passwd)
            

def writingfile():

    with open("passWD.txt", 'a') as file:

        for passWord in result:

            file.write(passWord+"\n")
            print("Data Written Sucessfully..")


if __name__ == "__main__":

    main()


