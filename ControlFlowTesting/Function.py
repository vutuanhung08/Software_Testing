def electricity_to_money(e):
    if not isinstance(e, int) or e < 0:
        return -1
    elif e <= 50:
        money = (e * 1678) * 1.08
    elif e <= 100:
        money = (83900 + (e - 50) * 1734) * 1.08
    elif e <= 200:
        money = (170600 + (e - 100) * 2014) * 1.08
    elif e <= 300:
        money = (372000 + (e - 200) * 2536) * 1.08
    elif e <= 400:
        money = (625600 + (e - 300) * 2834) * 1.08
    else:
        money = (909000 + (e - 400) * 2927) * 1.08
    money = round(money)
    return money
