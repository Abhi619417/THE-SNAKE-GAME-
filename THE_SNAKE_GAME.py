import pygame,sys
import time
import random

# initializing the window
pygame.init()

#defining the colors
white=(255,255,255)
black=(100,0,0)
red=(255,0,0)

#setting up the height and width of the screen
window_width=800
window_height=700

#displaying the screen
gameDisplay=pygame.display.set_mode((window_width,window_height))

#tittle of the game
pygame.display.set_caption('THE SNAKE GAME')

clock=pygame.time.Clock()
#frames per second
FPS=5
#block size of snake 
blockSize=20

noPixel=0

#exiting from the game
def myquit():
    pygame.quit()
    sys.exit(0)
    

font=pygame.font.SysFont(None, 25,bold=True)

    
#displaying the snake 
def snake(blockSize,snakeList):
    for size in snakeList:
        pygame.draw.rect(gameDisplay,black,[size[0]+5,size[1],blockSize,blockSize],2)

# display the message to screen with position on the screen
def message_to_screen(msg,color):
    screen_text=font.render(msg,True,color)
    gameDisplay.blit(screen_text,[window_width/4,window_height/2])
 
#key board handiling ,eating the apple ,increasing the snake size
def gameLoop():
    gameExit=False 
    gameOver=False
    
    #starting position of snake
    lead_x=window_width/2 
    lead_y=window_height/2
    
    change_pixels_of_x=0
    change_pixels_of_y=0
    
    #position of blocks of snake
    snakelist=[]
    
    #length of the snake
    snakeLength=1
    
    # initializing the position of apple on screen 
    randomAppleX=round(random.randrange(0,window_width-blockSize)/10.0)*10.0
    randomAppleY=round(random.randrange(0,window_height-blockSize)/10.0)*10.0
    
    while not gameExit:
        
        # if the snake touches touches the boundary or touches itself
        while gameOver==True:
            gameDisplay.fill(white)
            message_to_screen("Game over,press C to continue or Q to quit",red)
            pygame.display.update()
            
            for event in pygame.event.get():
                
                #if user want to closing the tab
                if event.type==pygame.QUIT:
                    gameOver=False
                    gameExit=True
                
                #if user want to continue or quit
                if event.type==pygame.KEYDOWN:
                    
                    #if user want to quit press q
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameOver=False
                       
                    #if user want to continue press c
                    if event.key==pygame.K_c:
                        #start the game again
                        gameLoop()
            
        #for handling the snake or closing the tab
        for event in pygame.event.get():
             
            #if user want to closing the tab
            if event.type==pygame.QUIT:
                gameExit=True
            
            #to handle the snake
            if event.type==pygame.KEYDOWN:
                  
                # if user press the escape key
                if event.key==pygame.K_ESCAPE:
                    #calling the user defind function my quit
                    myquit()
                 
                #to check user has press which key left,right,up,down
                
                #left key
                leftArrow=event.key==pygame.K_LEFT
                
                #right key
                rightArrow=event.key==pygame.K_RIGHT
                
                #up key
                upArrow=event.key==pygame.K_UP
                
                #down key
                downArrow=event.key=pygame.K_DOWN
                
                # for left key pressed    
                if leftArrow:
                        #changing the positions of x and y
                        change_pixels_of_x=-blockSize
                        change_pixels_of_y=noPixel
                    
                # for right key presses    
                elif rightArrow:
                        change_pixels_of_x=blockSize
                        change_pixels_of_y=noPixel
                        
                #for up key pressed    
                elif upArrow:
                        change_pixels_of_x=noPixel
                        change_pixels_of_y=-blockSize
                        
                #for downn key pressed    
                elif downArrow:
                        change_pixels_of_x=noPixel
                        change_pixels_of_y=blockSize
            
         #if snake touches the boundary
        '''if lead_x >=window_width or lead_x<0 or lead_y>=window_height or lead_y<0:
                gameOver=True
                message_to_screen("Game over,press C to continue or Q to quit",red)
           '''     
        #changing the position of head of snake    
        lead_x+=change_pixels_of_x
        lead_y+=change_pixels_of_y
         
        #if snake touches the boundary
        if lead_x >=window_width or lead_x<0 or lead_y>=window_height or lead_y<0:
            gameOver=True
            message_to_screen("Game over,press C to continue or Q to quit",red)
                
        gameDisplay.fill(white)
         
        #size of apple
        AppleThickness=20
            
        #print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])
        
        #displaying the apple
        pygame.draw.rect(gameDisplay,red,[randomAppleX,randomAppleY,AppleThickness,AppleThickness])
            
        #adding the position of snake to snake list         
        allspriteslist=[]
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)
        
        #deleting the previous block
        if len(snakelist)>snakeLength:
            del snakelist[0]
        
        # if the snake touches itself   
        for eachSegment in snakelist[:-1]:
            if eachSegment==allspriteslist:
                gameOver=True
                message_to_screen("Game over,press C to continue or Q to quit",red)
        #to display the snake      
        snake(blockSize,snakelist)
          
        #to update the screen
        pygame.display.update()
        
        # if the apple is straight away from mouth of snake    
        if lead_x>=randomAppleX and lead_x<=randomAppleX+AppleThickness:
            if lead_y>=randomAppleY and lead_y<=randomAppleY+AppleThickness:
                
                #changing the positions of apple
                randomAppleX=round(random.randrange(0,window_width-blockSize)/10.0)*10.0
                randomAppleY=round(random.randrange(0,window_height-blockSize)/10.0)*10.0
                
                #changing the length of the snake
                snakeLength+=1
    
        
        #change in frame per second            
        clock.tick(FPS)
    #quitiing the game
    pygame.quit()

#starting the game
gameLoop()   
            
