from collections import namedtuple
from base_prompt_engine import BasePromptEngine

SettingParam = namedtuple(
    "SettingParam", "steps, skip_steps, clip_guidance_scale, cutn_batches, cut_ic_pow, eta, clamp_max")

Artist = namedtuple("Artist", "name, enable")

SentencePattern = namedtuple(
    "SentencePattern", "prefix, artist_code_prefix, key_word, suffix")


class DLMPromptEngine(BasePromptEngine):
    _artist_list = {'0101': None,
                    '0102': Artist(name='Tatsuro Kiuchi', enable=True),
                    '0201': Artist(name='Aka mike winkelman', enable=True),
                    '0202': Artist(name='Raphael Lacoste', enable=True),
                    '0301': Artist(name='Jacek Yerka', enable=True),
                    '0302': Artist(name='Rene Magritte', enable=True),
                    '0401': Artist(name='Simon Stalenhag', enable=True),
                    '0402': Artist(name='Ross Tran', enable=True),
                    '0501': Artist(name='Pascal Campion', enable=True),
                    '0502': Artist(name='Atey Ghailan', enable=True)}

    _sentence_pattern_list = {0: None,
                              1: SentencePattern(prefix='A beautiful Chinese Shanshui painting', artist_code_prefix='01', key_word=None, suffix='Trending on artstation.'),
                              2: SentencePattern(prefix='A beautiful VR 3D painting by ', artist_code_prefix='02', key_word='Unreal Engine, 3d real-time rendering, 4k, high-definitio', suffix='Trending on artstation.'),
                              3: SentencePattern(prefix='A picture by ', artist_code_prefix='03', key_word=None, suffix='Trending on artstation.'),
                              4: SentencePattern(prefix='A image by ', artist_code_prefix='04', key_word=None, suffix='Trending on artstation.'),
                              5: SentencePattern(prefix='A modern picture by ', artist_code_prefix='05', key_word=None, suffix='Trending on artstation.')}

    _rule_list = {}
    _rule_list["0101"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0102"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0201"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0202"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0301"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0302"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0401"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0402"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0501"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0502"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)


if __name__ == "__main__":
    test_style = 2

    prompt_engine = DLMPromptEngine()

    sentence, rule = prompt_engine.get_generation_config(
        text_prompt="a group of small animals are feeding, playing and resting on the grass", style=test_style)
    print("main->sentence: {}".format(sentence))

    if rule is None:
        print("main->rule: {}".format(rule))
    else:
        print("main->rule.step: {}".format(rule.steps))
