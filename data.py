from classes import Time   # keep your Time class import

routes = {
    # Sacramento
    ("Sacramento", "San Francisco"): [87.6, Time(1, 35)],
    ("Sacramento", "San Jose")     : [121.2, Time(1, 55)],
    ("Sacramento", "Fremont")      : [90.3, Time(1, 30)],
    ("Sacramento", "Stockton")     : [46.7, Time(0, 45)],
    ("Sacramento", "Modesto")      : [72.5, Time(1, 10)],
    ("Sacramento", "Fresno")       : [170.1, Time(2, 40)],
    ("Sacramento", "San Luis Obispo"): [306.9, Time(4, 50)],
    ("Sacramento", "Bakersfield")  : [254.8, Time(3, 50)],
    ("Sacramento", "Los Angeles")  : [379.1, Time(5, 55)],
    ("Sacramento", "Riverside")    : [403.4, Time(6, 15)],
    ("Sacramento", "Irvine")       : [403.8, Time(6, 15)],
    ("Sacramento", "Long Beach")   : [387.6, Time(6, 0)],
    ("Sacramento", "San Diego")    : [489.1, Time(7, 30)],

    # San Francisco
    ("San Francisco", "San Jose")  : [48.5, Time(0, 50)],
    ("San Francisco", "Fremont")   : [43.6, Time(0, 45)],
    ("San Francisco", "Stockton")  : [78.5, Time(1, 25)],
    ("San Francisco", "Modesto")   : [91.6, Time(1, 40)],
    ("San Francisco", "Fresno")    : [186.2, Time(2, 55)],
    ("San Francisco", "San Luis Obispo"): [230.9, Time(3, 50)],
    ("San Francisco", "Bakersfield"): [282.8, Time(4, 30)],
    ("San Francisco", "Los Angeles"): [381.8, Time(6, 0)],
    ("San Francisco", "Riverside") : [415.7, Time(6, 30)],
    ("San Francisco", "Irvine")    : [419.6, Time(6, 35)],
    ("San Francisco", "Long Beach"): [390.6, Time(6, 10)],
    ("San Francisco", "San Diego") : [498.4, Time(7, 40)],

    # San Jose
    ("San Jose", "Fremont")        : [16.2, Time(0, 20)],
    ("San Jose", "Stockton")       : [58.4, Time(1, 0)],
    ("San Jose", "Modesto")        : [72.5, Time(1, 15)],
    ("San Jose", "Fresno")         : [159.2, Time(2, 30)],
    ("San Jose", "San Luis Obispo"): [188.7, Time(3, 10)],
    ("San Jose", "Bakersfield")    : [235.8, Time(3, 40)],
    ("San Jose", "Los Angeles")    : [338.4, Time(5, 15)],
    ("San Jose", "Riverside")      : [372.3, Time(5, 45)],
    ("San Jose", "Irvine")         : [376.2, Time(5, 50)],
    ("San Jose", "Long Beach")     : [347.2, Time(5, 25)],
    ("San Jose", "San Diego")      : [455.0, Time(7, 0)],
    ("San Jose","San Francisco")  : [48.5, Time(0, 50)],

    # Fremont
    ("Fremont", "Stockton")        : [42.9, Time(0, 45)],
    ("Fremont", "Modesto")         : [57.0, Time(1, 0)],
    ("Fremont", "Fresno")          : [143.7, Time(2, 15)],
    ("Fremont", "San Luis Obispo") : [191.0, Time(3, 15)],
    ("Fremont", "Bakersfield")     : [240.2, Time(3, 45)],
    ("Fremont", "Los Angeles")     : [342.8, Time(5, 20)],
    ("Fremont", "Riverside")       : [376.7, Time(5, 50)],
    ("Fremont", "Irvine")          : [380.6, Time(5, 55)],
    ("Fremont", "Long Beach")      : [351.6, Time(5, 30)],
    ("Fremont", "San Diego")       : [459.4, Time(7, 5)],

    # Stockton
    ("Stockton", "San Jose")       : [58.4, Time(1, 0)],
    ("Stockton", "Modesto")        : [30.2, Time(0, 30)],
    ("Stockton", "Fresno")         : [116.8, Time(1, 45)],
    ("Stockton", "San Luis Obispo"): [247.9, Time(4, 0)],
    ("Stockton", "Bakersfield")    : [202.9, Time(3, 5)],
    ("Stockton", "Los Angeles")    : [326.2, Time(5, 0)],
    ("Stockton", "Riverside")      : [350.5, Time(5, 20)],
    ("Stockton", "Irvine")         : [350.9, Time(5, 25)],
    ("Stockton", "Long Beach")     : [334.7, Time(5, 10)],
    ("Stockton", "San Diego")      : [436.2, Time(6, 40)],

    # Modesto
    ("Modesto", "Fresno")          : [86.6, Time(1, 20)],
    ("Modesto", "San Luis Obispo") : [217.7, Time(3, 30)],
    ("Modesto", "Bakersfield")     : [172.7, Time(2, 40)],
    ("Modesto", "Los Angeles")     : [296.0, Time(4, 35)],
    ("Modesto", "Riverside")       : [320.3, Time(4, 55)],
    ("Modesto", "Irvine")          : [320.7, Time(4, 55)],
    ("Modesto", "Long Beach")      : [304.5, Time(4, 40)],
    ("Modesto", "San Diego")       : [406.0, Time(6, 15)],

    # Fresno
    ("Fresno", "San Luis Obispo")  : [130.4, Time(2, 10)],
    ("Fresno", "Bakersfield")      : [108.7, Time(1, 35)],
    ("Fresno", "Los Angeles")      : [221.7, Time(3, 20)],
    ("Fresno", "Riverside")        : [246.0, Time(3, 40)],
    ("Fresno", "Irvine")           : [246.4, Time(3, 40)],
    ("Fresno", "Long Beach")       : [230.2, Time(3, 25)],
    ("Fresno", "San Diego")        : [331.7, Time(5, 0)],

    # San Luis Obispo
    ("San Luis Obispo", "Bakersfield"): [109.8, Time(1, 50)],
    ("San Luis Obispo", "Los Angeles"): [186.2, Time(2, 55)],
    ("San Luis Obispo", "Riverside")  : [216.5, Time(3, 20)],
    ("San Luis Obispo", "Irvine")     : [208.6, Time(3, 10)],
    ("San Luis Obispo", "Long Beach") : [185.0, Time(2, 50)],
    ("San Luis Obispo", "San Diego")  : [272.8, Time(4, 5)],

    # Bakersfield
    ("Bakersfield", "Los Angeles") : [112.5, Time(1, 45)],
    ("Bakersfield", "Riverside")   : [136.8, Time(2, 5)],
    ("Bakersfield", "Irvine")      : [137.2, Time(2, 5)],
    ("Bakersfield", "Long Beach")  : [121.0, Time(1, 50)],
    ("Bakersfield", "San Diego")   : [222.5, Time(3, 25)],

    # SoCal
    ("Los Angeles", "Riverside")   : [55.9, Time(0, 55)],
    ("Los Angeles", "Irvine")      : [45.0, Time(0, 45)],
    ("Los Angeles", "Long Beach")  : [24.0, Time(0, 30)],
    ("Los Angeles", "San Diego")   : [121.0, Time(1, 50)],

    ("Riverside", "Irvine")        : [33.1, Time(0, 35)],
    ("Riverside", "Long Beach")    : [48.6, Time(0, 50)],
    ("Riverside", "San Diego")     : [95.4, Time(1, 30)],

    ("Irvine", "Long Beach")       : [25.0, Time(0, 30)],
    ("Irvine", "San Diego")        : [86.0, Time(1, 20)],

    ("Long Beach", "San Diego")    : [93.0, Time(1, 30)]
}


