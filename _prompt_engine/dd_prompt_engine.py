from base_prompt_engine import BasePromptEngine

class DDPromptEngine(BasePromptEngine):
    pass

if __name__ == "__main__":
    test_style = 5

    prompt_engine = DDPromptEngine()

    sentence, rule = prompt_engine.get_generation_config(
        text_prompt="a group of small animals are feeding, playing and resting on the grass", style=test_style)
    print("main->sentence: {}".format(sentence))

    if rule is None:
        print("main->rule: {}".format(rule))
    else:
        print("main->rule.step: {}".format(rule.steps))




