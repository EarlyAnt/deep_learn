import random
from collections import namedtuple

SettingParam = namedtuple(
    "SettingParam", "steps, skip_steps, clip_guidance_scale, cutn_batches, cut_ic_pow, eta, clamp_max")

Artist = namedtuple("Artist", "name, enable")

SentencePattern = namedtuple(
    "SentencePattern", "prefix, artist_code_prefix, key_word, suffix")

# 6种风格
# 0-无(其他)
# 1-中国风
# 2-3D渲染
# 3-超现实主义
# 4-cg幻想
# 5-现代插画


class PromptEngine:
    _artist_list = {'0101': None,
                    '0201': Artist(name='Aka mike winkelman', enable=True),
                    '0202': Artist(name='Raphael Lacoste', enable=True),
                    '0301': Artist(name='Jacek Yerka', enable=True),
                    '0302': Artist(name='Rene Magritte', enable=True),
                    '0303': Artist(name='Igor Morski', enable=True),
                    '0304': Artist(name='Andre Breton', enable=True),
                    '0401': Artist(name='Simon Stalenhag', enable=True),
                    '0402': Artist(name='Ross Tran', enable=True),
                    '0403': Artist(name='Liam Wong', enable=True),
                    '0404': Artist(name='Thomas Kinkade', enable=True),
                    '0405': Artist(name='John Harris', enable=True),
                    '0501': Artist(name='Pascal Campion', enable=True),
                    '0502': Artist(name='Atey Ghailan', enable=True),
                    '0503': Artist(name='Tatsuro Kiuchi', enable=True)}

    _sentence_pattern_list = {0: None,
                              1: SentencePattern(prefix='A beautiful Chinese Shanshui painting', artist_code_prefix='01', key_word=None, suffix='Trending on artstation.'),
                              2: SentencePattern(prefix='A beautiful VR 3D painting by ', artist_code_prefix='02', key_word='Unreal Engine, 3d real-time rendering, 4k, high-definitio', suffix='Trending on artstation.'),
                              3: SentencePattern(prefix='A picture by ', artist_code_prefix='03', key_word=None, suffix='Trending on artstation.'),
                              4: SentencePattern(prefix='A image by ', artist_code_prefix='04', key_word=None, suffix='Trending on artstation.'),
                              5: SentencePattern(prefix='A modern picture by ', artist_code_prefix='05', key_word=None, suffix='Trending on artstation.')}

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

    def _get_suffix(self, sentence_pattern):
        if sentence_pattern.key_word is not None:
            return "{}, Trending on artstation.".format(sentence_pattern.key_word)
        else:
            return 'Trending on artstation.'

    def _get_artist_list(self, code_prefix):
        artist_list = []
        for item in self._artist_list.items():
            if item[0].startswith(code_prefix) and item[1] != None and item[1].enable == True:
                artist_list.append(item)
        return artist_list

    def get_rule(self, style):
        print("get_rule->style: {}".format(style))
        sentence_pattern = self._sentence_pattern_list[style]
        if sentence_pattern is not None:
            artists_list = self._get_artist_list(
                code_prefix=sentence_pattern.artist_code_prefix)
            if artists_list != None and len(artists_list) > 0:
                print("get_rule->artists_list: {}".format(artists_list))
                index = random.randint(0, len(artists_list) - 1)
                print("get_rule->index: {}".format(index))
                artist = artists_list[index]
                print("get_rule->artist_code: {}".format(artist[0]))
                rule = self._rule_list[artist[0]]
                print("get_rule->rule: {}".format(rule))
                return rule

        print("get_rule->none rule")
        return None

    def make_sentense(self, text_prompt, style):
        print("make_sentense->text_prompt: {}".format(text_prompt))
        print("make_sentense->style: {}".format(style))
        sentence = text_prompt
        sentence_pattern = self._sentence_pattern_list[style]
        print("make_sentense->sentence_pattern: {}".format(sentence_pattern))
        artist_name = ''
        key_word = ''
        if sentence_pattern is not None:
            artists_list = self._get_artist_list(
                code_prefix=sentence_pattern.artist_code_prefix)
            if artists_list != None and len(artists_list) > 0:
                print("make_sentense->artists_list: {}".format(artists_list))
                index = random.randint(0, len(artists_list) - 1)
                print("make_sentense->index: {}".format(index))
                artist = artists_list[index]
                print("make_sentense->artist_code: {}".format(artist[0]))
                artist_name = artist[1].name
                print("make_sentense->artist_name: {}".format(artist_name))
                key_word = sentence_pattern.key_word
                print("make_sentense->key_word: {}".format(key_word))
                sentence = "{}{}, {}. {}".format(
                    sentence_pattern.prefix, artist_name, text_prompt, self._get_suffix(sentence_pattern))
            else:
                sentence = "{}, {}. {}".format(
                    sentence_pattern.prefix, text_prompt, self._get_suffix(sentence_pattern))

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
