#import explorerhat
import minecraft
from time import sleep as sleep
import block
from thermometer import *

th = MCThermometer()


mc = minecraft.Minecraft.create()

mc.postToChat("Hello World")

playerPos = mc.player.getPos()
blockPos=playerPos
blockPos.x = playerPos.x+1
for x in range(5):
    for z in range(5):
        blockobj = block.Block(th.blockselect(x,z))
        mc.setBlock(blockPos.x+x,blockPos.z+z,blockPos.y,blockobj)

for x in range(5):
    for z in range(5,10):
        blockobj = block.Block(th.blockselect(x,4))
        mc.setBlock(blockPos.x+x,blockPos.z+z,blockPos.y,blockobj)


