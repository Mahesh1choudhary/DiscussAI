from app_v1.llm.llm_model import LLMModel
from typing import Any
from tenacity import retry, stop_after_attempt
from langchain_community.callbacks import get_openai_callback


def call_llm_with_retry(
        client:Any,
        llm_model:LLMModel,
        response_model:Any,
        messages:list,
        agent_name:str,
        method_name:str
) -> Any:
    retry_count = 3 # TODO: should be config driven
    total_attempts = retry_count + 1

    @retry(stop = stop_after_attempt(total_attempts))
    def _call_llm():
        try:
            return client.chat.completions.create(
                model=llm_model.get_model_name(),
                response_model=response_model,
                messages=messages,
                max_retries=0 # Disabling, handled by tenacity retry
            )
        except Exception as e:
            raise

    parsed_output = _call_llm()
    return parsed_output
