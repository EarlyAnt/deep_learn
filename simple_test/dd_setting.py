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

artist_list = {'0101': 'Chinese ink painting',
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

style_list = {0: None,
              1: StyleConfig(artists=['0101'], prefix='A beautiful Chinese ink'),
              2: StyleConfig(artists=['0201', '0202', '0203'], prefix='A beautiful VR 3D painting by '),
              3: StyleConfig(artists=['0301', '0302', '0303'], prefix='A picture by '),
              4: StyleConfig(artists=['0401', '0402', '0403', '0404'], prefix='A image by '),
              5: StyleConfig(artists=['0501'], prefix='A modern picture by ')}

rule_list = {}
rule_list["0101"] = SettingParam(
    steps=200, skip_steps=20, clip_guidance_scale=13000, cutn_batches=2)
rule_list["0201"] = SettingParam(
    steps=250, skip_steps=20, clip_guidance_scale=10000, cutn_batches=4)
rule_list["0202"] = SettingParam(
    steps=250, skip_steps=20, clip_guidance_scale=10000, cutn_batches=4)
rule_list["0203"] = SettingParam(
    steps=250, skip_steps=20, clip_guidance_scale=10000, cutn_batches=4)
rule_list["0301"] = SettingParam(
    steps=200, skip_steps=20, clip_guidance_scale=13000, cutn_batches=2)
rule_list["0302"] = SettingParam(
    steps=200, skip_steps=20, clip_guidance_scale=13000, cutn_batches=2)
rule_list["0303"] = SettingParam(
    steps=200, skip_steps=20, clip_guidance_scale=13000, cutn_batches=2)
rule_list["0401"] = SettingParam(
    steps=150, skip_steps=10, clip_guidance_scale=10000, cutn_batches=4)
rule_list["0402"] = SettingParam(
    steps=150, skip_steps=10, clip_guidance_scale=10000, cutn_batches=4)
rule_list["0403"] = SettingParam(
    steps=150, skip_steps=10, clip_guidance_scale=10000, cutn_batches=4)
rule_list["0404"] = SettingParam(
    steps=150, skip_steps=10, clip_guidance_scale=10000, cutn_batches=4)
rule_list["0501"] = SettingParam(
    steps=200, skip_steps=20, clip_guidance_scale=13000, cutn_batches=2)


def get_suffix():
    return 'Trending on artstation.'

def get_setting(style_code):
    print("get_setting->style_code: {}".format(style_code))
    style = style_list[style_code]
    if style is not None and len(style.artists) > 0:
        print("get_setting->style: {}".format(style))
        artists_list = style.artists
        print("get_setting->artists_list: {}".format(artists_list))
        index = random.randint(0, len(artists_list) - 1)
        print("get_setting->index: {}".format(index))
        artist = artists_list[index]
        print("get_setting->artist: {}".format(artist))

        setting_param = rule_list[artist]
        print("get_setting->setting_param: {}".format(setting_param))
        return setting_param
    else:
        print("get_setting->none artist")
        return None

def make_image(text_prompt, style):
    print("make_image->start ================================================")

    print("make_image->text_prompt: {}".format(text_prompt))
    print("make_image->style: {}".format(style))
    style = style_list[style]
    artist = ''
    if style is not None and len(style.artists) > 0:
        artists_list = style.artists
        print("make_image->artists_list: {}".format(artists_list))
        index = random.randint(0, len(artists_list) - 1)
        print("make_image->index: {}".format(index))
        artist_code = artists_list[index]
        print("make_image->artist_code: {}".format(artist_code))
        artist = artist_list[artist_code]
        print("make_image->artist: {}".format(artist))

    print("make_image->full prompt: {}{}, {}. {}".format(style.prefix,
          artist, text_prompt, get_suffix()))

    print("make_image->complete ---------------------------------------------")


if __name__ == "__main__":
    get_setting(style_code=4)

    make_image(
        text_prompt="a group of small animals are feeding, playing and resting on the grass", style=3)
