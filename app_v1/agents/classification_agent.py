from typing import Sequence

from autogen_agentchat.agents import BaseChatAgent
from autogen_agentchat.base import Response
from autogen_agentchat.messages import BaseChatMessage, TextMessage
from autogen_core import CancellationToken
from langchain_core.prompts import PromptTemplate

from app_v1.agents.helpers import call_llm_with_retry
from app_v1.llm.llm_manager import LLMManager

llm_manager = LLMManager()

class ClassificationAgent(BaseChatAgent):

    async def on_messages(self, messages: Sequence[BaseChatMessage], cancellation_token: CancellationToken) -> Response:

        result = classify(messages)
        return Response(
            chat_message = TextMessage(content=result, source = self.name)
        )

    def __init__(self, name: str):
        super().__init__(name, description = "Classification agent that classifies the post content")

    @property
    def produced_message_types(self) -> Sequence[type[BaseChatMessage]]:
        return TextMessage,

    async def on_reset(self, cancellation_token: CancellationToken) -> None:
        pass



async def classify(post_data:str )-> Response:

    llm_model = llm_manager.get_classification_model()
    template = PromptTemplate(
        input_variables=["data"],
        template = llm_model.get_post_classification_template(),
    )
    prompt = template.format(data = post_data)

    try:
        messages = [
            {"role":"system", "content": " you are a post classification expert"},
            {"role":"user", "content": prompt}

        ]

        client = llm_model.initialize_model()
        result = call_llm_with_retry(client= client, llm_model=llm_model, response_model=Response,
                            messages=messages, agent_name = llm_model.get_model_name(), method_name = "classify")

        result_dict = result.model_dump()
        #TODO: extract required output
        return result_dict

    except Exception as e:
        #TODO: handled each error( Retry and others) accordingly
        raise e

