from app.llm.llm_model import LLMModel


class GPT51Model(LLMModel):

    def initialize_model(self, temperature: int = 0):
        return


    def get_post_classification_template(self):
        return