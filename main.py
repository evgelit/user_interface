from tkinter import *
from tkextrafont import Font
import pyglet

pyglet.font.add_file("Inika.ttf")
pyglet.font.add_file("Inter.ttf")
window = Tk()

def label(window, text, size, x, y, width, height):
    font = Font(family="Inter", size=size)
    label_frame = Frame(window, borderwidth=0, relief=SOLID, width=width, height=height, bg='#D9D9E2')
    label_frame.place(x=(x + width / 2), y=(y + height / 2), anchor=CENTER)

    _label = Label(label_frame, text=text, font=font)
    _label.place(anchor=CENTER, x=width / 2, y=height / 2)


def button(window, text, size, x, y, width, height, bg, fg):
    font = ("Inter.ttf", size)
    button_frame = Frame(window, borderwidth=0, relief=SOLID, width=width, height=height,bg='#D9D9E2')
    button_frame.place(x=(x + width / 2), y=(y + height / 2), anchor=CENTER)
    button_frame.pack_propagate(False)

    button = Button(button_frame, text=text, bg=bg, fg=fg, relief=FLAT)
    button.configure(font=font)
    button.pack(fill="both")

window.title('Desktop 1')
window.geometry("1440x1024")
window.configure(bg='#D9D9E2')

label(window, "NAME", 35, 85, 27, 130, 42)
label(window, "desktop wallet", 20, 53, 70, 200, 28)

label(window, "Title", 20, 416, 26, 71, 35)
label(window, "Balance", 20, 679, 26, 119, 35)
label(window, "Value", 20, 879, 26, 82, 35)
label(window, "Price", 20, 1036, 26, 82, 35)

button(window, "USD", 15, 163, 106, 51, 42, "#3E3E3E", "#FFFFFF")
label(window, "0.00", 20, 63, 100, 90, 56)

button(window, "Wallet", 30, 27, 242, 219, 56, "#3E3E3E", "#FFFFFF")
button(window, "Buy crypto", 30, 27, 318, 219, 56, "#3E3E3E", "#FFFFFF")
button(window, "Exchange", 30, 27, 397, 219, 56, "#3E3E3E", "#FFFFFF")

button(window, "Settings", 30, 27, 858, 219, 56, "#3E3E3E", "#FFFFFF")
button(window, "Exit", 30, 27, 935, 219, 56, "#3E3E3E", "#FFFFFF")

button(window, "", 30, 291, 90, 1125, 78, "#767676", "#3E3E3E")
label(window, "Tether USDT", 20, 394, 109, 187, 35)
label(window, "0 USDT", 20, 681, 109, 114, 35)
label(window, "$ 0", 20, 895, 109, 51, 35)
label(window, "$ 0", 20, 1046, 109, 51, 35)

button(window, "", 30, 291, 187, 1125, 78, "#767676", "#3E3E3E")
label(window, "Tron", 20, 394, 207, 187, 35)
label(window, "0 TRX", 20, 681, 207, 114, 35)
label(window, "$ 0", 20, 895, 207, 51, 35)
label(window, "$ 0", 20, 1046, 207, 51, 35)

window.mainloop()
