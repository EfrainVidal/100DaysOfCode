from turtle import Turtle

# create a tuple of positions for each starting segment of the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # a list of segments/piece for the snake
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # create 3 snake pieces to start game
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake_piece = Turtle(shape="square")
        new_snake_piece.color("white")
        new_snake_piece.penup()
        new_snake_piece.goto(position)
        self.segments.append(new_snake_piece)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        # create a for loop to move each piece in to last place of the piece in front of it
        for snake_piece in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_piece - 1].xcor()
            new_y = self.segments[snake_piece - 1].ycor()
            self.segments[snake_piece].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)  # move the first snake piece forward

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
