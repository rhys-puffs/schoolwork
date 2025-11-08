# Program ID: second_project.py
# Purpose: Create a concert reservation system
# Revision History: created by Rhys Haskett, November 2025

data = []   #List to hold all the data from the file
concert_hall = [] #2D List to hold the items
temp_list = []  #Temporary list for 5 items at a time
#filename = input("Enter file name to load: ")

def print_2d_list():
    for index, item in enumerate(concert_hall):
        print(f"Row: {index + 1}: {concert_hall[index]}")
    return


def add_reservation(row, column):

    pass

try:

    #file = open(f"{filename}", "r")
    file = open(f"x.txt", "r")
    print("\nFile loaded successfully.\n\n")

    for line in file:
        line = line.strip() #Strips the whitespaces or new lines from each row of data from x.txt

        if line != "":
            data.append(line)

    file.close()

except FileNotFoundError:
    print("Error in loading file, exiting.")

#Iterates through the text file and adds five items at a time into temp_list, before putting the temp_list into the final_list and repeating
for i in data:
    temp_list.append(i)

    if len(temp_list) == 5:
        concert_hall.append(temp_list)
        temp_list = []

print_2d_list()
print("\n\nMain Menu")
print("-------------------------------")
print("1. Add New Reservation")
print("2. Edit Existing Reservation")
print("3. Cancel Reservation")
print("4. Display Seating Chart")
print("5. Save Reservations to a file")
print("6. Exit")
print("-------------------------------")

