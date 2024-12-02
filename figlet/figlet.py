# import sys
import sys
# import figlets
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()
args = ["-f","--font"]

if len(sys.argv) == 1:
    pick = random.choice(fonts)
    figlet.setFont(font=pick)
elif len(sys.argv) == 3:
    if sys.argv[2] not in fonts:
        sys.exit("Font not found")
    if sys.argv[1] not in args:
        sys.exit("wrong parameter")
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Argument error")

words = input("Input: ").strip()

print(figlet.renderText(words))