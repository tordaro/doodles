from dataclasses import dataclass
from typing import Protocol


class AuthProvider(Protocol):
    def retrieve_credentials(self) -> str:
        ...


class ServiceProvider(Protocol):
    def connect(self, credentials: str) -> None:
        ...

    def get_context(self) -> str:
        ...


class StoreManager(Protocol):
    def initialize(self, contect) -> None:
        ...


@dataclass
class CloudService:
    auth_provider: AuthProvider
    service: ServiceProvider
    storage_manager: StoreManager

    def connect(self) -> None:
        print("Connecting to the cloud service.")
        credentials = self.auth_provider.retrieve_credentials()
        self.service.connect(credentials)
        context = self.service.get_context()
        self.storage_manager.initialize(context)
        print("Cloud service connected.")
