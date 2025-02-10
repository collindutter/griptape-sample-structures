from griptape.structures import Agent
from griptape.utils import GriptapeCloudStructure

with GriptapeCloudStructure(observe=True):
    Agent(stream=True).run("What is 2 + 2")
