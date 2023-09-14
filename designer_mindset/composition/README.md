# Composition
In this exercise, you'll practice with composition and abstraction to improve code that is used by a famous YouTuber to manage backing up his video files.

It relies on a (fake) cloudengine package that has a CloudProvider abstract base class. This class expects a region (this refers to the data center that is used), an authentication object used to access the cloud resource, as well as a secure flag (it doesn't really matter what this actually is, but set it to True for more security!).

The code below is part of a script that this famous YouTuber uses to search through video backups, which are stored in a bucket (= file storage location) in the cloud:

```python
class ACCloud(CloudProvider):
  def __init__(self, bucket_name: str, region: str) -> None:
    authentication = GoogleAuth("service_key.json")
    super().__init__(
      region=region,
      http_auth=authentication,
      secure=True,
    )
    self.bucket_name = bucket_name

  def find_files(
    self,
    query: str,
    max_result: int
  ) -> list[str]:
    response = self.filter_by_query(
      bucket=self.bucket_name,
      query=query,
      max=max_result
    )
    return response["result"]["data"][0]

class VideoStorage(ACCloud):
  def __init__(self) -> None:
    super().__init__(
      bucket_name="video-backup.arjancodes.com",
      region="eu-west-1c",
    )
```

The code extends the capability of CloudProvider by using two inheritance layers: one layer to add a convenience method for finding files, and one layer to create a default video storage access point for ACCloud.

The problem with all these layers of inheritance is that the code becomes hard to read. Also, there are simpler solutions than inheritance if you just want to define a few default arguments. This is the case with the VideoStorage class, which does only that and nothing else. In many cases, composition offers a simpler solution than inheritance.

a) Refactor this code so that it no longer uses inheritance, but relies on composition instead.

b) Refactor the code once more so that find_files is no longer dependent on the cloudengine package.