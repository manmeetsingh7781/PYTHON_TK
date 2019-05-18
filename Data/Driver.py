"""
Goal To create a ID card based on GUI
Things it should have

1. Name, age, address, sex, address right side of picture
2. Picture on Left corner

create a folder of driver info and read from it

"""
import os


class Driver:
    name = None
    dob_day, dob_month, dob_year = (None, None, None)

    def __init__(self, name, age, dob_day, dob_month, dob_year, sex, experience, address):
        self.name = name
        self.age = age
        self.sex = sex
        self.dob_day = dob_day
        self.dob_month = dob_month
        self.dob_year = dob_year
        self.experience = experience
        self.address = address
        self.save_info()

    def save_info(self):
        formated_dob = str(str(self.dob_day) + '-'+ str(self.dob_month) +'-'+ str(self.dob_year))
        try:
            os.mkdir(os.getcwd()+"/Drivers/")
        except FileExistsError:
            pass
        try:
            os.mkdir(os.getcwd() + "/Drivers/" + self.name + " " + formated_dob)
        except: pass
        with open(os.getcwd()+"/Drivers/"+str(self.name)+ " " + formated_dob+"/"+self.name+" " + formated_dob+"-info.dat", "w") as f:
            f.write("Name: " + self.name + '\n')
            f.write("Age: " + str(self.age) + '\n')
            f.write("Date Of Birth: " + formated_dob + '\n')
            f.write("Sex: " + self.sex + '\n')
            f.write("Experience: " + str(self.experience) + '\n')
            f.write("Address: " + str(self.address) + '\n')


def get_driver_information(driver):
    return ("Name: " + driver.name
    +"\nAge: " + str(driver.age)
    +"\nSex: " + driver.sex
    +"\nExperience: " + str(driver.experience)
    +"\nAddress: " + str(driver.address))
