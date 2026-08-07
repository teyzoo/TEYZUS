from app.result_card.keyboard import (
    result_keyboard
)



def build_result_card(
    username: str,
    available: bool,
    score: float = 0,
    price: str = "$0"
):

    status = (
        "⚡ Свободен"
        if available
        else "❌ Занят"
    )


    text = f"""
🚀 TEYZUS AI

✅ USERNAME:

@{username}


📖 Читаемость:
⭐ {score}/10


🤖 AI Score:
⭐ {score}/10


💰 Цена:
{price}


{status}
"""


    return (
        text,
        result_keyboard()
    )
