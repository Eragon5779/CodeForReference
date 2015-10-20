def any_arrows(arrows):
    for x in arrows:
        if "damaged" not in x or x['damaged'] == False:
            return True
    return False
