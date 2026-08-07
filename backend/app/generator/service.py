import random

from app.generator.categories import CATEGORIES



def generate_username(
    length: int,
    numbers: bool = False,
    category: str = None
):

    words = []


    if category:

        words = CATEGORIES.get(
            category,
            []
        )


    if not words:

        for value in CATEGORIES.values():

            words.extend(
                value
            )


    results = []


    while len(results) < 20:

        word = random.choice(
            words
        )


        username = word


        if numbers:

            username += str(
                random.randint(
                    1,
                    999
                )
            )


        username = username[:length]


        if len(username) == length:

            results.append(
                username
            )


    return list(
        set(results)
    )
