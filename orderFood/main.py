from tkinter import *

food = ['pizza', 'hamburger', 'hotdog']

def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered hamburger!")
    elif x.get() == 2:
        print("You ordered hotdog!")
    else:
        print("Huh")

window = Tk()

pizzaImage = PhotoImage(file='images/pizza.png')
hamburgerImage = PhotoImage(file='images/hamburger.png')
hotdogImage = PhotoImage(file='images/hotdog.png')
foodImage = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=('Impact', 50),
                              image=foodImage[index],
                              compound='left',
                              indicatoron=0,  # it makes it like a push button
                              command=order
                              )
    radiobutton.pack(anchor=W)

window.mainloop()
