#import explorerhat
import minecraft
from time import sleep as sleep
import block
from thermometer import *

playerPos = 0 
blockPos = 0 

def __init__():#Create instance of thermometer
    th = MCThermometer()
#Connect to minecraft
    mc = minecraft.Minecraft.create()
    global playerPos 
    playerPos= mc.player.getPos()

def create():
    global blockPos 
    mc.postToChat("Creating Thermometer")
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
            
def setValue(high,low,value,hight):
    global blockPos
    redBlocks = (value/high)*hight 
    mc.setBlocks(blockPos.x + 2 ,blockPos.y + 5,blockPos.z,blockPos.x + 2 ,blockPos.y + 5+ redBlocks,blockPos.z,block.BLOCK(35,14)
    
    


