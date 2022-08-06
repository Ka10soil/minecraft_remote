# Hello World for Minecraft Java Edition 1.16.5
# mcje, MCJE: Minecraft Java Edition
from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)


mc.setBlocks(-10, 63, 10,  -30, 83, 30,  param.GLASS)
mc.setBlocks(-11, 64, 11,  -29, 80, 29,  param.WATER)
mc.setBlocks(-11, 81, 11,  -29, 83, 29,  param.AIR)
mc.setBlocks(-10, 63, 10,  -30, 63, 30,  param.SEA_LANTERN_BLOCK)
