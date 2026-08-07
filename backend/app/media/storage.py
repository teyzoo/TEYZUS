from pathlib import Path


MEDIA_FOLDER = Path(
    "media"
)


def ensure_media():

    MEDIA_FOLDER.mkdir(
        exist_ok=True
    )
