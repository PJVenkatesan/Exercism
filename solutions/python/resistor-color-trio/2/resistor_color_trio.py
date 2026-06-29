def label(colors):
    resistor_dict = {'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}
    og_ohms = str(resistor_dict[colors[0]]) + str(resistor_dict[colors[1]])
    total_ohms = int(og_ohms) * 10**(resistor_dict[colors[2]])
    if total_ohms > 10**9:
        return f"{int(total_ohms/(10**9))} gigaohms"
    if total_ohms > 10**6:
        return f"{int(total_ohms/(10**6))} megaohms"
    if total_ohms >= 1000:
        return f"{int(total_ohms/1000)} kiloohms"
    return f"{total_ohms} ohms"
