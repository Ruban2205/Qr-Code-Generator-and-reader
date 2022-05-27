from tkinter import *
from tkinter import messagebox
from tkinter import font
from PIL import ImageTk, Image
from tkinter import filedialog
import cv2
import function
import os

print(cv2.getBuildInformation())

# Creating a Window
window = Tk()
window.title("QR-Code Generator and Reader - Ruban Gino Singh")
window.geometry("1350x750")
window.resizable(False, False)
window.iconbitmap("qr-code.ico")


# Function to Show Information message
def showInfo(title, message):
    messagebox.showinfo(title, message)

# Function to show Warning message
def showWarning(title, message):
    messagebox.showwarning(title, message)

#Function to show error message
def showError(title, message):
    messagebox.showerror(title, message)


# Functions
def generateQR(name="display.png"):
    global displayCanvas
    global displayImage

    if textEntry.get(1.0, "end-1c") != "":
        # text = textEntry.get(1.0, "end-1c")
        # image = qrcode.make(text)
        # image.save(name)
        # Imported this above three lines from function.py 

        function.generateForSave(name, text=textEntry.get(1.0, "end-1c"))

        # Below code to display the generated QR
        displayImage = Image.open(name)
        displayImage = displayImage.resize((370, 370))
        displayImage = ImageTk.PhotoImage(displayImage)
        displayCanvas.create_image(185, 185, anchor=CENTER, image=displayImage)
        print(displayImage)

        showInfo("Success!!", "Your Image Generated successfully!! Click Save button to save your image.")

    else:
        showError("Error!!", "Text field is Empty!!")


def saveQR():
    if textEntry.get(1.0, "end-1c") != "":

        fileName = filedialog.asksaveasfilename(
            initialdir="/", title="Save your file...", filetypes=(("PNG File", ".png"), ("All files", "*.*")))

        # Below code to handle Cancel Button while saving the image
        if fileName != "":
            try:
                # generateQR(name=str(fileName + ".png"))
                function.generateForSave(name=str(fileName + ".png"), text=textEntry.get(1.0, "end-1c"))
                showInfo("Image Saved", "Image Saved Successfully!! \nLocation: " + fileName)
                
                textEntry.delete(1.0, END)
                displayCanvas.delete("all")

                print("Save Function executed")
            except:
                pass

            # Below code to call applause-man.png to the canvas.
            displayPNG = Image.open("applause-man.png")
            displayPNG = displayPNG.resize((271, 371))
            displayPNG = ImageTk.PhotoImage(displayPNG)
            displayImg = displayCanvas.create_image(185, 185, anchor=CENTER, image=displayPNG)
            displayCanvas.insert(displayImg)
        else:
            showError("Error!!", "Please choose Location!!")
    else:
        showError('Error!!', "Text box is empty! \nWrite/Create something before save!")


def openQR():
    global displayImage
    global displayCanvas
    global openFileName

    openFileName = filedialog.askopenfilename(initialdir="/", filetypes=(("PNG File", ".png"), ("All Files", "*.*")))

    # Below code to handle the cancel button while open a file
    if openFileName != "":
        displayCanvas.delete("all")
        displayImage = ImageTk.PhotoImage(Image.open(openFileName))
        displayCanvas.create_image(185, 185, anchor=CENTER, image=displayImage)
    else: 
        showError("Error!!", "Please Choose Location!")


def readQR():
    try:
        read = cv2.QRCodeDetector()
        val, _, _ = read.detectAndDecode(cv2.imread(openFileName))
        textEntry.insert(1.0, str(val))
        showInfo("Success!!", "Successfully readed the QR!! \nReaded QR is shown in the text box. \nClick Clear to make another one!")
        print("QR Readed")
    except NameError:
        return showError("Error!!", "Please open the image before your read!")

def clearQR():
    textEntry.delete(1.0, END)
    displayCanvas.delete("all")

    showInfo("Success!!", "Text Box and Display Box are Cleared!! \nClick Generate or Open for further Operations!!")

    # Canvas for Image
    displayPNG = Image.open("hi-man.png")
    displayPNG = displayPNG.resize((369, 314))
    displayPNG = ImageTk.PhotoImage(displayPNG)
    displayImg = displayCanvas.create_image(185, 185, anchor=CENTER, image=displayPNG)   
    displayCanvas.insert(displayImg)

def about():
    showInfo("About QR", "App: QR Generator and Reader\nDeveloped by Ruban Gino Singh\nWebsite: www.rubangino.in\n\nQR Generator and Reader was an Amazing Desktop application to Generate and Read QR codes with one-touch functionality.\n\nWorking Functionality: \n1) Generate Button - Write some texts or links in the text box and click Generate button to generate the QR code. Then the QR code is shown instead of the image displayed on the right.\n2) Save Button - After the QR generated, click the save button to save the image in the preferred location. Please ensure that you can able to save the QR code only after the QR is Generated.\n3) Read Button - Read button is used to read the QR, Please Ensure that the QR must be opened before clicking the read button.\n4) Open Button - Open button is used to open the QR from any of the locations in your system.\n5) Clear Button - Clear button is simply used as a refresh button in this application to refresh the QR code as well as the text box.\n\nThanks for using this application.\n\nWarm love from Ruban Gino Singh - www.rubangino.in")
    print("About function Executed")

def website(): 
    os.system("start \"\" https://rubangino.in")
    print("Website launched successfully!")

# Text - Label
mainTitle = Label(window, text="QR-Code Generator and Reader", font=("Segoe UI", 30, 'bold'))
mainTitle.place(x=424, y=60)

generateText = Label(window, text="Generate", font=("Segoe UI", 30))
generateText.place(x=102, y=173)

footerText = Label(window, text="Developed by: www.rubangino.in", font=("Segoe UI", 20))
footerText.place(x=469, y=663)

# Generate Entry
textEntry = Text(window, font=("Segoe UI", 14))
textEntry.place(x=100, y=281, width=411, height=173)

# Buttons
generateBtn = Button(window, text="Generate", font=('Segoe UI', 14, 'bold'), bg="#1A1A1A", fg="white", command=generateQR)
generateBtn.place(x=102, y=516, width=188, height=61)

saveBtn = Button(window, text="Save", font=('Segoe UI', 14, 'bold'), bg="#1A1A1A", fg="white", command=saveQR)
saveBtn.place(x=325, y=516, width=188, height=61)

readBtn = Button(window, text="Read", font=('Segoe UI', 14, 'bold'), bg="#1A1A1A", fg="white", command=readQR)
readBtn.place(x=548, y=517, width=188, height=61)

openBtn = Button(window, text="Open", font=("Segoe UI", 14, "bold"), bg="#1A1A1A", fg="white", command=openQR)
openBtn.place(x=546, y=281, width=188, height=61)

clearBtn = Button(window, text="Clear", font=("Segoe UI", 14, "bold"), bg="#1A1A1A", fg="white", command=clearQR)
clearBtn.place(x=546, y=393, width=188, height=61)

# Image Button 1
Img1 = Image.open("about.png")
Img1 = Img1.resize((20, 20))
aboutImg = ImageTk.PhotoImage(Img1)
aboutBtn = Button(window, text="About", font=("Segoe UI", 12, "bold"), bg="#D3D3D3", fg="black", image=aboutImg, compound=LEFT, command=about)
aboutBtn.place(x=274, y=650, width=135, height=60)

# Image Button 2
Img2 = Image.open("website.png")
Img2 = Img2.resize((20, 20))
webImg = ImageTk.PhotoImage(Img2)
webBtn = Button(window, text="Website", font=('Segoe UI', 12, 'bold'), bg="#D3D3D3", fg="black", image=webImg, compound=LEFT, command=website)
webBtn.place(x=941, y=650, width=135, height=60)

# Canvas to Display the image
displayCanvas = Canvas(window, width=370, height=370)
displayCanvas.place(x=880, y=190)


# Canvas for Image
displayPNG = Image.open("hi-man.png")
displayPNG = displayPNG.resize((369, 314))
displayPNG = ImageTk.PhotoImage(displayPNG)
displayCanvas.create_image(185, 185, anchor=CENTER, image=displayPNG)

window.mainloop()
