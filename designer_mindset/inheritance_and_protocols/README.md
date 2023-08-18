## 1. Social media channels

You just landed a job at "SocialOverlord", a company developing a SaaS product allowing you to write and schedule posts to a variety of social networks.

The whole backend is written in Python (yay!), but unfortunately, the person you're replacing didn't know classes exist (ehrm...) and so they used tuples to represent all the data in the system (not so yay...). Here's a code example:

```python
# each social channel has a type
# and the current number of followers
SocialChannel = tuple[str, int]

# each post has a message and the timestamp when it should be posted
Post = tuple[str, int]

def post_a_message(channel: SocialChannel, message: str) -> None:
  type, _ = channel
  if type == "youtube":
    post_to_youtube(channel, message)
  elif type == "facebook":
    post_to_facebook(channel, message)
  elif type == "twitter":
    post_to_twitter(channel, message)

def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
  for post in posts:
    message, timestamp = post
    for channel in channels:
      if timestamp <= time():
        post_a_message(channel, message)
```

a) From tuples to classes

Refactor this code so that it uses classes instead of tuples to represent social channels and posts. As a starting point, use the code download for this exercise.
b) Improving the post_a_message function

The post_a_message function isn't great. The if-statement has to check for each different type of social network and then call a different method. If you want to add support for a new social network, you'll need to add an extra elif part, making the code harder and harder to read.

Implement a new version of the code that uses abstraction to solve the problem.

Bonus challenge: is there a solution that doesn't need abstraction?

## 2. Html Trees

Consider the following classes:

```python
@dataclass
class Div:
  parent: Div | None = None
  x: int = 0
  y: int = 0

def compute_screen_position(self) -> tuple[int, int]:
  if not self.parent:
    return (self.x, self.y)
  parent_x, parent_y = self.parent.compute_screen_position()
  return (parent_x + self.x, parent_y + self.y)

@dataclass
class Button:
  parent: Div
  x: int
  y: int

def click(self) -> None:
  print("Click!")

@dataclass
class Span:
  parent: Div
  x: int
  y: int
  text: str
```

Of course, HTML has many more different elements. In the elements above, there is some duplication (in particular, the parent, x and y instance variables). Also, we'd like to be able to compute the position of any type of element, not just divs and be able to combine different elements in a tree.

a) Abstraction

Refactor the class hierarchy by introducing an abstract base class HTMLElement that divs, buttons, and spans are subclasses of. Minimize code duplication and make sure that each element is able to compute its position on the screen.

In order to get started more quickly, download the code for this exercise above (but don't look at the solution yet!).

 
b) Protocols

Can you use a protocol class just as easily instead of an abstract base class? What would need to be changed in the code for this to work?