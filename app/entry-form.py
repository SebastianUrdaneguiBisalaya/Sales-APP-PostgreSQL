import tkinter

window = tkinter.Tk()
window.title("Sales APP")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Information
user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row=0, column=0)

first_name_label = tkinter.Label(user_info_frame, text = "First Name")
first_name_label.grid(row=0, column=0)


# This function allows keep the app running
window.mainloop()