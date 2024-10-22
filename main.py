#   a123_apple_1.py
import turtle as trtl
import random

#-----setup-----
apple_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

appleOne = trtl.Turtle()
appleTwo = trtl.Turtle()
appleThree = trtl.Turtle()
appleFour = trtl.Turtle()
appleFive = trtl.Turtle()
appules = [appleOne, appleTwo, appleThree, appleFour, appleFive]
applesToUse = []
keysAvailable = ["s", "d", "j", "l"]
keysBeingUsed = ["a", "f", "g", "k", "h"]
for i in range(5):
  wn.tracer = False
  appules[i].penup()
  xCorToGo = random.randint(-100, 100)
  appules[i].goto(xCorToGo, random.randint(-15, 100))
  appules[i].pencolor("white")
  appules[i].pendown()
  appules[i].write(keysBeingUsed[i], font =("Arial", 50, "bold"))
  appules[i].penup()
  wn.tracer = True
  applesToUse.append(appules[i])

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def start_drop(event):
  global keysBeingUsed
  global keysAvailable
  global applesToUse
  for i in range(len(keysBeingUsed)):
    if (event == keysBeingUsed[i]):
      drop_apple(applesToUse[i])
      keysAvailable.append(event)
      print(keysAvailable)
      keysBeingUsed[i] = " "
      print(keysBeingUsed)


def drop_apple(appleToDrop):
  global apple
  appleToDrop.clear()
  if (appleToDrop.ycor() > -150):
    appleToDrop.sety(appleToDrop.ycor() - 10)
    wn.ontimer(drop_apple(appleToDrop), 100)
  else:
    reset_apple(appleToDrop)

def reset_apple(appleToReset):
  global wn
  global keysAvailable
  global keysBeingUsed
  global applesToUse
  wn.tracer = False
  xCorToGo = random.randint(-100, 100)
  appleToReset.goto(xCorToGo, random.randint(-15, 50))
  appleToReset.pendown()

  keyToPress = random.choice(keysAvailable)
  for i in range(len(keysAvailable)):
    if (keyToPress == keysAvailable[i]):
      keysAvailable.pop(keysAvailable[i])
  for n in range(len(applesToUse)):
    if (appleToReset == applesToUse[n]):
      keysBeingUsed[n] = keyToPress
  appleToReset.write(keyToPress, font = ("Arial", 50, "bold"))
  appleToReset.penup()
  wn.tracer = True




#-----function calls-----
for i in range(5):
  draw_apple(applesToUse[i])
wn.bgpic("background.gif")
for n in keysBeingUsed:
    wn.onkeypress(lambda n=n: start_drop(n), str(n))
wn.listen()
wn.mainloop()