print("PUP Enrollment Form")

name = input("Enter your full name: ")
age =  input("Enter your age: ")
previous_gwa = input("Enter your previous general weighted average: ")
is_cloudArchitech = input("Are you a member of the AWS Cloud Club? (yes/no): "). lower() == "yes"
print("")
print("Your Enrollment Form:")
print("Name: ", name)
print("Age: ", age)
print("GWA: ", previous_gwa)
print("Awstraunot: ", is_cloudArchitech)