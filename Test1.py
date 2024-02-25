# I want to write program that will sign student into the attended.txt to later grade it.


from datetime import datetime

def signInSheet():
    i = 0 # counter
    with open("attended.txt", "a") as file: # open file
        now = datetime.now() # current time
        current_day = now.strftime("%B %d") # date
        file.write("\n\n" + current_day + "\n")

        while True:
            checker = input("If you want to close signin sheet press 0, else press 1: ")
            if checker == "0":
                file.close()
                break
            else:
                userName = input("Please Enter your name: ")
                pittID = input("Enter your pittID: ")
                now = datetime.now()
                current_datetime = now.strftime("%B %d %H:%M")
                print(f"Welcome to the class {userName} at {current_datetime}")

                i += 1
                file.write(f"{i} {userName} {pittID} {current_datetime}\n")

if __name__ == "__main__":
    SignInSheet()
