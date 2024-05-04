import sys
sys.path.append("../")

import API

API.WriteLine("Welcome to the Plugin!")
API.WriteLine("Say Hello!")

while API.GetInput().lower() != "hello":
    API.WriteLine("SAY HELLO NOW")

API.WriteLine("You're free now")