import math
import ITEMS, ZONES

TILEIDOFFSET = 0X80


def romOffset(zone, address):
    return zone + address + math.floor(address / 0x800) * 0x130

def write_word(fd, address, value):
    x1, x2, x3, x4 = (value & 0xFFFFFFFF).to_bytes(4, 'little')
    fd[address] = x1
    fd[address + 1] = x2
    fd[address + 2] = x3
    fd[address + 3] = x4

def dump_items():
    results = []
    for z in ZONES.ZONES_LIST:
        if z.id == "ST0":
            continue
        for i in ITEMS.ITEMS_LIST:
            if not i.entities:
                continue
            for e in i.entities:
                if e[0] == z.num:
                    results.append(f"{z.id}, {e[1]} -> {i.name}")

    with open("items.txt", "w") as fd:
        for r in results:
            fd.write(r)
            fd.write("\n")






print(hex(romOffset(0x069d1598, 0x1300)))

#ZONES_LIST.append(Zone(48, "RBO7", "Akmodan II", 0x069d1598, rew=0x1300))
#ZONES_LIST.append(Zone(41, "RBO0", "Trio", 0x064705f8, rew=0x1988))
#ZONES_LIST.append(Zone(44, "RBO3", "Medusa", 0x067422a8, rew=0x12a8))
#ZONES_LIST.append(Zone(49, "RBO8", "Galamoth", 0x06a5f2e8, rew=0x2334))
#ZONES_LIST.append(Zone(43, "RBO2", "Death", 0x06620c28, rew=0x1788))
#ZONES_LIST.append(Zone(46, "RBO5", "Doppleganger40", 0x06861468, rew=0x4348))
#ZONES_LIST.append(Zone(42, "RBO1", "Beezlebub", 0x06590a18, rew=0x1550))
#ZONES_LIST.append(Zone(45, "RBO4", "Creature", 0x067cfff8, rew=0x13b4))
#ZONES_LIST.append(Zone(30, "RNZ1", "Reverse Clock Tower", 0x059bb0d8, rew=0x2570, items=0x0ec8))
#ZONES_LIST.append(Zone(34, "BO1", "Legion", 0x0606dab8, rew=0x1b98))
#ZONES_LIST.append(Zone(37, "BO4", "Doppleganger10", 0x06246d38, rew=0x42b0))
#ZONES_LIST.append(Zone(11, "NO3", "Castle Entrance", 0x04b665e8, items=0x1c8c)) 49e6978 194f90
#ZONES_LIST.append(Zone(13, "NO4", "Underground Caverns", 0x04c307e8, items=0x1928))
#ZONES_LIST.append(Zone("NZ0", "Alchemy Laboratory", 0x054b0c88, items=0x13b0))
#ZONES_LIST.append(Zone("RBO3", "Medusa", 0x067422a8, rew=0x12a8))
#ITEMS_LIST.append(Item("Alucart mail", TYPES.ARMOR, 258, [[ZONEID.NO0, 6, [0x3698, 0x4518]]]))
