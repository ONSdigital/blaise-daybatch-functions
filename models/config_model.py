import os

from dataclasses import dataclass


@dataclass
class Config:
    blaise_server_park: str
    blaise_api_url: str

    @classmethod
    def from_env(cls):
        return cls(
            blaise_server_park=os.getenv("BLAISE_SERVER_PARK"),
            blaise_api_url=os.getenv("BLAISE_API_URL"),
        )

    def log(self):
        print(f"Configuration - blaise_server_park: {self.blaise_server_park}")
        print(f"Configuration - blaise_api_url: {self.blaise_api_url}")
