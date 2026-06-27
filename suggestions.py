def get_suggestion(temp):
    
    if temp >= 35:
        return "Hot weather. Drink plenty of water."

    elif temp >= 20:
        return "Pleasant weather. Enjoy your day."

    elif temp >= 10:
        return "Cool weather. Light jacket recommended."

    else:
        return "Cold weather. Wear warm clothes."