import explorerhat
import minecraft
from time import sleep as sleep
import block

blocks = [block.WOOD_PLANKS,block.COAL_ORE,block.IRON_ORE,block.GOLD_ORE,block.WOOD_PLANKS,block.GOLD_ORE,block.WOOD_PLANKS]

def box(event,number):
  playerPos = mc.player.getPos()
  x = int(3*explorerhat.analog.one.read())
  y =int(2* explorerhat.analog.one.read())
  for q in range(x):
    for i in range(x):
      mc.setBlock(playerPos.x+i,playerPos.y+q,playerPos.z+1,blocks[int(explorerhat.analog.one.read())])
    for i in range(x):
      mc.setBlock(playerPos.x+x,playerPos.y+q,playerPos.z+1-i,blocks[int(explorerhat.analog.one.read())])
    for i in range(x):
      mc.setBlock(playerPos.x+x-i,playerPos.y+q,playerPos.z+1-x,blocks[int(explorerhat.analog.one.read())])
    for i in range(x):
      mc.setBlock(playerPos.x,playerPos.y+q,playerPos.z-x+i+1,blocks[int(explorerhat.analog.one.read())])
    

def putblock(event,number):
  mc.postToChat('Block!!')
  playerPos = mc.player.getPos()
  
  mc.setBlock(playerPos.x+1,playerPos.y,playerPos.z+1,blocks[int(explorerhat.analog.one.read())])

mc = minecraft.Minecraft.create()

mc.postToChat("Hello World")

explorerhat.touch.pressed(box)
explorerhat.touch.released(box)

while 1:
  mc.postToChat(int(3*explorerhat.analog.one.read()))
  sleep(0.5)

explorerhat.pause()
