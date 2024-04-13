import turtle
import math

def julia(z , c , max_iter=20):
    # Limiting value
    if abs(z) > 10 ** 12:
        return float("nan")
    elif max_iter > 0:
        return julia(z ** 2 + c, c, max_iter - 1)
    # Once max_iter iterationsnare over, return
    else:
        return z ** 2 + c

# Screen limits
screen_width = 800
screen_height = 600

# Complex plane limits
complexPlaneX, complexPlaneY = (-2.0, 2.0), (-2.0, 2.0)

# Discretization step - To control resolution
step = 1.5

# Turtle windows configuration
turtle.tracer(0, 0) # Turn OFF animation
screen = turtle.Screen()
screen.title("Julia Fractal")

turt = turtle.Turtle()
turt.penup()

# Calculation of conversion factors - pixel to complex plane coordinates

# px * pixelToX = x in complex plane coords
# py * pixelToY = y in complex plane coords
pixelToX, pixelToY = (complexPlaneX[1] - complexPlaneX[0])/screen_width, (complexPlaneY[1] - complexPlaneY[0])/screen_height

julia_constant = complex(-0.7, 0.27015)

# plot
for px in range(-int(screen_width/2), int(screen_width/2), int(step)):
    for py in range(-int(screen_width/2), int(screen_width/2), int(step)):
        x, y = px * pixelToX, py * pixelToY
        z = complex(x, y)
        m =  julia(z, julia_constant)
        
        # Che k if real part is not NaN
        if not math.isnan(m.real):
            r = int(abs(math.sin(m.imag)) * 255)
            g = int(abs(math.sin(m.imag + (2 * math.pi / 3))) * 255)
            b = int(abs(math.sin(m.imag + (4 * math.pi / 3))) * 255)
            color = (r, g, b)
            
            hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])
            turt.color(hex_color)
            turt.dot(2.4, hex_color) # Put dot at current pixel. Size=2.4
            turt.goto(px, py) # Move to next pixel
    turtle.update() # Update after one py loop

turtle.mainloop()
