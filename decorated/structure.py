import sys
from griptape.structures import Agent
from griptape.utils import GriptapeCloudStructure

with GriptapeCloudStructure(observe=True):
    Agent(stream=True).run(*sys.argv[1:])
