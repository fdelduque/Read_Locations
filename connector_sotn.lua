-- zone start 2 byte, zone loot flag, id, name, items
local locations = {
0x189c, 0x000000, "STO", "Final Stage: Bloodlines", {},
0x8704, 0x03bf06, "ARE", "Colosseum", {"Heart Vessel", "Shield rod", "EMPTY", "Blood cloak", "Knight shield", "Library card", "Green tea", "Holy sword"},
0xb6d4, 0x03befc, "CAT", "Catacombs", {"Cat-eye circl.", "Icebrand", "Walk armor", "Mormegil", "Library card", "EMPTY", "Heart Vessel BR Mask", "Ballroom mask", "Bloodstone", "Life Vessel", "Heart Vessel", "Cross shuriken",
					"Cross shuriken", "Karma Coin", "Karma Coin", "EMPTY", "Spike Breaker", "Monster vial 3", "Monster vial 3", "Monster vial 3", "Monster vial 3"},
0x0e7C, 0x03bec4, "CEN", "Center Cube", {"Holy Glasses"}, -- 0x03bec4 probably CG seen
0xdea4, 0x03bf02, "CHI", "Abandoned Mine", {"Power of Sire", "Karma Coin", "EMPTY", "EMPTY", "Ring of Ares", "Combat knife", "Shiitake", "Shiitake", "Barley tea", "Peanuts", "Peanuts", "Peanuts", "Peanuts"},
0x5fb8, 0x03beff, "DAI", "Royal Chapel", {"Ankh of Life", "Morningstar", "Silver Ring", "Aquamarine", "Mystic pendant", "Magic Missile", "Shuriken", "TNT", "Boomerang", "Goggles", "Silver plate", "Str. potion",
					"Life Vessel", "Zircon", "Cutlass", "Potion"},
0x6fc0, 0x000000, "DRE", "Nightmare", {},
0xf160, 0x03befa, "LIB", "Long Library", {"EMPTY", "Stone Mask", "Holy Rod", "EMPTY", "Bronze cuirass", "Takemitsu", "Onyx", "Frankfurter", "Potion", "Antivenom", "Topaz Circlet"},
0x37B8, 0x03beec, "NO0", "Marble Galley", {"Life Vessel left", "Alucart Shield", "Heart Vessel right", "Life apple middle", "Hammer middle", "Potion middle",
				"Alucart Mail", "Alucart Sword", "Life Vessel inside", "Heart Vessel inside", "Library Card jewel", "Attack Potion jewel", "Hammer spirit", "Str. Potion spirit"},
0x1a20, 0x03beee, "NO1", "Outer Wall", {"Jewel Knuckles", "Mirror Cuirass", "Heart Vessel by elevator", "Garnet", "Gladius", "Life Vessel bellow elevator", "Zircon"},
0x8744, 0x03bef0, "NO2", "Olrox's Quarters", {"EMPTY", "Heart Vessel", "EMPTY", "EMPTY", "Broadsword", "Onyx", "Cheese", "Manna prism", "Resist fire", "Luck potion", "Estoc", "Iron ball", "Garnet"},
0x187c, 0x03bef2, "NO3", "Castle Entrance", {"Heart Vessel death", "Life Vessel potion", "Life Apple hidden", "EMPTY", "Shield Potion", "Holy Mail", "Life Vessel UC", "Heart Vessel teleport",
				"Life Vessel entry"},
0x90ec, 0x03bef2, "NP3", "Castle Entrance after AL", {"Heart Vessel death", "Life Vessel potion", "Life Apple hidden", "EMPTY", "Shield Potion", "Holy Mail", "Life Vessel UC", "Heart Vessel teleport",
				"Life Vessel entry", "Jewel Sword hidden"},
0xa620, 0x03bef4, "NO4", "Underground Caverns", {"Heart Vessel 0", "Life Vessel 1", "Crystal cloak", "EMPTY", "Antivenom", "Life Vessel 5", "Life Vessel 6", "Herald Shield", "EMPTY", "Zircon", "EMPTY", "Bandanna",
					"Shiitake", "Claymore", "Meal ticket", "Meal ticket", "Meal ticket", "Meal ticket", "Moonstone", "Scimitar", "Resist ice", "Pot roast", "Onyx", "Knuckle duster", "Life Vessel 24", "Elixir",
					"Toadstool", "Shiitake", "Life Vessel 28", "Heart Vessel 29", "Pentagram", "Secret boots", "Shiitake", "Toadstool", "EMPTY", "Shiitake", "Nunchaku"},
0x9504, 0x03bf0b, "NZ0", "Alchemy Laboratory", {"Hide Cuirass", "Heart Vessel", "Cloth Cape", "Life Vessel", "EMPTY", "EMPTY", "Sunglasses", "Resist Thunder", "Leather Shield", "Basilard", "Potion"},
0xc710, 0x03bf0d, "NZ1", "Clock Tower", {"Magic Missele", "Pentagram", "EMPTY", "Star Flail", "Gold Plate", "Steel Helm", "Healing Mail", "Bekatowa", "Shaman Shield", "Ice Mail", "Life Vessel", "Heart Vessel"},
0xd660, 0x03bf08, "TOP", "Castle Keep", {"Turquoise", "Turkey wall", "Fire mail wall", "Tyrfing", "Sirloin", "Turkey", "Pot Roast", "Frankfurter", "Resist stone", "Resist dark", "Resist holy", "Platinum mail", "Falchion",
					"Life Vessel", "Life Vessel", "Heart Vessel", "Heart Vessel", "EMPTY", "Heart Vessel Richter"},
0x8218, 0x000000, "WRP", "Warp Rooms", {},
0x6b70, 0x03bf3b, "RARE", "Reverse Colosseum", {"Fury plate", "Zircon", "Buffalo star", "Gram", "Aquamarine", "Heart Vessel", "Life Vessel", "Heart Vessel"},
0x3f80, 0x03bf2b, "RCAT", "Floating Catacombs", {"Magic Missile", "Buffalo star wall", "Resist thunder", "Resist fire", "Karma Coin", "Karma Coin", "Red bean bun", "Elixir", "Library card", "Life Vessel", "Heart Vessel",
					"Shield potion", "Attack potion", "Necklace of J", "Diamond", "Heart Vessel", "Life Vessel", "Ruby circlet"},
0x049c, 0x000000, "RCEN", "Reverse Center Cube", {},
0xac24, 0x03bf33, "RCHI", "Cave", {"Power of Sire", "Life apple", "Alucard sword", "Green tea", "Power of Sire", "EMPTY", "Shiitake", "Shiitake"},
0x465c, 0x03bf2f, "RDAI", "Anti-Chapel", {"EMPTY", "EMPTY", "Fire boomerang", "Diamond", "Zircon", "Heart Vessel", "Shuriken", "TNT", "Boomerang", "Javelin", "Manna prism", "Smart potion", "Life Vessel", "Talwar",
					"Bwaka knife", "Magic Missile", "Twilight cloak", "Heart Vessel"},
0x2b90, 0x03bf27, "RLIB", "Forbidden Library", {"Turquoise", "Opal", "Library card", "Resist fire", "Resist ice", "Resist stone", "Neutron bomb", "Badelaire", "Staurolite"},
0x7354, 0x03bf13, "RNO0", "Black Marble Gallery", {"Library card", "Potion", "Antivenom", "Life Vessel", "Heart Vessel", "Resist dark", "Resist holy", "Resist thunder", "Resist fire", "Meal ticket",
					"Iron ball", "Heart Refresh inside"},
0x9ccc, 0x03bf17, "RNO1", "Reverse Outer Wall", {"Heart Vessel", "Shotel", "Hammer", "Life Vessel", "Luck potion", "Shield potion", "High potion", "Garnet"},
0x6d20, 0x03bf1b, "RNO2", "Death Wing's Lair", {"Opal", "Sword of Hador", "High potion", "Shield potion", "Luck potion", "Manna prism", "Aquamarine", "Alucard mail", "Life Vessel", "Heart Refresh hidden",
					"Shuriken", "Heart Vessel"},
0x3ee0, 0x03bf1f, "RNO3", "Reverse Entrance", {"Hammer", "Antivenom", "High potion", "Heart Vessel", "Zircon", "Opal", "Beryl circlet", "Fire boomerang", "Life Vessel", "Talisman"},
0xA214, 0x03bf23, "RNO4", "Reverse Caverns", {"Alucard shield", "Shiitake", "Toadstool", "Shiitake", "Garnet", "Bat Pentagram", "Life Vessel", "Heart Vessel", "Potion", "Shiitake", "Shiitake", "Opal", "Life Vessel",
					"Diamond", "Zircon", "Heart Vessel", "Meal ticket", "Meal ticket", "Meal ticket", "Meal ticket", "Meal ticket", "Zircon", "Pot roast", "Dark Blade", "Manna prism", "Elixir", "Osafune katana"},
0xcc34, 0x03bf43, "RNZ0", "Necromancy Laboratory", {"EMPTY", "Heart Vessel", "Life Vessel", "Goddess shield", "Manna prism", "Katana", "High potion", "Turquoise", "Ring of Arcana", "Resist dark"},
0xced0, 0x03bf47, "RNZ1", "Reverse Clock Tower", {"Magic Missile", "Karma Coin", "Str. potion", "Luminus", "Smart potion", "Dragon helm", "Diamond", "Life apple", "Sunstone", "Life Vessel", "Heart Vessel", "Moon rod"},
0x2524, 0x03bf3f, "RTOP", "Reverse Castle Keep", {"Sword of Dawn", "Iron ball", "Zircon", "EMPTY", "Bastard sword", "Life Vessel", "Heart Vessel", "Life Vessel", "Heart Vessel", "Life Vessel", "Heart Vessel", "Royal cloak",
					"EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "Resist fire", "Resist ice", "Resist thunder", "Resist stone", "High potion", "Garnet", "Lightning mail", "Library card"},
0xa198, 0x000000, "RWRP", "Reverse Warp rooms", {},
0xc10c, 0x000000, "BO0", "Olrox", {},
0x55d0, 0x000000, "BO1", "Legion", {},
0x76a0, 0x000000, "BO2", "Werewolf & Minotaur", {},
0x6734, 0x000000, "BO3", "Scylla", {},
0x69ec, 0x000000, "BO4", "Doppleganger10", {},
0x6be4, 0x000000, "BO5", "Hippogryph", {},
0x9b84, 0x000000, "BO6", "Richter", {},
0x6678, 0x000000, "BO7", "Cerberus", {},
0xa094, 0x000000, "RBO0", "Fake Trevor/Grant/Sypha", {},
0x5174, 0x000000, "RBO1", "Beezlebub", {},
0x1ab0, 0x000000, "RBO2", "Death", {},
0x31c8, 0x000000, "RBO3", "Medusa", {},
0x8e3c, 0x000000, "RBO4", "Creature", {},
0x5920, 0x000000, "RBO5", "Doppleganger40", {},
0x54ec, 0x000000, "RBO6", "Shaft/Dracula", {},
0x5f04, 0x000000, "RBO7", "Akmodan II", {},
0x9dc8, 0x000000, "RBO8", "Galamoth", {}
} 
-- id, name, address
local items = {0, "Heart", 0x000000, 1, "Big Heart", 0x000000, 2, "$1", 0x000000, 3, "$25", 0x000000, 4, "$50", 0x000000, 5, "$100", 0x000000, 6, "$250", 0x000000, 7, "$400", 0x000000, 9, "$1000", 0x000000, 10, "$2000", 0x000000, 1, "Monster vial 1", 0x09798B,
 				2, "Monster vial 2", 0x09798C, 3, "Monster vial 3", 0x09798D, 4, "Shield rod", 0x09798E, 5, "Leather shield", 0x09798F, 6, "Knight shield", 0x097990, 7, "Iron shield", 0x097991, 8, "AxeLord shield", 0x097992, 9, "Herald shield", 0x097993,
				10, "Dark shield", 0x097994, 11, "Goddess shield", 0x097995, 12, "Shaman shield", 0x097996, 13, "Medusa shield", 0x097997, 14, "Skull shield", 0x097998, 15, "Fire shield", 0x097999, 16, "Alucard shield", 0x09799A, 17, "Sword of dawn", 0x09799B,
				18, "Basilard", 0x09799C, 19, "Short sword", 0x09799D, 20, "Combat knife", 0x09799E, 21, "Nunchaku", 0x09799F, 22, "Were bane", 0x0979A0, 23, "Rapier", 0x0979A1, 24, "Karma coin", 0x0979A2, 25, "Magic missile", 0x0979A3, 26, "Red rust", 0x0979A4,
				27, "Takemitsu", 0x0979A5, 28, "Shotel", 0x0979A6, 29, "Orange", 0x0979A7, 30, "Apple", 0x0979A8, 31, "Banana", 0x0979A9, 32, "Grapes", 0x0979AA, 33, "Strawberry", 0x0979AB, 34, "Pineapple", 0x0979AC, 35, "Peanuts", 0x0979AD,
				36, "Toadstool", 0x0979A6, 37, "Shiitake", 0x0979AF, 38, "Cheesecake", 0x0979B0, 39, "Shortcake", 0x0979B1, 40, "Tart", 0x0979B2, 41, "Parfait", 0x0979B3, 42, "Pudding", 0x0979B4,	43, "Ice cream", 0x0979B5, 44, "Frankfurter", 0x0979B6,
				45, "Hamburger", 0x0979B7, 46, "Pizza", 0x0979B8, 47, "Cheese", 0x0979B9, 48, "Ham and eggs", 0x0979BA, 49, "Omelette", 0x0979BB, 50, "Morning set", 0x0979BC, 51, "Lunch A", 0x0979BD, 52, "Lunch B", 0x0979BE, 53, "Curry rice", 0x0979BF,
				54, "Gyros plate", 0x0979C0, 55, "Spaghetti", 0x0979C1, 56, "Grape juice", 0x0979C2, 57, "Barley tea", 0x0979C3, 58, "Green tea", 0x0979C4, 59, "Natou", 0x0979C5, 60, "Ramen", 0x0979C6, 61, "Miso soup", 0x0979C7, 62, "Sushi", 0x0979C8,
				63, "Pork bun", 0x0979C9, 64, "Red bean bun", 0x0979CA, 65, "Chinese bun", 0x0979CB, 66, "Dim sum set", 0x0979CC, 67, "Pot roast", 0x0979CD, 68, "Sirloin", 0x0979CE, 69, "Turkey", 0x0979CF, 70, "Meal ticket", 0x0979D0, 71, "Neutron bomb", 0x0979D1,
				72, "Power of Sire", 0x0979D2, 73, "Pentagram", 0x0979D3, 74, "Bat Pentagram", 0x0979D4, 75, "Shuriken", 0x0979D5, 76, "Cross shuriken", 0x0979D6, 77, "Buffalo star", 0x0979D7, 78, "Flame star", 0x0979D8, 79, "TNT", 0x0979D9,
				80, "Bwaka knife", 0x0979DA, 81, "Boomerang", 0x0979DB, 82, "Javelin", 0x0979DC, 83, "Tyrfing", 0x0979DD, 84, "Namakura", 0x0979DE, 85, "Knuckle duster", 0x0979DF, 86, "Gladius", 0x0979E0, 87, "Scimitar", 0x0979E1, 88, "Cutlass", 0x0979E2,
				89, "Saber", 0x0979E3, 90, "Falchion", 0x0979E4, 91, "Broadsword", 0x0979E5, 92, "Bekatowa", 0x0979E6, 93, "Damascus sword", 0x0979E7, 94, "Hunter sword", 0x0979E8, 95, "Estoc", 0x0979E9, 96, "Bastard sword", 0x0979EA, 97, "Jewel knuckles", 0x0979EB,
				98, "Claymore", 0x0979EC, 99, "Talwar", 0x0979ED, 100, "Katana", 0x0979EE, 101, "Flamberge", 0x0979EF, 102, "Iron Fist", 0x0979F0, 103, "Zwei hander", 0x0979F1, 104, "Sword of hador", 0x0979F2, 105, "Luminus", 0x0979F3, 106, "Harper", 0x0979F4,
				107, "Obsidian sword", 0x0979F5, 108, "Gram", 0x0979F6, 109, "Jewel sword", 0x0979F7, 110, "Mormegil", 0x0979F8, 111, "Firebrand", 0x0979F9, 112, "Thunderbrand", 0x0979FA, 113, "Icebrand", 0x0979FB, 114, "Stone sword", 0x0979FC,
				115, "Holy sword", 0x0979FD, 116, "Terminus est", 0x0979FE, 117, "Marsil", 0x0979FF, 118, "Dark blade", 0x097A00, 119, "Heaven sword", 0x097A01, 120, "Fist of Tulkas", 0x097A02, 121, "Gurthang", 0x097A03, 122, "Mourneblade", 0x097A04,
				123, "Alucard sword", 0x097A05, 124, "Mablung sword", 0x097A06, 125, "Badelaire", 0x097A07,	126, "Sword familiar", 0x097A08, 127, "Great sword", 0x097A09, 128, "Mace", 0x097A0A, 129, "Morningstar", 0x097A0B, 130, "Holy rod", 0x097A0C,
				131, "Star flail", 0x097A0D, 132, "Moon rod", 0x097A0E, 133, "Chakram", 0x097A0F, 134, "Fire boomerang", 0x097A10, 135, "Iron ball", 0x097A11, 136, "Holbein dagger", 0x097A12, 137, "Blue knuckles", 0x097A13, 138, "Dynamite", 0x097A14,
				139, "Osafune katana", 0x097A15, 140, "Masamune", 0x097A16, 141, "Muramasa", 0x097A17, 142, "Heart refresh", 0x097A18, 143, "Runesword", 0x097A19, 144, "Antivenom", 0x097A1A, 145, "Uncurse", 0x097A1B, 146, "Life apple", 0x097A1C,
				147, "Hammer", 0x097A1D, 148, "Str. potion", 0x097A1E, 149, "Luck potion", 0x097A1F, 150, "Smart potion", 0x097A20, 151, "Attack potion", 0x097A21, 152, "Shield potion", 0x097A22,	153, "Resist fire", 0x097A23, 154, "Resist thunder", 0x097A24,
				155, "Resist ice", 0x097A25, 156, "Resist stone", 0x097A26, 157, "Resist holy", 0x097A27, 158, "Resist dark", 0x097A28, 159, "Potion", 0x097A29, 160, "High potion", 0x097A2A, 161, "Elixir", 0x097A2B, 162, "Manna prism", 0x097A2C,
				163, "Vorpal blade", 0x097A2D, 164, "Crissaegrim", 0x097A2E, 165, "Yasutsuna", 0x097A2F, 166, "Library card", 0x097A30, 167, "Alucart shield", 0x097A31, 168, "Alucart sword", 0x097A32, 170, "Cloth tunic", 0x097A34, 171, "Hide cuirass", 0x097A35,
				172, "Bronze cuirass", 0x097A36, 173, "Iron cuirass", 0x097A37, 174, "Steel cuirass", 0x097A38, 175, "Silver plate", 0x097A39, 176, "Gold plate", 0x097A3A, 177, "Platinum mail", 0x097A3B, 178, "Diamond plate", 0x097A3C, 179, "Fire mail", 0x097A3D,
				180, "Lightning mail", 0x097A3E, 181, "Ice mail", 0x097A3F, 182, "Mirror cuirass", 0x097A40, 183, "Spike breaker", 0x097A41, 184, "Alucard mail", 0x097A42,	185, "Dark armor", 0x097A43, 186, "Healing mail", 0x097A44, 187, "Holy mail", 0x097A45,
				188, "Walk armor", 0x097A46, 189, "Brilliant mail", 0x097A47, 190, "Mojo mail", 0x097A48, 191, "Fury plate", 0x097A49, 192, "Dracula tunic", 0x097A4A, 193, "God's garb", 0x097A4B, 194, "Axe Lord armor", 0x097A4C, 196, "Sunglasses", 0x097A4E,
				197, "Ballroom mask", 0x097A4F, 198, "Bandanna", 0x097A50, 199, "Felt hat", 0x097A51, 200, "Velvet hat", 0x097A52, 201, "Goggles", 0x097A53, 202, "Leather hat", 0x097A54, 203, "Holy glasses", 0x097A55, 204, "Steel helm", 0x097A56,
				205, "Stone mask", 0x097A57, 206, "Circlet", 0x097A58, 207, "Gold circlet", 0x097A59, 208, "Ruby circlet", 0x097A5A, 209, "Opal circlet", 0x097A5B, 210, "Topaz circlet", 0x097A5C, 211, "Beryl circlet", 0x097A5D, 212, "Cat-eye circl.", 0x097A5E,
				213, "Coral circlet", 0x097A5F, 214, "Dragon helm", 0x097A60, 215, "Silver crown", 0x097A61, 216, "Wizard hat", 0x097A62, 218, "Cloth cape", 0x097A64, 219, "Reverse cloak", 0x097A65, 220, "Elven cloak", 0x097A66, 221, "Crystal cloak", 0x097A67,
				222, "Royal cloak", 0x097A68, 223, "Blood cloak", 0x097A69, 224, "Joseph's cloak", 0x097A6A, 225, "Twilight cloak", 0x097A6B, 227, "Moonstone", 0x097A6D, 228, "Sunstone", 0x097A6E, 229, "Bloodstone", 0x097A6F, 230, "Staurolite", 0x097A70,
				231, "Ring of pales", 0x097A71, 232, "Zircon", 0x097A72, 233, "Aquamarine", 0x097A73, 234, "Turquoise", 0x097A74, 235, "Onyx", 0x097A75, 236, "Garnet", 0x097A76, 237, "Opal", 0x097A77, 238, "Diamond", 0x097A78, 239, "Lapis lazuli", 0x097A79,
				240, "Ring of ares", 0x097A7A, 241, "Gold ring", 0x097A7B, 242, "Silver ring", 0x097A7C, 243, "Ring of varda", 0x097A7D, 244, "Ring of arcana", 0x097A7E, 245, "Mystic pendant", 0x097A7F, 246, "Heart broach", 0x097A80, 247, "Necklace of j", 0x097A81,
				248, "Gauntlet", 0x097A82, 249, "Ankh of life", 0x097A83, 250, "Ring of feanor", 0x097A84, 251, "Medal", 0x097A85, 252, "Talisman", 0x097A86, 253, "Duplicator", 0x097A87, 254, "King's stone", 0x097A88, 255, "Covenant stone", 0x097A89,
				256, "Nauglamir", 0x097A8A,	257, "Secret boots", 0x097A8B, 258, "Alucart mail", 0x097a8c
}

local pos_x = 0
local pos_y = 10

function grant_item_byid(num_id)
	if num_id > 258 then
		console.log("Invalid id!")
		return
	end
	name = items[((num_id - 1) * 3) + 32]
	grant_item_byname(name)
end

function grant_item_byname(item_name)
	size = table.getn(items)
	local address, itemqty, itemid = 0, 0, 0
	
	for i = 32, size, 3 do
		if items[i] == item_name then
			address = items[i+1]
			itemid = items[i-1]
			break
		end
	end
	if address ~= 0 then
		itemqty = mainmemory.read_u8(address)
		if itemqty < 255 then itemqty = itemqty + 1 end
		if itemqty == 1 then
			organize_inventory(itemid)
		end
		mainmemory.write_u8(address, itemqty)
	else
		console.log("Item " .. item_name .. " not found!")
	end
end

function organize_inventory(item_id)
	max_index = 0
	start_address = 0
	item_start_address = 0
	offset = 169
	item_offset = 0
	
	if item_id > 0 and item_id <= 168 then --hand
		start_address = 0x097a8d
		item_start_address = 0x09798b
		offset = 0
		max_index = 168
	elseif (item_id > 168 and item_id <= 194) or item_id == 258 then --chest 258 Alucart mail
		start_address = 0x097b36
		item_start_address = 0x097a34
		max_index = 27
	elseif item_id > 195 and item_id <= 216 then --helm
		start_address = 0x097b50
		item_start_address = 0x097a4e
		max_index = 21
		item_offset = 0x1a
	elseif item_id > 217 and item_id <= 225 then --cloak
		start_address = 0x097b66
		item_start_address = 0x097a64
		max_index = 8
		item_offset = 0x30
	elseif item_id > 225 and item_id <= 257 then --trinket
		start_address = 0x097b6f
		item_start_address = 0x097a6d
		max_index = 30
		item_offset = 0x39
	end
		
	for i = 1, max_index, 1 do
		address = start_address + i
		byte = mainmemory.read_u8(address)
		qty = mainmemory.read_u8(item_start_address + byte - 1 - item_offset)
		if qty == 0 then
			mainmemory.write_u8(address, item_id - offset)
			mainmemory.write_u8(start_address + item_id - offset - item_offset, byte)
			break
		end
	end
end

while true do
	local flag = 0
	local flag2 = 0
	local zone = 0
	local size = 0
		
	gui.clearGraphics()
	
	size = table.getn(locations)
	
	
	for i = 1, size, 5 do
		zone = mainmemory.read_u16_le(0x180000)
		
		if zone == locations[i] then
			gui.drawText(0, 0, locations[i+2] .. " - " .. locations[i+3])
			items = locations[i+4]
			if locations[i+2] == "TOP" or locations[i+2] == "CAT" or locations[i+2] == "RTOP" or locations[i+2] == "RNO4" or locations[i+2] == "RCAT" or locations[i+2] == "RDAI" then
				flag = mainmemory.read_u32_le(locations[i+1])
			elseif locations[i+2] == "NO4" then
				flag = mainmemory.read_u32_le(locations[i+1])
				flag2 = mainmemory.read_u16_le(locations[i+1] + 4)
			else
				flag = mainmemory.read_u16_le(locations[i+1])
			end
			
			if locations[i+2] == "ARE" then
				if mainmemory.read_u16_le(0x03ca38) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 20, "Minotaur", color)
			end
			if locations[i+2] == "CAT" then
				if mainmemory.read_u16_le(0x03ca34) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 40, "Legion", color)
			end
			if locations[i+2] == "CHI" then
				if mainmemory.read_u16_le(0x03ca5c) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Cerberus", color)
			if mainmemory.readbyte(0x03be3d) == 0 then
					color = "red"
				else
					color = nil
				end
				gui.drawText(0, 40, "Turkey", color)
			end
			if locations[i+2] == "DAI" then
				if mainmemory.read_u16_le(0x03ca44) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Hippogryph", color)
			end
			if locations[i+2] == "LIB" then
				if mainmemory.readbyte(0x03be60) == 0 then
					color = "red"
				else
					color = nil
				end
				gui.drawText(0, 20, "Bump librarian", color)
				if mainmemory.read_u16_le(0x03ca6c) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Lesser Demon", color)
			end
			if locations[i+2] == "NZ0" then
				if mainmemory.read_u16_le(0x03ca40) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Slogra and Gaibon", color)
			end
			if locations[i+2] == "NO1" then
				if bit.check(mainmemory.readbyte(0x03bdfe), 0) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Pot Roast", color)
				if mainmemory.read_u16_le(0x03ca30) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 40, "Doppelganger10", color)
			end
			if locations[i+2] == "NO2" then
				if mainmemory.read_u16_le(0x03ca2c) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 20, "Olrox", color)
			end
			if locations[i+2] == "NO3" or locations[i+2] == "NP3" then
				if bit.check(mainmemory.readbyte(0x03be1f), 0) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Pot Roast", color)
				if bit.check(mainmemory.readbyte(0x03be24), 0) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 40, "Turkey", color)
			end
			if locations[i+2] == "NO4" then
				if mainmemory.read_u16_le(0x03ca3c) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 50, "Scylla", color)
				if mainmemory.read_u16_le(0x03ca4c) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 60, "Succubus", color)
			end
			if locations[i+2] == "NZ1" then
				if bit.check(mainmemory.readbyte(0x03be8f), 0) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Pot Roast", color)
				if bit.check(mainmemory.readbyte(0x03be8f), 3) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 40, "TNT", color)
				if bit.check(mainmemory.readbyte(0x03be8f), 2) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 50, "Bwaka", color)
				if bit.check(mainmemory.readbyte(0x03be8f), 1) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 60, "Shuriken", color)
				if mainmemory.read_u16_le(0x03ca50) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 70, "Karasuman", color)
			end
			if locations[i+2] == "RARE" then
				if mainmemory.read_u16_le(0x03ca54) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 20, "Fake Trevor/Grant/Sypha", color)
			end
			if locations[i+2] == "RCAT" then
				if mainmemory.read_u16_le(0x03ca7c) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 40, "Galamoth", color)
			end
			if locations[i+2] == "RCHI" then
				if mainmemory.read_u16_le(0x03ca58) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 20, "Death", color)
			end
			if locations[i+2] == "RDAI" then
				if mainmemory.read_u16_le(0x03ca64) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Medusa", color)
			end
			if locations[i+2] == "RNO1" then
				if mainmemory.read_u16_le(0x03ca68) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 20, "Creature", color)
				if bit.check(mainmemory.readbyte(0x03be04), 0) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Dim sum set", color)
			end
			if locations[i+2] == "RNO2" then
				if mainmemory.read_u16_le(0x03ca74) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Akmodan II", color)
			end
			if locations[i+2] == "RNO3" then
				if bit.check(mainmemory.readbyte(0x03be27), 0) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Pot Roast", color)
			end
			if locations[i+2] == "RNO4" then
				if mainmemory.read_u16_le(0x03ca70) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 40, "Doppleganger40", color)
			end
			if locations[i+2] == "RNZ0" then
				if mainmemory.read_u16_le(0x03ca48) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Beezlebub", color)
			end
			if locations[i+2] == "RNZ1" then
				if mainmemory.read_u16_le(0x03ca78) ~= 0 then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 30, "Darkwing Bat", color)
				if bit.check(mainmemory.readbyte(0x03be97), 1) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 40, "Shuriken", color)
				if bit.check(mainmemory.readbyte(0x03be97), 2) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 50, "Bwaka", color)
				if bit.check(mainmemory.readbyte(0x03be97), 3) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 60, "TNT", color)
				if bit.check(mainmemory.readbyte(0x03be97), 0) then
					color = nil
				else
					color = "red"
				end
				gui.drawText(0, 70, "Turkey", color)
			end
						
			for i, v in ipairs(items) do
				if v == "EMPTY" then 
				else
					if i > 32 then
						if bit.check(flag2, i - 33) then
							color = nil
						else
							color = "red"
						end
					else
						if bit.check(flag, i - 1) then
							color = nil
						else
							color = "red"
						end
					end
					gui.drawText(pos_x, pos_y, v .. "/", color)
					pos_x = pos_x + string.len(v) * 8 + 5
					if pos_x > 700 then
						pos_x = 0
						pos_y = pos_y + 10
					end
				end
			end
		end
	end
	
	pos_x = 0
	pos_y = 10

	emu.frameadvance();
end

--[[
--== Shortcuts ==--
rb    = memory.read_u8
rw    = memory.read_u16_be
rws   = memory.read_s16_be
r24   = memory.read_u24_be
rl    = memory.read_u32_be
box   = gui.drawBox
text  = gui.pixelText
line  = gui.drawLine
AND   = bit.band
SHIFT = bit.rshift

rnd1     = rl (0xff001c)
rnd2     = rw (0xff0020)
working  = rb (0xff0073)
xblocks  = rw (0xff00d4)
mapw     = rw (0xff00d4)*8
--]]