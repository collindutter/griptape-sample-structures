from griptape.structures import Agent
from griptape.utils.griptape_cloud_utils import GriptapeCloudContext


@GriptapeCloudContext()
def run(args: str) -> None:
    Agent().run(args)


with GriptapeCloudContext():
    print("FOOOOOOOO")

run("Write a poem")
