from cryptography.fernet import Fernet
import sys
import vectors

#CONST
HELP_PROMPT = """
Here is a list of all commands:
"""

SCREEN_SIZE = vectors.Vector2D(1000, 800)
REFRESH_RATE = 5
Fullscreen = False

Font = "Fonts/DOS.ttf"
Font_Size = 40
Line_Spacing = 5

Font_To_Pixel_Ratio = Font_Size * 0.75

max_line_length = int(SCREEN_SIZE.x/Font_To_Pixel_Ratio)
Max_StdOut_Len = 100

CurrentUser = None

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

Background = BLACK
TextColour = WHITE

OS_KEY = b'pDFVE6RdoxBwdQUnqKnfzSB9-ptvnjekJTm3pQzZUA8='
OS_FERNET = Fernet(OS_KEY)
DEFAULT_PATH = "user_hdd"
Hard_Drive_Name = "Disk.bin"
Hard_Drive_Chunk_Name_Len = 10
DELIMITER = b"\n"

#VAR
current_path = ""
Hard_Drive = Hard_Drive_Name
IsGraphicsRunning = True
screen, clock = None, None
StdOut_offset = vectors.Vector2D(0, 0)
Bottomrow_offset = vectors.Vector2D(0, 0)
PreRenderBottomLine = ""

def get_dir():
    current = f"{DEFAULT_PATH}/{current_path}"

    if len(current_path) > 0:
        current += "/"

    return current

def reset():
    global StdOut_offset
    global Bottomrow_offset
    StdOut_offset = vectors.Vector2D(0, 0)
    Bottomrow_offset = vectors.Vector2D(0, 0)