from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from vectors import Vector2D
import pygame.freetype
from pygame.locals import *
import settings

DELIMITER = settings.DELIMITER

pygame.font.init()
font = pygame.font.Font(settings.Font, settings.Font_Size)
#font = pygame.font.SysFont(settings.Font, settings.Font_Size)
StdOut = []

Bottom_Row = font.render("", True, settings.TextColour, None)

StdOut_Render_Offset_Mul = settings.Font_Size

def GetLinePos(Index=0):
    
    y = (Index + settings.StdOut_offset.y + settings.StdOut_offset_from_line_anmount.y) * settings.Line_Spacing * settings.Font_To_Pixel_Ratio
    LinePosition = Vector2D(0, y)
    
    return LinePosition

def Render_Shell():
    
    for Index, TextObj in enumerate(StdOut):
        
        LinePosition = GetLinePos(Index=Index)
        #Index*settings.Font_To_Pixel_Ratio + settings.StdOut_offset.y * StdOut_Render_Offset_Mul * settings.Line_Spacing)

        settings.screen.blit(TextObj, (LinePosition.x, LinePosition.y))
        #print(f"Rendered TextObject {StdOut}")

def Render_User_Input():
    
    UserLinePos = Vector2D(0, settings.SCREEN_SIZE.y-StdOut_Render_Offset_Mul - settings.Bottomrow_offset.y)
    settings.screen.blit(Bottom_Row, (UserLinePos.x, UserLinePos.y))

#Render the Console Output
def RenderStdOut():
    Render_Shell()
    Render_User_Input()

#This adds a line to StdOut
#Function deals with Paragraphs
def WriteLn(Text):
    global StdOut
    max_line_length = settings.max_line_length

    if len(StdOut) > settings.Max_StdOut_Len:
        del StdOut[0]

    lines = []
    while len(Text) > max_line_length:
        lines.append(Text[:max_line_length])
        Text = Text[max_line_length:]
    lines.append(Text)

    # Render each line
    for line in lines:
        #print(f"Current: {line}")
        textSurfaceObj = font.render(line, True, settings.TextColour, None)
        StdOut.append(textSurfaceObj)

#The bottom row is where the User input is at
def WriteBottomRow(Text):
    global Bottom_Row
    Bottom_Row = font.render(f"{settings.PreRenderBottomLine}{settings.get_dir()} {Text}", 
                             True, settings.TextColour, None)

#Rendering Loop
def InitGraphics(Fullscreen):
    isRunning = True
    
    pygame.init()
    screen = None
    
    if Fullscreen:
        screen = pygame.display.set_mode(flags=FULLSCREEN)
    else:
        screen = pygame.display.set_mode((settings.SCREEN_SIZE.x, settings.SCREEN_SIZE.y))
    pygame.display.set_caption("OS")
    clock = pygame.time.Clock()

    if screen == None or clock == None:
        print("Error Initializing Graphics: Missing Components")
        return

    settings.screen = screen
    settings.clock = clock

    #print("Starting Loop")

    while isRunning:
        #print("Running")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        settings.screen.fill(settings.Background)
        RenderStdOut()
        pygame.display.flip()
    
    settings.IsGraphicsRunning = False