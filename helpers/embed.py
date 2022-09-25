from typing import Dict, NoReturn, Union

from discord import Embed as Ebd


class EmbedHelper:
    def __init__(
            self,
            title: str,
            color: str,
            description: Union[str, None] = None,
            url: Union[str, None] = None,
            thumb: Union[str, None] = None,
            fields: Union[list[Dict], None] = None,
            author: Union[Dict, None] = None,
            image: Union[str, None] = None
    ):
        self.title: str = title
        self.color: str = color
        self.description: Union[str, None] = description
        self.url: Union[str, None] = url
        self.thumb: Union[str, None] = thumb
        self.fields: Union[list[Dict], None] = fields
        self.embed: Union[Ebd, None] = None
        self.author: Union[Dict, None] = author
        self.image: Union[str, None] = image

    def generate_embed(self):
        self.embed = Ebd(title=self.title, color=self.color)

        if self.description:
            self.embed.description = self.description

        if self.url:
            self.embed.url = self.url

        if self.thumb:
            self.embed.set_thumbnail(url=self.thumb)

        if self.author:
            self.embed.set_author(**self.author)

        if self.fields:
            self.generate_fields()

        if self.image:
            self.embed.set_image(url=self.image)

        return

    def generate_fields(self) -> NoReturn:
        [self.embed.add_field(**field) for field in self.fields]
