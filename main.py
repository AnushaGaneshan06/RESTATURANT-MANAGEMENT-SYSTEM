from tkinter import *
from tkinter import filedialog, messagebox
import random
import time
import requests


def reset():
    textReceipt.delete(1.0, END)
    e_Rice.set("0")
    e_Sambar.set("0")
    e_Fish.set("0")
    e_Dosa.set("0")
    e_Idli.set("0")
    e_Vaadai.set("0")
    e_Briyani.set("0")
    e_Parotta.set("0")
    e_Noddles.set("0")

    e_lassi.set("0")
    e_coffee.set("0")
    e_faluda.set("0")
    e_mojito.set("0")
    e_milkshake.set("0")
    e_juice.set("0")
    e_capasino.set("0")
    e_americano.set("0")
    e_softdrinks.set("0")

    e_chocolate.set("0")
    e_oreo.set("0")
    e_apple.set("0")
    e_kitkat.set("0")
    e_vanilla.set("0")
    e_banana.set("0")
    e_brownie.set("0")
    e_pineapple.set("0")
    e_blackforest.set("0")

    textRice.config(state=DISABLED)
    textSambar.config(state=DISABLED)
    textDosa.config(state=DISABLED)
    textIdli.config(state=DISABLED)
    textVaadai.config(state=DISABLED)
    textBriyani.config(state=DISABLED)
    textFish.config(state=DISABLED)
    textParotta.config(state=DISABLED)
    textNoddles.config(state=DISABLED)

    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textmojito.config(state=DISABLED)
    textmilkshake.config(state=DISABLED)
    textjuice.config(state=DISABLED)
    textcapasino.config(state=DISABLED)
    textamericano.config(state=DISABLED)
    textsoftdrinks.config(state=DISABLED)

    textchocolate.config(state=DISABLED)
    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textblackforest.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')


def create_feedback_window():
    root2 = Toplevel()
    root2.title("Feedback Form")
    root2.config(bg='gray')  # Set the background color to gray
    root2.geometry('485x620+50+50')

    # Try to load the feedback image
    try:
        logoImage = PhotoImage(file='feedback.png')  # Update with your feedback image
    except:
        logoImage = None  # Handle missing image

    label = Label(root2, image=logoImage, bg='gray') if logoImage else Label(root2, bg='gray')
    label.pack(pady=5)

    feedbackLabel = Label(root2, text='Feedback', font=('arial', 18, 'bold underline'), bg='gray', fg='black')
    feedbackLabel.pack(pady=5)

    textarea = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
    textarea.pack(pady=5)
    textarea.insert(END, 'Please enter your feedback here...\n')

    def save_feedback():
        feedback = textarea.get(1.0, END).strip()

        # Check if the feedback is not empty and does not contain default text
        if not feedback or feedback == "Please enter your feedback here...":
            messagebox.showerror('Error', 'Feedback cannot be empty or default text.')
            return

        # Open file dialog to save the feedback
        url = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if url:  # Check if a file was actually chosen
            try:
                with open(url, 'w') as file:
                    file.write(feedback)
                messagebox.showinfo("Information", "Your feedback was saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {e}")

    saveButton = Button(root2, text='SAVE FEEDBACK', font=('arial', 19, 'bold'), bg='white', fg='black', bd=7,
                        relief=GROOVE,
                        command=save_feedback)
    saveButton.pack(pady=5)

    root2.mainloop()


def save():
    if textReceipt.get(1.0, END) == "\n":
        pass
    else:
        url = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if url:  # Check if a file was actually chosen
            try:
                with open(url, 'w') as file:
                    bill_data = textReceipt.get(1.0, END)  # Assuming textReceipt is a tkinter Text widget
                    file.write(bill_data)
                messagebox.showinfo("Information", "Your bill saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {e}")


def receipt():
    global billnumber, date
    if costoffoodvar.get() != "" or costofdrinksvar.get() != "" or costofcakesvar.get() != "":
        textReceipt.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = "BILL" + str(x)
        date = time.strftime("%d/%m/%Y")
        textReceipt.insert(END, "Receipt Ref:\t\t" + billnumber + "\t\t" + date + "\n\n")
        textReceipt.insert(END, "******************************************************************\n\n")
        textReceipt.insert(END, "Items:\t\t Cost Of Items(Rs\n")
        textReceipt.insert(END, "******************************************************************\n\n")

        if e_Rice.get() != "0":
            textReceipt.insert(END, f"Rice\t\t\t{int(e_Rice.get()) * 10}\n\n")

        if e_Sambar.get() != '0':
            textReceipt.insert(END, f'Sambar\t\t\t{int(e_Sambar.get()) * 60}\n\n')

        if e_Fish.get() != '0':
            textReceipt.insert(END, f'Fish\t\t\t{int(e_Fish.get()) * 100}\n\n')

        if e_Dosa.get() != '0':
            textReceipt.insert(END, f'Dosa:\t\t\t{int(e_Dosa.get()) * 30}\n\n')

        if e_Idli.get() != '0':
            textReceipt.insert(END, f'Idli:\t\t\t{int(e_Idli.get()) * 50}\n\n')

        if e_Vaadai.get() != '0':
            textReceipt.insert(END, f'Vaadai:\t\t\t{int(e_Vaadai.get()) * 100}\n\n')

        if e_Briyani.get() != '0':
            textReceipt.insert(END, f'Briyani:\t\t\t{int(e_Briyani.get()) * 40}\n\n')

        if e_Parotta.get() != '0':
            textReceipt.insert(END, f'Poratta:\t\t\t{int(e_Parotta.get()) * 120}\n\n')

        if e_Noddles.get() != '0':
            textReceipt.insert(END, f'Noddles:\t\t\t{int(e_Noddles.get()) * 120}\n\n')

        if e_lassi.get() != '0':
            textReceipt.insert(END, f'Lassi:\t\t\t{int(e_lassi.get()) * 50}\n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee:\t\t\t{int(e_coffee.get()) * 40}\n\n')

        if e_faluda.get() != '0':
            textReceipt.insert(END, f'Faluda:\t\t\t{int(e_faluda.get()) * 80}\n\n')

        if e_mojito.get() != '0':
            textReceipt.insert(END, f'mojito:\t\t\t{int(e_mojito.get()) * 30}\n\n')

        if e_milkshake.get() != '0':
            textReceipt.insert(END, f'milkshake:\t\t\t{int(e_milkshake.get()) * 40}\n\n')

        if e_juice.get() != '0':
            textReceipt.insert(END, f'juice:\t\t\t{int(e_juice.get()) * 60}\n\n')

        if e_capasino.get() != '0':
            textReceipt.insert(END, f'capasino:\t\t\t{int(e_capasino.get()) * 20}\n\n')

        if e_americano.get() != '0':
            textReceipt.insert(END, f'americano:\t\t\t{int(e_americano.get()) * 50}\n\n')

        if e_softdrinks.get() != '0':
            textReceipt.insert(END, f'softdrinks:\t\t\t{int(e_softdrinks.get()) * 80}\n\n')

        if e_chocolate.get() != '0':
            textReceipt.insert(END, f'chocolate:\t\t\t{int(e_chocolate.get()) * 400}\n\n')

        if e_oreo.get() != '0':
            textReceipt.insert(END, f'oreo:\t\t\t{int(e_oreo.get()) * 300}\n\n')

        if e_apple.get() != '0':
            textReceipt.insert(END, f'apple:\t\t\t{int(e_apple.get()) * 500}\n\n')

        if e_kitkat.get() != '0':
            textReceipt.insert(END, f'kitkat:\t\t\t{int(e_kitkat.get()) * 450}\n\n')

        if e_vanilla.get() != '0':
            textReceipt.insert(END, f'vanilla:\t\t\t{int(e_vanilla.get()) * 800}\n\n')

        if e_banana.get() != '0':
            textReceipt.insert(END, f'banana:\t\t\t{int(e_banana.get()) * 620}\n\n')

        if e_brownie.get() != '0':
            textReceipt.insert(END, f'brownie:\t\t\t{int(e_brownie.get()) * 700}\n\n')

        if e_pineapple.get() != '0':
            textReceipt.insert(END, f'pineapple:\t\t\t{int(e_pineapple.get()) * 550}\n\n')

        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'blackforest:\t\t\t{int(e_blackforest.get()) * 550}\n\n')
        textReceipt.insert(END, "******************************************************************\n\n")

        if costoffoodvar.get() != "0 Rs":
            textReceipt.insert(END, f"Cost Of Food \t\t\t{priceofFood}Rs\n\n")
        if costoffoodvar.get() != "0 Rs":
            textReceipt.insert(END, f"Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n")
        if costoffoodvar.get() != "0 Rs":
            textReceipt.insert(END, f"Cost Of Cake\t\t\t{priceofCakes}Rs\n\n")

        textReceipt.insert(END, f"Sub Total\t\t\t{subtotalofItems}Rs\n\n")
        textReceipt.insert(END, f"Service Tax\t\t\t{50}Rs\n\n")
        textReceipt.insert(END, f"Total Cost\t\t\t{subtotalofItems + 50}Rs\n\n")
        textReceipt.insert(END, "******************************************************************\n\n")
    else:
        messagebox.showerror("error", "no items are selected")


def totalcost():
    global priceofFood, priceofDrinks, priceofCakes, subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
            var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
            var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
            var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
            var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
            var26.get() != 0 or var27.get() != 0:
        item1 = int(e_Rice.get())
        item2 = int(e_Sambar.get())
        item3 = int(e_Fish.get())
        item4 = int(e_Dosa.get())
        item5 = int(e_Idli.get())
        item6 = int(e_Vaadai.get())
        item7 = int(e_Briyani.get())
        item8 = int(e_Parotta.get())
        item9 = int(e_Noddles.get())

        item10 = int(e_lassi.get())
        item11 = int(e_coffee.get())
        item12 = int(e_faluda.get())
        item13 = int(e_mojito.get())
        item14 = int(e_milkshake.get())
        item15 = int(e_juice.get())
        item16 = int(e_capasino.get())
        item17 = int(e_americano.get())
        item18 = int(e_softdrinks.get())

        item19 = int(e_chocolate.get())
        item20 = int(e_oreo.get())
        item21 = int(e_apple.get())
        item22 = int(e_kitkat.get())
        item23 = int(e_vanilla.get())
        item24 = int(e_banana.get())
        item25 = int(e_brownie.get())
        item26 = int(e_pineapple.get())
        item27 = int(e_blackforest.get())

        priceofFood = ((item1 * 10) + (item2 * 60) + (item3 * 100) + (item4 * 50) + (item5 * 40) + (item6 * 30) + (
                item7 * 120) + (item8 * 100) + (item9 * 120))
        priceofDrinks = (item10 * 50) + (item11 * 40) + (item12 * 80) + (item13 * 30) + (item14 * 40) + (item15 * 60) \
                        + (item16 * 20) + (item17 * 50) + (item18 * 80)
        priceofCakes = (item19 * 400) + (item20 * 300) + (item21 * 500) + (item22 * 550) + (item23 * 450) + (
                item24 * 800) \
                       + (item25 * 620) + (item26 * 700) + (item27 * 550)

        costoffoodvar.set(str(priceofFood) + " Rs")
        costofdrinksvar.set(str(priceofDrinks) + " Rs")
        costofcakesvar.set(str(priceofCakes) + " Rs")

        subtotalofItems = priceofFood + priceofDrinks + priceofCakes
        subtotalvar.set(str(subtotalofItems) + " Rs")

        servicetaxvar.set("50  Rs")

        totalcost = subtotalofItems + 50
        totalcostvar.set(str(totalcost) + " Rs")
    else:
        messagebox.showerror("error", "No items is selected")


# -------------------------------------
# food function
def Rice():
    if var1.get() == 1:
        textRice.config(state=NORMAL)
        textRice.delete(0, END)
        textRice.focus()
    else:
        textRice.config(state=DISABLED)
        e_Rice.set("0")


def Sambar():
    if var2.get() == 1:
        textSambar.config(state=NORMAL)
        textSambar.delete(0, END)
        textSambar.focus()
    else:
        textSambar.config(state=DISABLED)
        e_Sambar.set("0")


def Fish():
    if var3.get() == 1:
        textFish.config(state=NORMAL)
        textFish.delete(0, END)
        textFish.focus()
    else:
        textFish.config(state=DISABLED)
        e_Fish.set("0")


def Dosa():
    if var4.get() == 1:
        textDosa.config(state=NORMAL)
        textDosa.delete(0, END)
        textDosa.focus()
    else:
        textDosa.config(state=DISABLED)
        e_Dosa.set("0")


def Idli():
    if var5.get() == 1:
        textIdli.config(state=NORMAL)
        textIdli.delete(0, END)
        textIdli.focus()
    else:
        textIdli.config(state=DISABLED)
        e_Idli.set("0")


def Vaadai():
    if var6.get() == 1:
        textVaadai.config(state=NORMAL)
        textVaadai.delete(0, END)
        textVaadai.focus()
    else:
        textVaadai.config(state=DISABLED)
        e_Vaadai.set("0")


def Briyani():
    if var7.get() == 1:
        textBriyani.config(state=NORMAL)
        textBriyani.delete(0, END)
        textBriyani.focus()
    else:
        textBriyani.config(state=DISABLED)
        e_Briyani.set("0")


def Parotta():
    if var8.get() == 1:
        textParotta.config(state=NORMAL)
        textParotta.delete(0, END)
        textParotta.focus()
    else:
        textParotta.config(state=DISABLED)
        e_Parotta.set("0")


def Noddles():
    if var9.get() == 1:
        textNoddles.config(state=NORMAL)
        textNoddles.delete(0, END)
        textNoddles.focus()
    else:
        textNoddles.config(state=DISABLED)
        e_Noddles.set("0")


# -----------------------------------------------------------------------------------------------------------------------
def lassi():
    if var10.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0, END)
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set("0")


def coffee():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0, END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set("0")


def faluda():
    if var12.get() == 1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0, END)
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set("0")


def mojito():
    if var13.get() == 1:
        textmojito.config(state=NORMAL)
        textmojito.delete(0, END)
        textmojito.focus()
    else:
        textmojito.config(state=DISABLED)
        e_mojito.set("0")


def milkshake():
    if var14.get() == 1:
        textmilkshake.config(state=NORMAL)
        textmilkshake.delete(0, END)
        textmilkshake.focus()
    else:
        textmilkshake.config(state=DISABLED)
        e_milkshake.set("0")


def juice():
    if var15.get() == 1:
        textjuice.config(state=NORMAL)
        textjuice.delete(0, END)
        textjuice.focus()
    else:
        textjuice.config(state=DISABLED)
        e_juice.set("0")


def capasino():
    if var16.get() == 1:
        textcapasino.config(state=NORMAL)
        textcapasino.delete(0, END)
        textcapasino.focus()
    else:
        textcapasino.config(state=DISABLED)
        e_capasino.set("0")


def americano():
    if var17.get() == 1:
        textamericano.config(state=NORMAL)
        textamericano.delete(0, END)
        textamericano.focus()
    else:
        textamericano.config(state=DISABLED)
        e_americano.set("0")


def softdrinks():
    if var18.get() == 1:
        textsoftdrinks.config(state=NORMAL)
        textsoftdrinks.delete(0, END)
        textsoftdrinks.focus()
    else:
        textsoftdrinks.config(state=DISABLED)
        e_softdrinks.set("0")


# ----------------------------------------------------------------------------------------------------------------------
# cakes
def chocolate():
    if var19.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.delete(0, END)
        textchocolate.focus()
    else:
        textchocolate.config(state=DISABLED)
        e_chocolate.set("0")


def oreocake():
    if var20.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0, END)
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set("0")


def applecake():
    if var21.get() == 1:
        textapple.config(state=NORMAL)
        textapple.delete(0, END)
        textapple.focus()
    else:
        textapple.config(state=DISABLED)
        e_apple.set("0")


def kitkatcake():
    if var22.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0, END)
        textkitkat.focus()
    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set("0")


def vanillacake():
    if var23.get() == 1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0, END)
        textvanilla.focus()
    else:
        textvanilla.config(state=DISABLED)
        e_vanilla.set("0")


def bananacake():
    if var24.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.delete(0, END)
        textbanana.focus()
    else:
        textbanana.config(state=DISABLED)
        e_banana.set("0")


def browniecake():
    if var25.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0, END)
        textbrownie.focus()
    else:
        textbrownie.config(state=DISABLED)
        e_brownie.set("0")


def pineapplecake():
    if var26.get() == 1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0, END)
        textpineapple.focus()
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set("0")


def blackforestcake():
    if var27.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0, END)
        textblackforest.focus()
    else:
        textblackforest.config(state=DISABLED)
        e_blackforest.set("0")


# ----------------------------------------------------------------------------------------------------------------------
root = Tk()

root.geometry("1270x690+0+0")

root.resizable(0, 0)
root.title("RESTAURANT MANAGEMENT SYSTEM")
root.config(bg="gray")

topFrame = Frame(root, bd=10, relief=RIDGE, bg="gray")
topFrame.pack(side=TOP)
labelTitle = Label(topFrame, text="Restaurant Management System", font=("times of roman", 25, "bold"), fg="brown",
                   bd=9, bg="white", width=61)
labelTitle.grid(row=0, column=0)
# --------------------------------------
# frames
menuFrame = Frame(root, bd=10, relief=RIDGE, bg="black")
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg="white", pady=10)
costFrame.pack(side=BOTTOM)
# foods
foodFrame = LabelFrame(menuFrame, text="Food", font=("arial", 19, "bold"), bd=10, relief=RIDGE, fg="brown", bg="white")
foodFrame.pack(side=LEFT)
# drinks
drinksFrame = LabelFrame(menuFrame, text="Drinks", font=("arial", 19, "bold"), bd=10, relief=RIDGE, fg="brown")
drinksFrame.pack(side=LEFT)
# cakes
cakesFrame = LabelFrame(menuFrame, text="Cakes", font=("arial", 19, "bold"), bd=10, relief=RIDGE, fg="brown")
cakesFrame.pack(side=LEFT)
# -------------------------------------------right frame
rightFrame = Frame(root, bd=15, relief=RIDGE, bg="gray")
rightFrame.pack(side=RIGHT)

# calculator
calculatorFrame = Frame(rightFrame, bd=8, relief=RIDGE, bg="gray")
calculatorFrame.pack()

# receipt
receiptFrame = Frame(rightFrame, bd=4, relief=RIDGE, bg="gray")
receiptFrame.pack()

# button
buttonFrame = Frame(rightFrame, bd=3, relief=RIDGE, bg="gray")
buttonFrame.pack()

# ----------------------------------------------------
# VARIABLE DECLARATION
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
# ----------------------------------------------------------
# VARIABLE DECLARATION ENTITIES
e_Rice = StringVar()
e_Sambar = StringVar()
e_Fish = StringVar()
e_Dosa = StringVar()
e_Idli = StringVar()
e_Vaadai = StringVar()
e_Briyani = StringVar()
e_Parotta = StringVar()
e_Noddles = StringVar()
# ------------------------------------------------
# DRINKS ENTITIES VARIABLES
e_lassi = StringVar()
e_coffee = StringVar()
e_faluda = StringVar()
e_mojito = StringVar()
e_milkshake = StringVar()
e_juice = StringVar()
e_capasino = StringVar()
e_americano = StringVar()
e_softdrinks = StringVar()
# --------------------------------------------
# CAKE ENTITIES

e_chocolate = StringVar()
e_oreo = StringVar()
e_apple = StringVar()
e_kitkat = StringVar()
e_vanilla = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_blackforest = StringVar()
# -----------------------------------------------------
# food box inside 0
e_Rice.set("0")
e_Sambar.set("0")
e_Fish.set("0")
e_Dosa.set("0")
e_Idli.set("0")
e_Vaadai.set("0")
e_Briyani.set("0")
e_Parotta.set("0")
e_Noddles.set("0")
# --------------------------------------------------------
# drinks 0 to count
e_lassi.set("0")
e_coffee.set("0")
e_faluda.set("0")
e_mojito.set("0")
e_milkshake.set("0")
e_juice.set("0")
e_capasino.set("0")
e_americano.set("0")
e_softdrinks.set("0")
# ----------------------------------------------------------
# cakes entities
e_chocolate.set("0")
e_oreo.set("0")
e_apple.set("0")
e_kitkat.set("0")
e_vanilla.set("0")
e_banana.set("0")
e_brownie.set("0")
e_pineapple.set("0")
e_blackforest.set("0")
# -----------------------------------------------------------
# down cost var declaration
costoffoodvar = StringVar()
costofdrinksvar = StringVar()
costofcakesvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

# -----------------------------------------------------
# food variety
Rice = Checkbutton(foodFrame, text="Rice", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var1,
                   command=Rice)
Rice.grid(row=0, column=0, sticky=W)

Sambar = Checkbutton(foodFrame, text="Sambar", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var2,
                     command=Sambar)
Sambar.grid(row=1, column=0, sticky=W)

Fish = Checkbutton(foodFrame, text="Fish", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var3,
                   command=Fish)
Fish.grid(row=2, column=0, sticky=W)

Dosa = Checkbutton(foodFrame, text="Dosa", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var4,
                   command=Dosa)
Dosa.grid(row=3, column=0, sticky=W)

Idli = Checkbutton(foodFrame, text="Idli", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var5,
                   command=Idli)
Idli.grid(row=4, column=0, sticky=W)

Vaadai = Checkbutton(foodFrame, text="Vaadai", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var6,
                     command=Vaadai)
Vaadai.grid(row=5, column=0, sticky=W)

Briyani = Checkbutton(foodFrame, text="Briyani", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var7,
                      command=Briyani)
Briyani.grid(row=6, column=0, sticky=W)

Parotta = Checkbutton(foodFrame, text="Parotta", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var8,
                      command=Parotta)
Parotta.grid(row=7, column=0, sticky=W)

Noddles = Checkbutton(foodFrame, text="Noddles", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var9,
                      command=Noddles)
Noddles.grid(row=8, column=0, sticky=W)
# ----------------------------------------------
# ENTITIES FIELD FOR FOOD ITEMS
# ------------------------------------------------

textRice = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_Rice)
textRice.grid(row=0, column=1)

textSambar = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_Sambar)
textSambar.grid(row=1, column=1)

textFish = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_Fish)
textFish.grid(row=2, column=1)

textDosa = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_Dosa)
textDosa.grid(row=3, column=1)

textIdli = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_Idli)
textIdli.grid(row=4, column=1)

textVaadai = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_Vaadai)
textVaadai.grid(row=5, column=1)

textBriyani = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_Briyani)
textBriyani.grid(row=6, column=1)

textParotta = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_Parotta)
textParotta.grid(row=7, column=1)

textNoddles = Entry(foodFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_Noddles)
textNoddles.grid(row=8, column=1)

# --------------------------------------------------------------------------
# DRINKS
# -----------------------------------------------------------------------------
lassi = Checkbutton(drinksFrame, text="lassi", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var10,
                    command=lassi)
lassi.grid(row=0, column=0, sticky=W)

coffee = Checkbutton(drinksFrame, text="coffee", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var11,
                     command=coffee)
coffee.grid(row=1, column=0, sticky=W)

faluda = Checkbutton(drinksFrame, text="faluda", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var12,
                     command=faluda)
faluda.grid(row=2, column=0, sticky=W)

mojito = Checkbutton(drinksFrame, text="mojito", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var13,
                     command=mojito)
mojito.grid(row=3, column=0, sticky=W)

milkshake = Checkbutton(drinksFrame, text="milkshake", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                        variable=var14, command=milkshake)
milkshake.grid(row=4, column=0, sticky=W)

juice = Checkbutton(drinksFrame, text="juice", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var15,
                    command=juice)
juice.grid(row=5, column=0, sticky=W)

capasino = Checkbutton(drinksFrame, text="capasino", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var16,
                       command=capasino)
capasino.grid(row=6, column=0, sticky=W)

americano = Checkbutton(drinksFrame, text="americano", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                        variable=var17, command=americano)
americano.grid(row=7, column=0, sticky=W)

softdrinks = Checkbutton(drinksFrame, text="softdrinks", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                         variable=var18, command=softdrinks)
softdrinks.grid(row=8, column=0, sticky=W)
# -----------------------------------------------------------------------
# DRINKS ENTITIES FOR DRINKS ITEMS
# -------------------------------------------------------------------------
textlassi = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_lassi)
textlassi.grid(row=0, column=1)

textcoffee = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=1, column=1)

textfaluda = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_faluda)
textfaluda.grid(row=2, column=1)

textmojito = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_mojito)
textmojito.grid(row=3, column=1)

textmilkshake = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_milkshake)
textmilkshake.grid(row=4, column=1)

textjuice = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_juice)
textjuice.grid(row=5, column=1)

textcapasino = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_capasino)
textcapasino.grid(row=6, column=1)

textamericano = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_americano)
textamericano.grid(row=7, column=1)

textsoftdrinks = Entry(drinksFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                       textvariable=e_softdrinks)
textsoftdrinks.grid(row=8, column=1)

# ---------------------------------------------------------------------------------------
# CAKES FRAME
# -----------------------------------------------------------------------------------------
chocolate = Checkbutton(cakesFrame, text="chocolate", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var19,
                        command=chocolate)
chocolate.grid(row=0, column=0, sticky=W)

oreocake = Checkbutton(cakesFrame, text="oreo", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var20,
                       command=oreocake)
oreocake.grid(row=1, column=0, sticky=W)

applecake = Checkbutton(cakesFrame, text="apple", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var21,
                        command=applecake)
applecake.grid(row=2, column=0, sticky=W)

kitkatcake = Checkbutton(cakesFrame, text="kitkat", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var22,
                         command=kitkatcake)
kitkatcake.grid(row=3, column=0, sticky=W)

vanillacake = Checkbutton(cakesFrame, text="vanilla", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var23,
                          command=vanillacake)
vanillacake.grid(row=4, column=0, sticky=W)

bananacake = Checkbutton(cakesFrame, text="banana", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var24,
                         command=bananacake)
bananacake.grid(row=5, column=0, sticky=W)

browniecake = Checkbutton(cakesFrame, text="brownie", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var25,
                          command=browniecake)
browniecake.grid(row=6, column=0, sticky=W)

pineapplecake = Checkbutton(cakesFrame, text="pineapple", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                            variable=var26, command=pineapplecake)
pineapplecake.grid(row=7, column=0, sticky=W)

blackforestcake = Checkbutton(cakesFrame, text="blackforest", font=("arial", 18, "bold"), onvalue=1, offvalue=0,
                              variable=var27, command=blackforestcake)
blackforestcake.grid(row=8, column=0, sticky=W)

# -------------------------------------------------------------------------------------
# CAKE ENTITIES BOX
# ----------------------------------------------------------------------------------------

textchocolate = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_chocolate)
textchocolate.grid(row=0, column=1)

textoreo = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
textoreo.grid(row=1, column=1)

textapple = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_apple)
textapple.grid(row=2, column=1)

textkitkat = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_kitkat)
textkitkat.grid(row=3, column=1)

textvanilla = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_vanilla)
textvanilla.grid(row=4, column=1)

textbanana = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_banana)
textbanana.grid(row=5, column=1)

textbrownie = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_brownie)
textbrownie.grid(row=6, column=1)

textpineapple = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=e_pineapple)
textpineapple.grid(row=7, column=1)

textblackforest = Entry(cakesFrame, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED,
                        textvariable=e_blackforest)
textblackforest.grid(row=8, column=1)
# ----------------------------------------------------------------------------------------------------------------------
# COST LABELS $ ENTRY FIELD
# ----------------------------------------------------------------------------------------------------------------------
# food cost
# ----------
labelCostofFood = Label(costFrame, text="Cost of Foods", font=("arial", 16, "bold"), bg="white", fg="black")
labelCostofFood.grid(row=0, column=0)

textCostofFood = Entry(costFrame, font=("arial", 16, "bold"), bd=6, width=14, state="readonly",
                       textvariable=costoffoodvar)
textCostofFood.grid(row=0, column=1, padx=36)
# --------------------------------------------------------------------------------------------------------------------
# drinks cost
# ---------------
labelCostofDrinks = Label(costFrame, text="Cost of Drinks", font=("arial", 16, "bold"), bg="white", fg="black")
labelCostofDrinks.grid(row=1, column=0)

textCostofDrinks = Entry(costFrame, font=("arial", 16, "bold"), bd=6, width=14, state="readonly",
                         textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1, column=1, padx=36)
# ---------------
# cakes cost
# ---------------
labelCostofCakes = Label(costFrame, text="Cost of Cakes", font=("arial", 16, "bold"), bg="white", fg="black")
labelCostofCakes.grid(row=2, column=0)

textCostofCakes = Entry(costFrame, font=("arial", 16, "bold"), bd=6, width=14, state="readonly",
                        textvariable=costofcakesvar)
textCostofCakes.grid(row=2, column=1, padx=36)
# ----------------------------------------------------------------------------------------------------------------------
# SUBTOTAL
labelSubTotal = Label(costFrame, text="SubTotal", font=("arial", 16, "bold"), bg="white", fg="black")
labelSubTotal.grid(row=0, column=2)

textSubTotal = Entry(costFrame, font=("arial", 16, "bold"), bd=6, width=14, state="readonly", textvariable=subtotalvar)
textSubTotal.grid(row=0, column=3, padx=36)
# ----------------------------------------------------------------------------------------------------------------------
# tax cost
labelServiceTax = Label(costFrame, text="ServiceTax", font=("arial", 16, "bold"), bg="white", fg="black")
labelServiceTax.grid(row=1, column=2)

textServiceTax = Entry(costFrame, font=("arial", 16, "bold"), bd=6, width=14, state="readonly",
                       textvariable=servicetaxvar)
textServiceTax.grid(row=1, column=3, padx=36)
# -----------------------------------------------------------------------------------------------------------------------
# total cost
labelTotalCost = Label(costFrame, text="Total Cost", font=("arial", 16, "bold"), bg="white", fg="black")
labelTotalCost.grid(row=2, column=2)

textTotalCost = Entry(costFrame, font=("arial", 16, "bold"), bd=6, width=14, state="readonly",
                      textvariable=totalcostvar)
textTotalCost.grid(row=2, column=3, padx=36)
# ----------------------------------------------------------------------------------------------------------------------
# buttons
buttonTotal = Button(buttonFrame, text="Total", font=("arial", 14, "bold"), fg="white", bg="black", bd=3, padx=5,
                     command=totalcost)
buttonTotal.grid(row=0, column=0)
# receipt
buttonReceipt = Button(buttonFrame, text="Receipt", font=("arial", 14, "bold"), fg="white", bg="black", bd=3, padx=5,
                       command=receipt)
buttonReceipt.grid(row=0, column=1)
# save
buttonSave = Button(buttonFrame, text="Save", font=("arial", 14, "bold"), fg="white", bg="black", bd=3, padx=5,
                    command=save)
buttonSave.grid(row=0, column=2)
# feedback
buttonFeedback = Button(buttonFrame, text="Feedback", font=("arial", 14, "bold"), fg="white", bg="black", bd=3, padx=5,
                        command=create_feedback_window)
buttonFeedback.grid(row=0, column=3)
# reset
buttonReset = Button(buttonFrame, text="Reset", font=("arial", 14, "bold"), fg="white", bg="black", bd=3, padx=5,
                     command=reset)  # Note the lowercase 'command' here
buttonReset.grid(row=0, column=4)
# buttonReset.grid(row=0, column=4)
# TEXT AREA
textReceipt = Text(receiptFrame, font=("arial", 12, "bold"), bd=3, width=44, height=14)
textReceipt.grid(row=0, column=0)
# ----------------------------------------------------------------------------------------------------------------------
# CALCULATOR
# ----------------------------------------------------------------------------------------------------------------------
operator = ""  # hold the value


def buttonClick(numbers):
    global operator
    operator = operator + numbers
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)


def clear():
    global operator
    operator = ""
    calculatorField.delete(0, END)


def answer():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0, END)
    calculatorField.insert(0, result)
    operator = ""


calculatorField = Entry(calculatorFrame, font=("arial", 16, "bold"), width=33, bd=4)
calculatorField.grid(row=0, column=0, columnspan=4)

button7 = Button(calculatorFrame, text="7", font=("arial", 16, "bold"), fg="black", bg="gray", bd=6, width=6,
                 command=lambda: buttonClick("7"))
button7.grid(row=1, column=0)

button8 = Button(calculatorFrame, text="8", font=("arial", 16, "bold"), fg="black", bg="gray", bd=6, width=6,
                 command=lambda: buttonClick("8"))
button8.grid(row=1, column=1)

button9 = Button(calculatorFrame, text="9", font=("arial", 16, "bold"), fg="black", bg="gray", bd=6, width=6,
                 command=lambda: buttonClick("9"))
button9.grid(row=1, column=2)

buttonPlus = Button(calculatorFrame, text="+", font=("arial", 16, "bold"), fg="black", bg="gray", bd=6, width=6,
                    command=lambda: buttonClick("+"))
buttonPlus.grid(row=1, column=3)

button4 = Button(calculatorFrame, text="4", font=("arial", 16, "bold"), fg="black", bg="gray", bd=6, width=6,
                 command=lambda: buttonClick("4"))
button4.grid(row=2, column=0)

button5 = Button(calculatorFrame, text="5", font=("arial", 16, "bold"), fg="black", bg="gray", bd=6, width=6,
                 command=lambda: buttonClick("5"))
button5.grid(row=2, column=1)

button6 = Button(calculatorFrame, text="6", font=("arial", 16, "bold"), fg="black", bg="gray", bd=6, width=6,
                 command=lambda: buttonClick("6"))
button6.grid(row=2, column=2)

buttonMinus = Button(calculatorFrame, text="-", font=("arial", 16, "bold"), fg="black", bg="gray", bd=6, width=6,
                     command=lambda: buttonClick("-"))
buttonMinus.grid(row=2, column=3)

button1 = Button(calculatorFrame, text="1", font=("arial", 16, "bold"), fg="black", bg="gray", bd=6, width=6,
                 command=lambda: buttonClick("1"))
button1.grid(row=3, column=0)

button2 = Button(calculatorFrame, text="2", font=("arial", 16, "bold"), fg="black", bg="gray", bd=6, width=6,
                 command=lambda: buttonClick("2"))
button2.grid(row=3, column=1)

button3 = Button(calculatorFrame, text="3", font=("arial", 16, "bold"), fg="black", bg="gray", bd=6, width=6,
                 command=lambda: buttonClick("3"))
button3.grid(row=3, column=2)

buttonMul = Button(calculatorFrame, text="*", font=("arial", 16, "bold"), fg="black", bg="gray", bd=6, width=6,
                   command=lambda: buttonClick("*"))
buttonMul.grid(row=3, column=3)

buttonAns = Button(calculatorFrame, text="Ans", font=("arial", 16, "bold"), fg="white", bg="black", bd=6, width=6,
                   command=answer)
buttonAns.grid(row=4, column=0)

buttonClear = Button(calculatorFrame, text="Clear", font=("arial", 16, "bold"), fg="white", bg="black", bd=6, width=6,
                     command=clear)
buttonClear.grid(row=4, column=1)

button0 = Button(calculatorFrame, text="0", font=("arial", 16, "bold"), fg="white", bg="black", bd=6, width=6,
                 command=lambda: buttonClick("0"))
button0.grid(row=4, column=2)

buttonDiv = Button(calculatorFrame, text="/", font=("arial", 16, "bold"), fg="white", bg="black", bd=6, width=6,
                   command=lambda: buttonClick("/"))
buttonDiv.grid(row=4, column=3)

root.mainloop()
