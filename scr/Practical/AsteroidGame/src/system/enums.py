from system.object.sound import Sound
from system.object.background import Background
from system.object.display import gen_screen, display

size = width, height = display.size

screen = gen_screen(size)

bg = Background("../res/bg/bg-root.jpeg")
font = "../res/font/game-font.ttf"
bg_item = "../res/bg/bg-cometa.png"

sound = Sound()
