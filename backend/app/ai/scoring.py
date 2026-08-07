def analyze_username(username: str):

    length = len(username)

    readability = max(
        10 - length / 3,
        1
    )

    rarity = (
        10
        if length <= 5
        else 7
    )

    beauty = (
        10
        if username.isalpha()
        else 7
    )

    brand = (
        10
        if len(username) <= 8
        else 6
    )

    liquidity = (
        beauty +
        rarity +
        brand
    ) / 3


    total = (
        beauty +
        readability +
        rarity +
        brand +
        liquidity
    ) / 5


    return {
        "beauty": round(beauty, 1),
        "readability": round(readability, 1),
        "rarity": round(rarity, 1),
        "brand": round(brand, 1),
        "liquidity": round(liquidity, 1),
        "total": round(total, 1)
    }
