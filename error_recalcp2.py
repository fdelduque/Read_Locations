import multiprocessing
import concurrent.futures
from functools import partial

eccFLut = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118,
           120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216,
           218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 29, 31, 25, 27, 21, 23, 17, 19, 13, 15, 9, 11, 5, 7, 1, 3, 61, 63, 57, 59, 53, 55, 49, 51, 45, 47, 41, 43, 37, 39, 33, 35, 93, 95, 89, 91, 85, 87, 81,
           83, 77, 79, 73, 75, 69, 71, 65, 67, 125, 127, 121, 123, 117, 119, 113, 115, 109, 111, 105, 107, 101, 103, 97, 99, 157, 159, 153, 155, 149, 151, 145, 147, 141, 143, 137, 139, 133, 135, 129, 131, 189, 191, 185, 187, 181, 183, 177, 179, 173, 175, 169,
           171, 165, 167, 161, 163, 221, 223, 217, 219, 213, 215, 209, 211, 205, 207, 201, 203, 197, 199, 193, 195, 253, 255, 249, 251, 245, 247, 241, 243, 237, 239, 233, 235, 229, 231, 225, 227]
eccBLut = [0, 244, 245, 1, 247, 3, 2, 246, 243, 7, 6, 242, 4, 240, 241, 5, 251, 15, 14, 250, 12, 248, 249, 13, 8, 252, 253, 9, 255, 11, 10, 254, 235, 31, 30, 234, 28, 232, 233, 29, 24, 236, 237, 25, 239, 27, 26, 238, 16, 228, 229, 17, 231, 19, 18, 230, 227,
           23, 22, 226, 20, 224, 225, 21, 203, 63, 62, 202, 60, 200, 201, 61, 56, 204, 205, 57, 207, 59, 58, 206, 48, 196, 197, 49, 199, 51, 50, 198, 195, 55, 54, 194, 52, 192, 193, 53, 32, 212, 213, 33, 215, 35, 34, 214, 211, 39, 38, 210, 36, 208, 209, 37,
           219, 47, 46, 218, 44, 216, 217, 45, 40, 220, 221, 41, 223, 43, 42, 222, 139, 127, 126, 138, 124, 136, 137, 125, 120, 140, 141, 121, 143, 123, 122, 142, 112, 132, 133, 113, 135, 115, 114, 134, 131, 119, 118, 130, 116, 128, 129, 117, 96, 148, 149,
           97, 151, 99, 98, 150, 147, 103, 102, 146, 100, 144, 145, 101, 155, 111, 110, 154, 108, 152, 153, 109, 104, 156, 157, 105, 159, 107, 106, 158, 64, 180, 181, 65, 183, 67, 66, 182, 179, 71, 70, 178, 68, 176, 177, 69, 187, 79, 78, 186, 76, 184, 185,
           77, 72, 188, 189, 73, 191, 75, 74, 190, 171, 95, 94, 170, 92, 168, 169, 93, 88, 172, 173, 89, 175, 91, 90, 174, 80, 164, 165, 81, 167, 83, 82, 166, 163, 87, 86, 162, 84, 160, 161, 85]
edcLut = [0, 2425422081, 2434859521, 28312320, 2453734401, 47187200, 56624640, 2482046721, 2491484161, 68159744, 94374400, 2503019265, 113249280, 2521894145, 2548108801, 124784384, 2566983681, 160436480, 136319488, 2561741569, 188748800, 2614170881,
          2590053889, 183506688, 226498560, 2635143425, 2627803649, 204479232, 2680232961, 256908544, 249568768, 2658213633, 2181111809, 311435520, 320872960, 2209424129, 272638976, 2161190145, 2170627585, 300951296, 377497600, 2249271553, 2275486209,
          389032704, 2227252225, 340798720, 367013376, 2238787329, 452997120, 2341548289, 2317431297, 447755008, 2302751745, 433075456, 408958464, 2297509633, 2407610369, 521156864, 513817088, 2385591041, 499137536, 2370911489, 2363571713, 477118208,
          3019980801, 613433600, 622871040, 3048293121, 641745920, 3067168001, 3076605441, 670058240, 545277952, 2953922817, 2980137473, 556813056, 2999012353, 575687936, 601902592, 3010547457, 754995200, 3180417281, 3156300289, 749753088, 3208729601,
          802182400, 778065408, 3203487489, 3112261633, 688937216, 681597440, 3090242305, 734026752, 3142671617, 3135331841, 712007424, 905994240, 2794545409, 2803982849, 934306560, 2755748865, 886072576, 895510016, 2784061185, 2726389761, 839936256,
          866150912, 2737924865, 817916928, 2689690881, 2715905537, 829452032, 2936107009, 1066430720, 1042313728, 2930864897, 1027634176, 2916185345, 2892068353, 1022392064, 998275072, 2870049025, 2862709249, 976255744, 2848029697, 961576192, 954236416,
          2826010369, 3623976961, 1217429760, 1226867200, 3652289281, 1245742080, 3671164161, 3680601601, 1274054400, 1283491840, 3692136705, 3718351361, 1295026944, 3737226241, 1313901824, 1340116480, 3748761345, 1090555904, 3515977985, 3491860993, 1085313792,
          3544290305, 1137743104, 1113626112, 3539048193, 3582040065, 1158715648, 1151375872, 3560020737, 1203805184, 3612450049, 3605110273, 1181785856, 1509990400, 3398541569, 3407979009, 1538302720, 3359745025, 1490068736, 1499506176, 3388057345, 3464603649,
          1578150144, 1604364800, 3476138753, 1556130816, 3427904769, 3454119425, 1567665920, 3271667713, 1401991424, 1377874432, 3266425601, 1363194880, 3251746049, 3227629057, 1357952768, 1468053504, 3339827457, 3332487681, 1446034176, 3317808129, 1431354624,
          1424014848, 3295788801, 1811988480, 4237410561, 4246848001, 1840300800, 4265722881, 1859175680, 1868613120, 4294035201, 4169254913, 1745930496, 1772145152, 4180790017, 1791020032, 4199664897, 4225879553, 1802555136, 4110536705, 1703989504, 1679872512,
          4105294593, 1732301824, 4157723905, 4133606913, 1727059712, 1635833856, 4044478721, 4037138945, 1613814528, 4089568257, 1666243840, 1658904064, 4067548929, 3993100289, 2123424000, 2132861440, 4021412609, 2084627456, 3973178625, 3982616065, 2112939776,
          2055268352, 3927042305, 3953256961, 2066803456, 3905022977, 2018569472, 2044784128, 3916558081, 1996550144, 3885101313, 3860984321, 1991308032, 3846304769, 1976628480, 1952511488, 3841062657, 3816945665, 1930492160, 1923152384, 3794926337, 1908472832,
          3780246785, 3772907009, 1886453504]
SYNCHEADER = [0,255,255,255,255,255,255,255,255,255,255,0]

def read(fd, address, length, buf = 0, offset = 0):
    if buf:
        for i in range(length):
            buf[offset + i] = fd[address + i]
    return fd[address:(address + length)]

def write(fd, address, data):
    fd[address:(address + len(data))] = data

def set32lsb(p, value):
    for i in range(0,4):
        p[i] = (value >> 8*i) & 0xFF

def edcComputeblock(src, dest):
    edc = 0
    i = 0
    for size in range(len(src),0,-1):
        index = (edc ^ src[i]) & 0xFF
        edc = (edc >> 8) ^ edcLut[index]
        i+=1
    set32lsb(dest, edc)

def eccComputeblock(src, majorCount, minorCount, majorMulti, minorInc, dest):
    size = majorCount * minorCount
    i = 0
    while i < majorCount:
        index = (i >>1) * majorMulti + (i & 1)
        eccA, eccB, j = [0]*3

        while j < minorCount:
            temp = src[index]
            index += minorInc
            if index >= size:
                index -= size
            eccA ^= temp
            eccB ^= temp
            eccA = eccFLut[eccA]
            j+=1
        eccA = eccBLut[eccFLut[eccA] ^ eccB]
        dest[i] = eccA
        dest[i + majorCount] = eccA ^ eccB
        i+=1

def eccGenerate(fd, offset, zeroaddress = False):
    if zeroaddress:
        savedAddress = read(fd, offset + 12, 4)
        write(fd, offset + 12, [0] * 4)
    else:
        savedAddress = [None] * 4

    sector = read(fd, offset + 0xC, 0x8BC)
    ecc = [None] * 2 * 86
    eccComputeblock(sector, 86, 24, 2, 86, ecc)
    write(fd, offset + 0x81C, ecc[0:(2 * 86)])
    sector[0x810:] = ecc[0:(2* 86)]
    eccComputeblock(sector, 52, 43, 86, 88, ecc)
    write(fd, offset + 0x8C8, ecc[0:(2 * 52)])

    if zeroaddress:
       write(fd, offset + 12, savedAddress)

def eccEdcGenerate(fd, offset):
    write(fd, offset, SYNCHEADER)
    edc = [0] * 4
    match (read(fd, offset + 0x0F,1)[0]):
        case 0x00:
            zeros = bytearray(0x920)
            write(fd, offset + 0x10, zeros)
        case 0x01:
            sector = read(fd, offset, 0x810)
            edcComputeblock(sector, edc)
            write(fd, offset + 0x810, edc)
            zeros = bytearray(8)
            write(fd, offset + 0x814, zeros)
            eccGenerate(fd, offset)
        case 0x02:
            flags = read(fd, offset + 0x10, 4)
            write(fd, offset + 0x14, flags)
            if not (read(fd, offset + 0x12, 1)[0] & 0x20):
                sector = read(fd, offset + 0x10, 0x808)
                edcComputeblock(sector, edc)
                write(fd, offset + 0x818, edc)
                eccGenerate(fd, offset, True)
            else:
                sector = read(fd, offset + 0x10, 0x91C)
                edcComputeblock(sector, edc)
                write(fd, offset + 0x92C, edc)

def anyNonZero(data,given_length):
    return any(el for el in data[:given_length])

def memcmp(a, b, given_length):
    return int(a[:given_length] != b[:given_length])

def edcVerify(fd):
    myedc = [0] * 4
    header = read(fd, 0, len(SYNCHEADER))
    if memcmp(header, SYNCHEADER, len(SYNCHEADER)):
        return 1
    match read(fd, 0x0F,1)[0]:
        case 0x00:
            return anyNonZero(read(fd, 0x10, 0x920), 0x920)
        case 0x01:
            sector = read(fd, 0, 0x810 + 4)
            edcComputeblock(sector[0:0x810], myedc)
            return memcmp(myedc, sector[0x810:], 4)
        case 0x02:
            type = read(fd, 0x10, 8)
            if memcmp(type, type[4:], 4):
                return 1
            if not (type[2] & 0x20):
                sector = read(fd, 0x10, 0x808 + 4)
                edcComputeblock(sector[0:0x808], myedc)
                return memcmp(myedc, sector[0x808:], 4)
            else:
                sector = read(fd, 0x10, 0x91C + 4)
                edcComputeblock(sector[0:0x91C], myedc)
                return memcmp(myedc, sector[0x91C:], 4)
    return 1

def audioGuess(sector):
    if (
        not memcmp(sector, SYNCHEADER, len(SYNCHEADER)) and
        sector[0xD] < 0x60 and
        sector[0xE] < 0x75 and
        sector[0xF] < 3
    ):
        return 0
    return 1

"""def process_sector_multi(f, b, e, fd, sector = 0):
    global eccFLut, eccBLut, edcLut
    eccFLut = f
    eccBLut = b
    edcLut = e
    buf = [0] * 16
    read(fd, 0, len(buf), buf)
    if audioGuess(buf) and not False:
        print('warning: sector ', sector, ' looks like an audio sector, will recalculate earlier sectors only')
        return 0
    eccEdcGenerate(fd, 0)
    return fd
"""
def process_sector_multi(fd, sector = 0):
    buf = [0] * 16
    read(fd, 0, len(buf), buf)
    if audioGuess(buf) and not False:
        print('warning: sector ', sector, ' looks like an audio sector, will recalculate earlier sectors only')
        return 0
    eccEdcGenerate(fd, 0)
    return fd


def eccEdcCalc():
    start = 16 * 2352
        
    
    
    print("Starting pool")

    #chunks = [fd[x:x + 2352] for x in range(start, len(fd), 2352)]
    #chunks = [fd[x:x + 2352] for x in range(start, start + (10 * 2352), 2352)]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        with open("C:/python teste/hello/Castlevania - Symphony of the Night (USA) (Track 1).bin", "rb") as inFile:
            fd = list(inFile.read())
            data = fd[0:start]
            chunks = [fd[x:x + 2352] for x in range(start, len(fd), 2352)]
            print("working....")
            for r in executor.map(process_sector_multi, chunks):
                data.extend(r)
    

    """for r in map(process_sector_multi, chunks):
         data.extend(r)"""
        
    
    print("inside after pool: ", data[39776:39780])
    print("Ending pool")

    print(len(data))

    return data
