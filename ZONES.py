from dataclasses import dataclass

@dataclass(frozen=True)
class Zone:
    num: int
    id: str
    name: str
    pos: int
    rew: int = 0
    items: int = 0

ZONES_LIST = []

ZONES_LIST.append(Zone(0, "ST0", "Final Stage: Bloodlines", 0x0533efc8, items=0x0a60))
ZONES_LIST.append(Zone(1, "ARE", "Colosseum", 0x043c2018, items=0x0fe8))
ZONES_LIST.append(Zone(2, "CAT", "Catacombs", 0x0448f938, items=0x174c))
ZONES_LIST.append(Zone(3, "CEN", "Center Cube", 0x0455bff8) )
ZONES_LIST.append(Zone(4, "CHI", "Abandoned Mine", 0x045e8ae8, items=0x09e4))
ZONES_LIST.append(Zone(5, "DAI", "Royal Chapel", 0x04675f08, items=0x0ec0))
ZONES_LIST.append(Zone(6, "DRE", "Nightmare", 0x05af2478))
ZONES_LIST.append(Zone(7, "LIB", "Long Library", 0x047a1ae8, items=0x1a90))
ZONES_LIST.append(Zone(8, "NO0", "Marble Gallery", 0x048f9a38, items=0x1100))
ZONES_LIST.append(Zone(9, "NO1", "Outer Wall", 0x049d18b8, items=0x1a2c))
ZONES_LIST.append(Zone(10, "NO2", "Olrox´s Quarters", 0x04aa0438, items=0x0fec))
ZONES_LIST.append(Zone(11, "NO3", "Castle Entrance", 0x04b665e8, items=0x1c8c))
ZONES_LIST.append(Zone(12, "NP3", "Castle Entrance (after visiting Alchemy Laboratory)", 0x053f4708, items=0x1618))
ZONES_LIST.append(Zone(13, "NO4", "Underground Caverns", 0x04c307e8, items=0x1928))
ZONES_LIST.append(Zone(14, "NZ0", "Alchemy Laboratory", 0x054b0c88, items=0x13b0))
ZONES_LIST.append(Zone(15, "NZ1", "Clock Tower", 0x055724b8, items=0x111c))
ZONES_LIST.append(Zone(16, "TOP", "Castle Keep", 0x0560e7b8, items=0x0d10))
ZONES_LIST.append(Zone(17, "WRP", "Warp rooms", 0x05883408))
ZONES_LIST.append(Zone(18, "RARE", "Reverse Colosseum", 0x057509e8, items=0x0a3c))
ZONES_LIST.append(Zone(19, "RCAT", "Floating Catacombs", 0x04cfa0b8, items=0x13c8))
ZONES_LIST.append(Zone(20, "RCEN", "Reverse Center Cube", 0x056bd9e8))
ZONES_LIST.append(Zone(21, "RCHI", "Cave", 0x04da4968, items=0x07cc))
ZONES_LIST.append(Zone(22, "RDAI", "Anti-Chapel", 0x04e31458, items=0x0d2c))
ZONES_LIST.append(Zone(23, "RLIB", "Forbidden Library", 0x04ee2218, items=0x0bc8))
ZONES_LIST.append(Zone(24, "RNO0", "Black Marble Gallery", 0x04f84a28, items=0x0f8c))
ZONES_LIST.append(Zone(25, "RNO1", "Reverse Outer Wall", 0x0504f558, items=0x0ae4))
ZONES_LIST.append(Zone(26, "RNO2", "Death Wing´s Lair", 0x050f7948, items=0x0d40))
ZONES_LIST.append(Zone(27, "RNO3", "Reverse Entrance", 0x051ac758, items=0x0f10))
ZONES_LIST.append(Zone(28, "RNO4", "Reverse Caverns", 0x0526a868, items=0x1620))
ZONES_LIST.append(Zone(29, "RNZ0", "Necromancy Laboratory", 0x05902278, items=0x0cc8))
ZONES_LIST.append(Zone(30, "RNZ1", "Reverse Clock Tower", 0x059bb0d8, rew=0x2570, items=0x0ec8))
ZONES_LIST.append(Zone(31, "RTOP", "Reverse Castle Keep", 0x057df998, items=0x07c8))
ZONES_LIST.append(Zone(32, "RWRP", "Reverse Warp rooms", 0x05a6e358))
ZONES_LIST.append(Zone(33, "BO0", "Olrox", 0x05fa9dc8, rew=0x24d4))
ZONES_LIST.append(Zone(34, "BO1", "Legion", 0x0606dab8, rew=0x1b98))
ZONES_LIST.append(Zone(35, "BO2", "Werewolf & Minotaur", 0x060fca68, rew=0x181c))
ZONES_LIST.append(Zone(36, "BO3", "Scylla", 0x061a60b8, rew=0x1c60, items=0x108c))
ZONES_LIST.append(Zone(37, "BO4", "Doppleganger10", 0x06246d38, rew=0x42b0))
ZONES_LIST.append(Zone(38, "BO5", "Hippogryph", 0x06304e48, rew=0x18b8))
ZONES_LIST.append(Zone(39, "BO6", "Richter", 0x063aa448, rew=0x2f90))
ZONES_LIST.append(Zone(40, "BO7", "Cerberus", 0x066b32f8, rew=0x1440))
ZONES_LIST.append(Zone(41, "RBO0", "Trio", 0x064705f8, rew=0x1988))
ZONES_LIST.append(Zone(42, "RBO1", "Beezlebub", 0x06590a18, rew=0x1550))
ZONES_LIST.append(Zone(43, "RBO2", "Death", 0x06620c28, rew=0x1788))
ZONES_LIST.append(Zone(44, "RBO3", "Medusa", 0x067422a8, rew=0x12a8))
ZONES_LIST.append(Zone(45, "RBO4", "Creature", 0x067cfff8, rew=0x13b4))
ZONES_LIST.append(Zone(46, "RBO5", "Doppleganger40", 0x06861468, rew=0x4348))
ZONES_LIST.append(Zone(47, "RBO6", "Shaft/Dracula", 0x0692b668))
ZONES_LIST.append(Zone(48, "RBO7", "Akmodan II", 0x069d1598, rew=0x1300))
ZONES_LIST.append(Zone(49, "RBO8", "Galamoth", 0x06a5f2e8, rew=0x2334))