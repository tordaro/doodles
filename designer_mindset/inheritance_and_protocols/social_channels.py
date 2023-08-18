from abc import ABC, abstractmethod
from time import time
from dataclasses import dataclass


class SocialChannel(ABC):
    followers: int

    @abstractmethod
    def post_message(self, message: str) -> None:
        pass

    @property
    @abstractmethod
    def type(self) -> str:
        pass


@dataclass
class YouTubeChannel(SocialChannel):
    followers: int

    def post_message(self, message: str) -> None:
        print(f"{self.type} channel: {message}")

    @property
    def type(self) -> str:
        return "youtube"


@dataclass
class FacebookChannel(SocialChannel):
    followers: int

    def post_message(self, message: str) -> None:
        print(f"{self.type} channel: {message}")

    @property
    def type(self) -> str:
        return "facebook"


@dataclass
class TwitterChannel(SocialChannel):
    followers: int

    def post_message(self, message: str) -> None:
        print(f"{self.type} channel: {message}")

    @property
    def type(self) -> str:
        return "twitter"


@dataclass
class Post:
    message: str
    timestamp: int


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        for channel in channels:
            if post.timestamp <= time():
                channel.post_message(post.message)


def main() -> None:
    posts = [
        Post(
            "Grandma's carrot cake is available again (limited quantities!)!",
            1568123400,
        ),
        Post("Get your carrot cake now, the promotion ends today!", 1568133400),
    ]
    channels = [
        YouTubeChannel(100),
        FacebookChannel(100),
        TwitterChannel(100),
    ]
    process_schedule(posts, channels)


if __name__ == "__main__":
    main()
