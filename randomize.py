from dataclasses import dataclass
from sys import platform
import math
import subprocess
import random

import ZONES, ITEMS,TYPES


  



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
            for e in i.entities: #[ZONE, INDEX, [ADDRESSES]
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

    """print("Relics:")
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
                    results.append(result)"""
    dumpResults(results)
  
    with open("Castlevania - Symphony of the Night (USA) (Track 1).bin", "wb") as outFile:
        outFile.write(bytearray(file))


print("DONE EDITING")
if platform == "win32":
    print("ERROR RECALC")
    subprocess.call(["error_recalc", "Castlevania - Symphony of the Night (USA) (Track 1).bin"])
else:
    print("ERROR RECALC FAILED")
print("ALL DONE")