"""

1. Create a Driver Registration Form

Should have class and must be treated as wild card
Must accept Driver as a parameter and show its ID with picture
"""
from Data import Driver
import tkinter as tk
import os
import datetime
from tkinter import filedialog, messagebox


class Window:
    frame = None
    minimum_age = 18
    canvas = None
    backButton = None
    label = None
    search_driver_btn  = None
    my_driver = Driver.Driver
    color = 'white'
    choose_a_file_text = "Choose a Driver Photo"

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tk = tk.Tk()
        self.canvas = tk.Canvas(self.tk, width=self.width, height=self.height)
        self.frame = tk.Frame(self.tk, bg=self.color, width=self.width, height=self.height)
        # Placing stuff to the screen
        self.tk.title("My Trucking")
        self.tk.iconbitmap(os.getcwd()+"/Images/icon.ico")
        self.canvas.pack()
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)


    def show_main_menu(self, destroy_objects=None):

        self.label = tk.Label(self.frame, bg=self.color, text="Main Menu",  font=("Rouge", 16))

        driver_signup = tk.Button(self.frame, text="Register Driver", font=("Rouge", 16), command=lambda: self.show_driver_signup())
        objects = [self.label, driver_signup]
        self.search_driver_btn = tk.Button(self.frame, text="Search for Driver", font=("Rouge", 16), command=lambda: self.search_driver(objects))
        self.label.place(relx=0, rely=-0.4, relwidth=1, relheight=1)
        driver_signup.place(relx=.15, rely=.2, relwidth=0.3, relheight=0.15)
        self.search_driver_btn.place(relx=.55, rely=.2, relwidth=0.3, relheight=0.15)

        if destroy_objects is not None:
            self.destroy_object(*destroy_objects)
            self.backButton.destroy()

    def show_driver_signup(self):
        self.label = tk.Label(self.frame, bg=self.color, text="Register Driver",  font=("Rouge", 16))
        name = tk.Entry(self.frame, bg=self.color, font=("Rouge", 12))
        name_label = tk.Label(self.frame, bg=self.color, text="Enter Name", font=("Rouge", 14))
        age = tk.Spinbox(self.frame, bg=self.color, from_=self.minimum_age, to=70, font=("Rouge", 12))

        age_label = tk.Label(self.frame, bg=self.color, text="Enter  Age", font=("Rouge", 14))
        dob_label = tk.Label(self.frame, bg=self.color, text="Enter  DOB", font=("Rouge", 14))
        format_text = tk.Label(self.frame, bg=self.color, text='(DD/MM/YYYY)')
        dob_day = tk.Entry(self.frame, bg=self.color, font=("Rouge", 12))

        dob_month = tk.Entry(self.frame, bg=self.color, font=("Rouge", 12))

        dob_year = tk.Entry(self.frame, bg=self.color, font=("Rouge", 12))

        sex_label = tk.Label(self.frame, bg=self.color, text="Choose Gender", font=("Rouge", 14))
        sex = tk.StringVar(self.frame)
        sex.set("Choose A Gender")
        choices = ['Male', 'Female', 'Mai kyo Dassa']
        popupMenu = tk.OptionMenu(self.frame, sex, *choices)
        experience = tk.Spinbox(self.frame, bg=self.color, from_=0, to=100, font=("Rouge", 12))
        experience_label = tk.Label(self.frame, bg=self.color, text="Enter Experience", font=("Rouge", 14))
        address = tk.Entry(self.frame, bg=self.color, font=("Rouge", 12))
        address_label = tk.Label(self.frame, bg=self.color, text="Enter Address", font=("Rouge", 14))
        choose_a_file = tk.Button(self.frame, text=self.choose_a_file_text, command=lambda: self.get_file_path())
        Submit_form = tk.Button(self.frame, text="Submit", font=("Rouge", 12), command=lambda:self.submit_form(name, age, dob_day, dob_month, dob_year, sex, experience, address))
        dob_day.insert(0, datetime.datetime.now().day)
        dob_month.insert(0, datetime.datetime.now().month)
        dob_year.insert(0, datetime.datetime.now().year - self.minimum_age)
        # Things to destroy
        objects = [dob_label, dob_day, dob_year, dob_month, self.label, name, name_label, address, address_label, age, age_label, experience, experience_label, choose_a_file, Submit_form, sex_label, popupMenu]
        self.backButton = tk.Button(self.frame, bg=self.color, text="Go Back to Home", command=lambda: self.show_main_menu(objects))

        #Placing on screen
        self.label.place(relx=0, rely=-0.4, relwidth=1, relheight=1)
        self.backButton.place(relx=0, rely=0, relwidth=0.2, relheight=0.05)
        name.place(relx=0.3, rely=0.3, relheight=0.03, relwidth=0.3)
        age.place(relx=0.3, rely=0.4, relheight=0.03, relwidth=0.3)
        dob_day.place(relx=0.3, rely=0.5, relheight=0.03, relwidth=0.04)
        dob_month.place(relx=0.35, rely=0.5, relheight=0.03, relwidth=0.04)
        dob_year.place(relx=0.4, rely=0.5, relheight=0.03, relwidth=0.06)
        format_text.place(relx=0.50, rely=0.5, relheight=0.03, relwidth=0.1)
        popupMenu.place(relx=0.3, rely=0.6)
        experience.place(relx=0.3, rely=0.7, relheight=0.03, relwidth=0.3)
        address.place(relx=0.3, rely=0.8, relheight=0.03, relwidth=0.3)
        choose_a_file.place(relx=0.3, rely=0.9, relheight=0.03, relwidth=0.3)

        name_label.place(relx=0.01, rely=0.3, relheight=0.03, relwidth=0.2)
        age_label.place(relx=0.001, rely=0.4, relheight=0.03, relwidth=0.2)
        dob_label.place(relx=0.001, rely=0.5, relheight=0.03, relwidth=0.2)
        sex_label.place(relx=0.01, rely=0.6, relheight=0.03, relwidth=0.2)
        experience_label.place(relx=0.03, rely=0.7, relheight=0.03, relwidth=0.2)
        address_label.place(relx=0.02, rely=0.8, relheight=0.03, relwidth=0.2)
        Submit_form.place(relx=0.02, rely=0.9, relheight=0.03, relwidth=0.2)

    def search_driver(self, destroy_object=None):
        #seach box    - Button
        # should show the Driver as a Wild Card
        if destroy_object is not None:
            self.search_driver_btn.destroy()
            self.destroy_object(*destroy_object)

        self.label = tk.Label(self.frame, bg=self.color, text="Search Driver",  font=("Rouge", 16))
        search_bar = tk.Entry(self.frame, font=("Rouge", 16))
        search_btn = tk.Button(self.frame, text="Search", command=lambda: self.find_driver_file(search_bar.get()))
        objects = [self.label, search_bar, search_btn]

        self.backButton = tk.Button(self.frame, bg=self.color, text="Go Back to Home", command=lambda: self.show_main_menu(objects))
        self.label.place(relx=0, rely=-0.4, relwidth=1, relheight=1)
        search_bar.place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.04)
        search_btn.place(relx=0.25, rely=0.25, relwidth=0.1, relheight=0.04)
        self.backButton.place(relx=0, rely=0, relwidth=0.2, relheight=0.05)

    # Search driver pending
    def find_driver_file(self, driver):
        content = []
        try:
            with open(os.getcwd()+"/Drivers/"+driver+"/"+driver+"-info.dat", 'r') as file:
                for i in file.readlines():
                    content.append(i)
        except:
            messagebox.showerror("Error", "File Not Found")

        # Re-implementing this Object to create a new Frame
        id_frame = Window(600, 400)
        id_frame.tk.title(driver)
        id_frame.show_id_card(*content)
        id_frame.start_loop()
        #Saved data from file into array now make it ID card


    def show_id_card(self, *driver):
        gap_x = 100; gap_y = 200
        for i in driver:
            print(i)
            tk.Label(self.frame, text=i).place(x=gap_x, y=gap_y)
            gap_x+=100
            gap_y +=100



    @staticmethod
    def destroy_object(*obj):
        for i in obj:
            i.destroy()

    def submit_form(self, *entry):
        formated_dob = str(str(entry[2].get()) + '-'+ str(entry[3].get()) +'-'+ str(entry[4].get()))
        try:
            os.mkdir(os.getcwd() + "/Drivers/")
        except FileExistsError:
            pass
        try:
            os.mkdir(os.getcwd() + "/Drivers/" + entry[0].get() + " " + formated_dob)
        except:
            pass
        content = []
        for each in entry:
            content.append(each.get())
        self.my_driver = Driver.Driver(*content)
        to_path = os.getcwd()+"/Drivers/"+self.my_driver.name+ " " + str(formated_dob)+"/"
        file_format = ""
        try:
            if str(self.path).endswith(".png"):
                file_format = ".png"
            elif str(self.path).endswith(".jpeg"):
                file_format = ".jpeg"
            elif str(self.path).endswith(".jpg"):
                file_format = ".jpg"
            input_file = open(self.path, 'rb')
            output_file = open(to_path+self.my_driver.name+" "+ formated_dob +"-image"+file_format, 'wb')
            for each in input_file:
                output_file.write(each)
            messagebox.showinfo("Form Submission", "Form has been submitted")
        except:
            messagebox.showerror("Error", "Pick A Profile Picture")
        finally:
            exit(0)

    def get_file_path(self):
        self.path = filedialog.askopenfilename(initialdir=os.getcwd(), title = "Select file",filetypes = (("jpeg files","*.jpeg"),("png files","*.png"), ("jpg files","*.jpg")))
        self.choose_a_file_text = "Driver Picture"
        self.choose_a_file = tk.Label(self.frame, text=self.path[40::])
        self.choose_a_file.place(relx=0.3, rely=0.8, relheight=0.03, relwidth=0.4)

    # Starting the Main loop
    def start_loop(self):
        self.tk.mainloop()
