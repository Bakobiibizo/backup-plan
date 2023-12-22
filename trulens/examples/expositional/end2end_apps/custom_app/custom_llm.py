from time import sleep

from trulens_eval.tru_custom_app import instrument


class CustomLLM:

    def __init__(self, model: str = "derp"):
        self.model = model

    @instrument
    def generate(self, prompt: str):
        sleep(0.01)

        return f"herp {prompt[::-1]} derp"
