#Importing Turtle and Random modules
import turtle as trtl
import random as rand


#Creating screen and background
wn = trtl.Screen()
wn.bgpic("halloween.png")

#creating candy object
candy = trtl.Turtle()
#Creating Candies List
candies = ['zTwix.gif', 'ghost1.gif', 'ghost2.gif', 'giphy.gif', 'skittles.gif', 'snickers.gif', ]

wn.addshape('zTwix.gif')
candy.shape('zTwix.gif')

num = len(candies) - 1

#Changing location of Candy
def pos_change():
  candy.penup()
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-200,200)
  candy.goto(new_xpos, new_ypos)

candy.score = 0

# randomizes the candy being clicked
def candy_clicked(x,y):
  pos_change()
  num2 = rand.randint(0,num)
  candies2 = candies[num2]
  wn.addshape(candies2)
  candy.shape(candies2)
  candy.score += 5
  print(candy.score)

# running the function
candy.onclick(candy_clicked)



#Window
wn.mainloop()
