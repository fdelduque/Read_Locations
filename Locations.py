from dataclasses import dataclass
from sys import platform
import math
import subprocess
import random

import ZONES, ITEMS

@dataclass(frozen=True)
class Item:
    name: str
    type: int
    id: int
    entities: list[int] = None #[[ZONE, INDEX, [ADDRESSES]]]

@dataclass(frozen=True)
class Relic:
    name: str
    id: int
    entities: list[int] = None #[[ZONE, [ADDRESSES]]]
    asX: int = 0x0
    asY: int = 0x0

def romOffset(zone, address):
    return zone.pos + address + math.floor(address / 0x800) * 0x130

def write_short(fd, address, value):
    x1, x2 = (value & 0xFFFF).to_bytes(2, 'little')
    fd[address] = x1
    fd[address + 1] = x2

def write_word(fd, address, value):
    x1, x2, x3, x4 = (value & 0xFFFFFFFF).to_bytes(4, 'little')
    fd[address] = x1
    fd[address + 1] = x2
    fd[address + 2] = x3
    fd[address + 3] = x4
    return address + 4


def dumpResults(result):
    with open("dump.txt", "w") as fd:
        for r in results:
            fd.write(r)
            fd.write("\n")

with open("original.bin", "rb") as inFile:
    file = list(inFile.read())


if __name__ == '__main__':
    results = []
    print("Items:")
    for i in ITEMS.ITEMS_LIST:
        if i.entities:
            new_item = random.choice([3, 4, 5, 6, 7, 9])
            for e in i.entities: #[[ZONE, INDEX, [ADDRESSES]]]
                if ZONES.ZONES_LIST[e[0]].id == "ST0":
                    continue
                if i.id == -2:
                    for add in e[2]:
                        offset = add + e[1] * 0x02
                        write_short(file, offset, new_item)
                        r = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + i.name + " @ " + hex(offset) + " = " + ITEMS.ITEMS_LIST[new_item].name
                        print(r)
                        results.append(r)
                elif i.id == -3:
                    for add in e[2]:
                        offset = add + e[1] * 0x02
                        write_short(file, offset, 0x16)
                        r = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + i.name + " @ " + hex(offset) + " = Sword Card"
                        print(r)
                        results.append(r)
                        continue
                else:
                    if e[1] == -1:
                        for add in e[2]:
                            r = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + i.name + " @ " + hex(add)
                            print(r)
                            write_short(file, add, 0x0)
                            results.append(r)
                    else:
                        offset = ZONES.ZONES_LIST[e[0]].items + 0x02 * e[1]
                        address = romOffset(ZONES.ZONES_LIST[e[0]], offset)
                        write_short(file, address, new_item)
                        r = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + i.name + " @ " + hex(address) + " = " + ITEMS.ITEMS_LIST[new_item].name
                        print(r)
                        results.append(r)

    print("Relics:")
    for r in ITEMS.RELICS_LIST:
        if r.name == "Bat Card":
            address = 0x054b1d58
            write_short(file, address, 0x16)
            result = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + r.name + " @ " + hex(offset) + " = " + ITEMS.RELICS_LIST[0x16].name
            print(result)
            results.append(result)
            continue
        if r.name == "Skill of Wolf":
            address = 0x054b1d5a
            write_short(file, address, 0x16)
            result = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + r.name + " @ " + hex(offset) + " = " + ITEMS.RELICS_LIST[0x16].name
            print(result)
            results.append(result)
            continue
        if r.entities:
            for e in r.entities:
                for add in e[1]:
                    offset = romOffset(ZONES.ZONES_LIST[e[0]], add + 0x08)
                    write_short(file, offset, 0x16)
                    result = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + r.name + " @ " + hex(offset) + " = " + ITEMS.RELICS_LIST[0x16].name
                    print(result)
                    results.append(result)
    dumpResults(results)
    

    #remove medusa relic(NEED MORE TESTING)
    """index = 11 # ?? 11
    id = 0
    #patch item table
    offset = romOffset(0x04e31458, 0x0d2c + 0x02 * index)
    write_short(file, offset, id + ITEMS.TILEIDOFFSET)
    #foreach entity 0x1dc4 
    offset = romOffset(0x04e31458, 0x1dc4 + 0x02)
    write_short(file, offset, 0xc9)
    offset = romOffset(0x04e31458, 0x1dc4 + 0x04)
    write_short(file, offset, 0x0c)
    offset = romOffset(0x04e31458, 0x1dc4 + 0x08)
    write_short(file, offset, index)
    # entity 0x2730 
    offset = romOffset(0x04e31458, 0x2730 + 0x02)
    write_short(file, offset, 0xc9)
    offset = romOffset(0x04e31458, 0x2730 + 0x04)
    write_short(file, offset, 0x0c)
    offset = romOffset(0x04e31458, 0x2730 + 0x08)
    write_short(file, offset, index)
    # Patch instructions that load a relic.
    write_word(file, 0x06757b54, 0x34020000)
    # Patch boss reward.
    write_short(file, romOffset(0x067422a8, 0x12a8), id + ITEMS.TILEIDOFFSET)
    # Até aqui é suficiente para cair 2 items
    # Entry point
    offset = romOffset(0x04e31458, 0x034950)
    offset = write_word(file, offset, 0x00000000) #j inj
    #correto da anterior offset = write_word(file, offset, 0x08071e40) trava o load
    offset = write_word(file, offset, 0x00041400) #sll v0, a0, 10
    #Zero tile function if item is equipped.
    offset = romOffset(0x04e31458, 0x047900)
    offset = write_word(file, offset, 0x34090000 + id + ITEMS.TILEIDOFFSET) #ori t1, r0, id
    #foreach 'r':  0x097c00
    offset = write_word(file, offset, 0x3c080009) #lui t0, 0x8009
    offset = write_word(file, offset, 0x91087c00) #lbu t0, slot (t0)
    offset = write_word(file, offset, 0x00000000) #nop
    offset = write_word(file, offset, 0x1108fff1) #beq t0, t1, pc + next 0x1108fff1
    offset = write_word(file, offset, 0x00000000) #nop    
    #foreach 'l':  0x097c04
    offset = write_word(file, offset, 0x3c080009) #lui t0, 0x8009 
    offset = write_word(file, offset, 0x91087c04) #lbu t0, slot (t0)
    offset = write_word(file, offset, 0x00000000) #nop
    offset = write_word(file, offset, 0x1108fff1) #beq t0, t1, pc + next 0x1108fff1
    offset = write_word(file, offset, 0x00000000) #nop   
    #fim foreach
    #Inventory check
    offset = write_word(file, offset, 0x3c088009) #lui t0, 0x8009
    offset = write_word(file, offset, 0x91080080) #lbu t0, 0x798a + id (v0) 0x91080080
    offset = write_word(file, offset, 0x00000000) #nop
    offset = write_word(file, offset, 0x11000004) #beq t0, r0, pc + 0x14
    offset = write_word(file, offset, 0x3409000f) #ori t1, r0, 0x000f
    offset = write_word(file, offset, 0x3c088018) #lui t0, 0x8018
    #foreach entity 0x1dc4, 0x2730
    offset = write_word(file, offset, 0xa5091dc8) #sh t1, entity + 4 (t0) 0xa5091dc8
    offset = write_word(file, offset, 0xa5092734) #sh t1, entity + 4 (t0) 0xa5092734
    #return
    offset = write_word(file, offset, 0x03e00008) #jr ra
    offset = write_word(file, offset, 0x00000000) #nop"""
  
    with open("Castlevania - Symphony of the Night (USA) (Track 1).bin", "wb") as outFile:
        outFile.write(bytearray(file))


print("DONE EDITING")
if platform == "win32":
    print("ERROR RECALC")
    subprocess.call(["error_recalc", "Castlevania - Symphony of the Night (USA) (Track 1).bin"])
else:
    print("ERROR RECALC FAILED")
print("ALL DONE")





