import math, re
import ITEMS, ZONES, TYPES

TILEIDOFFSET = 0X80


def romOffset(zone, address):
    return zone + address + math.floor(address / 0x800) * 0x130

def write_word(fd, address, value):
    x1, x2, x3, x4 = (value & 0xFFFFFFFF).to_bytes(4, 'little')
    fd[address] = x1
    fd[address + 1] = x2
    fd[address + 2] = x3
    fd[address + 3] = x4

def dumpResults(filename, result):
    with open(filename, "w") as fd:
        for r in result:
            fd.write(r)

def dumpItems():
    results = []
    for i in ITEMS.ITEMS_LIST:
        results.append(f'{i.name},{i.type},{i.id},{i.entities}\n')

    dumpResults("items.txt", results)

def dumpLocation():
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

# Read item.js and dump on a txt file
def dumpRandomitems():
    start = end = 0
    items = []
    names = []
    types = []
    ids = []
    tiles = []
    tile = []
    result = []
    
    with open("items.js", "r") as fd:
        buffer = fd.read()

    buffer = buffer[buffer.find("[{") + 1:]
    buffer = buffer[:buffer.rfind("}]") + 1]
    buffer = re.sub(r"\s+", "", buffer)
    
    while buffer.find("{name:", start) != -1:
        start = buffer.find("{name:", start) 
        end = buffer.find("},{name:", start)
        items.append(buffer[start:end])
        start = end

    for i in items:
        start = end = 0
        start = i.find("name:'", start) + len("name:'")
        end = i.index("'", start)
        names.append(i[start:end])

        start = i.find("type:", start) + len("type:")
        end = i.index(",", start)
        types.append(i[start:end])

        start = i.find("id:", start) + len("id:")
        end = i.index(",", start)
        ids.append(i[start:end])

        if i.find("tiles:", start) != -1:
            start = i.find("tiles:", start) + len("tiles:")
            end = i.index("}]", start) + len("}],")
            tiles.append(i[start:end])
        else:
            tiles.append("")

    start = end = 0
    buffer = []
    for t in tiles:
        while t.find("}", start) != -1:
            start = t.index("{", start)
            end = t.index("}", start)
            buffer.append(t[start:end])
            start = end + 1
        tile.append(buffer)
        start = end = 0
        buffer = []
            
        

    for i, v in enumerate(ids):
            r = f"ITEMS_LIST.append(Item(\"{names[i]}\", {types[i]}, {v}, "
            if(len(tiles[i]) == 0):
                pass
            else:
                r += "["
                for t in tile[i]:
                    if t.find("candle") != -1 or t.find("enemy") != -1 or t.find("tank") != -1 or t.find("shop") != -1:
                        continue
                    
                    else:
                        if t.find("addresses") != -1:
                            #Zone
                            start = t.find("[") + 1
                            end = t.find("]", start)
                            r += f"[{t[start:end]}, -1, ["
                            #addresses
                            start = t.find("addresses:", start) + len("addresses:") + 1
                            end = t.find("]", start)
                            r += f"{t[start:end]}]], "

                        if t.find("index:") != -1:
                            #Zone
                            start = t.find("[") + 1
                            end = t.find("]", start)
                            r += f"[{t[start:end]}, "
                            #index
                            start = t.find("index:", start) + len("index:")
                            end = t.find(",", start)
                            r += f"{t[start:end]}, ["
                            #entities
                            start = t.find("[", start) + len("[")
                            end = t.find("]", start)
                            r += f"{t[start:end]}]], "

            r = r[:r.rfind(',')]
            if r[-1] == ']':
                r += ']'
            r += "))\n"
            result.append(r)


#ITEMS_LIST.append(Item("Heart", TYPES.HEART, 0))
#ITEMS_LIST.append(Item("Rapier", TYPES.WEAPON1, 23))
#ITEMS_LIST.append(Item("Takemitsu", TYPES.WEAPON2, 27, [[ZONEID.LIB, 5, [0x377c, 0x3f10]]]))
#ITEMS_LIST.append(Item("Monster vial 3", TYPES.USABLE, 3, [[ZONEID.CAT, 17, [0x3206, 0x3ae6]], [ZONEID.CAT, 18, [0x321a, 0x3afa]], [ZONEID.CAT, 19, [0x3224, 0x3b04]], [ZONEID.CAT, 20, [0x3238, 0x3b18]]]))
    dumpResults("dump.txt", buffer)
    dumpResults("dump_items.txt", items)
    dumpResults("dump_names.txt", names)
    dumpResults("dump_types.txt", types)
    dumpResults("dump.id", ids)
    dumpResults("dump_tiles.txt", tiles)
    dumpResults("dump_results.txt", result)
    

    """dumpResults("dump.txt", buffer)
    dumpResults("name.txt", name)
    dumpResults("type.txt", type)
    dumpResults("id.txt", id)
    dumpResults("tiles.txt", tiles)
    dumpResults("results.txt", results)"""

def items_ap():
    types = ["Heart", "Gold", "Subweapon", "Powerup", "Weapon1", "Weapon2", "Shield", "Helmet", "Armor", "Cloak", "Accessory", "Usable", "Relic", "BReward"]
    results = []
    for i in ITEMS.ITEMS_LIST:
        results.append(f'"{i.name}": ItemData({i.id}, Type.{types[i.type].upper()}),\n')
    
    dumpResults("itemsap.txt", results)


print(hex(romOffset(0x069d1598, 0x1300)))
items_ap()


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
