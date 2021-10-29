import turtle as trtl
import random as rand
#creating candy object
candy = trtl.Turtle()
wn = trtl.Screen()
candies = ["zTwix.gif, ghost1.gif, ghost2.gif"]

def function(x):
  wn.addshape(x)
  candy.shape(x)
function(candies)

def pos_change():
  candy.penup()
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-200,200)
  candy.goto(new_xpos, new_ypos)

def candy_clicked(x,y):
  pos_change()

candy.onclick(candy_clicked)
#wn.bgpic("halloween.jpg")
wn.mainloop()