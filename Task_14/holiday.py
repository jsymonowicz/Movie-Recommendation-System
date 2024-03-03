'''
The program calculates the total cost of the user's holidays, including the expenses for the plane, hotel, car rental, and the sum total of these three.
I choose to base the daily cost of a car rental and hotel room on a chosen city. Therefore, my functions 'car_rental' and 'hotel_cost' must have two input values: city and number of days
All prices are in pounds [£].
'''

##### Dictionary with prices for individual cities #####   
#Each city is assigned to an index number and prices [£] per day as follows:
#index: [city name, flight cost, daily hotel cost, daily car rental cost]
city_details = {
    1: ['London', 1239, 560, 23],
    2: ['Paris', 670, 400, 56],
    3: ['Madrid', 450, 180, 78],
    4: ['Warsaw', 230, 220, 45],
    5: ['Berlin', 190, 220, 76]
}

##### Defining functions called in the programme #####
#Function returning total cost for the flight based on a chosen city
def plane_cost(city_flight):
    #Accessing plane cost for a chosen city
    plane_cost = city_details[city_flight][1]
    return (plane_cost)

#Function returning total cost for the hotel stay based on a chosen city and number of days of stay
def hotel_cost(city_flight, num_nights):
    #Accessing daily hotel room cost for a chosen city
    room_per_night = city_details[city_flight][2]
    #Calculating costs
    hotel_cost = room_per_night * num_nights
    return (hotel_cost)

#Function returning total cost for the car rental based on a chosen city and number of rental days
def car_rental(city_flight, rental_days):
    #Accessing daily car rental cost for a chosen city
    car_per_night = city_details[city_flight][3]
    #Calculating costs
    car_rental = car_per_night * rental_days
    return (car_rental)
    
#Function returning total cost for holidays
#This function calls all three of above functions
def holiday_cost(hotel_cost, plane_cost, car_rental):
    holiday_cost = hotel_cost + plane_cost + car_rental
    return (holiday_cost)


##### Main #####
#Print out possible cities to visit
print("Possible cities to visit:")
for i in city_details:
    print(f"{i}\t{city_details[i][0]}")
    
#Define max index number that the user can enter in city selection
max_city_index = len(city_details)

#Input destination city in form of the number (more user friendly)
while True:
#Checking if input value is an integer:
    try:
        city_flight = int(input("Choose the number of the city you are flying to: "))
        #Checking if input value is in city_details length range
        if city_flight >= 1 and city_flight <= max_city_index:
            break
        else:
            print(f"Entered number must be from 1 to {max_city_index}.")
    except ValueError:
        print("Entered value is not a number.")

#Input number of days to stay in the hotel
while True:
#Checking if input value is an integer:
    try:
        num_nights = int(input("Enter number of nights of your stay in a hotel: "))
        #Checking if entered number is none negative
        if num_nights >= 0:
            break
        else:
            print("Entered number is negative!")
    except ValueError:
        print("Entered value is not a number.")
 
#Input number of days for which you will be renting a car
while True:
#Checking if input number is an integer
    try:
        rental_days = int(input("Enter number of days for which you will be renting a car: "))
        #Checking if entered number is none negative
        if rental_days >= 0:
            break
        else:
            print("Entered number is negative!")
    except ValueError:
        print("Entered value is not a number.")

#Accessing the name of the chosen city
city = city_details[city_flight][0]

#Calling functions and calculating expenses
plane_cost = plane_cost(city_flight)
hotel_cost = hotel_cost(city_flight, num_nights)
car_rental = car_rental(city_flight, rental_days)
holiday_cost = holiday_cost(hotel_cost, plane_cost, car_rental)

#Printing out the calculated expenses
print("***")
print(f"Here are the details about your holidays in {city}.")
print(f"The plane cost is £{plane_cost}.")
print(f"The total hotel cost is £{hotel_cost}.")
print(f"The total car rental cost is £{car_rental}.")
print(f"To sum up, the total cost of your holidays is £{holiday_cost}.")