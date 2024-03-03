#Ask user to enter the times for events of a triathlon:
swimming = int(input("Enter swimming time in minutes: "))
cycling = int(input("Enter cycling time in minutes: "))
running = int(input("Enter running time in minutes: "))

#Print total time taken to complete triathlon:
total_time = swimming + cycling + running
print(f"Total time taken to complete triathlon was {total_time} min.")

#Calculate received award:
if total_time >= 111:
    print("No award")
elif total_time >= 106:
    print("Your award is: Provincial Scroll")
elif total_time >= 101:
    print("Your award is: Provincial Half Colours")
else:
    print("Your award is: Provincial Colours")