# Hello World for Minecraft Java Edition 1.16.5
# mcje, MCJE: Minecraft Java Edition
from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)

size = 5
x = -14
y = 63
z = 14
blockType = param.STONE
for num in range(size):
    mc.setBlocks(x+size-1-num, y+num, z+size-1-num, x-size+1+num, y+num, z-size+1+num, blockType)