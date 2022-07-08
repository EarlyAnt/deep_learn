import random
from collections import namedtuple

SettingParam = namedtuple(
    "SettingParam", "steps, skip_steps, clip_guidance_scale, cutn_batches")

StyleConfig = namedtuple("StyleConfig", "artists, prefix")

# 5种风格
# 01-中国风
# 02-3D渲染
# 03-超现实主义
# 04-cg幻想
# 05-现代插画


class PromptEngine:
    _artist_list = {'0101': 'Chinese ink painting',
                    '0201': 'Aka mike winkelman',
                    '0202': 'high-definition',
                    '0203': 'Unreal Engine',
                    '0301': 'Jacek Yerka',
                    '0302': 'Rene Magritte',
                    '0303': 'Igor Morski',
                    '0401': 'Simon Stalenhag',
                    '0402': 'Ross Tran',
                    '0403': 'Liam WongJohn Harris',
                    '0404': 'Thomas Kinkade',
                    '0501': 'Pascal Campion'}

    _style_list = {0: None,
                   1: StyleConfig(artists=['0101'], prefix='A beautiful Chinese ink'),
                   2: StyleConfig(artists=['0201', '0202', '0203'], prefix='A beautiful VR 3D painting by '),
                   3: StyleConfig(artists=['0301', '0302', '0303'], prefix='A picture by '),
                   4: StyleConfig(artists=['0401', '0402', '0403', '0404'], prefix='A image by '),
                   5: StyleConfig(artists=['0401', '0402', '0403', '0404'], prefix='A modern picture by ')}

    _rule_list = {}
    _rule_list["0101"] = SettingParam(
        steps=250, skip_steps=25, clip_guidance_scale=8000, cutn_batches=4)
    _rule_list["0201"] = SettingParam(
        steps=250, skip_steps=20, clip_guidance_scale=10000, cutn_batches=4)
    _rule_list["0202"] = SettingParam(
        steps=250, skip_steps=20, clip_guidance_scale=10000, cutn_batches=4)
    _rule_list["0203"] = SettingParam(
        steps=250, skip_steps=20, clip_guidance_scale=10000, cutn_batches=4)
    _rule_list["0301"] = SettingParam(
        steps=200, skip_steps=20, clip_guidance_scale=13000, cutn_batches=2)
    _rule_list["0302"] = SettingParam(
        steps=200, skip_steps=20, clip_guidance_scale=13000, cutn_batches=2)
    _rule_list["0303"] = SettingParam(
        steps=200, skip_steps=20, clip_guidance_scale=13000, cutn_batches=2)
    _rule_list["0401"] = SettingParam(
        steps=150, skip_steps=10, clip_guidance_scale=10000, cutn_batches=4)
    _rule_list["0402"] = SettingParam(
        steps=150, skip_steps=10, clip_guidance_scale=10000, cutn_batches=4)
    _rule_list["0403"] = SettingParam(
        steps=150, skip_steps=10, clip_guidance_scale=10000, cutn_batches=4)
    _rule_list["0404"] = SettingParam(
        steps=150, skip_steps=10, clip_guidance_scale=10000, cutn_batches=4)
    _rule_list["0501"] = SettingParam(
        steps=200, skip_steps=20, clip_guidance_scale=13000, cutn_batches=2)

    def _get_suffix(self):
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
        style = self._style_list[style]
        artist = ''
        if style is not None and len(style.artists) > 0:
            artists_list = style.artists
            print("make_sentense->artists_list: {}".format(artists_list))
            index = random.randint(0, len(artists_list) - 1)
            print("make_sentense->index: {}".format(index))
            artist_code = artists_list[index]
            print("make_sentense->artist_code: {}".format(artist_code))
            artist = self._artist_list[artist_code]
            print("make_sentense->artist: {}".format(artist))
            sentence = "{}{}, {}. {}".format(
                style.prefix, artist, text_prompt, self._get_suffix())
        else:
            sentence = text_prompt
        print("make_sentense->full prompt: {}".format(sentence))
        return sentence


if __name__ == "__main__":
    test_style = 0

    prompt_engine = PromptEngine()

    sentence = prompt_engine.make_sentense(
        text_prompt="a group of small animals are feeding, playing and resting on the grass", style=test_style)
    print("main->sentence: {}".format(sentence))

    rule = prompt_engine.get_rule(style=test_style)
    if rule is None:
        print("main->rule: {}".format(rule))
    else:
        print("main->rule.step: {}".format(rule.steps))
