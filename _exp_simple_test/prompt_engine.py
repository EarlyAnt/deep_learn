import random
from collections import namedtuple

SettingParam = namedtuple(
    "SettingParam", "steps, skip_steps, clip_guidance_scale, cutn_batches, cut_ic_pow, eta, clamp_max")

StyleConfig = namedtuple("StyleConfig", "artists, prefix")

# 5种风格
# 01-中国风
# 02-3D渲染
# 03-超现实主义
# 04-cg幻想
# 05-现代插画


class PromptEngine:
    _artist_list = {'0101': '',
                    '0201': 'Aka mike winkelman',
                    '0202': 'Raphael Lacoste',
                    '0301': 'Jacek Yerka',
                    '0302': 'Rene Magritte',
                    '0303': 'Igor Morski',
                    '0304': 'Andre Breton',
                    '0401': 'Simon Stalenhag',
                    '0402': 'Ross Tran',
                    '0403': 'Liam Wong',
                    '0404': 'Thomas Kinkade',
                    '0405': 'John Harris',
                    '0501': 'Pascal Campion',
                    '0502': 'Atey Ghailan',
                    '0503': 'Tatsuro Kiuchi'}

    _style_list = {0: None,
                   1: StyleConfig(artists=['0101'], prefix='A beautiful Chinese ink'),
                   2: StyleConfig(artists=['0201', '0202'], prefix='A beautiful VR 3D painting by '),
                   3: StyleConfig(artists=['0301', '0302', '0303', '0304'], prefix='A picture by '),
                   4: StyleConfig(artists=['0401', '0402', '0403', '0404', '0405'], prefix='A image by '),
                   5: StyleConfig(artists=['0501', '0502', '0503'], prefix='A modern picture by ')}

    _style_key_word = {
        0: None,
        1: None,
        2: 'Unreal Engine',
        3: None,
        4: None,
        5: None
    }

    _rule_list = {}
    _rule_list["0101"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0201"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0202"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0301"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0302"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0303"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0304"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0401"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0402"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0403"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0404"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0405"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0501"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0502"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)
    _rule_list["0503"] = SettingParam(
        steps=150, skip_steps=20, clip_guidance_scale=10000, cutn_batches=2, cut_ic_pow=10, eta=0.1, clamp_max=0.09)

    def _get_suffix(self, key_word):
        if key_word is not None:
            return "{}, Trending on artstation.".format(key_word)
        else:
            return 'Trending on artstation.'

    def get_rule(self, style):
        print("get_rule->style: {}".format(style))
        selected_style = self._style_list[style]
        if selected_style is not None and len(selected_style.artists) > 0:
            artists_list = selected_style.artists
            print("get_rule->artists_list: {}".format(artists_list))
            index = random.randint(0, len(artists_list) - 1)
            print("get_rule->index: {}".format(index))
            artist_code = artists_list[index]
            print("get_rule->artist_code: {}".format(artist_code))
            rule = self._rule_list[artist_code]
            print("get_rule->rule: {}".format(rule))
            return rule
        else:
            print("get_rule->none rule")
            return None

    def make_sentense(self, text_prompt, style):
        print("make_sentense->text_prompt: {}".format(text_prompt))
        print("make_sentense->style: {}".format(style))
        styleObject = self._style_list[style]
        artist = ''
        key_word = ''
        if styleObject is not None and len(styleObject.artists) > 0:
            artists_list = styleObject.artists
            print("make_sentense->artists_list: {}".format(artists_list))
            index = random.randint(0, len(artists_list) - 1)
            print("make_sentense->index: {}".format(index))
            artist_code = artists_list[index]
            print("make_sentense->artist_code: {}".format(artist_code))
            artist = self._artist_list[artist_code]
            print("make_sentense->artist: {}".format(artist))
            key_word = self._style_key_word[style]
            print("make_sentense->key_word: {}".format(key_word))
            sentence = "{}{}, {}. {}".format(
                styleObject.prefix, artist, text_prompt, self._get_suffix(key_word))
        else:
            sentence = text_prompt
        print("make_sentense->full prompt: {}".format(sentence))
        return sentence


if __name__ == "__main__":
    test_style = 2

    prompt_engine = PromptEngine()

    sentence = prompt_engine.make_sentense(
        text_prompt="a group of small animals are feeding, playing and resting on the grass", style=test_style)
    print("main->sentence: {}".format(sentence))

    rule = prompt_engine.get_rule(style=test_style)
    if rule is None:
        print("main->rule: {}".format(rule))
    else:
        print("main->rule.step: {}".format(rule.steps))
