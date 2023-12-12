local pos_x = 0
local pos_y = 10
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

while true do
	local flag = 0
	local flag2 = 0
	local zone = 0
	local size = 0
		
	gui.clearGraphics()
	
	size = table.getn(locations)
	
	
	for i = 1, size, 5 do
		zone = mainmemory.read_u16_le(0x180000)
		--gui.drawText(0, 0, zone)
		
		
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

			--gui.drawText(0, 60, flag)
			--gui.drawText(0, 70, flag2)
			
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