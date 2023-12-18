#Just messing around. There is no LOGIC it´s gonna be probably unbeatable
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


def dumpResults(result, sorted_list=False):
    if sorted_list:
        result = sorted(result)
    with open("dump.txt", "w") as fd:
        for r in result:
            fd.write(r)
            fd.write("\n")

with open("original.bin", "rb") as inFile:
    file = list(inFile.read())


if __name__ == '__main__':
    results = []
    relics_to_place = list(range(0, 30))
    print("Items:")
    for i in ITEMS.ITEMS_LIST:
        if i.entities:
            for e in i.entities: #[ZONE, INDEX, [ADDRESSES]
                new_item_id = random.randrange(1, 258)
                if new_item_id == 12 or new_item_id == 23:
                    item_to_place = ITEMS.get_nameid(new_item_id, random.choice([False, True]))
                else:
                    item_to_place = ITEMS.get_nameid(new_item_id)
                if ZONES.ZONES_LIST[e[0]].id == "ST0":
                    continue
                if i.id == -2:
                    for add in e[2]:
                        offset = add + e[1] * 0x02
                        write_short(file, offset, item_to_place[1])
                        r = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + i.name + " @ " + hex(offset) + " = " + item_to_place[0]
                        print(r)
                        results.append(r)
                elif i.id == -3:
                    for add in e[2]:
                        offset = add + e[1] * 0x02
                        relic_id = relics_to_place.pop(random.randrange(len(relics_to_place)))
                        write_short(file, offset, relic_id)
                        r = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + i.name + " @ " + hex(offset) + ITEMS.RELICS_LIST[relic_id].name
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
                        write_short(file, address, item_to_place[1])
                        r = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + i.name + " @ " + hex(address) + " = " + item_to_place[0]
                        print(r)
                        results.append(r)

    print("Relics:")
    for r in ITEMS.RELICS_LIST:
        if r.name == "Jewel of Open" or r.name == "Sprite Card" or r.name == "Nosedevil Card":
            continue
        if len(relics_to_place) != 0:
            relic_id = relics_to_place.pop(random.randrange(len(relics_to_place)))
        else:
            relic_id = 0x16
        
        if r.name == "Bat Card":
            address = 0x054b1d58
            write_short(file, address, relic_id)
            result = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + r.name + " @ " + hex(address) + " = " + ITEMS.RELICS_LIST[relic_id].name
            print(result)
            results.append(result)
            continue
        if r.name == "Skill of Wolf":
            address = 0x054b1d5a
            write_short(file, address, relic_id)
            result = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + r.name + " @ " + hex(address) + " = " + ITEMS.RELICS_LIST[relic_id].name
            print(result)
            results.append(result)
            continue
        if r.entities:
            for e in r.entities:
                for add in e[1]:
                    offset = romOffset(ZONES.ZONES_LIST[e[0]], add + 0x08)
                    write_short(file, offset, relic_id)
                    result = ZONES.ZONES_LIST[e[0]].id + " - " + ZONES.ZONES_LIST[e[0]].name + ": " + r.name + " @ " + hex(offset) + " = " + ITEMS.RELICS_LIST[relic_id].name
                    print(result)
                    results.append(result)
 
    dumpResults(results, True)
  
    with open("Castlevania - Symphony of the Night (USA) (Track 1).bin", "wb") as outFile:
        outFile.write(bytearray(file))


print("DONE EDITING")
if platform == "win32":
    print("ERROR RECALC")
    subprocess.call(["error_recalc", "Castlevania - Symphony of the Night (USA) (Track 1).bin"])
else:
    print("ERROR RECALC FAILED")
print("ALL DONE")