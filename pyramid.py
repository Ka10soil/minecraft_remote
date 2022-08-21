# Hello World for Minecraft Java Edition 1.16.5
# mcje, MCJE: Minecraft Java Edition
from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)
#sizeはピラミッドの段数
#x,y,zは作成されるピラミッドの中心となる座標
#blockTypeはピラミッドの材質

def pyramid(size, x, y, z, blockType):
    for num in range(size):
        mc.setBlocks(x+size-1-num, y+num, z+size-1-num, x-size+1+num, y+num, z-size+1+num, blockType)

