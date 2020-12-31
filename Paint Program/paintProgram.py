#PaintProgram.py
from pygame import *
from random import *
from math import *
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
size=(1400,800)
screen = display.set_mode(size)
tool="pencil"
stampName=''
col=BLACK
size=1
polygonPoints=[]

display.set_caption('Dragon Ball Z Paint') #changes name of the window
icon=image.load('images/icon.jpg')  #changes icon of the window
display.set_icon(icon)
######load ALL pictures---------------------------------------------------------------------------------
background1=image.load("images/dbzBackground.jpg")
background2=image.load("images/dbzBackground2.jpg")
background3=image.load("images/dbzBackground3.jpg")
background4=image.load("images/dbzBackground4.jpg")

wheelPic=image.load("images/colwheel.jpg")
pencil=image.load("images/pencil icon.jpg")
eraser=image.load("images/eraser icon.jpg")
eyeDropper=image.load("images/eyeDropper.jpg")
sprayPaint=image.load("images/spray paint icon.jpg")
rectangule=image.load('images/rectangule.jpg')
FilledRectangule=image.load('images/FilledRectangule.jpg')
Clear=image.load('images/Clear.jpg')
Ellipse=image.load('images/Ellipse.jpg')
FilledEllipse=image.load('images/FilledEllipse.jpg')
PaintBrush=image.load('images/paint brush.jpg')
Line=image.load('images/line.jpg')
Polygon=image.load('images/polygon.jpg')

Triangule=image.load('images/triangule.jpg')

Undo=image.load('images/undo.jpg')
Redo=image.load('images/redo.jpg')

hit=image.load("images/hit.jpg")
beerus=image.load("images/beerus.jpg")
goku1=image.load("images/gokuNormal.jpg")
goku2=image.load("images/gokuSS3.jpg")
Vegeta=image.load("images/gokuUI.jpg")
whis=image.load("images/whis.jpg")
frieza=image.load('images/Frieza.jpg')
majinBuu=image.load('images/majinBuu.jpg')

earth=image.load('images/earth.jpg')
gokusHouse=image.load('images/gokusHouse.jpg')
namek=image.load('images/namek.jpg')

mixer.init()
mixer.music.load('DBZ theme.mp3')
mixer.music.play(-1)

#####SIZE OF EVERYTHING ON THE ACTUAL SCREEN-----------------------------------------------------------
#resizes image for the size they will be as icons
BACKGROUND1=transform.scale(background1,(1400,800))
BACKGROUND2=transform.scale(background2,(1400,800))
BACKGROUND3=transform.scale(background3,(1400,800))
BACKGROUND4=transform.scale(background4,(1400,800))

WHEELPIC=transform.scale(wheelPic,(175,175))
UNDO=transform.scale(Undo,(51,51))
REDO=transform.scale(Redo,(51,51))
PENCIL=transform.scale(pencil,(51,51))
ERASER=transform.scale(eraser,(51,51))
SPRAYPAINT=transform.scale(sprayPaint,(51,51))
EYEDROPPER=transform.scale(eyeDropper,(51,51))
RECTANGULE=transform.scale(rectangule,(51,51))
FILLEDRECTANGULE=transform.scale(FilledRectangule,(51,51))
ELLIPSE=transform.scale(Ellipse,(51,51))
FELLIPSE=transform.scale(FilledEllipse,(51,51))
CLEAR=transform.scale(Clear,(51,51))
PAINTBRUSH=transform.scale(PaintBrush,(51,51))
POLYGON=transform.scale(Polygon,(51,51))
LINE=transform.scale(Line,(51,51))

TRIANGULE=transform.scale(Triangule,(51,51))
              
goku=transform.scale(goku1,(100,150))
gokuGod=transform.scale(goku2,(100,150))
vegeta1=transform.scale(Vegeta,(100,150))
hit1=transform.scale(hit,(100,150))
beerus1=transform.scale(beerus,(100,150))
whis1=transform.scale(whis,(100,150))
frieza1=transform.scale(frieza,(100,150))
majinBuu1=transform.scale(majinBuu,(100,150))

earth1=transform.scale(earth,(240,170))
gokusHouse1=transform.scale(gokusHouse,(240,170))
namek1=transform.scale(namek,(240,170))

#######ACTUAL SIZES WHEN YOU PLACE THE STAMPS---------------------------------------------------------------------------
#resizes the stamps/backgrounds 
gokuStamp=transform.scale(goku1,(150,200))
gokuGodStamp=transform.scale(goku2,(150,200))
vegetaStamp=transform.scale(Vegeta,(150,200))
hitStamp=transform.scale(hit,(150,200))
beerusStamp=transform.scale(beerus,(150,200))
whisStamp=transform.scale(whis,(150,200))
friezaStamp=transform.scale(frieza,(150,200))
buuStamp=transform.scale(majinBuu,(150,200))

earthBackground=transform.scale(earth,(800,550))
GokusHouseBackground=transform.scale(gokusHouse,(800,550))
NamekBackground=transform.scale(namek,(800,550))

##############################defining all RECTS-----------------------------------------------------
#defines rects for the pics/tools to be blitted into
totalScreen=Rect(0,0,1400,800)
canvasRect=Rect(300,100,800,550)
wheelRect=Rect(75,100,175,175)

pencilRect=Rect(75,300,51,51)
eraserRect=Rect(137,300,51,51)
dropperRect=Rect(199,300,51,51)

sprayRect=Rect(75,375,51,51)
RectanguleRect=Rect(137,375,51,51)
FRectanguleRect=Rect(199,375,51,51)

ClearRect=Rect(75,450,51,51)
EllipseRect=Rect(137,450,51,51)
FEllipseRect=Rect(199,450,51,51)

BrushRect=Rect(75,525,51,51)
LineRect=Rect(137,525,51,51)
PolygonRect=Rect(199,525,51,51)

UndoRect=Rect(75,600,51,51)
TrianguleRect=Rect(137,600,51,51)
RedoRect=Rect(199,600,51,51)

wallpaperRect1=Rect(1130,100,240,170)
wallpaperRect2=Rect(1130,290,240,170)
wallpaperRect3=Rect(1130,480,240,170)

toolRectList=[pencilRect,eraserRect,dropperRect,sprayRect,
          RectanguleRect,FRectanguleRect,ClearRect,EllipseRect,
          FEllipseRect,BrushRect,LineRect,PolygonRect,
          UndoRect,RedoRect,TrianguleRect]

#Generating the background---------------------------------------------------------------------

backgroundsList=[BACKGROUND1,BACKGROUND2,BACKGROUND3,BACKGROUND4] #makes a list of possible backgrounds
bPos=randint(0,3)   #gets a random number and generates that index from the list of backgrounds
screen.blit(backgroundsList[bPos],totalScreen)
draw.rect(screen,WHITE,canvasRect)

#-------------------------------------------------------------------------------

screen.blit(WHEELPIC,wheelRect)
screen.blit(UNDO,UndoRect)
screen.blit(REDO,RedoRect)
screen.blit(PENCIL,pencilRect)
screen.blit(ERASER,eraserRect)
screen.blit(SPRAYPAINT,sprayRect)
screen.blit(EYEDROPPER,dropperRect)
screen.blit(RECTANGULE,RectanguleRect)
screen.blit(FILLEDRECTANGULE,FRectanguleRect)
screen.blit(CLEAR,ClearRect)
screen.blit(ELLIPSE,EllipseRect)
screen.blit(FELLIPSE,FEllipseRect)
screen.blit(PAINTBRUSH,BrushRect)
screen.blit(LINE,LineRect)
screen.blit(POLYGON,PolygonRect)

screen.blit(TRIANGULE,(TrianguleRect))

screen.blit(earth1,wallpaperRect1)
screen.blit(gokusHouse1,wallpaperRect2)
screen.blit(namek1,wallpaperRect3)

###stamp/sticker rects-------------------------------------------------------------------------------------------------

gokuRect1=Rect(300,650,100,150)
gokuRect2=Rect(400,650,100,150)
vegetaRect=Rect(500,650,100,150)
hitRect=Rect(600,650,100,150)
beerusRect=Rect(700,650,100,150)
whisRect=Rect(800,650,100,150)
friezaRect=Rect(900,650,100,150)
buuRect=Rect(1000,650,100,150)

stampList=[gokuRect1,gokuRect2,vegetaRect,hitRect,
           beerusRect,whisRect,friezaRect,buuRect] #makes a list of the stamp rects

screen.blit(goku,gokuRect1)
screen.blit(gokuGod,gokuRect2)
screen.blit(vegeta1,vegetaRect)
screen.blit(hit1,hitRect)
screen.blit(beerus1,beerusRect)
screen.blit(whis1,whisRect)
screen.blit(frieza1,friezaRect)
screen.blit(majinBuu1,buuRect)

undoList=[screen.subsurface(canvasRect).copy()] #creates a list for screen captures
undoPos=0 #position of the screen capture being blitted

#'Circle' function for brush/eraser--------------------------------------------

def circle(surface,color,starting,ending,radius):
    dx=ending[0]-starting[0]        #Takes the two points and calculates the distance between the x's and the y's
    dy=ending[1]-starting[1]        
    distance=max(abs(dx),abs(dy))   #calculates the largest distance (max) out of the 2
                                    #absolute value so the values are NOT negative
    for i in range(distance):                   #Goes up by 1 to the distance
        x=int(starting[0]+float(i)/distance*dx) #Uses Similar Triangles and gets all of the points
        y=int(starting[1]+float(i)/distance*dy) #on the line with ratios and draws circles on all of these points
        draw.circle(surface,color,(x,y),radius)

#############################Start of actual program-------------------------------------------------------------------------------

start = 0,0
running=True
while running:
    click=False
    for evt in event.get():
        if evt.type == QUIT: 
            running = False
        if evt.type==MOUSEBUTTONDOWN:
            screencopy=screen.copy() #copys the screen so stamps can be moved around
            if evt.button==1:        #also, uses pics of the screen for undo/redo   
                start=evt.pos
                click=True
            if evt.button==4:
                size+=1
            if evt.button==5:
                size-=1
        if evt.type==MOUSEBUTTONUP:
            if canvasRect.collidepoint(mx,my) or wallpaperRect1.collidepoint(mx,my) or wallpaperRect2.collidepoint(mx,my) or wallpaperRect3.collidepoint(mx,my):
                #if tool is used on canvas or wallpaper is blitted on screen, then take a screen capture
                if undoPos<len(undoList)-1:
                    del undoList[undoPos+1:] 
                undoList+=[screen.subsurface(canvasRect).copy()] #adds surface to the list of screen captures
                undoPos+=1 #adds to UndoPos to keep track of the number of pictures

    draw.rect(screen,col,(1130,20,240,60),0) #draws a rect of the current colour the user has selected
        
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed() ###mb --- mouse button                                    

    if click:
        omx,omy=mx,my
    #fonts------------------------------------------------------------------------
    #loads the fonts
    font.init()
    comicFont=font.SysFont('Comic Sans MS',20)

    #displaying coordinates-------------------------------------------------------
    #gets the current position of the user's mouse

    CoordBox=Rect(1130,670,240,110)
    draw.rect(screen,(86,151,255),CoordBox,0)
    if canvasRect.collidepoint(mx,my):
        DisplayX='X Coordinate: '+str(mx-300)
        DisplayY='Y Coordinate: '+str(my-100)
        Pos1=comicFont.render(DisplayX,False,BLACK)
        Pos2=comicFont.render(DisplayY,False,BLACK)
        screen.blit(Pos1,(1160,680))
        screen.blit(Pos2,(1160,750))
    else:
        DisplayX='X Coordinate: '+str('---') # if mx,my is not touching the canvas, then display '---'
        DisplayY='Y Coordinate: '+str('---')
        Pos1=comicFont.render(DisplayX,False,BLACK)
        Pos2=comicFont.render(DisplayY,False,BLACK)
        screen.blit(Pos1,(1160,680))
        screen.blit(Pos2,(1160,750))

    #drawing the rects-----------------------------------------------------------------------------------------------------
    #draws the boxes for the tool images to be in
        
    draw.rect(screen,GREEN,UndoRect,2)
    draw.rect(screen,GREEN,RedoRect,2)
    draw.rect(screen,GREEN,pencilRect,2)
    draw.rect(screen,GREEN,eraserRect,2)
    draw.rect(screen,GREEN,sprayRect,2)
    draw.rect(screen,GREEN,dropperRect,2)
    draw.rect(screen,GREEN,gokuRect1,2)
    draw.rect(screen,GREEN,gokuRect2,2)
    draw.rect(screen,GREEN,vegetaRect,2)
    draw.rect(screen,GREEN,hitRect,2)
    draw.rect(screen,GREEN,beerusRect,2)
    draw.rect(screen,GREEN,whisRect,2)
    draw.rect(screen,GREEN,friezaRect,2)
    draw.rect(screen,GREEN,buuRect,2)
    draw.rect(screen,GREEN,RectanguleRect,2)
    draw.rect(screen,GREEN,FRectanguleRect,2)
    draw.rect(screen,GREEN,ClearRect,2)
    draw.rect(screen,GREEN,EllipseRect,2)
    draw.rect(screen,GREEN,FEllipseRect,2)
    draw.rect(screen,GREEN,BrushRect,2)
    draw.rect(screen,GREEN,LineRect,2)
    draw.rect(screen,GREEN,PolygonRect,2)
    draw.rect(screen,GREEN,TrianguleRect,2)
    draw.rect(screen,GREEN,wallpaperRect1,2)
    draw.rect(screen,GREEN,wallpaperRect2,2)
    draw.rect(screen,GREEN,wallpaperRect3,2)
    
    #Checking if tools/stamps are clicked---------------------------------------
    #determines which tool is selected
    if click and pencilRect.collidepoint(mx,my):
        tool="pencil"
    if click and eraserRect.collidepoint(mx,my):
        tool="eraser"
    if click and sprayRect.collidepoint(mx,my):
        tool='spray paint'
    if click and dropperRect.collidepoint(mx,my):
        tool='eye dropper'
    if click and gokuRect1.collidepoint(mx,my):
        tool='gokuStamp'
        stampName=gokuStamp
    if click and gokuRect2.collidepoint(mx,my):
        tool='gokuGodStamp'
        stampName=gokuGodStamp
    if click and vegetaRect.collidepoint(mx,my):
        tool='vegetaStamp'
        stampName=vegetaStamp
    if click and hitRect.collidepoint(mx,my):
        tool='hitStamp'
        stampName=hitStamp
    if click and beerusRect.collidepoint(mx,my):
        tool='beerusStamp'
        stampName=beerusStamp
    if click and whisRect.collidepoint(mx,my):
        tool='whisStamp'
        stampName=whisStamp
    if click and friezaRect.collidepoint(mx,my):
        tool='friezaStamp'
        stampName=friezaStamp
    if click and buuRect.collidepoint(mx,my):
        tool='buuStamp'
        stampName=buuStamp
    if click and RectanguleRect.collidepoint(mx,my):
        tool='rect'
    if click and FRectanguleRect.collidepoint(mx,my):
        tool='F rect'
    if click and ClearRect.collidepoint(mx,my):
        tool='clear'
        draw.rect(screen,WHITE,canvasRect)
    if click and EllipseRect.collidepoint(mx,my):
        tool='ellipse'
    if click and FEllipseRect.collidepoint(mx,my):
        tool='F ellipse'
    if click and BrushRect.collidepoint(mx,my):
        tool='brush'
    if click and LineRect.collidepoint(mx,my):
        tool='line'
    if click and PolygonRect.collidepoint(mx,my):
        tool='polygon'
    if click and TrianguleRect.collidepoint(mx,my):
        tool='triangule'
    if click and wallpaperRect1.collidepoint(mx,my):
        tool='back1'
        screen.blit(earthBackground,(300,100))
    if click and wallpaperRect2.collidepoint(mx,my):
        tool='back2'
        screen.blit(GokusHouseBackground,(300,100))
    if click and wallpaperRect3.collidepoint(mx,my):
        tool='back3'
        screen.blit(NamekBackground,(300,100))
    #undo button
    if click:
        if UndoRect.collidepoint(mx,my):
            tool='undo'
            if len(undoList)-1>0: #checks if list is empty or not
                undoPos-=1 #subtracts from the counter to get the right position
                screen.blit(undoList[undoPos],(300,100)) #blits the capture
            if undoPos<=1: 
                screen.blit(undoList[undoPos],(300,100)) #blits the capture
                undoPos=1 #sets a restriction so the index does NOT go below 0
    #redo button
    if click:
        if RedoRect.collidepoint(mx,my):
            tool='redo'
            if len(undoList)-1>0: #checks if list is empty or not
                if undoPos>=len(undoList)-1: #makes sure the index doesnt go out of range
                    screen.blit(undoList[undoPos],(300,100)) #blits the capture
                else:
                    undoPos+=1 #adds from the counter to get the right position
                    screen.blit(undoList[undoPos],(300,100)) #blits the capture

                
    ###outlining the selected tool

    if tool=='pencil':
        draw.rect(screen,RED,toolRectList[0],2)
    if tool=='eraser':
        draw.rect(screen,RED,toolRectList[1],2)
    if tool=='eye dropper':
        draw.rect(screen,RED,toolRectList[2],2)
    if tool=='spray paint':
        draw.rect(screen,RED,toolRectList[3],2)
    if tool=='rect':
        draw.rect(screen,RED,toolRectList[4],2)
    if tool=='F rect':
        draw.rect(screen,RED,toolRectList[5],2)
    if tool=='clear':
        draw.rect(screen,RED,toolRectList[6],2)
    if tool=='ellipse':
        draw.rect(screen,RED,toolRectList[7],2)
    if tool=='F ellipse':
        draw.rect(screen,RED,toolRectList[8],2)
    if tool=='brush':
        draw.rect(screen,RED,toolRectList[9],2)
    if tool=='line':
        draw.rect(screen,RED,toolRectList[10],2)
    if tool=='polygon':
        draw.rect(screen,RED,toolRectList[11],2)
    if tool=='undo':
        draw.rect(screen,RED,toolRectList[12],2)
    if tool=='redo':
        draw.rect(screen,RED,toolRectList[13],2)
    if tool=='triangule':
        draw.rect(screen,RED,toolRectList[14],2)
    if tool=='gokuStamp':
        draw.rect(screen,RED,stampList[0],2)
    if tool=='gokuGodStamp':
        draw.rect(screen,RED,stampList[1],2)
    if tool=='vegetaStamp':
        draw.rect(screen,RED,stampList[2],2)
    if tool=='hitStamp':
        draw.rect(screen,RED,stampList[3],2)
    if tool=='beerusStamp':
        draw.rect(screen,RED,stampList[4],2)
    if tool=='whisStamp':
        draw.rect(screen,RED,stampList[5],2)
    if tool=='friezaStamp':
        draw.rect(screen,RED,stampList[6],2)
    if tool=='buuStamp':
        draw.rect(screen,RED,stampList[7],2)
    if tool=='back1':
        draw.rect(screen,RED,wallpaperRect1,2)
    if tool=='back2':
        draw.rect(screen,RED,wallpaperRect2,2)
    if tool=='back3':
        draw.rect(screen,RED,wallpaperRect3,2)
        
    ####changing the colour----------------------------------------------------------
        
    if click:
        if wheelRect.collidepoint(mx,my):
            col=screen.get_at((mx,my))
            draw.rect(screen,col,(1130,20,240,60),0)
    #if colour wheel is CLICKED (not mb[0]==1), allows colour to be changed
            
    ######using the selected tool-------------------------------------------------

    if mb[0]==1:
        if canvasRect.collidepoint(mx,my):#clicked on canvas
            screen.set_clip(canvasRect)#only allows the CANVAS to be modified
            if tool=="pencil":
                size=1
                draw.line(screen,col,(omx,omy),(mx,my),size)
                omx,omy=mx,my
                #draws line from old x,old y value to current x,y
            if tool=="eraser":
                circle(screen,WHITE,(mx,my),start,size)
                #uses the created 'circle' function to draw a smooth eraser
                start=mx,my
                if size<1:
                    size=1
                if size>30:
                    size=30
            if tool=='spray paint':
                if size>30:
                    size=30
                if size<1:
                    size=1
                for i in range(15):
                    radius=size #size isnt used in circles, so the radius variable is just set equal to the size
                    randmx=randint(-radius,radius)#creates random points in the range of the radius
                    randmy=randint(-radius,radius)
                    if radius>=((randmx)**2+(randmy)**2)**0.5:
                        #uses the distance formula to check if the points
                        #created are actually within the radius
                        draw.circle(screen,col,(mx+randmx,my+randmy),0)
                        #draws small circles within the radius of a bigger circle
            if tool=='gokuStamp':
                screen.blit(screencopy,(0,0))
                screen.blit(gokuStamp,(mx-75,my-100))
                #allows the selected stamps to be placed/dragged around
            if tool=='gokuGodStamp':
                screen.blit(screencopy,(0,0))
                screen.blit(gokuGodStamp,(mx-75,my-100))
            if tool=='vegetaStamp':         
                screen.blit(screencopy,(0,0))
                screen.blit(vegetaStamp,(mx-75,my-100))
            if tool=='hitStamp':
                screen.blit(screencopy,(0,0))
                screen.blit(hitStamp,(mx-75,my-100))
            if tool=='beerusStamp':
                screen.blit(screencopy,(0,0))
                screen.blit(beerusStamp,(mx-75,my-100))
            if tool=='whisStamp':
                screen.blit(screencopy,(0,0))
                screen.blit(whisStamp,(mx-75,my-100))
            if tool=='friezaStamp':
                screen.blit(screencopy,(0,0))
                screen.blit(friezaStamp,(mx-75,my-100))
            if tool=='buuStamp':
                screen.blit(screencopy,(0,0))
                screen.blit(buuStamp,(mx-75,my-100))
            if tool=='eye dropper':
                if canvasRect.collidepoint(mx,my):
                    col=screen.get_at((mx,my))
                #gets a colour from the canvas
            if tool=='rect':
                screen.blit(screencopy,(0,0))
                draw.rect(screen,col,(omx,omy,mx-omx,my-omy),size)
                #draws a rectangule with length that varies 
                #depending on how big the user makes it
                if size>1:
                    size=1
            if tool=='F rect':
                screen.blit(screencopy,(0,0))
                draw.rect(screen,col,(omx,omy,mx-omx,my-omy),0)
            if tool=='ellipse':
                if size<1:
                    size=1
                if size>1:
                    size=1
                screen.blit(screencopy,(0,0))
                elRect=Rect(omx,omy,mx-omx,my-omy)
                #creates a rect in which the ellipse will be drawn
                elRect.normalize()
                #normalizes the rect so it won't be shaped oddly
                try:
                    if elRect.height<size*2 or elRect.width<size*2: #checks to make sure if the diameter is bigger than the width/height
                        draw.ellipse(screen,col,(elRect))
                    else:
                        draw.ellipse(screen,col,(elRect),size)
                except:
                    pass #passes so the program wont crash if the ellipse cant be drawn
            if tool=='F ellipse':
                screen.blit(screencopy,(0,0))
                elRect=Rect(omx,omy,mx-omx,my-omy)
                elRect.normalize()
                draw.ellipse(screen,col,(elRect))
            if tool=='brush':
                circle(screen,col,(mx,my),start,size)
                #uses the created 'circle' function to draw a smooth brush
                start=mx,my
                if size<1:
                    size=1
                if size>30:
                    size=30
            if tool=='line':
                screen.blit(screencopy,(0,0))
                draw.line(screen,col,(omx,omy),(mx,my),1)
                #takes a point and allows the user to draw a line from the
                #clicked point to their new mx,my position
            if tool=='triangule':
                screen.blit(screencopy,(0,0))
                pointsList=([mx,my],[omx,omy],[omx,my])
                #gets a list of points for the draw.polygon function
                #to use and draw lines between
                draw.polygon(screen,col,pointsList,1)
                #draws the triangule
            screen.set_clip(None) #EVERYTHING can be modified
    if canvasRect.collidepoint(mx,my):
        if tool=='polygon':
            size=1
            if click:
                polygonPoints.append((mx,my))
                #adds the point clicked to a list
                if len(polygonPoints)>1: #checks if list of points is greater than 1
                    draw.line(screen,col,(polygonPoints[-2]),(polygonPoints[-1]),size)
                    #draws a line from the 2nd last to the last point in the list
            if mb[2]==1 and len(polygonPoints)>1: #checks for right click and length of list again
                draw.line(screen,col,(polygonPoints[-1]),(polygonPoints[0]),size)
                #if right click, draws a point from the last point to the first point
                polygonPoints=[]
                #empties the list
                       
            screen.set_clip(None) #EVERYTHING can be modified
            
    display.flip()  
quit() 


































