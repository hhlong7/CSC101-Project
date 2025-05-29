from classes import Time   # keep your Time class import

routes = {
    # Sacramento
    ("Sacramento", "San Francisco"): [87.6, Time(1, 35, 0)],
    ("Sacramento", "San Jose")     : [121.2, Time(1, 55, 0)],
    ("Sacramento", "Fremont")      : [90.3, Time(1, 30, 0)],
    ("Sacramento", "Stockton")     : [46.7, Time(0, 45, 0)],
    ("Sacramento", "Modesto")      : [72.5, Time(1, 10, 0)],
    ("Sacramento", "Fresno")       : [170.1, Time(2, 40, 0)],
    ("Sacramento", "San Luis Obispo"): [306.9, Time(4, 50, 0)],
    ("Sacramento", "Bakersfield")  : [254.8, Time(3, 50, 0)],
    ("Sacramento", "Los Angeles")  : [379.1, Time(5, 55, 0)],
    ("Sacramento", "Riverside")    : [403.4, Time(6, 15, 0)],
    ("Sacramento", "Irvine")       : [403.8, Time(6, 15, 0)],
    ("Sacramento", "Long Beach")   : [387.6, Time(6, 0, 0)],
    ("Sacramento", "San Diego")    : [489.1, Time(7, 30, 0)],

    # San Francisco
    ("San Francisco", "San Jose")  : [48.5, Time(0, 50, 0)],
    ("San Francisco", "Fremont")   : [43.6, Time(0, 45, 0)],
    ("San Francisco", "Stockton")  : [78.5, Time(1, 25, 0)],
    ("San Francisco", "Modesto")   : [91.6, Time(1, 40, 0)],
    ("San Francisco", "Fresno")    : [186.2, Time(2, 55, 0)],
    ("San Francisco", "San Luis Obispo"): [230.9, Time(3, 50, 0)],
    ("San Francisco", "Bakersfield"): [282.8, Time(4, 30, 0)],
    ("San Francisco", "Los Angeles"): [381.8, Time(6, 0, 0)],
    ("San Francisco", "Riverside") : [415.7, Time(6, 30, 0)],
    ("San Francisco", "Irvine")    : [419.6, Time(6, 35, 0)],
    ("San Francisco", "Long Beach"): [390.6, Time(6, 10, 0)],
    ("San Francisco", "San Diego") : [498.4, Time(7, 40, 0)],

    # San Jose
    ("San Jose", "Fremont")        : [16.2, Time(0, 20, 0)],
    ("San Jose", "Stockton")       : [58.4, Time(1, 0, 0)],
    ("San Jose", "Modesto")        : [72.5, Time(1, 15, 0)],
    ("San Jose", "Fresno")         : [159.2, Time(2, 30, 0)],
    ("San Jose", "San Luis Obispo"): [188.7, Time(3, 10, 0)],
    ("San Jose", "Bakersfield")    : [235.8, Time(3, 40, 0)],
    ("San Jose", "Los Angeles")    : [338.4, Time(5, 15, 0)],
    ("San Jose", "Riverside")      : [372.3, Time(5, 45, 0)],
    ("San Jose", "Irvine")         : [376.2, Time(5, 50, 0)],
    ("San Jose", "Long Beach")     : [347.2, Time(5, 25, 0)],
    ("San Jose", "San Diego")      : [455.0, Time(7, 0, 0)],

    # Fremont
    ("Fremont", "Stockton")        : [42.9, Time(0, 45, 0)],
    ("Fremont", "Modesto")         : [57.0, Time(1, 0, 0)],
    ("Fremont", "Fresno")          : [143.7, Time(2, 15, 0)],
    ("Fremont", "San Luis Obispo") : [191.0, Time(3, 15, 0)],
    ("Fremont", "Bakersfield")     : [240.2, Time(3, 45, 0)],
    ("Fremont", "Los Angeles")     : [342.8, Time(5, 20, 0)],
    ("Fremont", "Riverside")       : [376.7, Time(5, 50, 0)],
    ("Fremont", "Irvine")          : [380.6, Time(5, 55, 0)],
    ("Fremont", "Long Beach")      : [351.6, Time(5, 30, 0)],
    ("Fremont", "San Diego")       : [459.4, Time(7, 5, 0)],

    # Stockton
    ("Stockton", "Modesto")        : [30.2, Time(0, 30, 0)],
    ("Stockton", "Fresno")         : [116.8, Time(1, 45, 0)],
    ("Stockton", "San Luis Obispo"): [247.9, Time(4, 0, 0)],
    ("Stockton", "Bakersfield")    : [202.9, Time(3, 5, 0)],
    ("Stockton", "Los Angeles")    : [326.2, Time(5, 0, 0)],
    ("Stockton", "Riverside")      : [350.5, Time(5, 20, 0)],
    ("Stockton", "Irvine")         : [350.9, Time(5, 25, 0)],
    ("Stockton", "Long Beach")     : [334.7, Time(5, 10, 0)],
    ("Stockton", "San Diego")      : [436.2, Time(6, 40, 0)],

    # Modesto
    ("Modesto", "Fresno")          : [86.6, Time(1, 20, 0)],
    ("Modesto", "San Luis Obispo") : [217.7, Time(3, 30, 0)],
    ("Modesto", "Bakersfield")     : [172.7, Time(2, 40, 0)],
    ("Modesto", "Los Angeles")     : [296.0, Time(4, 35, 0)],
    ("Modesto", "Riverside")       : [320.3, Time(4, 55, 0)],
    ("Modesto", "Irvine")          : [320.7, Time(4, 55, 0)],
    ("Modesto", "Long Beach")      : [304.5, Time(4, 40, 0)],
    ("Modesto", "San Diego")       : [406.0, Time(6, 15, 0)],

    # Fresno
    ("Fresno", "San Luis Obispo")  : [130.4, Time(2, 10, 0)],
    ("Fresno", "Bakersfield")      : [108.7, Time(1, 35, 0)],
    ("Fresno", "Los Angeles")      : [221.7, Time(3, 20, 0)],
    ("Fresno", "Riverside")        : [246.0, Time(3, 40, 0)],
    ("Fresno", "Irvine")           : [246.4, Time(3, 40, 0)],
    ("Fresno", "Long Beach")       : [230.2, Time(3, 25, 0)],
    ("Fresno", "San Diego")        : [331.7, Time(5, 0, 0)],

    # San Luis Obispo
    ("San Luis Obispo", "Bakersfield"): [109.8, Time(1, 50, 0)],
    ("San Luis Obispo", "Los Angeles"): [186.2, Time(2, 55, 0)],
    ("San Luis Obispo", "Riverside")  : [216.5, Time(3, 20, 0)],
    ("San Luis Obispo", "Irvine")     : [208.6, Time(3, 10, 0)],
    ("San Luis Obispo", "Long Beach") : [185.0, Time(2, 50, 0)],
    ("San Luis Obispo", "San Diego")  : [272.8, Time(4, 5, 0)],

    # Bakersfield
    ("Bakersfield", "Los Angeles") : [112.5, Time(1, 45, 0)],
    ("Bakersfield", "Riverside")   : [136.8, Time(2, 5, 0)],
    ("Bakersfield", "Irvine")      : [137.2, Time(2, 5, 0)],
    ("Bakersfield", "Long Beach")  : [121.0, Time(1, 50, 0)],
    ("Bakersfield", "San Diego")   : [222.5, Time(3, 25, 0)],

    # SoCal
    ("Los Angeles", "Riverside")   : [55.9, Time(0, 55, 0)],
    ("Los Angeles", "Irvine")      : [45.0, Time(0, 45, 0)],
    ("Los Angeles", "Long Beach")  : [24.0, Time(0, 30, 0)],
    ("Los Angeles", "San Diego")   : [121.0, Time(1, 50, 0)],

    ("Riverside", "Irvine")        : [33.1, Time(0, 35, 0)],
    ("Riverside", "Long Beach")    : [48.6, Time(0, 50, 0)],
    ("Riverside", "San Diego")     : [95.4, Time(1, 30, 0)],

    ("Irvine", "Long Beach")       : [25.0, Time(0, 30, 0)],
    ("Irvine", "San Diego")        : [86.0, Time(1, 20, 0)],

    ("Long Beach", "San Diego")    : [93.0, Time(1, 30, 0)]
}
