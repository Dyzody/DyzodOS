from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import keyboard_driver
import pygame
from vectors import Vector2D
import pygame.freetype
from pygame.locals import *
import settings

DELIMITER = settings.DELIMITER
pygame.font.init()
font = pygame.font.Font(settings.Font, settings.Font_Size)

render_frame_functions = {}
StdOut = []

Bottom_Row = font.render("", True, settings.TextColour, None)

StdOut_Render_Offset_Mul = settings.Font_Size

def GetLinePos(Index=0) -> Vector2D:
    
    y = (Index + settings.StdOut_offset.y + settings.StdOut_offset_from_line_anmount.y) * settings.Line_Spacing * settings.Font_To_Pixel_Ratio
    LinePosition = Vector2D(0, y)
    
    return LinePosition

def onrenderframe(func, params) -> str:
    Obj_Reference = f"FUN {len(render_frame_functions)}"
    render_frame_functions[Obj_Reference] = (func, (params))
    return Obj_Reference

def getrenderparams(Obj_Reference) -> tuple:
    func, params = render_frame_functions[Obj_Reference]
    return params

def changerenderparams(Obj_Reference, newparams) -> None:
    func, params = render_frame_functions[Obj_Reference]
    render_frame_functions[Obj_Reference] = (func, (newparams))

def unbindfromframe(Obj_Reference) -> None:
    del render_frame_functions[Obj_Reference]

def DrawRect(pos:Vector2D, size:Vector2D, color:tuple=settings.WHITE) -> pygame.rect:
    return pygame.draw.rect(settings.screen, color, (pos.x, pos.y, size.x, size.y))

def Render_Shell() -> None:
    for Index, TextObj in enumerate(StdOut):
        LinePosition = GetLinePos(Index=Index)
        settings.screen.blit(TextObj, (LinePosition.x, LinePosition.y))
        #print(f"Rendered TextObject {StdOut}")

def Render_User_Input() -> None:
    UserLinePos = Vector2D(0, settings.SCREEN_SIZE.y-StdOut_Render_Offset_Mul - settings.Bottomrow_offset.y)
    settings.screen.blit(Bottom_Row, (UserLinePos.x, UserLinePos.y))

#Render the Console Output
def RenderStdOut() -> None:
    Render_Shell()
    Render_User_Input()

#This adds a line to StdOut
#Function deals with Paragraphs
def WriteLn(Text) -> None:
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
def WriteBottomRow(Text) -> None:
    print("Rendering: " + Text)
    global Bottom_Row
    Bottom_Row = font.render(f"{settings.PreRenderBottomLine}{settings.get_dir()} {Text}", 
                             True, settings.TextColour, None)

#Rendering Loop
def InitGraphics(Fullscreen) -> None:
    isRunning = True

    pygame.init()
    settings.currentpygame = pygame
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
            #print(event)
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.TEXTINPUT:
                keyboard_driver.log_keystroke_text(event)
                WriteBottomRow(settings.InputBuffer)
            if event.type == pygame.KEYDOWN:
                keyboard_driver.log_otherinp(event)
                WriteBottomRow(settings.InputBuffer)
                
        settings.screen.fill(settings.Background)
        
        #print(f"Function contains {render_frame_functions}")

        frame_functions_copy = render_frame_functions.copy()

        for function_reference in frame_functions_copy:
            #print(function_reference)
            funct, params = frame_functions_copy[function_reference]
            print(params)
            
            print(*params[0].InText())
            
            if isinstance(params, tuple):
                funct(*params)
            else:
                funct(params)

        RenderStdOut()
        pygame.display.flip()
    
    settings.IsGraphicsRunning = False#
    return False