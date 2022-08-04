import random

# 6种风格
# 0-无(其他)
# 1-中国风
# 2-3D渲染
# 3-超现实主义
# 4-cg幻想
# 5-现代插画


class BasePromptEngine:
    def get_generation_config(self, text_prompt, style):
        print("need to overwrite !!!")
        print("BasePromptEngine.get_generation_config->text prompt: {}, style: {}".format(text_prompt, style))
        return None


if __name__ == "__main__":
    test_style = 5

    prompt_engine = BasePromptEngine()
    prompt_engine.get_generation_config(text_prompt="抽象方法不执行任何逻辑", style=0)
