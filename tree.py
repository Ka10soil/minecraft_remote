# Hello World for Minecraft Java Edition 1.16.5
# mcje, MCJE: Minecraft Java Edition
from mcje.minecraft import Minecraft
import param_MCJE as param
import time

from pyramid import pyramid

mc = Minecraft.create(port=param.PORT_MC)

def tree(height, thickness,  x, y, z, blockType):
    l = int(height/2)
    thickness = thickness -1
    a = 0

    for num in range(height):
        mc.setBlocks(x + thickness, y + a, z + thickness,  x + thickness, y + a, z + thickness,  blockType)
        a = a + 1
        time.sleep(1)
    pyramid(l, x, y + l, z, param.Acacia_Leaves)

tree(10, 1, 10, 63, 10, param.Acacia_Wood)


