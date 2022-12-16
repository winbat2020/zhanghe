import pymem

Game = pymem.Pymem("hl2.exe") # 游戏进程

def Get_moduladdr(dll): # 读DLL模块基址
    modules = list(Game.list_modules()) # 列出exe的全部DLL模块
    for module in modules:
        if module.name == dll:
            #print(module.name) # 模块名字
            #print(module.lpBaseOfDll) # 模块基址
            #print("找到了")
            Moduladdr = module.lpBaseOfDll
    return Moduladdr

Char_Modlue = Get_moduladdr("server.dll") # 读DLL模块基址
My_addr = Game.read_int(Char_Modlue + 0x4F615C)
My_x = Game.read_float(My_addr + 0x308)
My_y = Game.read_float(My_addr + 0x30C)
My_z = Game.read_float(My_addr + 0x310)
My_hp = Game.read_int(My_addr + 0xE4)
My_camp = Game.read_int(My_addr + 0x1F4)
print("   My |",My_camp, "|",My_hp,"|", My_x, "|", My_y, "|", My_z)
