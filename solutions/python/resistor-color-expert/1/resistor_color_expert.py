def resistor_label(colors):
    amount = "ohms"
    res_colors = {'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}
    tol = {'grey':'0.05%','violet':'0.1%','blue':'0.25%','green':'0.5%','brown':'1%','red':'2%','gold':'5%','silver':'10%'}
    if len(colors) == 1:
        return "0 ohms"
    if len(colors) == 4:
        num = str(res_colors[colors[0]]) + str(res_colors[colors[1]])
        val = int(num) * 10**res_colors[colors[2]]
        if val >= 1000000:
            amount = "megaohms"
            val /= 1000000
        if val >= 1000:
            amount = "kiloohms"
            val /= 1000
        return f"{is_round(val)} {amount} ±{tol[colors[3]]}"
    if len(colors) == 5:
        num = str(res_colors[colors[0]]) + str(res_colors[colors[1]]) + str(res_colors[colors[2]])
        val = int(num) * 10**res_colors[colors[3]]
        if val >= 1000000:
            amount = "megaohms"
            val /= 1000000
        if val >= 1000:
            amount = "kiloohms"
            val /= 1000
        return f"{is_round(val)} {amount} ±{tol[colors[4]]}"
def is_round(input):
    if round(input) == input:
        return int(input)
    return input
