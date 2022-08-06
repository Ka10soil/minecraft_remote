# Hello World for Minecraft Java Edition 1.16.5
# mcje, MCJE: Minecraft Java Edition
from mcje.minecraft import Minecraft
import param_MCJE as param
import time

mc = Minecraft.create(port=param.PORT_MC)

a = 63
for num in range(15):
    mc.setBlocks(-10, 63, 10,  -15, a, 15,  param.AIR)
    a = a + 1
    time.sleep(1)
