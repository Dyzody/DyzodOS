from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import pygame.freetype
from pygame.locals import *
import settings

DELIMITER = settings.DELIMITER

pygame.font.init()
font = pygame.font.Font(settings.Font, settings.Font_Size)
#font = pygame.font.SysFont(settings.Font, settings.Font_Size)
StdOut = []

Bottom_Row = font.render("", True, settings.TextColour, None)

StdOut_Render_Offset_Mul = settings.Font_Size*settings.Line_Spacing

#Render the Console Output
def RenderStdOut(Flush=True):
    if Flush:
        settings.screen.fill(settings.Background)
    for Index, TextObj in enumerate(StdOut):
        settings.screen.blit(TextObj, (0, 0+Index*StdOut_Render_Offset_Mul
                                       + settings.StdOut_offset.y * StdOut_Render_Offset_Mul))
        #print(f"Rendered TextObject {StdOut}")
    settings.screen.blit(Bottom_Row, (0, settings.SCREEN_SIZE.y-10))
    pygame.display.flip()

#This adds a line to StdOut
#Function deals with Paragraphs
def WriteLn(Text):
    global StdOut
    max_line_length = settings.max_line_len
    
    if len(StdOut) > settings.Max_StdOut_Len:
        del StdOut[0]

    lines = []
    while len(Text) > max_line_length:
        lines.append(Text[:max_line_length])
        Text = Text[max_line_length:]
    lines.append(Text)

    # Render each line
    for index, line in enumerate(lines):
        #print(f"Current: {line}")
        textSurfaceObj = font.render(line, True, settings.TextColour, None)
        StdOut.append(textSurfaceObj)

#The bottom row is where the User input is at
def WriteBottomRow(Text):
    global Bottom_Row
    Bottom_Row = font.render(settings.PreRenderBottomLine+Text, True, settings.TextColour, None)

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

    settings.screen = screen
    settings.clock = clock

    #print("Starting Loop")

    while isRunning:
        #print("Running")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        RenderStdOut(True)
    
    settings.IsGraphicsRunning = False