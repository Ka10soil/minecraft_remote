# Hello World for Minecraft Java Edition 1.16.5
# mcje, MCJE: Minecraft Java Edition
from mcje.minecraft import Minecraft
import param_MCJE as param
import time

from pyramid import pyramid

mc = Minecraft.create(port=param.PORT_MC)

block1 = 1

def tree(height, thickness,  x, y, z, block1):
    if block1 == 1 :
        blockType = param.Acacia_Wood
    if block1 ==2 :
        blockType = param.Oak_Wood

    l = int(height/2)
    thickness = thickness -1
    a = 0

    for num in range(height -2):
        mc.setBlocks(x + thickness, y + a, z + thickness,  x + thickness, y + a, z + thickness,  blockType)
        a = a + 1
        time.sleep(1)

    if block1 == 1 :
        blockType = param.Acacia_Leaves
    if block1 == 2 :
        blockType = param.Oak_Leaves
    pyramid(l, x, y + l, z, blockType)

tree(10, 1, 10, 63, 10, 1)


