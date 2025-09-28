import turtle
import math

def draw_tree(branch_length, level):
    if level == 0:
        return
    
    # Малюємо стовбур
    turtle.forward(branch_length)

    # Зберігаємо поточну позицію і кут
    x, y = turtle.position()
    angle = turtle.heading()

    # Ліва гілка
    turtle.left(45)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1)

    # Повертаємось назад
    turtle.penup()
    turtle.setposition(x, y)
    turtle.setheading(angle)
    turtle.pendown()

    # Права гілка
    turtle.right(45)
    draw_tree(branch_length * math.sqrt(2) / 2, level - 1)

    # Повертаємось назад до початку гілки
    turtle.penup()
    turtle.setposition(x, y)
    turtle.setheading(angle)
    turtle.pendown()

def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 8): "))
    turtle.speed(0)  
    turtle.left(90)   # Повертаємо вгору
    turtle.up()
    turtle.goto(0, -250)  # Стартова точка внизу екрана
    turtle.down()
    draw_tree(100, level)  # Початковий розмір стовбура
    turtle.done()

if __name__ == "__main__":
    main()
