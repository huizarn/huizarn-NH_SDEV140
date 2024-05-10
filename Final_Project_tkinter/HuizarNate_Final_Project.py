from tkinter import *
from PIL import ImageTk,Image

'''
root: This variable holds the main window of the application.
root = Tk() # Creates the main window using Tkinter.
home_image: This variable holds the image displayed on the home screen.
home_image = ImageTk.PhotoImage(Image.open("KCC.png")) # Loads the image for the home screen.
selections: This dictionary variable stores selections made by the user during the ordering process.
selections = {"order_type": "", "style": "", "size": "", "toppings": []} # Dictionary to store selections made by the user during the ordering process.

def select_order_type(order_type): # Function to handle the selection of order type (Dine-in or Carry out).
def order_style(): # Function to select the ice cream style (Cone or Sundae).
def order_size(): # Function to select the size of the ice cream.
def order_toppings(): # Function to select toppings for the ice cream.
def order_review(): # Function to review the ice cream order before submission.
def submit(): # Function to submit the ice cream order.
GUI elements:
welcome, in_or_out, in_order, out_order, exit_order, home_img: Labels and buttons displayed on the main window.
GUI elements such as labels, buttons, and list boxes are created and placed within different windows or frames to interact with the user.'''


# Initialize the main Tkinter window
root = Tk()
root.title("Kevin's Creamy Confections")

# This disables the maximize button
root.resizable(0, 0)  

# Load the image for the home screen
home_image = ImageTk.PhotoImage(Image.open("KCC.png"))

# Dictionary to store selections made by the user during the ordering process
selections = {"order_type": "", "style": "", "size": "", "toppings": []}

def select_order_type(order_type):
    """
    Function to handle the selection of order type (Dine-in or Carry out).

    Args:
    order_type (str): The type of order selected by the user.
    """
    selections["order_type"] = order_type
    order_style()

def order_style():
    """
    Function to select the ice cream style (Cone or Sundae).
    """
    # Create a new window for selecting the ice cream style
    window = Toplevel()
    window.resizable(0, 0)
    window.title("Kevin's Creamy Confections")

    # GUI elements for selecting style
    choose_your_style = Label(window, text="Kevin's Creamy Confections. \n Please choose your style!", font=5)
    choose_your_style.grid(row=0, columnspan=2)

    # Button for selecting Cone style
    cone = Button(window, text="Cone", command=lambda: select_style("Cone"), height=5, width=10)
    cone.grid(row=2, column=0, pady=5)

    # Button for selecting Sundae style
    sundae = Button(window, text="Sundae", command=lambda: select_style("Sundae"), height=5, width=10)
    sundae.grid(row=2, column=1, pady=5)

    # Buttons for navigation
    return_screen = Button(window, text="Return to previous screen", command=window.destroy)
    return_screen.grid(row=3, columnspan=2, pady=5)

    exit_order = Button(window, text="Cancel and close order", command=root.destroy)
    exit_order.grid(row=4, columnspan=2, pady=5)

    def select_style(style):
        """
        Function to handle the selection of ice cream style.

        Args:
        style (str): The style of ice cream selected by the user.
        """
        selections["style"] = style
        order_size()

def order_size():
    """
    Function to select the size of the ice cream.
    """
    # Create a new window for selecting the ice cream size
    window = Toplevel()
    window.resizable(0, 0)
    window.title("Kevin's Creamy Confections")

    # GUI elements for selecting size
    choose_your_size = Label(window, text="Kevin's Creamy Confections. \n Please choose your size!", font=5)
    choose_your_size.grid(row=0, columnspan=3)

    # Buttons for selecting different scoop sizes
    scoop1 = Button(window, text="One Scoop", command=lambda: select_size("One Scoop"), height=5, width=10)
    scoop1.grid(row=2, column=0, pady=5)

    scoop2 = Button(window, text="Two Scoops", command=lambda: select_size("Two Scoops"), height=5, width=10)
    scoop2.grid(row=2, column=1, pady=5)

    scoop3 = Button(window, text="Three Scoops", command=lambda: select_size("Three Scoops"), height=5, width=10)
    scoop3.grid(row=2, column=2, pady=5)

    # Buttons for navigation
    return_screen = Button(window, text="Return to previous screen", command=window.destroy)
    return_screen.grid(row=3, columnspan=3, pady=5)

    exit_order = Button(window, text="Cancel and close order", command=root.destroy)
    exit_order.grid(row=4, columnspan=3, pady=5)

    def select_size(size):
        """
        Function to handle the selection of ice cream size.

        Args:
        size (str): The size of ice cream selected by the user.
        """
        selections["size"] = size
        order_toppings()

def order_toppings():
    """
    Function to select toppings for the ice cream.
    """
    # Create a new window for selecting toppings
    window = Toplevel()
    window.resizable(0, 0)
    window.title("Kevin's Creamy Confections")

    # GUI elements for selecting toppings
    choose_your_toppings = Label(window, text="Kevin's Creamy Confections. \n Please choose your toppings!", font=5)
    choose_your_toppings.grid(row=0, columnspan=3)

    # Listbox to display available toppings
    toppings = Listbox(window, selectmode="multiple")
    toppings.config(width=0,height=0)
    items = ["Nuts", "Chocolate", "Strawberry and pineapple syrup", "Whip cream", "Sprinkles", "Sugar cookies", "Bananas", "Cherry on top"]
    for item in items:
        toppings.insert(END, item)
    toppings.grid(row=1, columnspan=3)

    # Button to proceed to review the order
    review_order = Button(window, text="Review Order", command=lambda: [select_toppings(), order_review()])
    review_order.grid(row=2, columnspan=3, pady=5)

    # Buttons for navigation
    return_screen = Button(window, text="Return to previous screen", command=window.destroy)
    return_screen.grid(row=3, columnspan=3, pady=5)

    exit_order = Button(window, text="Cancel and close order", command=root.destroy)
    exit_order.grid(row=4, columnspan=3, pady=5)

    def select_toppings():
        """
        Function to handle the selection of toppings.
        """
        selections["toppings"] = [items[i] for i in toppings.curselection()]

def order_review():
    """
    Function to review the ice cream order before submission.
    """
    # Create a new window for reviewing the order
    window = Toplevel()
    window.resizable(0, 0)
    window.title("Kevin's Creamy Confections")

    # GUI elements for reviewing the order
    review = Label(window, text="Kevin's Creamy Confections. \n Please review your order below!", font=5)
    review.grid(row=0, columnspan=3)

    order_type_label = Label(window, text=f"Order Type: {selections['order_type']}")
    order_type_label.grid(row=1, columnspan=3)

    style_label = Label(window, text=f"Style: {selections['style']}")
    style_label.grid(row=2, columnspan=3)

    size_label = Label(window, text=f"Size: {selections['size']}")
    size_label.grid(row=3, columnspan=3)

    # Display selected toppings, if any
    if not selections["toppings"]:
        toppings_label = Label(window, text="Toppings: No toppings added")
        toppings_label.grid(row=4, columnspan=3)
    else:
        toppings_label = Label(window, text=f"Toppings: {', '.join(selections['toppings'])}")
        toppings_label.grid(row=4, columnspan=3)

    # Button to submit the order
    submit_order = Button(window, text="Submit Order", command=submit)
    submit_order.grid(row=5, columnspan=3, pady=5)

    # Buttons for navigation
    return_screen = Button(window, text="Return to previous screen", command=window.destroy)
    return_screen.grid(row=6, columnspan=3, pady=5)

    exit_order = Button(window, text="Cancel and close order", command=root.destroy)
    exit_order.grid(row=7, columnspan=3, pady=5)

def submit():
    """
    Function to submit the ice cream order.
    """
    # Create a new window to confirm order submission
    window = Toplevel()
    window.resizable(0, 0)
    window.title("Kevin's Creamy Confections")

    # GUI elements for submission confirmation
    review = Label(window, text="Kevin's Creamy Confections. \n Your order was submitted!", font=5)
    review.grid(row=1, columnspan=3)

    # Button to close the window and return to main screen
    exit_order = Button(window, text="Cancel and close order", command=root.destroy)
    exit_order.grid(row=2, columnspan=3, pady=5)

    # Display home image
    home_img = Label(window, image=home_image)
    home_img.grid(row=0, columnspan=3)

# GUI elements for the main screen
welcome = Label(root, text="Welcome to Kevin's Creamy Confections. \n Please place your order!", font=5)
welcome.grid(row=1, columnspan=2)

in_or_out = Label(root, text="Dine-in or Carry out?", font=1)
in_or_out.grid(row=2, columnspan=2, pady=5)

# Button for selecting Dine-in option
in_order = Button(root, text="Dine-in", command=lambda: select_order_type("Dine-in"), height=5, width=10)
in_order.grid(row=3, column=0, pady=5)

# Button for selecting Carry out option
out_order = Button(root, text="Carry out", command=lambda: select_order_type("Carry out"), height=5, width=10)
out_order.grid(row=3, column=1, pady=5)

# Button to cancel the order and close the application
exit_order = Button(root, text="Cancel", command=root.destroy)
exit_order.grid(row=4, columnspan=2, pady=5)

# Display home image
home_img = Label(root, image=home_image)
home_img.grid(row=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()