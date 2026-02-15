from app_v1.agents.agent_constants import AgentNames
from app_v1.agents.classification_agent import ClassificationAgent


class ClassificationService:


    def classify(self ):

        classification_agent = ClassificationAgent(AgentNames.CLASSIFICATION_AGENT)
