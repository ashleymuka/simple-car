'''
Author: Ashley Muka
Assignment Title: Simple Car
Assignment Description: Given two integers that represent the miles to drive forward and the miles to drive in reverse as user inputs, create a SimpleCar object that performs the following operations:
Drives input number of miles forward
Drives input number of miles in reverse
Honks the horn
Reports car status
Due Date:08/23/2023
Date Created:08/23/2023
Date Last Modified:08/23/2023

'''


 
class SimpleCar:
    def __init__(self):
        self.miles = 0

    def drive_forward(self, dist):
        self.miles += dist

    def drive_reverse(self, dist):
        self.miles -= dist

    def honk(self):
        print("beep beep")

    def status(self):
        print(f'Car has driven: {self.miles} miles')


if __name__ == "__main__":

#data abstraction
    
    car = SimpleCar()

#input
    
    forward = int(input())
    backup = int(input())

#process and output

    car.drive_forward(forward)
    car.drive_reverse(backup)
    car.honk()
    car.status()       
    
    
