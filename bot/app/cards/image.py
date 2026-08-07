from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1200
HEIGHT = 630


def create_username_card(
    username: str,
    score: float | None,
    price: str
):

    image = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        "#050B18"
    )

    draw = ImageDraw.Draw(
        image
    )

    font = ImageFont.load_default()


    draw.text(
        (80, 70),
        "🚀 TEYZUS AI",
        font=font
    )


    draw.text(
        (80, 180),
        f"@{username}",
        font=font
    )


    draw.text(
        (80, 300),
        f"🤖 AI Score: {score or '-'}",
        font=font
    )


    draw.text(
        (80, 390),
        f"💰 Price: {price}",
        font=font
    )


    folder = Path(
        "cards"
    )

    folder.mkdir(
        exist_ok=True
    )


    path = folder / (
        f"{username}.png"
    )


    image.save(
        path
    )


    return str(path)
