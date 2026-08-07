from app.ai.scoring import analyze_username
from app.pricing.estimator import estimate_price


def enrich_username(
    username: str
):

    ai_result = analyze_username(
        username
    )


    price_result = estimate_price(
        username,
        ai_result["total"]
    )


    return {
        "username": username,

        "ai_score": ai_result["total"],

        "beauty": ai_result["beauty"],

        "readability": ai_result["readability"],

        "rarity": ai_result["rarity"],

        "brand": ai_result["brand"],

        "liquidity": ai_result["liquidity"],

        "estimated_price_min":
            price_result["min_price"],

        "estimated_price_max":
            price_result["max_price"],

        "category":
            price_result["category"]
    }
