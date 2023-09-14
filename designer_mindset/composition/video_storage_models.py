from cloudengine import CloudProvider
from cloudengine.google import GoogleAuth
from dataclasses import dataclass

REGION = "eu-west-1c"
BUCKET = "video-backup.arjancodes.com"


@dataclass
class ACCloud:
    cloud_provider: CloudProvider
    bucket_name: str

    def find_files(self, query: str, max_result: int) -> list[str]:
        response = self.cloud_provider.filter_by_query(bucket=self.bucket_name, query=query, max=max_result)
        return response["result"]["data"][0]


def create_cloud_provider(region: str = REGION, bucket_name=BUCKET) -> ACCloud:
    authentication = GoogleAuth("service_key.json")
    cloud = CloudProvider(region=region, http_auth=authentication, secure=True)
    return ACCloud(cloud_provider=cloud, bucket_name=bucket_name)


def find_files(
    cloud_provider: CloudProvider,
    bucket_name: str,
    query: str,
    max_result: int,
) -> list[str]:
    """Function to avoid ACCloud entirely."""
    response = cloud_provider.filter_by_query(bucket=bucket_name, query=query, max=max_result)
    return response["result"]["data"][0]
