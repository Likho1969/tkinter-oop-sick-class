# Likho Kapesi

# importing everything in the tkinter module
from tkinter import *
from tkinter import messagebox    # importing the messagebox from the tkinter module

root = Tk()    # creating a window
root.title("StudentNo: 1200066350054: Likho Kapesi")
root.geometry("600x500")    # setting the window size
root.config(bg="tan")     # changing the window background-color

# Sick-class program that will implement the concept of inheritance using the Sick superclass
# and Influenza and Cancer subclasses


class Sick:    # creating Sick superclass

    """Sick Class, initializing the variables to be derived by the subclasses"""

    def __init__(self):

        # Creating Label Widgets

        # creating app_heading Label
        self.app_heading = Label(root, text="CANCER SCAN  &  INFLUENZA CONSULTATION", fg="red", height=2, bg="black", font=70)
        self.app_heading.place(x=120, y=20)   # positioning the app_heading Label

        self.sickness_code = Label(root, text="Sickness Code:", bg="tan")  # creating sickness_code Label
        self.sickness_code.place(x=25, y=90, anchor="w")  # positioning the sickness_code Label

        # creating treatment_duration Label
        self.treatment_duration = Label(root, text="Duration of Treatment:", bg="tan")
        self.treatment_duration.place(x=25, y=130, anchor="w")  # positioning the treatment_duration Label

        self.duration_unit = Label(root, text="Weeks/Months", bg="tan")  # creating duration_unit Label
        self.duration_unit.place(x=390, y=120)    # positioning the duration_unit Label

        self.doc_rac_num = Label(root, text="Doctor's Practice Number:", bg="tan")  # creating doc_rac_num Label
        self.doc_rac_num.place(x=25, y=170, anchor="w")  # positioning the doc_rac_num Label

        self.fee = Label(root, text="Scan/Consultation Fee:", bg="tan")   # creating fee Label
        self.fee.place(x=25, y=210, anchor="w")  # positioning the fee Label

        # creating amount_paid_label Label
        self.amount_paid_label = Label(root, text="Amount paid for treatment:", bg="yellow")
        self.amount_paid_label.place(x=25, y=350)  # positioning the amount_paid_label Label

        # Creating Entry Widgets

        self.sick_id = Entry(root)  # creating sick_id Entry
        self.duration = Entry(root, width=10)  # creating duration Entry
        self.doc_id = Entry(root)   # creating doc_id Entry
        self.scan_or_consult = Entry(root)  # creating scan_or_consult Entry

        self.sick_id.place(x=300, y=80)  # positioning the sick_id Entry
        self.duration.place(x=300, y=120)  # positioning the duration Entry
        self.doc_id.place(x=300, y=160)  # positioning the doc_id Entry
        self.scan_or_consult.place(x=300, y=200)  # positioning the scan_or_consult Entry

        self.v = IntVar()

        # creating cancer_radio Radiobutton
        self.cancer_radio = Radiobutton(root, text="Cancer", variable=self.v, value=1, bg="blue", fg="white")

        # creating influenza_radio Radiobutton
        self.influenza_radio = Radiobutton(root, text="Influenza", variable=self.v, value=2, bg="navy", fg="white")

        self.cancer_radio.place(x=180, y=280)  # positioning the cancer_radio Radiobutton
        self.influenza_radio.place(x=290, y=280)  # positioning the influenza_radio Radiobutton

        # defining a function that will evaluate the user's choice/ option using the get() method
        def calculate():
            radio = self.v.get()
            if radio == 1:
                self.can = Cancer(self.scan_or_consult.get())

            elif radio == 2:
                self.flu = Influenza(self.scan_or_consult.get())

        # creating calc_btn Button and giving it the calculate() function
        calc_btn = Button(root, text="Calculate", command=calculate, bg="lime", width=10)
        calc_btn.place(x=25, y=420)   # positioning the calc_btn Button

        # defining a function to clear the input from a user
        def clear():
            self.sick_id.delete(0, 'end')
            self.duration.delete(0, 'end')
            self.doc_id.delete(0, 'end')
            self.scan_or_consult.delete(0, 'end')

        # creating the clear_btn Button and assigning it the clear() function
        clear_btn = Button(root, text="Clear", command=clear, bg="orange", width=10)
        clear_btn.place(x=225, y=420)  # positioning the clear_btn Button


# derived/ child class of the Sick super/ parent class
class Cancer(Sick):     # passing the parent class (Sick class) as a parameter

    """Cancer Scan fee and Amount Paid for Treatment"""

    def __init__(self, scan):
        super().__init__()    # giving access to methods/ attributes of the parent (Sick class) class
        self.amount_paid_display = Label(root, text="")
        self.amount_paid_display.place(x=210, y=350)
        self.medication = 400
        self.scan = scan

        if float(scan) > 600:
            messagebox.showerror("", "Sorry we cannot treat you")
        else:
            self.amount_paid = float(self.scan) + self.medication
            self.amount_paid_display.config(text="R "+str(round(self.amount_paid, 4)))


# derived/ child class of the Sick super/ parent class
class Influenza(Sick):    # passing the parent class (Sick class) as a parameter

    """Influenza Consultation fee and Amount Paid for Treatment"""

    def __init__(self, consult):
        super().__init__()     # giving access to methods/ attributes of the parent (Sick class) class
        self.x = StringVar()
        self.amount_paid_display = Label(root, textvariable=self.x)
        self.amount_paid_display.place(x=210, y=350)
        self.medication = 350.50
        self.consult = consult
        self.consult = float(consult)

        if self.consult > 600:
            self.consult = 0.98*self.consult
            self.amount_paid = float(self.consult) + self.medication
            self.x.set("R "+str(round(self.amount_paid, 2))+"")
        else:
            self.amount_paid = float(self.consult) + self.medication
            self.x.set("R "+str(round(self.amount_paid, 2))+"")

    # creating exit_btn Button and assigning it the destroy() method
    exit_btn = Button(root, text="Exit", command=root.destroy, bg="red", width=10)
    exit_btn.place(x=425, y=420)  # positioning the exit_btn Button


# instantiating the Sick class
obj_sick = Sick()

# start the app
root.mainloop()
