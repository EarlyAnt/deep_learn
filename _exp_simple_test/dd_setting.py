import random
from collections import namedtuple

SettingParam = namedtuple(
    "SettingParam", "display_rate, n_batches, batch_size, steps, skip_steps, cut_overview, cut_innercut, cut_ic_pow, cut_icgray_p")

StyleConfig = namedtuple("StyleConfig", "artists, prefix")

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
              5: StyleConfig(artists=['0401', '0402', '0403', '0404'], prefix='A modern picture by ')}

rule_list = {}
rule_list["0101"] = SettingParam(
    display_rate=1, n_batches=1, batch_size=1, steps=1, skip_steps=1, cut_overview=1, cut_innercut=1, cut_ic_pow=1, cut_icgray_p=1)
rule_list["0201"] = SettingParam(
    display_rate=2, n_batches=2, batch_size=2, steps=2, skip_steps=2, cut_overview=2, cut_innercut=2, cut_ic_pow=2, cut_icgray_p=2)
rule_list["0202"] = SettingParam(
    display_rate=3, n_batches=3, batch_size=3, steps=3, skip_steps=3, cut_overview=3, cut_innercut=3, cut_ic_pow=3, cut_icgray_p=3)
rule_list["0203"] = SettingParam(
    display_rate=4, n_batches=4, batch_size=4, steps=4, skip_steps=4, cut_overview=4, cut_innercut=4, cut_ic_pow=4, cut_icgray_p=4)


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
    # get_setting(style_code=2)

    make_image(
        text_prompt="a group of small animals are feeding, playing and resting on the grass", style=2)
