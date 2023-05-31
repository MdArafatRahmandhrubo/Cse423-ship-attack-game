from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

ship_body = [    (690, 750),    (660, 770),    (680, 740),    (690, 730),    (790, 745),    (780, 730),    (690, 730),    (690, 750)]


ship_speed = 2 # number of pixels to move in each frame
cannon_x = 520
cannon_y = 500
cannon_line_x_left = 480
cannon_line_y_left = 500
cannon_line_x_right = 560
cannon_line_y_right = 500
circles = []
ship = [660, 680, 690, 730, 740, 750, 760, 770, 780, 790, 745] # Global variable for your ship model
ship_direction = -1 # -1 for moving left to right, 1 for moving right to left


def iterate():
    glViewport(0, 0, 2000, 2000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 2000, 0.0, 2000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# def update_ship():
#     global ship_body, ship_speed, ship_direction
#     for i in range(len(ship_body)):
#         x, y = ship_body[i]
#         x += ship_speed * ship_direction
#         if x > 800:
#             x = -10
#         elif x < -10:
#             x = 800
#         ship_body[i] = (x, y)
    # for i in range(len(ship)):
    #     ship[i] -=2
def ball():
    global circles,ship_body,ship
    for c in circles:
        tx = c['x'] + c['dx']
        ty = c['y'] + c['dy']
        if tx < c['r'] or tx > 2000 - c['r']:
            c['dx'] *= -1
            tx = c['x'] + c['dx']
        if ty < c['r'] or ty > 2000 - c['r']:
            c['dy'] *= -1
            ty = c['y'] + c['dy']
        # check for collisions between the circle and the ship
        if ( c['x'] >790) and (c['y']>770):
            ship=[]
        for x, y in ship_body:
            if (x - c['x']) ** 2 + (y - c['y']) ** 2 < c['r'] ** 2:
                # circle has hit the ship, remove the ship by emptying its vertex list
                ship_body = []
                ship = []
                break
                
        if not ship_body:
            # the ship has been destroyed, stop iterating over the circles
            break
         # Calculate the distance from the ball's starting position

        c['x'] = tx
        c['y'] = ty
        c['r'] -= 0.2
        circle([tx, ty, c['r']], 'fill', 2, [0.43, .35, .21])




def draw_ship(): #basically Hit_box 
    glColor3f(0.43, 0.35, 0.21)
    glBegin(GL_LINE_STRIP)
    for x, y in ship_body:
        glVertex2f(x, y)
    glEnd()
    


# timer function that calls the update function and redraws the ship every 10 milliseconds
def timer_func(value):
    # update_ship()
    ball()
    glutPostRedisplay()
    glutTimerFunc(10, timer_func, 0)

# define a function to handle keyboard input
def shoot_circle(x, y):
    global circles

    # Add a new circle at the current cannon position
    circles.append({'x': x, 'y': y, 'r': 10, 'dx': 5, 'dy': 5})
    
def keyboard(key, x, y):
    global cannon_x,cannon_y,cannon_line_y_left,cannon_line_x_right,cannon_line_x_left,cannon_line_y_right
    if key == b'a': 
        if cannon_x >= 450:
            cannon_x -= 10
            cannon_line_x_left -= 10
            cannon_line_x_right -= 10
    elif key == b'd':
        if cannon_x <= 590:
            cannon_x += 10
            cannon_line_x_left += 10
            cannon_line_x_right += 10
    elif key == b'w':
        if cannon_y <= 520:
            cannon_y += 10
            cannon_line_y_left += 10
            cannon_line_y_right += 10

    elif key == b's':
        if cannon_y >= 380: 
            cannon_y -= 10
            cannon_line_y_left -= 10
            cannon_line_y_right -= 10
    elif key == b' ':
        shoot_circle(cannon_x,cannon_y) #Pass the head the of the cannon
    glutPostRedisplay()

def input1():
    a = (input("Enter ID: "))
    b = []
    for i in a:
        b.append(int(i))
    return b


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #testing phase
    x=500
    y=500
    r=200
    
    #circle([x,y,r],'hollow',[0.5,0.7,0.3])
    #point=line(100,100,500,500)
    #draw_points(point,8,color[])
    #box(300,300,800,300,800,800,300,800,'hollow',[0.5,0.7,0.3])
    #triangle(100,100,400,100,200,400,'hollow',[0.5,0.7,0.3])

    #fuunctions
    #line(x0,y0,x1,y1)
    #circle(value[x,y,r],type,size,color[])
    #box(x1,y1,x2,y2,x3,y3,x4,y4,type,size,color)
    #triangle(x1,y1,x2,y2,x3,y3,type,size,color)
    #draw(points,size,color)

    #pirate phase
    draw_points(line(0,400,375,400),2,[0.78,.57,.28])
    draw_points(line(665,400,1000,400),2,[0.78,.57,.28])
    draw_points(line(0,370,375,370),2,[0.78,.57,.28])
    draw_points(line(665,370,1000,370),2,[0.78,.57,.28])
    draw_points(line(375,400,375,370),2,[0.78,.57,.28])
    draw_points(line(665,400,665,370),2,[0.78,.57,.28])
    draw_points(line(0,370,375,370),2,[0.78,.57,.28])
    draw_points(line(0,400,0,370),2,[0.78,.57,.28])
    draw_points(line(1000,400,1000,370),2,[0.78,.57,.28])   #upper railing

    draw_points(line(0,370,0,200),2,[0.78,.57,.28])
    draw_points(line(90,370,90,200),2,[0.78,.57,.28])
    draw_points(line(110,370,110,200),2,[0.78,.57,.28])
    draw_points(line(210,370,210,200),2,[0.78,.57,.28])
    draw_points(line(230,370,230,200),2,[0.78,.57,.28])
    draw_points(line(330,370,330,200),2,[0.78,.57,.28])
    draw_points(line(350,370,350,200),2,[0.78,.57,.28])
    #draw_points(line(450,370,450,200),2,[0.78,.57,.28])
    #draw_points(line(470,370,470,200),2,[0.78,.57,.28])
    #draw_points(line(570,370,570,200),2,[0.78,.57,.28])
    #draw_points(line(590,370,590,200),2,[0.78,.57,.28])
    draw_points(line(690,370,690,200),2,[0.78,.57,.28])
    draw_points(line(710,370,710,200),2,[0.78,.57,.28])
    draw_points(line(810,370,810,200),2,[0.78,.57,.28])
    draw_points(line(830,370,830,200),2,[0.78,.57,.28])
    draw_points(line(930,370,930,200),2,[0.78,.57,.28])
    draw_points(line(950,370,950,200),2,[0.78,.57,.28]) #railing piller

    box(0,0,1000,0,1000,200,0,200,'hollow',3,[0.78,.57,.28])
    draw_points(line(0,160,1000,160),2,[0.43,.35,.21])
    draw_points(line(0,120,1000,120),2,[0.43,.35,.21])
    draw_points(line(0,80,1000,80),2,[0.43,.35,.21])
    draw_points(line(0,40,1000,40),2,[0.43,.35,.21]) #floor

    # draw_points(line(520,120,520,500),2,[0.43,.35,.21])
    circle([cannon_x,cannon_y,40],'hollow',3,[0.43,.35,.21])
    circle([520,220,80],'hollow',3,[0.43,.35,.21])
    draw_points(line(440,220,cannon_line_x_left,cannon_line_y_left),2,[0.43,.35,.21])
    draw_points(line(cannon_line_x_right,cannon_line_y_right,600,220),2,[0.43,.35,.21]) #canon

    triangle(440,220,440,120,340,120,"hollow",3,[0.43,.35,.21])
    triangle(600,220,600,120,700,120,"hollow",3,[0.43,.35,.21])#cannon stand
    try:
        draw_points(line(ship[2],ship[5],ship[7],ship[5]),2,[0.43,.35,.21])
        draw_points(line(ship[2],ship[5],ship[0],ship[7]),2,[0.43,.35,.21])
        draw_points(line(ship[7],ship[5],ship[9],ship[6]),2,[0.43,.35,.21])
        draw_points(line(ship[0],ship[7],ship[1],ship[4]),2,[0.43,.35,.21])
        draw_points(line(ship[1],ship[4],ship[2],ship[3]),2,[0.43,.35,.21])
        draw_points(line(ship[9],ship[6],ship[9],ship[10]),2,[0.43,.35,.21])
        draw_points(line(ship[9],ship[10],ship[8],ship[3]),2,[0.43,.35,.21])
        draw_points(line(ship[8],ship[3],ship[2],ship[3]),2,[0.43,.35,.21]) #ship body
        draw_points(line(725,750,725,820),4,[0.43,.35,.21])
        box(690,815,770,815,750,760,705,760,'hollow',2,[0.78,.57,.28])
    except IndexError:
        draw_points(line(725,750,725,820),4,[0.43,.35,.21])
        box(690,815,770,815,750,760,705,760,'hollow',2,[0.78,.57,.28])
    #movement function
    
    draw_ship()
    # update_ship()
    draw_points(line(725,750,725,820),4,[0.43,.35,.21])
    box(690,815,770,815,750,760,705,760,'hollow',2,[0.78,.57,.28]) #sail

    draw_points(line(0,825,1000,825),2,[0.43,.35,.21])  #sky border

    circle([850,950,30],'hollow',3,[0.43,.35,.21])  #sun

    global circles 
    for c in circles:
        circle([c['x'],c['y'], c['r']+1], 'fill',2, [0.43,.35,.21])

        


    glutSwapBuffers()


def mdl(xs,ys,xf,yf):
    dx=xf-xs
    dy=yf-ys
    d=2*dy-dx
    points=[xs,ys]

    while True:
        #NE
        if d>0:    
            xs+=1
            ys+=1
            points.append(xs)
            points.append(ys)
            d=d+2*dy-2*dx
        #E
        else:
            xs+=1
            points.append(xs)
            points.append(ys)
            d=d+2*dy

        if (xs>=xf):
            break   
    return points   

def line(x0,y0,x1,y1):
    
    dx=x1-x0
    dy=y1-y0
    #quarter 1
    if (dx>=0 and dy>=0):
        #zone 0
        if (abs(dx)>abs(dy)):
            xs=x0
            ys=y0
            xf=x1
            yf=y1
            points=mdl(xs,ys,xf,yf)
            points2=[]
            i=0
            while (i<=len(points)-1):
                points2.append(points[i])
                points2.append(points[i+1])
                i+=2
        #zone 1        
        else:
            xs=y0
            ys=x0
            xf=y1
            yf=x1
            points=mdl(xs,ys,xf,yf)
            points2=[]
            i=0
            while (i<=len(points)-1):
                points2.append(points[i+1])
                points2.append(points[i])
                i+=2
    
    #quarter 2        
    elif(dx<=0 and dy>=0):
        #zone 2
        if (abs(dx)<abs(dy)):
            xs=y0
            ys=x0*-1
            xf=y1
            yf=x1*-1
            points=mdl(xs,ys,xf,yf)
            points2=[]
            i=0
            while (i<=len(points)-1):
                points2.append(points[i+1]*-1)
                points2.append(points[i])
                i+=2
                
           
        #zone 3
        else:
            xs=x0*-1
            ys=y0
            xf=x1*-1
            yf=y1    
            points=mdl(xs,ys,xf,yf)
            points2=[]
            i=0
            while (i<=len(points)-1):
                points2.append(points[i]*-1)
                points2.append(points[i+1])
                i+=2
                
        #quarter 3       
    elif(dx<=0 and dy<=0):
        #zone 4
        if (abs(dx)>abs(dy)):
            xs=x0*-1
            ys=y0*-1
            xf=x1*-1
            yf=y1*-1
            points=mdl(xs,ys,xf,yf)
            points2=[]
            i=0
            while (i<=len(points)-1):
                points2.append(points[i]*-1)
                points2.append(points[i+1]*-1)
                i+=2
                
            #zone 5
        else:
            xs=y0*-1
            ys=x0*-1
            xf=y1*-1
            yf=x1*-1
            points=mdl(xs,ys,xf,yf)
            points2=[]
            i=0
            while (i<=len(points)-1):
                points2.append(points[i+1]*-1)
                points2.append(points[i]*-1)
                i+=2
                
        #quarter 4
    elif(dx>=0 and dy<=0):
        #zone 6
        if (abs(dx)<abs(dy)):
            xs=y0*-1
            ys=x0
            xf=y1*-1
            yf=x1
            points=mdl(xs,ys,xf,yf)
            points2=[]
            i=0
            while (i<=len(points)-1):
                points2.append(points[i+1])
                points2.append(points[i]*-1)
                i+=2
                
            #zone 7
        else:
            xs=x0
            ys=y0*-1
            xf=x1
            yf=y1*-1
            points=mdl(xs,ys,xf,yf)
            points2=[]
            i=0
            while (i<=len(points)-1):
                points2.append(points[i])
                points2.append(points[i+1]*-1)
                i+=2
    return points2            
    
def circle(val,type,size,color):
    x = val[0]
    y = val[1]
    r = val[2]
    a = []
    a=circle_formula(r)
    z=circle_8zone(a,x,y)
    
    if type=="hollow":
        draw_points(z,size,color)
    elif type=="fill":
        
        temp=[]
        i = 0

        while i <= len(z) - 1:
            j=0
            while j <= len(z) - 1:
                temp2=[]
                temp2=line(z[i],z[i+1],z[j],z[j+1])
                temp+=temp2
                j+=2
            i+=2    
        z+=temp    
        draw_points(z,5,color)    
    
def circle_8zone(a,x,y):

    i=0
    p=[]

    while i<=len(a)-1:
        p.append(a[i] + x)
        p.append(a[i+1] + y)
        #zone0
        p.append(a[i+1]+x)
        p.append(a[i]+y)
        #zone 2
        p.append(a[i]*-1+x)
        p.append(a[i+1]+y)
        #zone3
        p.append(a[i + 1]*-1+x)
        p.append(a[i]+y)
        #zone4
        p.append(a[i + 1]*-1+x)
        p.append(a[i]*-1+y)
        #zone 5
        p.append(a[i]*-1+x)
        p.append(a[i+1]*-1+y)
        #zone 6
        p.append(a[i]+x)
        p.append(a[i+1]*-1+y)
        #zone7
        p.append(a[i + 1]+x)
        p.append(a[i]*-1+y)
        i += 2

    return p

def circle_formula(r):
    x = 0
    y = r
    points = [x,r]
    d=1-r

    while True:
        # SE
        if d >= 0:
            x += 1
            y -= 1
            points.append(x)
            points.append(y)
            d = d + 2 * x - 2 * y + 5
        # E
        else:
            x += 1

            points.append(x)
            points.append(y)
            d = d + 2 * x + 3

        if (x >= y):
            break
    return points

def box(x1,y1,x2,y2,x3,y3,x4,y4,type,size,color):
    points=[]
    temp=line(x1,y1,x2,y2)
    points+=temp
    temp=line(x1,y1,x4,y4)
    points+=temp
    temp=line(x2,y2,x3,y3)
    points+=temp
    temp=line(x4,y4,x3,y3)
    points+=temp
    if type=='hollow':
        draw_points(points,size,color)
    elif type=="fill":
        i=0
        temp=[]
        while i<=len(points)-1:
            continue

def triangle(x1,y1,x2,y2,x3,y3,type,size,color):
    points=[]
    temp=line(x1,y1,x2,y2)
    points+=temp
    temp=line(x1,y1,x3,y3)
    points+=temp
    temp=line(x2,y2,x3,y3)
    points+=temp
    if type=='hollow':
        draw_points(points,5,color)
    elif type=="fill":
        i=0
        temp=[]
        while i<=len(points)-1:
            continue


def draw_points(points,size,color):
    glPointSize(size)
    glBegin(GL_POINTS)

    glColor3f(color[0],color[1],color[2])
    i = 0
    # print(points)
    while i <= len(points) - 1:
        glVertex2f(points[i], points[i + 1])
        i += 2
    glEnd()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(1000,1000)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Sea Of Thives")  # window name
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboard)
glutTimerFunc(10, timer_func, 0)


glutMainLoop()

# circle([7])
