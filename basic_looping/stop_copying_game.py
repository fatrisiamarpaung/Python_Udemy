# Stop Copying Me Game where the system will repeat everything until the user says "stop copying me"

message = input("Say Something: ")

#cara 1
while message != "stop copying me":
    print(message)
    message = input()
print("UGH FINE YOU WIN, BROTHER!!")

#cara 2
# while message != "stop copying me":
#     message = input(f"{message}\n") 
# print("UGH FINE YOU WIN, BROTHER!!")