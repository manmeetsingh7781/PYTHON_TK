"""
API:
    https://azure.microsoft.com/en-us/services/cognitive-services/bing-web-search-api/
After this try to create a web browser

1. Create a Driver Registration Form

Should have class and must be treated as wild card
Must accept Driver as a parameter and show its ID with picture
"""
from Data import Driver
import os, datetime
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image


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
        self.tk = Tk()
        self.canvas = Canvas(self.tk, width=self.width, height=self.height)
        self.frame = Frame(self.tk, bg=self.color, width=self.width, height=self.height)
        # Placing stuff to the screen
        self.tk.title("My Trucking")
        self.tk.iconbitmap(os.getcwd()+"/Images/icon.ico")
        self.canvas.pack()
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def show_main_menu(self, destroy_objects=None):
        self.label = Label(self.frame, bg=self.color, text="Main Menu",  font=("Rouge", 16))
        driver_signup = Button(self.frame, text="Register Driver", font=("Rouge", 16), command=lambda: self.show_driver_signup())
        objects = [self.label, driver_signup]
        self.search_driver_btn = Button(self.frame, text="Search for Driver", font=("Rouge", 16), command=lambda: self.search_driver(objects))
        self.label.place(relx=0, rely=-0.4, relwidth=1, relheight=1)
        driver_signup.place(relx=.15, rely=.2, relwidth=0.3, relheight=0.15)
        self.search_driver_btn.place(relx=.55, rely=.2, relwidth=0.3, relheight=0.15)
        if destroy_objects is not None:
            self.destroy_object(*destroy_objects)
            self.backButton.destroy()

    def show_driver_signup(self):
        self.label = Label(self.frame, bg=self.color, text="Register Driver",  font=("Rouge", 16))
        name = Entry(self.frame, bg=self.color, font=("Rouge", 12))
        name_label = Label(self.frame, bg=self.color, text="Enter Name", font=("Rouge", 14))
        age = Spinbox(self.frame, bg=self.color, from_=self.minimum_age, to=70, font=("Rouge", 12))
        age_label = Label(self.frame, bg=self.color, text="Enter  Age", font=("Rouge", 14))
        dob_label = Label(self.frame, bg=self.color, text="Enter  DOB", font=("Rouge", 14))
        format_text = Label(self.frame, bg=self.color, text='(DD-MM-YYYY)')
        dob_day = Entry(self.frame, bg=self.color, font=("Rouge", 12))
        dob_month = Entry(self.frame, bg=self.color, font=("Rouge", 12))
        dob_year = Entry(self.frame, bg=self.color, font=("Rouge", 12))
        sex_label = Label(self.frame, bg=self.color, text="Choose Gender", font=("Rouge", 14))
        sex = StringVar(self.frame)
        sex.set("Choose A Gender")
        choices = ['Male', 'Female', 'Mai kyo Dassa']
        popup_menu = OptionMenu(self.frame, sex, *choices)
        experience = Spinbox(self.frame, bg=self.color, from_=0, to=100, font=("Rouge", 12))
        experience_label = Label(self.frame, bg=self.color, text="Enter Experience", font=("Rouge", 14))
        address = Entry(self.frame, bg=self.color, font=("Rouge", 12))
        address_label = Label(self.frame, bg=self.color, text="Enter Address", font=("Rouge", 14))
        choose_a_file = Button(self.frame, text=self.choose_a_file_text, command=lambda: self.get_file_path())
        submit_form = Button(self.frame, text="Submit", font=("Rouge", 12), command=lambda:self.submit_form(name, age, dob_day, dob_month, dob_year, sex, experience, address))
        dob_day.insert(0, datetime.datetime.now().day)
        dob_month.insert(0, datetime.datetime.now().month)
        dob_year.insert(0, datetime.datetime.now().year - self.minimum_age)

        # Things to destroy
        objects = [dob_label, dob_day, dob_year, dob_month, self.label, name, name_label, address, address_label, age, age_label, experience, experience_label, choose_a_file, submit_form, sex_label, popup_menu]
        self.backButton = Button(self.frame, bg=self.color, text="Go Back to Home", command=lambda: self.show_main_menu(objects))

        #Placing on screen
        self.label.place(relx=0, rely=-0.4, relwidth=1, relheight=1)
        self.backButton.place(relx=0, rely=0, relwidth=0.2, relheight=0.05)
        name.place(relx=0.3, rely=0.3, relheight=0.03, relwidth=0.3)
        age.place(relx=0.3, rely=0.4, relheight=0.03, relwidth=0.3)
        dob_day.place(relx=0.3, rely=0.5, relheight=0.03, relwidth=0.04)
        dob_month.place(relx=0.35, rely=0.5, relheight=0.03, relwidth=0.04)
        dob_year.place(relx=0.4, rely=0.5, relheight=0.03, relwidth=0.06)
        format_text.place(relx=0.50, rely=0.5, relheight=0.03, relwidth=0.1)
        popup_menu.place(relx=0.3, rely=0.6)
        experience.place(relx=0.3, rely=0.7, relheight=0.03, relwidth=0.3)
        address.place(relx=0.3, rely=0.8, relheight=0.03, relwidth=0.3)
        choose_a_file.place(relx=0.3, rely=0.9, relheight=0.03, relwidth=0.3)
        name_label.place(relx=0.01, rely=0.3, relheight=0.03, relwidth=0.2)
        age_label.place(relx=0.001, rely=0.4, relheight=0.03, relwidth=0.2)
        dob_label.place(relx=0.001, rely=0.5, relheight=0.03, relwidth=0.2)
        sex_label.place(relx=0.01, rely=0.6, relheight=0.03, relwidth=0.2)
        experience_label.place(relx=0.03, rely=0.7, relheight=0.03, relwidth=0.2)
        address_label.place(relx=0.02, rely=0.8, relheight=0.03, relwidth=0.2)
        submit_form.place(relx=0.02, rely=0.9, relheight=0.03, relwidth=0.2)

    def search_driver(self, destroy_object=None):
        if destroy_object is not None:
            self.search_driver_btn.destroy()
            self.destroy_object(*destroy_object)
        self.label = Label(self.frame, bg=self.color, text="Search Driver",  font=("Rouge", 16))
        search_bar = Entry(self.frame, font=("Rouge", 16))
        search_btn = Button(self.frame, text="Search", command=lambda: self.find_driver_file(search_bar.get()))
        objects = [self.label, search_bar, search_btn]
        self.backButton = Button(self.frame, bg=self.color, text="Go Back to Home", command=lambda: self.show_main_menu(objects))
        self.label.place(relx=0, rely=-0.4, relwidth=1, relheight=1)
        search_bar.place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.04)
        search_btn.place(relx=0.25, rely=0.25, relwidth=0.1, relheight=0.04)
        self.backButton.place(relx=0, rely=0, relwidth=0.2, relheight=0.05)

    # Search driver pending
    def find_driver_file(self, driver):
        content = []
        driver = "cx 2152001"
        optimized_str = ""
        for i in driver:
            if i == "/" or i == "-":
                i = ""
            optimized_str += i
        driver = optimized_str
        # try:
        with open(os.getcwd()+"/Drivers/"+driver+"/"+driver+"-info.dat", 'r') as file:
            for i in file.readlines():
                content.append(i)

        image_link = os.getcwd() + "/Drivers/" + driver + "/" + driver + "-image"+self.get_file_extention(content[-1])
        self.show_id_card(image_link, *content)

        # except:
        #     messagebox.showerror("Error", "user Not Found")

    def show_id_card(self, link, *driver):
        content = ""
        formated_link = ""
        for i in link:
            if i == "\\":
                i = "/"
            formated_link += i
        for i in driver:
            content += i + '\n'
        print(formated_link)
        root = Tk()
        canvas = Canvas(root)
        img = ImageTk.PhotoImage(Image.open(
            "E:/Users/Honey Singh/PycharmProjects/Trucking Software - Manmeet Singh/Data/Drivers/cx 2152001/cx 2152001-image.jpeg"))
        canvas.create_image(0, 100, image=img)
        canvas.pack()
        root.mainloop()
        # frame = Window(600, 600)
        # img = ImageTk.PhotoImage(Image.open("E:/Users/Honey Singh/PycharmProjects/Trucking Software - Manmeet Singh/Data/Drivers/cx 2152001/cx 2152001-image.jpeg"))
        # canvas = tk.Canvas(frame.frame, bg=frame.color, width=600, height=600)
        # canvas.create_text(160, 240, font=("Rouge", 16), text=content)
        # canvas.create_image(0, 100, image=img)
        # canvas.pack()
        # frame.start_loop()
        # Show Image Pending

    def submit_form(self, *entry):
        formated_dob = str(str(entry[2].get()) + str(entry[3].get()) + str(entry[4].get()))
        try:
            os.mkdir(os.getcwd() + "/Drivers/")
        except FileExistsError:
            pass
        try:
            os.mkdir(os.getcwd() + "/Drivers/" + entry[0].get() + " " + formated_dob)
        except:
            pass

        try:
            content = []
            file_format = self.get_file_extention(self.path)
            for each in entry:
                content.append(each.get())

            content.append(file_format)
            self.my_driver = Driver.Driver(*content)
            to_path = os.getcwd() + "/Drivers/" + self.my_driver.name + " " + str(formated_dob) + "/"
            input_file = open(self.path, 'rb')
            output_file = open(to_path+self.my_driver.name+" "+ formated_dob +"-image"+file_format, 'wb')
            for each in input_file:
                output_file.write(each)
            messagebox.showinfo("Form Submission", "Form has been submitted")
        except:
            messagebox.showerror("Error", "Pick A Profile Picture")
        finally:
            exit(0)

    @classmethod
    def get_file_path(cls):
        cls.path = filedialog.askopenfilename(initialdir=os.getcwd(), title = "Select file",filetypes = (("jpeg files","*.jpeg"),("png files","*.png"), ("jpg files","*.jpg")))
        cls.choose_a_file_text = "Driver Picture"
        cls.choose_a_file = Label(cls.frame, text=cls.path[40::])
        cls.choose_a_file.place(relx=0.3, rely=0.9, relheight=0.03, relwidth=0.4)

    @staticmethod
    def get_file_extention(file):
        found = False
        string = ""
        for i in file:
            if i == ".":
                found = True
            if found and i != '\n':
                string += i
        return string

    @staticmethod
    def destroy_object(*obj):
        for i in obj:
            i.destroy()

    # Starting the Main loop
    def start_loop(self):
        self.tk.mainloop()
