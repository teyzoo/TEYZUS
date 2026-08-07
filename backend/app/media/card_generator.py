from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


CARD_WIDTH = 1200
CARD_HEIGHT = 630


def create_card(
    username: str,
    score: float,
    price: str
):

    image = Image.new(
        "RGB",
        (
            CARD_WIDTH,
            CARD_HEIGHT
        ),
        "#050B18"
    )


    draw = ImageDraw.Draw(
        image
    )


    font = ImageFont.load_default()


    draw.text(
        (80,80),
        "🚀 TEYZUS AI",
        font=font
    )


    draw.text(
        (80,180),
        f"@{username}",
        font=font
    )


    draw.text(
        (80,280),
        f"AI Score: {score}/10",
        font=font
    )


    draw.text(
        (80,380),
        f"Price: {price}",
        font=font
    )


    path = (
        Path("media")
        /
        f"{username}.png"
    )


    image.save(
        path
    )


    return str(path)
