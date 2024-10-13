import turtle

def koch_curve(t, size, order):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, size, order - 1)
        t.left(60)
        koch_curve(t, size, order - 1)
        t.right(120)
        koch_curve(t, size, order - 1)
        t.left(60)
        koch_curve(t, size, order - 1)

def draw_koch_snowflake(t, size, order):
    for _ in range(3):
        koch_curve(t, size, order)
        t.right(120)


def main(size=300):
    try:
        order = int(input("Enter recursion level for Koch snowflake: "))

        window = turtle.Screen()
        window.bgcolor("white")

        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(-size / 2, size / 3)
        t.pendown()

        draw_koch_snowflake(t, size, order)

        window.mainloop()
    except ValueError:
        print("Please enter a valid number")

if __name__ == "__main__":
    main()