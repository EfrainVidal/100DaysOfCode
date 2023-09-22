# from turtle import Turtle, Screen
#
# #variable   class
# timmy = Turtle()
# timmy.shape("turtle") # change shape of item created
# timmy.color("DarkSlateGray4") # change color of item created
#
# timmy.forward(100) # move forward 100 paces
#
# my_screen = Screen() # get screen class and assign to var
# my_screen.canvheight   # screen height
# my_screen.exitonclick() # stop screen from disappearing before clicking on it
# print(my_screen.canvheight)

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)