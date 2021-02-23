from datetime import datetime
from functools import cached_property
from typing import List
from os import path

from .config import settings, EPISODE_DATEFORMAT
from .utils import slugify


class Episode:
    number: int = 0
    season: int = 0

    file_url: str

    title: str
    subtitle: str
    author: str
    link: str
    published: datetime

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'<Episode: "{self}">'

    @cached_property
    def title_slug(self):
        return slugify(self.title)

    @cached_property
    def filename(self):
        if self.podcast.has_seasons:
            return f"S{self.season:02d}E{self.season:03d} {self.title_slug}"

        episode_date = self.publised.strftime(EPISODE_DATEFORMAT)
        return f"{episode_date} {self.title_slug}"

    @cached_property
    def full_path(self):
        return path.join(self.podcast.base_directory, self.filename)


class Podcast:
    episodes: List[Episode]

    title: str
    subtitle: str
    author: str
    language: str
    link: str

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'<Podcast: "{self}">'

    def __len__(self):
        return len(self.episodes)

    @cached_property
    def title_slug(self):
        return slugify(self.title)

    @cached_property
    def base_directory(self):
        return path.join(settings.BASE_PATH, self.title_slug)
