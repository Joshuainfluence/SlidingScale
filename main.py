from tkinter import *


def submit():
    # scale.get function returns an integer, so we have to convert it to a string
    print("The temperature is " + str(scale.get()) + " degrees celsius")


window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=("Consolas", 20),
              tickinterval=10, #numeric indicators on the scale
              showvalue=0, #hide current value
              troughcolor='#69eaff',
              fg='#ff1c00',
              bg='#000'
 )

# set the scale indicator to the center
scale.set(((scale['from']-scale['to'])/2) + scale['to'])
# to display the scale
scale.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()
