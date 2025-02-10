from griptape.structures import Agent
from griptape.utils import GriptapeCloud

with GriptapeCloud(observe=True):
    Agent(stream=True).run("What is 2 + 2")
