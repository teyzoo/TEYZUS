from app.cards.formatter import (
    format_score,
    format_price
)


def build_username_card(
    username,
    ai=None,
    price_min=None,
    price_max=None
):

    text = (
        "🚀 TEYZUS AI\n\n"
        "✅ USERNAME ANALYSIS\n\n"
        f"@{username}\n\n"
    )


    if ai:

        text += (
            "🤖 AI Score\n"
            f"{format_score(ai)}\n\n"
        )


    text += (
        "💰 Цена\n"
        f"{format_price(price_min, price_max)}\n"
    )


    return text
