from dataclasses import dataclass
import TYPES, ZONEID

TILEIDOFFSET = 0X80

@dataclass(frozen=True)
class Item:
    name: str
    type: int
    id: int
    entities: list[int] = None #[ZONE, INDEX, [ADDRESSES]]


@dataclass(frozen=True)
class Relic:
    name: str
    id: int
    entities: list[int] = None #[[ZONE, [ADDRESSES]]]
    asX: int = 0x0
    asY: int = 0x0

ITEMS_LIST = []
RELICS_LIST = []

ITEMS_LIST.append(Item("Heart", TYPES.HEART, 0))
ITEMS_LIST.append(Item("Big Heart", TYPES.HEART, 1))
ITEMS_LIST.append(Item("$1", TYPES.GOLD, 2))
ITEMS_LIST.append(Item("$25", TYPES.GOLD, 3))
ITEMS_LIST.append(Item("$50", TYPES.GOLD, 4))
ITEMS_LIST.append(Item("$100", TYPES.GOLD, 5))
ITEMS_LIST.append(Item("$250", TYPES.GOLD, 6))
ITEMS_LIST.append(Item("$400", TYPES.GOLD, 7))
ITEMS_LIST.append(Item("$1000", TYPES.GOLD, 9))
ITEMS_LIST.append(Item("$2000", TYPES.GOLD, 10))
ITEMS_LIST.append(Item("Monster vial 1", TYPES.USABLE, 1))
ITEMS_LIST.append(Item("Monster vial 2", TYPES.USABLE, 2))
ITEMS_LIST.append(Item("Monster vial 3", TYPES.USABLE, 3, [[ZONEID.CAT, 17, [0x3206, 0x3ae6]], [ZONEID.CAT, 18, [0x321a, 0x3afa]], [ZONEID.CAT, 19, [0x3224, 0x3b04]], [ZONEID.CAT, 20, [0x3238, 0x3b18]]]))
ITEMS_LIST.append(Item("Shield rod", TYPES.WEAPON1, 4, [[ZONEID.ARE, 1, [0x3180, 0x3808]]]))
ITEMS_LIST.append(Item("Leather shield", TYPES.SHIELD, 5, [[ZONEID.NZ0, 8, [0x2cf8, 0x36b4]]]))
ITEMS_LIST.append(Item("Knight shield", TYPES.SHIELD, 6, [[ZONEID.ARE, 4, [0x34e6, 0x3ba0]]]))
ITEMS_LIST.append(Item("Iron shield", TYPES.SHIELD, 7))
ITEMS_LIST.append(Item("AxeLord shield", TYPES.SHIELD, 8))
ITEMS_LIST.append(Item("Herald Shield", TYPES.SHIELD, 9, [[ZONEID.NO4, 7, [0x3fa0, 0x503c]]]))
ITEMS_LIST.append(Item("Dark Shield", TYPES.SHIELD, 10))
ITEMS_LIST.append(Item("Goddess shield", TYPES.SHIELD, 11, [[ZONEID.RNZ0, 3, [0x289a, 0x3166]]]))
ITEMS_LIST.append(Item("Shaman shield", TYPES.SHIELD, 12, [[ZONEID.NZ1, 8, [0x29c6, 0x33d2]]]))
ITEMS_LIST.append(Item("Medusa shield", TYPES.SHIELD, 13))
ITEMS_LIST.append(Item("Skull shield", TYPES.SHIELD, 14))
ITEMS_LIST.append(Item("Fire shield", TYPES.SHIELD, 15))
ITEMS_LIST.append(Item("Alucard shield", TYPES.SHIELD, 16, [[ZONEID.RNO4, 0, [0x3880, 0x47da]]]))
ITEMS_LIST.append(Item("Sword of Dawn", TYPES.WEAPON2, 17, [[ZONEID.RTOP, 0, [0x1c76, 0x2040]]]))
ITEMS_LIST.append(Item("Basilard", TYPES.WEAPON1, 18, [[ZONEID.NZ0, 9, [0x2ca8, 0x360a]]]))
ITEMS_LIST.append(Item("Short sword", TYPES.WEAPON1, 19))
ITEMS_LIST.append(Item("Combat knife", TYPES.WEAPON1, 20, [[ZONEID.CHI, 5, [0x1a84, 0x1df4]]]))
ITEMS_LIST.append(Item("Nunchaku", TYPES.WEAPON2, 21, [[ZONEID.NO4, 36, [0x3c4e, 0x4c72]]]))
ITEMS_LIST.append(Item("Were Bane", TYPES.WEAPON1, 22))
ITEMS_LIST.append(Item("Rapier", TYPES.WEAPON1, 23))
ITEMS_LIST.append(Item("Karma Coin", TYPES.USABLE, 24, [[ZONEID.CHI, 1, [0x1a8e, 0x1dfe]], [ZONEID.CAT, 14, [0x3346, 0x3c3a]], [ZONEID.CAT, 13, [0x335a, 0x3c30]], [ZONEID.RNZ1, 1, [0x2aea, 0x3316]], [ZONEID.RCAT, 4, [0x2d2a, 0x389e]]\
                                                   , [ZONEID.RCAT, 5, [0x2d3e, 0x38a8]]]))
ITEMS_LIST.append(Item("Magic Missile", TYPES.USABLE, 25, [[ZONEID.DAI, 5, [0x28f6, 0x32d8]], [ZONEID.NZ1, 0, [0x2a52, 0x34ea]], [ZONEID.RNZ1, 0, [0x2ad6, 0x32ee]], [ZONEID.RCAT, 0, [0x285c, 0x338a]], [ZONEID.RDAI, 15, [0x2562, 0x2ece]]]))
ITEMS_LIST.append(Item("Red Rust", TYPES.WEAPON2, 26))
ITEMS_LIST.append(Item("Takemitsu", TYPES.WEAPON2, 27, [[ZONEID.LIB, 5, [0x377c, 0x3f10]]]))
ITEMS_LIST.append(Item("Shotel", TYPES.WEAPON1, 28, [[ZONEID.RNO1, 1, [0x215c, 0x2852]]]))
ITEMS_LIST.append(Item("Orange", TYPES.USABLE, 29))
ITEMS_LIST.append(Item("Apple", TYPES.USABLE, 30))
ITEMS_LIST.append(Item("Banana", TYPES.USABLE, 31))
ITEMS_LIST.append(Item("Grapes", TYPES.USABLE, 32))
ITEMS_LIST.append(Item("Strawberry", TYPES.USABLE, 33))
ITEMS_LIST.append(Item("Pineapple", TYPES.USABLE, 34))
ITEMS_LIST.append(Item("Peanuts", TYPES.USABLE, 35, [[ZONEID.CHI, 9, [0x1a48, 0x1dc2]], [ZONEID.CHI, 10, [0x1a52, 0x1da4]], [ZONEID.CHI, 11, [0x1a5c, 0x1dae]], [ZONEID.CHI, 12, [0x1a66, 0x1db8]]]))
ITEMS_LIST.append(Item("Toadstool", TYPES.USABLE, 36, [[ZONEID.NO4, 26, [0x3c58, 0x4b3c]], [ZONEID.NO4, 33, [0x36d6, 0x4876]], [ZONEID.RNO4, 2, [0x31aa, 0x4078]]]))
ITEMS_LIST.append(Item("Shiitake", TYPES.USABLE, 37, [[ZONEID.NO4, 12, [0x3550, 0x461e]], [ZONEID.NO4, 35, [0x36ae, 0x4736]], [ZONEID.NO4, 27, [0x3bea, 0x4b0a]], [ZONEID.NO4, 32, [0x36cc, 0x47ea]], [ZONEID.CHI, 7, [0x1c46, 0x1fc0]], \
                                                 [ZONEID.CHI, 6, [0x1c6e, 0x1fca]], [ZONEID.RNO4, 1, [0x3bfa, 0x4b68]], [ZONEID.RNO4, 10, [0x31d2, 0x42a8]], [ZONEID.RNO4, 9, [0x3236, 0x42b2]], [ZONEID.RNO4, 3, [0x31b4, 0x4082]], \
                                                    [ZONEID.RCHI, 6, [0x1bd6, 0x204a]], [ZONEID.RCHI, 7, [0x1c30, 0x207c]]]))
ITEMS_LIST.append(Item("Cheesecake", TYPES.USABLE, 38))
ITEMS_LIST.append(Item("Shortcake", TYPES.USABLE, 39))
ITEMS_LIST.append(Item("Tart", TYPES.USABLE, 40))
ITEMS_LIST.append(Item("Parfait", TYPES.USABLE, 41))
ITEMS_LIST.append(Item("Pudding", TYPES.USABLE, 42))
ITEMS_LIST.append(Item("Ice cream", TYPES.USABLE, 43))
ITEMS_LIST.append(Item("Frankfurter", TYPES.USABLE, 44, [[ZONEID.TOP, 7, [0x241c, 0x29dc]], [ZONEID.LIB, 7, [0x379a, 0x3f24]]]))
ITEMS_LIST.append(Item("Hamburger", TYPES.USABLE, 45))
ITEMS_LIST.append(Item("Pizza", TYPES.USABLE, 46))
ITEMS_LIST.append(Item("Cheese", TYPES.USABLE, 47, [[ZONEID.NO2, 6, [0x34ac, 0x3be8]]]))
ITEMS_LIST.append(Item("Ham and eggs", TYPES.USABLE, 48))
ITEMS_LIST.append(Item("Omelette", TYPES.USABLE, 49))
ITEMS_LIST.append(Item("Morning set", TYPES.USABLE, 50))
ITEMS_LIST.append(Item("Lunch A", TYPES.USABLE, 51))
ITEMS_LIST.append(Item("Lunch B", TYPES.USABLE, 52))
ITEMS_LIST.append(Item("Curry rice", TYPES.USABLE, 53))
ITEMS_LIST.append(Item("Gyros plate", TYPES.USABLE, 54))
ITEMS_LIST.append(Item("Spaghetti", TYPES.USABLE, 55))
ITEMS_LIST.append(Item("Grape juice", TYPES.USABLE, 56, [[ZONEID.DAI, -1, [0x046c2658]]]))
ITEMS_LIST.append(Item("Barley tea", TYPES.USABLE, 57, [[ZONEID.CHI, 8, [0x1a3e, 0x1dd6]]]))
ITEMS_LIST.append(Item("Green tea", TYPES.USABLE, 58, [[ZONEID.ARE, 6, [0x3482, 0x3b0a]], [ZONEID.RCHI, 3, [0x1938, 0x1d98, 0x1a8c, 0x1ece]]]))
ITEMS_LIST.append(Item("Natou", TYPES.USABLE, 59))
ITEMS_LIST.append(Item("Ramen", TYPES.USABLE, 60))
ITEMS_LIST.append(Item("Miso soup", TYPES.USABLE, 61))
ITEMS_LIST.append(Item("Sushi", TYPES.USABLE, 62))
ITEMS_LIST.append(Item("Pork bun", TYPES.USABLE, 63, [[ZONEID.CAT, 15, [0x3404, 0x3ce4]]]))
ITEMS_LIST.append(Item("Red bean bun", TYPES.USABLE, 64, [[ZONEID.RCAT, 6, [0x2dde, 0x3902]]]))
ITEMS_LIST.append(Item("Chinese bun", TYPES.USABLE, 65))
ITEMS_LIST.append(Item("Dim Sum set", TYPES.USABLE, 66, [[ZONEID.RNO1, -1, [0x0507d08c]]]))
ITEMS_LIST.append(Item("Pot roast", TYPES.USABLE, 67, [[ZONEID.NO3, -1, [0x04ba9774, 0x05431554]], [ZONEID.NO1, -1, [0x04a197d8]], [ZONEID.NZ1, -1, [0x0557379c]], [ZONEID.RNZ1, -1, [0x059bc34c]], [ZONEID.RNO3, -1, [0x051e6e4c]], \
                                                  [ZONEID.TOP, 6, [0x2412, 0x29d2]], [ZONEID.NO4, 21, [0x41da, 0x5262]], [ZONEID.BO3, 21, [0x1d5c, 0x1f20]], [ZONEID.RNO4, 22, [0x39c0, 0x4910]]]))
ITEMS_LIST.append(Item("Sirloin", TYPES.USABLE, 68, [[ZONEID.TOP, 4, [0x23fe, 0x29be]]]))
ITEMS_LIST.append(Item("Turkey", TYPES.USABLE, 69, [[ZONEID.NO3, -1, [0x04baa2b0, 0x05431f60]], [ZONEID.TOP, 1, [0x2124, 0x282e]], [ZONEID.TOP, 5, [0x2408, 0x29c8]], [ZONEID.CHI, -1, [0x045e9602]]]))
ITEMS_LIST.append(Item("Meal ticket", TYPES.USABLE, 70, [[ZONEID.NO4, 14, [0x3640, 0x46b4]], [ZONEID.NO4, 15, [0x364a, 0x46be]], [ZONEID.NO4, 16, [0x362c, 0x46c8]], [ZONEID.NO4, 17, [0x3636, 0x46d2]], [ZONEID.RNO0, 9, [0x407c, 0x510e]], \
                                                    [ZONEID.RNO4, 16, [0x3056, 0x3fce]], [ZONEID.RNO4, 17, [0x3060, 0x3fba]], [ZONEID.RNO4, 18, [0x3074, 0x3fc4]], [ZONEID.RNO4, 19, [0x307e, 0x3fa6]], [ZONEID.RNO4, 20, [0x306a, 0x3fb0]]]))
ITEMS_LIST.append(Item("Neutron bomb", TYPES.USABLE, 71, [[ZONEID.RLIB, 6, [0x1ccc, 0x226c]], [ZONEID.ST0, -1, [0x119d00]]]))
ITEMS_LIST.append(Item("Power of Sire", TYPES.USABLE, 72, [[ZONEID.CHI, 0, [0x1a34, 0x1dcc]], [ZONEID.RCHI, 0, [0x1910, 0x1d7a]], [ZONEID.RCHI, 4, [0x1942, 0x1da2]]]))
ITEMS_LIST.append(Item("Pentagram", TYPES.USABLE, 73, [[ZONEID.NZ1, 1, [0x2a0c, 0x34f4]], [ZONEID.NO4, 30, [0x3f28, 0x4fb0]]]))
ITEMS_LIST.append(Item("Bat Pentagram", TYPES.USABLE, 74, [[ZONEID.RNO4, 5, [0x3754, 0x46a4]]]))
ITEMS_LIST.append(Item("Shuriken", TYPES.USABLE, 75, [[ZONEID.DAI, 6, [0x291e, 0x32b0]], [ZONEID.RDAI, 6, [0x1f9a, 0x27f8]], [ZONEID.RNO2, 10, [0x29ac, 0x3190]], [ZONEID.NZ1, -1, [0x055737a0]], [ZONEID.RNZ1, -1, [0x059bc350]]]))
ITEMS_LIST.append(Item("Cross shuriken", TYPES.USABLE, 76, [[ZONEID.CAT, 12, [0x333c, 0x3bea]], [ZONEID.CAT, 11, [0x3350, 0x3be0]]]))
ITEMS_LIST.append(Item("Buffalo star", TYPES.USABLE, 77, [[ZONEID.RCAT, 1, [0x2866, 0x3380]], [ZONEID.RARE, 2, [0x2400, 0x29aa]]]))
ITEMS_LIST.append(Item("Flame star", TYPES.USABLE, 78))
ITEMS_LIST.append(Item("TNT", TYPES.USABLE, 79, [[ZONEID.DAI, 7, [0x2946, 0x3292]], [ZONEID.RDAI, 7, [0x1f4a, 0x283e]], [ZONEID.NZ1, -1, [0x055737a8]], [ZONEID.RNZ1, -1, [0x059bc358]]]))
ITEMS_LIST.append(Item("Bwaka knife", TYPES.USABLE, 80, [[ZONEID.RDAI, 14, [0x254e, 0x2ed8]], [ZONEID.NZ1, -1, [0x055737a4]], [ZONEID.RNZ1, -1, [0x059bc354]]]))
ITEMS_LIST.append(Item("Boomerang", TYPES.USABLE, 81, [[ZONEID.DAI, 8, [0x2964, 0x326a]], [ZONEID.RDAI, 8, [0x1efa, 0x288e]]]))
ITEMS_LIST.append(Item("Javelin", TYPES.USABLE, 82, [[ZONEID.RDAI, 9, [0x1ed2, 0x28c0]]]))
ITEMS_LIST.append(Item("Tyrfing", TYPES.WEAPON1, 83, [[ZONEID.TOP, 3, [0x23b8, 0x2964]]]))
ITEMS_LIST.append(Item("Namakura", TYPES.WEAPON2, 84))
ITEMS_LIST.append(Item("Knuckle duster", TYPES.WEAPON1, 85, [[ZONEID.NO4, 23, [0x3c80, 0x4e66]]]))
ITEMS_LIST.append(Item("Gladius", TYPES.WEAPON1, 86, [[ZONEID.NO1, 4, [0x363e, 0x3e24]]]))
ITEMS_LIST.append(Item("Scimitar", TYPES.WEAPON1, 87, [[ZONEID.NO4, 19, [0x423e, 0x52bc]], [ZONEID.BO3, 19, [0x1e24, 0x1fde]]]))
ITEMS_LIST.append(Item("Cutlass", TYPES.WEAPON1, 88, [[ZONEID.DAI, 14, [0x3026, 0x3972]]]))
ITEMS_LIST.append(Item("Saber", TYPES.WEAPON1, 89))
ITEMS_LIST.append(Item("Falchion", TYPES.WEAPON1, 90, [[ZONEID.TOP, 12, [0x2476, 0x2a22]]]))
ITEMS_LIST.append(Item("Broadsword", TYPES.WEAPON1, 91, [[ZONEID.NO2, 4, [0x34c0, 0x3bd4]]]))
ITEMS_LIST.append(Item("Bekatowa", TYPES.WEAPON1, 92, [[ZONEID.NZ1, 7, [0x29e4, 0x33c8]]]))
ITEMS_LIST.append(Item("Damascus sword", TYPES.WEAPON1, 93))
ITEMS_LIST.append(Item("Hunter sword", TYPES.WEAPON1, 94))
ITEMS_LIST.append(Item("Estoc", TYPES.WEAPON2, 95, [[ZONEID.NO2, 10, [0x34e8, 0x3c06]]]))
ITEMS_LIST.append(Item("Bastard sword", TYPES.WEAPON1, 96, [[ZONEID.RTOP, 4, [0x1d66, 0x2162]]]))
ITEMS_LIST.append(Item("Jewel knuckles", TYPES.WEAPON1, 97, [[ZONEID.NO1, 0, [0x36d4, 0x3eba]]]))
ITEMS_LIST.append(Item("Claymore", TYPES.WEAPON2, 98, [[ZONEID.NO4, 13, [0x3406, 0x4448]]]))
ITEMS_LIST.append(Item("Talwar", TYPES.WEAPON1, 99, [[ZONEID.RDAI, 13, [0x2472, 0x2e06]]]))
ITEMS_LIST.append(Item("Katana", TYPES.WEAPON2, 100, [[ZONEID.RNZ0, 5, [0x2322, 0x2be4]]]))
ITEMS_LIST.append(Item("Flamberge", TYPES.WEAPON2, 101))
ITEMS_LIST.append(Item("Iron Fist", TYPES.WEAPON1, 102))
ITEMS_LIST.append(Item("Zwei hander", TYPES.WEAPON2, 103))
ITEMS_LIST.append(Item("Sword of Hador", TYPES.WEAPON1, 104, [[ZONEID.RNO2, 1, [0x29fc, 0x31e0]]]))
ITEMS_LIST.append(Item("Luminus", TYPES.WEAPON1, 105, [[ZONEID.RNZ1, 3, [0x2afe, 0x335c]]]))
ITEMS_LIST.append(Item("Harper", TYPES.WEAPON1, 106))
ITEMS_LIST.append(Item("Obsidian sword", TYPES.WEAPON2, 107))
ITEMS_LIST.append(Item("Gram", TYPES.WEAPON1, 108, [[ZONEID.RARE, 3, [0x2428, 0x29c8]]]))
ITEMS_LIST.append(Item("Jewel sword", TYPES.WEAPON1, 109, [[ZONEID.NP3, 9, [0x3e56, 0x459c]]]))
ITEMS_LIST.append(Item("Mormegil", TYPES.WEAPON1, 110, [[ZONEID.CAT, 3, [0x2c02, 0x34e2]]]))
ITEMS_LIST.append(Item("Firebrand", TYPES.WEAPON1, 111))
ITEMS_LIST.append(Item("Thunderbrand", TYPES.WEAPON1, 112))
ITEMS_LIST.append(Item("Icebrand", TYPES.WEAPON1, 113, [[ZONEID.CAT, 1, [0x2c3e, 0x351e]]]))
ITEMS_LIST.append(Item("Stone sword", TYPES.WEAPON1, 114))
ITEMS_LIST.append(Item("Holy sword", TYPES.WEAPON1, 115, [[ZONEID.ARE, 7, [0x34be, 0x3b46]]]))
ITEMS_LIST.append(Item("Terminus Est", TYPES.WEAPON1, 116))
ITEMS_LIST.append(Item("Marsil", TYPES.WEAPON1, 117))
ITEMS_LIST.append(Item("Dark Blade", TYPES.WEAPON1, 118, [[ZONEID.RNO4, 23, [0x309c, 0x3fec]]]))
ITEMS_LIST.append(Item("Heaven sword", TYPES.WEAPON1, 119))
ITEMS_LIST.append(Item("Fist of Tulkas", TYPES.WEAPON1, 120))
ITEMS_LIST.append(Item("Gurthang", TYPES.WEAPON1, 121))
ITEMS_LIST.append(Item("Mourneblade", TYPES.WEAPON1, 122))
ITEMS_LIST.append(Item("Alucard sword", TYPES.WEAPON1, 123, [[ZONEID.RCHI, 2, [0x1cda, 0x213a]]]))
ITEMS_LIST.append(Item("Mablung Sword", TYPES.WEAPON1, 124))
ITEMS_LIST.append(Item("Badelaire", TYPES.WEAPON1, 125, [[ZONEID.RLIB, 7, [0x1b00, 0x20a0]]]))
ITEMS_LIST.append(Item("Sword Familiar", TYPES.WEAPON1, 126))
ITEMS_LIST.append(Item("Great Sword", TYPES.WEAPON2, 127))
ITEMS_LIST.append(Item("Mace", TYPES.WEAPON1, 128))
ITEMS_LIST.append(Item("Morningstar", TYPES.WEAPON1, 129, [[ZONEID.DAI, 1, [0x2982, 0x3242]]]))
ITEMS_LIST.append(Item("Holy rod", TYPES.WEAPON1, 130, [[ZONEID.LIB, 2, [0x35b0, 0x3c5e]]]))
ITEMS_LIST.append(Item("Star flail", TYPES.WEAPON1, 131, [[ZONEID.NZ1, 3, [0x284a, 0x327e]]]))
ITEMS_LIST.append(Item("Moon rod", TYPES.WEAPON1, 132, [[ZONEID.RNZ1, 11, [0x2d06, 0x3578]]]))
ITEMS_LIST.append(Item("Chakram", TYPES.WEAPON1, 133))
ITEMS_LIST.append(Item("Fire boomerang", TYPES.USABLE, 134, [[ZONEID.RNO3, 7, [0x2d28, 0x33fe]], [ZONEID.RDAI, 2, [0x1e78, 0x2924]]]))
ITEMS_LIST.append(Item("Iron ball", TYPES.USABLE, 135, [[ZONEID.NO2, 11, [0x3470, 0x3b98]], [ZONEID.RTOP, 1, [0x1c80, 0x2004]], [ZONEID.RNO0, 10, [0x4568, 0x55be]]]))
ITEMS_LIST.append(Item("Holbein dagger", TYPES.WEAPON1, 136))
ITEMS_LIST.append(Item("Blue knuckles", TYPES.WEAPON1, 137))
ITEMS_LIST.append(Item("Dynamite", TYPES.USABLE, 138))
ITEMS_LIST.append(Item("Osafune katana", TYPES.WEAPON2, 139, [[ZONEID.RNO4, 26, [0x37c2, 0x473a]]]))
ITEMS_LIST.append(Item("Masamune", TYPES.WEAPON2, 140))
ITEMS_LIST.append(Item("Muramasa", TYPES.WEAPON2, 141))
ITEMS_LIST.append(Item("Heart Refresh", TYPES.USABLE, 142, [[ZONEID.RNO0, 11, [0x44fa, 0x555a]], [ZONEID.RNO2, 9, [0x2970, 0x3154]], [ZONEID.ST0, -1, [0x119ca4]]]))
ITEMS_LIST.append(Item("Runesword", TYPES.WEAPON1, 143))
ITEMS_LIST.append(Item("Antivenom", TYPES.USABLE, 144, [[ZONEID.LIB, 9, [0x3588, 0x3c40]], [ZONEID.NO4, 4, [0x3a6e, 0x4ca4]], [ZONEID.RNO0, 2, [0x3abe, 0x4a92]], [ZONEID.RNO3, 1, [0x2fda, 0x36ce]]]))
ITEMS_LIST.append(Item("Uncurse", TYPES.USABLE, 145))
ITEMS_LIST.append(Item("Life apple", TYPES.USABLE, 146, [[ZONEID.NO3, 2, [0x40a2, 0x4824]], [ZONEID.NP3, 2, [0x3e60, 0x4588]], [ZONEID.NO0, 3, [0x296c, 0x37f6]], [ZONEID.RNZ1, 7, [0x2a0e, 0x3276]], [ZONEID.RCHI, 1, [0x191a, 0x1d70]]]))
ITEMS_LIST.append(Item("Hammer", TYPES.USABLE, 147, [[ZONEID.NO0, 12, [0x3134, 0x3fa0]], [ZONEID.NO0, 4, [0x2976, 0x3800]], [ZONEID.RNO1, 2, [0x2170, 0x285c]], [ZONEID.RNO3, 0, [0x2f94, 0x36c4]]]))
ITEMS_LIST.append(Item("Str. potion", TYPES.USABLE, 148, [[ZONEID.NO0, 13, [0x3170, 0x3f14]], [ZONEID.DAI, 11, [0x2e82, 0x36c0]], [ZONEID.RNZ1, 2, [0x2af4, 0x3352]]]))
ITEMS_LIST.append(Item("Luck potion", TYPES.USABLE, 149, [[ZONEID.NO2, 9, [0x3984, 0x4098]], [ZONEID.RNO1, 4, [0x221a, 0x291a]], [ZONEID.RNO2, 4, [0x2948, 0x312c]]]))
ITEMS_LIST.append(Item("Smart potion", TYPES.USABLE, 150, [[ZONEID.RNZ1, 4, [0x2b12, 0x3348]], [ZONEID.RDAI, 11, [0x2288, 0x2d5c]]]))
ITEMS_LIST.append(Item("Attack potion", TYPES.USABLE, 151, [[ZONEID.NO0, 11, [0x372e, 0x45c2]], [ZONEID.RCAT, 12, [0x2b2c, 0x36b4]]]))
ITEMS_LIST.append(Item("Shield potion", TYPES.USABLE, 152, [[ZONEID.NO3, 4, [0x4156, 0x48ba]], [ZONEID.NP3, 4, [0x3f1e, 0x4632]], [ZONEID.RNO1, 5, [0x2350, 0x2a46]], [ZONEID.RCAT, 11, [0x2b36, 0x366e]], [ZONEID.RNO2, 3, [0x293e, 0x3122]]]))
ITEMS_LIST.append(Item("Resist fire", TYPES.USABLE, 153, [[ZONEID.NO2, 8, [0x397a, 0x40a2]], [ZONEID.RTOP, 17, [0x1e06, 0x2248]], [ZONEID.RLIB, 3, [0x1ace, 0x206e]], [ZONEID.RNO0, 8, [0x44b4, 0x5514]], [ZONEID.RCAT, 3, [0x2d48, 0x3858]]]))
ITEMS_LIST.append(Item("Resist thunder", TYPES.USABLE, 154, [[ZONEID.NZ0, 7, [0x2956,0x32c2]], [ZONEID.RTOP, 19, [0x1dfc,0x222a]], [ZONEID.RNO0, 7, [0x44aa, 0x550a]], [ZONEID.RCAT, 2, [0x2d34, 0x384e]]]))
ITEMS_LIST.append(Item("Resist ice", TYPES.USABLE, 155, [[ZONEID.NO4, 20, [0x4216, 0x52c6]], [ZONEID.BO3, 20, [0x1df2, 0x1fe8]], [ZONEID.RTOP, 18, [0x1de8, 0x223e]], [ZONEID.RLIB, 4, [0x1ad8, 0x2078]]]))
ITEMS_LIST.append(Item("Resist stone", TYPES.USABLE, 156, [[ZONEID.TOP, 8, [0x2430, 0x29e6]], [ZONEID.RTOP, 20, [0x1df2, 0x2234]], [ZONEID.RLIB, 5, [0x1ae2, 0x2082]]]))
ITEMS_LIST.append(Item("Resist holy", TYPES.USABLE, 157, [[ZONEID.TOP, 10, [0x2444, 0x29fa]], [ZONEID.RNO0, 6, [0x44dc, 0x553c]]]))
ITEMS_LIST.append(Item("Resist dark", TYPES.USABLE, 158, [[ZONEID.TOP, 9, [0x243a, 0x29f0]], [ZONEID.RNO0, 5, [0x44d2, 0x5532]], [ZONEID.RNZ0, 9, [0x262e, 0x2edc]]]))
ITEMS_LIST.append(Item("Potion", TYPES.USABLE, 159, [[ZONEID.NZ0, 10, [0x2b72, 0x3556]], [ZONEID.DAI, 15, [0x3008, 0x397c]], [ZONEID.LIB, 8, [0x357e, 0x3c36]], [ZONEID.NO0, 5, [0x2980, 0x380a]], [ZONEID.RNO0, 1, [0x3ab4, 0x4a2e]], [ZONEID.RNO4, 8, [0x3362, 0x414a]], \
                                                [ZONEID.ST0, -1, [0x119bb8]]]))
ITEMS_LIST.append(Item("High potion", TYPES.USABLE, 160, [[ZONEID.RTOP, 21, [0x1dde, 0x225c]], [ZONEID.RNO1, 6, [0x242c, 0x2a8c]], [ZONEID.RNO3, 2, [0x302a, 0x3700]], [ZONEID.RNZ0, 6, [0x2804, 0x30e4]], [ZONEID.RNO2, 2, [0x2a06, 0x31ea]]]))
ITEMS_LIST.append(Item("Elixir", TYPES.USABLE, 161, [[ZONEID.NO4, 25, [0x3dd4, 0x4e7a]], [ZONEID.RNO4, 25, [0x3416, 0x43de]], [ZONEID.RCAT, 7, [0x3036, 0x3b64]]]))
ITEMS_LIST.append(Item("Manna prism", TYPES.USABLE, 162, [[ZONEID.NO2, 7, [0x3970, 0x40ac]], [ZONEID.RNO4, 24, [0x342a, 0x42da]], [ZONEID.RNZ0, 4, [0x2598, 0x2dec]], [ZONEID.RDAI, 10, [0x2364,0x2d66]], [ZONEID.RNO2, 5, [0x2952, 0x3136]]]))
ITEMS_LIST.append(Item("Vorpal blade", TYPES.WEAPON1, 163))
ITEMS_LIST.append(Item("Crissaegrim", TYPES.WEAPON1, 164))
ITEMS_LIST.append(Item("Yasutsuna", TYPES.WEAPON2, 165))
ITEMS_LIST.append(Item("Library card", TYPES.USABLE, 166, [[ZONEID.NO0, 10, [0x3742, 0x45b8]], [ZONEID.CAT, 4, [0x3422, 0x3d02]], [ZONEID.ARE, 5, [0x352c, 0x3b78]], [ZONEID.RTOP, 24, [0x1e4c, 0x22a2]], [ZONEID.RLIB, 2, [0x1a56, 0x2000]], \
                                                      [ZONEID.RNO0, 0, [0x373a, 0x4a10]], [ZONEID.RCAT, 8, [0x3040, 0x3b5a]]])) 
ITEMS_LIST.append(Item("Alucart shield", TYPES.SHIELD, 167, [[ZONEID.NO0, 1, [0x3670, 0x44f0]]]))
ITEMS_LIST.append(Item("Alucart sword", TYPES.WEAPON1, 168, [[ZONEID.NO0, 7, [0x36a2, 0x4522]]]))
ITEMS_LIST.append(Item("Cloth tunic", TYPES.ARMOR, 170))
ITEMS_LIST.append(Item("Hide cuirass", TYPES.ARMOR, 171, [[ZONEID.NZ0, 0, [0x2df2, 0x377c]]]))
ITEMS_LIST.append(Item("Bronze cuirass", TYPES.ARMOR, 172, [[ZONEID.LIB, 4, [0x3286, 0x398e]]]))
ITEMS_LIST.append(Item("Iron cuirass", TYPES.ARMOR, 173))
ITEMS_LIST.append(Item("Steel cuirass", TYPES.ARMOR, 174))
ITEMS_LIST.append(Item("Silver plate", TYPES.ARMOR, 175, [[ZONEID.DAI, 10, [0x2da6, 0x36b6]]]))
ITEMS_LIST.append(Item("Gold plate", TYPES.ARMOR, 176, [[ZONEID.NZ1, 4, [0x287c, 0x3288]]]))
ITEMS_LIST.append(Item("Platinum mail", TYPES.ARMOR, 177, [[ZONEID.TOP, 11, [0x244e, 0x29b4]]]))
ITEMS_LIST.append(Item("Diamond plate", TYPES.ARMOR, 178))
ITEMS_LIST.append(Item("Fire mail", TYPES.ARMOR, 179, [[ZONEID.TOP, 2, [0x211a, 0x27a2]]]))
ITEMS_LIST.append(Item("Lightning mail", TYPES.ARMOR, 180, [[ZONEID.RTOP, 23, [0x1e2e, 0x227a]]]))
ITEMS_LIST.append(Item("Ice mail", TYPES.ARMOR, 181, [[ZONEID.NZ1, 9, [0x2a02, 0x33dc]]]))
ITEMS_LIST.append(Item("Mirror cuirass", TYPES.ARMOR, 182, [[ZONEID.NO1, 1, [0x36e8, 0x3ec4]]]))
ITEMS_LIST.append(Item("Spike Breaker", TYPES.ARMOR, 183, [[ZONEID.CAT, 16, [0x342c, 0x3d2a]]]))
ITEMS_LIST.append(Item("Alucard mail", TYPES.ARMOR, 184, [[ZONEID.RNO2, 7, [0x298e, 0x3172]]]))
ITEMS_LIST.append(Item("Dark armor", TYPES.ARMOR, 185))
ITEMS_LIST.append(Item("Healing mail", TYPES.ARMOR, 186, [[ZONEID.NZ1, 6, [0x2d18, 0x372e]]]))
ITEMS_LIST.append(Item("Holy mail", TYPES.ARMOR, 187, [[ZONEID.NO3, 5, [0x3ea4, 0x4630]], [ZONEID.NP3, 5, [0x3c44, 0x4380]]]))
ITEMS_LIST.append(Item("Walk armor", TYPES.ARMOR, 188, [[ZONEID.CAT, 2, [0x2c20, 0x3500]]]))
ITEMS_LIST.append(Item("Brilliant mail", TYPES.ARMOR, 189))
ITEMS_LIST.append(Item("Mojo mail", TYPES.ARMOR, 190))
ITEMS_LIST.append(Item("Fury plate", TYPES.ARMOR, 191, [[ZONEID.RARE, 0, [0x2446, 0x29e6]]]))
ITEMS_LIST.append(Item("Dracula tunic", TYPES.ARMOR, 192, [[ZONEID.LIB, -1, [0x047d9370]]]))
ITEMS_LIST.append(Item("God´s Garb", TYPES.ARMOR, 193))
ITEMS_LIST.append(Item("Axe Lord armor", TYPES.ARMOR, 194, [[ZONEID.LIB, -1, [0x047d9284]]]))
ITEMS_LIST.append(Item("Sunglasses", TYPES.HELMET, 196, [[ZONEID.NZ0, 6, [0x3108, 0x3a60]]]))
ITEMS_LIST.append(Item("Ballroom mask", TYPES.HELMET, 197, [[ZONEID.CAT, 7, [0x2eaa, 0x3762]]]))
ITEMS_LIST.append(Item("Bandanna", TYPES.HELMET, 198, [[ZONEID.NO4, 11, [0x3262, 0x42ea]]]))
ITEMS_LIST.append(Item("Felt hat", TYPES.HELMET, 199))
ITEMS_LIST.append(Item("Velvet hat", TYPES.HELMET, 200))
ITEMS_LIST.append(Item("Goggles", TYPES.HELMET, 201, [[ZONEID.DAI, 9, [0x289c, 0x31f2]]]))
ITEMS_LIST.append(Item("Leather hat", TYPES.HELMET, 202))
ITEMS_LIST.append(Item("Holy glasses", TYPES.HELMET, 203, [[ZONEID.CEN, -1, [0x0456e368]]]))
ITEMS_LIST.append(Item("Steel helm", TYPES.HELMET, 204, [[ZONEID.NZ1, 5, [0x2886, 0x3292]]]))
ITEMS_LIST.append(Item("Stone mask", TYPES.HELMET, 205, [[ZONEID.LIB, 1, [0x3312, 0x39ac]]]))
ITEMS_LIST.append(Item("Circlet", TYPES.HELMET, 206))
ITEMS_LIST.append(Item("Gold circlet", TYPES.HELMET, 207))
ITEMS_LIST.append(Item("Ruby circlet", TYPES.HELMET, 208, [[ZONEID.RCAT, 17, [0x25a0, 0x30c4]]]))
ITEMS_LIST.append(Item("Opal circlet", TYPES.HELMET, 209))
ITEMS_LIST.append(Item("Topaz circlet", TYPES.HELMET, 210, [[ZONEID.LIB, 10, [0x35a6, 0x3c68]]]))
ITEMS_LIST.append(Item("Beryl circlet", TYPES.HELMET, 211, [[ZONEID.RNO3, 6, [0x2daa, 0x3462]]]))
ITEMS_LIST.append(Item("Cat-eye circl.", TYPES.HELMET, 212, [[ZONEID.CAT, 0, [0x2e28, 0x3708]]]))
ITEMS_LIST.append(Item("Coral circlet", TYPES.HELMET, 213))
ITEMS_LIST.append(Item("Dragon helm", TYPES.HELMET, 214, [[ZONEID.RNZ1, 5, [0x2a36, 0x329e]]]))
ITEMS_LIST.append(Item("Silver crown", TYPES.HELMET, 215))
ITEMS_LIST.append(Item("Wizard hat", TYPES.HELMET, 216))
ITEMS_LIST.append(Item("Cloth cape", TYPES.CLOAK, 218, [[ZONEID.NZ0, 2, [0x2f32, 0x388a]]]))
ITEMS_LIST.append(Item("Reverse cloak", TYPES.CLOAK, 219))
ITEMS_LIST.append(Item("Elven cloak", TYPES.CLOAK, 220))
ITEMS_LIST.append(Item("Crystal cloak", TYPES.CLOAK, 221, [[ZONEID.NO4, 2, [0x3352, 0x43da]], [ZONEID.BO3, 2, [0x1e42, 0x2006]]]))
ITEMS_LIST.append(Item("Royal cloak", TYPES.CLOAK, 222, [[ZONEID.RTOP, 11, [0x1d16, 0x21a8]]]))
ITEMS_LIST.append(Item("Blood cloak", TYPES.CLOAK, 223, [[ZONEID.ARE, 3, [0x34a0, 0x3b28]]]))
ITEMS_LIST.append(Item("Joseph's cloak", TYPES.CLOAK, 224))
ITEMS_LIST.append(Item("Twilight cloak", TYPES.CLOAK, 225, [[ZONEID.RDAI, 16, [0x1d7e, 0x26d6]]]))
ITEMS_LIST.append(Item("Moonstone", TYPES.ACCESSORY, 227, [[ZONEID.NO4, 18, [0x3654, 0x46dc]]]))
ITEMS_LIST.append(Item("Sunstone", TYPES.ACCESSORY, 228, [[ZONEID.RNZ1, 8, [0x2a18, 0x326c]]]))
ITEMS_LIST.append(Item("Bloodstone", TYPES.ACCESSORY, 229, [[ZONEID.CAT, 8, [0x2e32, 0x3712]]]))
ITEMS_LIST.append(Item("Staurolite", TYPES.ACCESSORY, 230, [[ZONEID.RLIB, 8, [0x1b82, 0x2122]]]))
ITEMS_LIST.append(Item("Ring of Pales", TYPES.ACCESSORY, 231))
ITEMS_LIST.append(Item("Zircon", TYPES.ACCESSORY, 232, [[ZONEID.DAI, 13, [0x2f5e, 0x38aa]], [ZONEID.RDAI, 4, [0x1fd6, 0x27b2]], [ZONEID.NO1, 6, [0x3774, 0x3f3c]], [ZONEID.NO4, 9, [0x329e, 0x4308]], [ZONEID.RTOP, 2, [0x1b9a, 0x209a]], \
                                                   [ZONEID.RNO4, 14, [0x3b5a, 0x4ac8]], [ZONEID.RNO4, 21, [0x3af6, 0x4a28]], [ZONEID.RNO3, 4, [0x2d96, 0x3476]], [ZONEID.RARE, 1, [0x213a, 0x26e4]]]))
ITEMS_LIST.append(Item("Aquamarine", TYPES.ACCESSORY, 233, [[ZONEID.DAI, 3, [0x28ba, 0x3328]], [ZONEID.RNO2, 6, [0x2664, 0x2e34]], [ZONEID.RARE, 4, [0x2036, 0x2612]]]))
ITEMS_LIST.append(Item("Turquoise", TYPES.ACCESSORY, 234, [[ZONEID.TOP, 0, [0x212e, 0x2842]], [ZONEID.RLIB, 0, [0x1a42, 0x1fec]], [ZONEID.RNZ0, 7, [0x24d0, 0x2d10]]]))
ITEMS_LIST.append(Item("Onyx", TYPES.ACCESSORY, 235, [[ZONEID.LIB, 6, [0x3786, 0x3f1a]], [ZONEID.NO4, 22, [0x3d16, 0x4d6c]], [ZONEID.NO2, 5, [0x34b6, 0x3bde]]]))
ITEMS_LIST.append(Item("Garnet", TYPES.ACCESSORY, 236, [[ZONEID.NO1, 3, [0x37ba, 0x3f6e]], [ZONEID.NO2, 12, [0x3434, 0x3b5c]], [ZONEID.RTOP, 22, [0x1c6c, 0x1ffa]], [ZONEID.RNO1, 7, [0x2544, 0x2c8a]], [ZONEID.RNO4, 4, [0x381c, 0x476c]]]))
ITEMS_LIST.append(Item("Opal", TYPES.ACCESSORY, 237, [[ZONEID.RLIB, 1, [0x1a4c, 0x1ff6]], [ZONEID.RNO4, 11, [0x3bbe, 0x4b0e]], [ZONEID.RNO3, 5, [0x2da0, 0x346c]], [ZONEID.RNO2, 0, [0x29f2, 0x31d6]]]))
ITEMS_LIST.append(Item("Diamond", TYPES.ACCESSORY, 238, [[ZONEID.RNZ1, 6, [0x29dc, 0x3280]], [ZONEID.RNO4, 13, [0x2d72, 0x3cc2]], [ZONEID.RCAT, 14, [0x25be, 0x30e2]], [ZONEID.RDAI, 3, [0x1f36, 0x2852]]]))
ITEMS_LIST.append(Item("Lapis lazuli", TYPES.ACCESSORY, 239))
ITEMS_LIST.append(Item("Ring of Ares", TYPES.ACCESSORY, 240, [[ZONEID.CHI, 4, [0x1d0e, 0x207e]]]))
ITEMS_LIST.append(Item("Gold Ring", TYPES.ACCESSORY, 241, [[ZONEID.NO4, -1, [0x04c324b4]]]))
ITEMS_LIST.append(Item("Silver Ring", TYPES.ACCESSORY, 242, [[ZONEID.DAI, 2, [0x281a, 0x31c0]]]))
ITEMS_LIST.append(Item("Ring of Varda", TYPES.ACCESSORY, 243))
ITEMS_LIST.append(Item("Ring of Arcana", TYPES.ACCESSORY, 244, [[ZONEID.RNZ0, 8, [0x2368, 0x2c48]]]))
ITEMS_LIST.append(Item("Mystic pendant", TYPES.ACCESSORY, 245, [[ZONEID.DAI, 4, [0x28e2, 0x32f6]]]))
ITEMS_LIST.append(Item("Heart broach", TYPES.ACCESSORY, 246))
ITEMS_LIST.append(Item("Necklace of J", TYPES.ACCESSORY, 247, [[ZONEID.RCAT, 13, [0x25dc, 0x3100]]]))
ITEMS_LIST.append(Item("Gauntlet", TYPES.ACCESSORY, 248))
ITEMS_LIST.append(Item("Ankh of Life", TYPES.ACCESSORY, 249, [[ZONEID.DAI, 0, [0x2928, 0x32a6]]]))
ITEMS_LIST.append(Item("Ring of Feanor", TYPES.ACCESSORY, 250))
ITEMS_LIST.append(Item("Medal", TYPES.ACCESSORY, 251))
ITEMS_LIST.append(Item("Talisman", TYPES.ACCESSORY, 252, [[ZONEID.RNO3, 9, [0x2d00, 0x33cc]]]))
ITEMS_LIST.append(Item("Duplicator", TYPES.ACCESSORY, 253))
ITEMS_LIST.append(Item("King's stone", TYPES.ACCESSORY, 254))
ITEMS_LIST.append(Item("Covenant stone", TYPES.ACCESSORY, 255))
ITEMS_LIST.append(Item("Nauglamir", TYPES.ACCESSORY, 256))
ITEMS_LIST.append(Item("Secret boots", TYPES.ACCESSORY, 257, [[ZONEID.NO4, 31, [0x37da, 0x47e0]]]))
ITEMS_LIST.append(Item("Alucart mail", TYPES.ARMOR, 258, [[ZONEID.NO0, 6, [0x3698, 0x4518]]]))

ITEMS_LIST.append(Item("Heart Vessel", TYPES.POWERUP, 12, [[ZONEID.NO2, 1, [0x3718, 0x3e7c]], [ZONEID.NO3, 0, [0x3e68, 0x45f4]], [ZONEID.NP3, 0, [0x3c08, 0x4344]], [ZONEID.NO3, 7, [0x4066, 0x47f2]], [ZONEID.NP3, 7, [0x3e1a, 0x4556]], [ZONEID.NZ0, 1, [0x2eec, 0x3844]], \
                                                      [ZONEID.TOP, 15, [0x25f2, 0x2b8a]], [ZONEID.TOP, 16, [0x25de, 0x2b9e]], [ZONEID.TOP, 18, [0x2250, 0x2748]], [ZONEID.NZ1, 11, [0x2458, 0x2e64]], [ZONEID.NO1, 2, [0x3b34, 0x4220]], \
                                                        [ZONEID.NO0, 2, [0x367a, 0x44fa]], [ZONEID.NO0, 9, [0x36ca, 0x454a]], [ZONEID.NO4, 0, [0x3316, 0x439e, 0x380c, 0x4ace]], [ZONEID.NO4, 29, [0x4176, 0x5208]], [ZONEID.CAT, 6, [0x2ea0, 0x3730]], \
                                                            [ZONEID.CAT, 10, [0x31a2, 0x3a82]], [ZONEID.ARE, 0, [0x3162, 0x3768]], [ZONEID.RTOP, 6, [0x1d52, 0x2176]], [ZONEID.RTOP, 8, [0x1d34, 0x218a]], [ZONEID.RTOP, 10, [0x1d20, 0x219e]], \
                                                                [ZONEID.RNZ1, 10, [0x25e0, 0x2e2a]], [ZONEID.RNO1, 0, [0x2058, 0x26fe]], [ZONEID.RNO0, 4, [0x3bb8, 0x4c18]], [ZONEID.RNO4, 7, [0x31dc, 0x4154]], [ZONEID.RNO4, 15, [0x2e12, 0x3dc6]], \
                                                                    [ZONEID.RCAT, 10, [0x2974, 0x348e]], [ZONEID.RCAT, 15, [0x2816, 0x333a]], [ZONEID.RNO3, 3, [0x2e5e, 0x3566]], [ZONEID.RNZ0, 1, [0x26b0, 0x2f7c]], [ZONEID.RDAI, 5, [0x1fae, 0x27e4]], \
                                                                        [ZONEID.RDAI, 17, [0x25a8, 0x2f00]], [ZONEID.RARE, 5, [0x219e, 0x27ac]], [ZONEID.RARE, 7, [0x21b2, 0x27c0]], [ZONEID.RNO2, 11, [0x2aa6, 0x329e]]]))
ITEMS_LIST.append(Item("Life Vessel", TYPES.POWERUP, 23, [[ZONEID.NO3, 1, [0x3e86, 0x4612]], [ZONEID.NP3, 1, [0x3c26, 0x4362]], [ZONEID.NO3, 6, [0x4228, 0x49b4]], [ZONEID.NP3, 6, [0x400e, 0x474a]], [ZONEID.NO3, 8, [0x41ec, 0x491e]], [ZONEID.NP3, 8, [0x3fd2, 0x4696]], \
                                      [ZONEID.NZ0, 3, [0x2a28, 0x338a]], [ZONEID.DAI, 12, [0x2d9c, 0x36ca]], [ZONEID.TOP, 13, [0x25d4, 0x2b80]], [ZONEID.TOP, 14, [0x25e8, 0x2b94]], [ZONEID.NZ1, 10, [0x243a, 0x2e5a]], [ZONEID.NO1, 5, [0x3bc0, 0x4450]], \
                                      [ZONEID.NO0, 0, [0x3652, 0x44d2]], [ZONEID.NO0, 8, [0x36c0, 0x4540]], [ZONEID.NO4, 1, [0x3334, 0x43bc]], [ZONEID.NO4, 28, [0x4130, 0x51fe]], [ZONEID.NO4, 6, [0x3f6e, 0x5000]], [ZONEID.NO4, 5, [0x3a64, 0x4cea]], \
                                        [ZONEID.NO4, 24, [0x3cee, 0x4e70]], [ZONEID.CAT, 9, [0x3198, 0x3a78]], [ZONEID.RTOP, 9, [0x1d2a, 0x2194]], [ZONEID.RTOP, 7, [0x1d48, 0x2180]], [ZONEID.RTOP, 5, [0x1d5c, 0x216c]], [ZONEID.RNZ1, 9, [0x25c2, 0x2e34]], \
                                            [ZONEID.RNO1, 3, [0x21de, 0x28d4]], [ZONEID.RNO0, 3, [0x3c1c, 0x4c22]], [ZONEID.RNO4, 12, [0x3b96, 0x4af0]], [ZONEID.RNO4, 6, [0x336c, 0x4122]], [ZONEID.RCAT, 16, [0x2820, 0x3344]], [ZONEID.RCAT, 9, [0x296a, 0x3498]], \
                                                [ZONEID.RNO3, 8, [0x2ce2, 0x33ae]], [ZONEID.RNZ0, 2, [0x26f6, 0x2fc2]], [ZONEID.RDAI, 12, [0x23be, 0x2d52]], [ZONEID.RNO2, 8, [0x2b78, 0x33c0]], [ZONEID.RARE, 6, [0x21a8, 0x27b6]]]))


RELICS_LIST.append(Relic("Soul of Bat", 0, [[ZONEID.LIB, [0x3826, 0x3f06]]]))
RELICS_LIST.append(Relic("Fire of Bat", 1, [[ZONEID.NZ1, [0x28ae, 0x32ba]]], asY=0x00c9))
RELICS_LIST.append(Relic("Echo of Bat", 2, [[ZONEID.NO2, [0x35f6, 0x3d1e]]], asY=0x009d))
RELICS_LIST.append(Relic("Force of Echo", 3, [[ZONEID.RNO4, [0x3718, 0x4686]]], asY=0x00b9))
RELICS_LIST.append(Relic("Soul of Wolf", 4, [[ZONEID.NO1, [0x3c2e, 0x4356]]], asY=0x0331))
RELICS_LIST.append(Relic("Power of Wolf", 5, [[ZONEID.NO3, [0x41e2, 0x4914]], [ZONEID.NP3, [0x3fbe, 0x468c]]], asY=0x00c8))
RELICS_LIST.append(Relic("Skill of Wolf", 6, [[ZONEID.NZ0, [0x3054, 0x3998]]], asX=0x007e, asY=0x00b9))
RELICS_LIST.append(Relic("Form of Mist", 7, [[ZONEID.ARE, [0x304a, 0x36c8]]], asY=0x0099))
RELICS_LIST.append(Relic("Power of Mist", 8, [[ZONEID.TOP, [0x2138, 0x27ac]]], asY=0x04c8))
RELICS_LIST.append(Relic("Gas Cloud", 9, [[ZONEID.RCAT, [0x2596, 0x30ba]]], asX=0x0016, asY=0x00b1))
RELICS_LIST.append(Relic("Cube of Zoe", 10, [[ZONEID.NO3, [0x411a, 0x48a6]], [ZONEID.NP3, [0x3ece, 0x460a]]], asY=0x007b))
RELICS_LIST.append(Relic("Spirit Orb", 11, [[ZONEID.NO0, [0x309e, 0x3ff0]]], asX=0x0043))
RELICS_LIST.append(Relic("Gravity Boots", 12, [[ZONEID.NO0, [0x298a, 0x37ec]]], asY=0x00b9))
RELICS_LIST.append(Relic("Leap Stone", 13, [[ZONEID.TOP, [0x2142, 0x286a]]], asY=0x0729))
RELICS_LIST.append(Relic("Holy Symbol", 14, [[ZONEID.NO4, [0x3ea6, 0x4f38]]], asY=0x00b9))
RELICS_LIST.append(Relic("Faerie Scroll", 15, [[ZONEID.LIB, [0x3510, 0x3a92]]], asY=0x00b9))
RELICS_LIST.append(Relic("Jewel of Open", 16))
RELICS_LIST.append(Relic("Merman Statue", 17, [[ZONEID.NO4, [0x4004, 0x50aa]]], asY=0x00b9))
RELICS_LIST.append(Relic("Bat Card", 18, [[ZONEID.NZ0, [0x2a8c, 0x33d0, 0x2ad2, 0x343e]]], asX=0x007e, asY=0x00b9)) # nao pode ser trocado por item/ mesa na main ram 182a8c item 180fa0
RELICS_LIST.append(Relic("Ghost Card", 19, [[ZONEID.TOP, [0x25fc, 0x2ba8]]], asY=0x02a8))
RELICS_LIST.append(Relic("Faerie Card", 20, [[ZONEID.LIB, [0x3574, 0x3c2c]]], asY=0x00b9))
RELICS_LIST.append(Relic("Demon Card", 21, [[ZONEID.CHI, [0x1ade, 0x1e62]]], asY=0x00b8))
RELICS_LIST.append(Relic("Sword Card", 22, [[ZONEID.NO2, [0x3416, 0x3b3e]]], asY=0x009c))
RELICS_LIST.append(Relic("Sprite Card", 23))
RELICS_LIST.append(Relic("Nosedevil Card", 24))
RELICS_LIST.append(Relic("Heart of Vlad", 25, [[ZONEID.RDAI, [0x1dc4, 0x2730]]]))
RELICS_LIST.append(Item("Tooth of Vlad",  26, [[ZONEID.RNO1, 0, [0x2332, 0x2a1e]]]))
RELICS_LIST.append(Item("Rib of Vlad", 27, [[ZONEID.RNO2, 0, [0x29d4, 0x31b8]]]))
RELICS_LIST.append(Item("Ring of Vlad", 28, [[ZONEID.RNZ1, 0, [0x2dce, 0x3640]]]))
RELICS_LIST.append(Item("Eye of Vlad", 29, [[ZONEID.RCHI, 0, [0x18f2, 0x1d52]]]))

#Boss Rewards
# -2 can be an item
# -3 only a relic

#Olrox BO0
ITEMS_LIST.append(Item("BO0 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.NO2, 0, [0x05fac75c]]]))
#Legion BO1
ITEMS_LIST.append(Item("BO1 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.CAT, 1, [0x0606f9e0]]]))
#Werewolf & Minotaur B02
ITEMS_LIST.append(Item("B02 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.ARE, 2, [0x060fe614]]]))
#Scylla B03
ITEMS_LIST.append(Item("B03 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.NO4, 3, [0x061a80a8]]]))
#Doppleganger10 B04
ITEMS_LIST.append(Item("BO4 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.NO1, 4, [0x0624b968]]]))
#Hippogryph B05
ITEMS_LIST.append(Item("BO5 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.DAI, 6, [0x06306a90]]]))
#Cerberus B07
ITEMS_LIST.append(Item("B07 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.CHI, 5, [0x066b4998]]]))
#Gaibon/Slogra B08 
ITEMS_LIST.append(Item("BO8 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.NZ0, 5, [0x054b3ac8]]]))
#Lesser Demon B09
ITEMS_LIST.append(Item("BO9 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.LIB, 7, [0x047a53c4]]]))
#Karasuman BO10
ITEMS_LIST.append(Item("BO10 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.NZ1, 7, [0x05574d60]]]))
#Trio RBO0
ITEMS_LIST.append(Item("RBO0 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.RARE, 2, [0x06472310]]]))
#Beezlebub RBO1
ITEMS_LIST.append(Item("RBO1 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.RNZ0, 5, [0x065921c8]]]))
#Death RBO2
ITEMS_LIST.append(Item("RBO2 Life Vessel", TYPES.BREWARD, -3, [[ZONEID.RCHI, 21, [0x06622610]]]))
#Medusa RBO3
ITEMS_LIST.append(Item("RBO3 Life Vessel", TYPES.BREWARD, -3, [[ZONEID.RDAI, 17, [0x067437b0]]]))
#Creature RBO4
ITEMS_LIST.append(Item("RBO4 Life Vessel", TYPES.BREWARD, -3, [[ZONEID.NZ1, 18, [0x067d160c]]]))
#Doppleganger40 RBO5
ITEMS_LIST.append(Item("RBO5 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.RNO4, 4, [0x06866130]]]))
#Akmodan II RBO7
ITEMS_LIST.append(Item("RBO7 Life Vessel", TYPES.BREWARD, -3, [[ZONEID.RNO2, 19, [0x069d2af8]]]))
#Galamoth RBO8
ITEMS_LIST.append(Item("RBO8 Life Vessel", TYPES.BREWARD, -2, [[ZONEID.RCAT, 5, [0x06a61adc]]]))
#Darkwing Bat RBO9
ITEMS_LIST.append(Item("RBO9 Life Vessel", TYPES.BREWARD, -3, [[ZONEID.NZ1, 20, [0x059bdb08]]]))

def get_nameid(num_id, heart = False):
    for i in ITEMS_LIST:
        if i.id == num_id:
            if heart and (i.type == TYPES.HEART or i.type == TYPES.GOLD or i.type == TYPES.POWERUP):
                return (i.name, i.id)
            else:
                return (i.name, i.id + TILEIDOFFSET)
            
    return("Empty hand", 0)