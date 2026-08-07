def estimate_price(
    username: str,
    ai_score: float | None = None
):

    length = len(username)

    base_price = 5


    if length <= 4:
        base_price = 500

    elif length <= 6:
        base_price = 100

    elif length <= 8:
        base_price = 30


    if ai_score:
        multiplier = 1 + (
            ai_score / 10
        )

        base_price *= multiplier


    category = "general"


    if username.lower().endswith(
        ("ai", "bot", "x")
    ):
        category = "technology"


    return {
        "min_price": round(
            base_price * 0.7,
            2
        ),

        "max_price": round(
            base_price * 1.5,
            2
        ),

        "category": category
    }
