'''
Assignment Description: Given two integers that represent the miles to 
drive forward and the miles to drive in reverse as user inputs, 
create a SimpleCar object that performs the following operations:
1. Drives input number of miles forward
2. Drives input number of miles in reverse
3. Honks the horn
4. Reports car status

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
  
    car = SimpleCar()
    
    forward = int(input())
    backup = int(input())

    car.drive_forward(forward)
    car.drive_reverse(backup)
    car.honk()
    car.status()       
    
    
