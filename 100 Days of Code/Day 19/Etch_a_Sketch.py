import turtle as tl

t = tl.Turtle()
scr = tl.Screen()

def move_fd():
    t.fd(10)

def move_bw():
    t.backward(10)

def clockwise():
    t.rt(10)

def counter_clockwise():
    t.lt(10)

def clear():
    t.clear()

scr.listen()

scr.onkeypress(fun=move_fd, key='w')
scr.onkeypress(fun=move_bw, key='s')
scr.onkeypress(fun=counter_clockwise, key='a')
scr.onkeypress(fun=clockwise, key='d')
scr.onkeypress(fun=clear, key='c')

scr.exitonclick()

