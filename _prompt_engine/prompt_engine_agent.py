from dd_prompt_engine import DDPromptEngine
from dlm_prompt_engine import DLMPromptEngine


class PromptEngineAgent:
    @classmethod
    def get_generation_config(self, agent_name, text_prompt, style):
        switch = {
            'dd_01': DDPromptEngine.get_generation_config(text_prompt=text_prompt, style=style),
            'dlm_01': DLMPromptEngine.get_generation_config(text_prompt=text_prompt, style=style)
        }
        return switch.get(agent_name)


if __name__ == "__main__":
    fullSettingParam = PromptEngineAgent.get_generation_config(
        "dd_01", "a group of small animals are feeding, playing and resting on the grass", 2)
    print("main->sentence: {}".format(fullSettingParam.text_prompts))
    print("main->steps: {}".format(fullSettingParam.steps))
