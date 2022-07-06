import random
from collections import namedtuple

artists = {'0101': 'Chinese ink painting',
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

styles = {0: [],
          1: ['0101'],
          2: ['0201', '0202', '0203'],
          3: ['0301', '0302', '0303'],
          4: ['0401', '0402', '0403', '0404']}

SettingParam = namedtuple(
    "SettingParam", "display_rate, n_batches, batch_size, steps, skip_steps, cut_overview, cut_innercut, cut_ic_pow, cut_icgray_p")


def get_rules():
    rules = {}
    rules["0101"] = SettingParam(
        display_rate=1, n_batches=1, batch_size=1, steps=1, skip_steps=1, cut_overview=1, cut_innercut=1, cut_ic_pow=1, cut_icgray_p=1)
    rules["0201"] = SettingParam(
        display_rate=2, n_batches=2, batch_size=2, steps=2, skip_steps=2, cut_overview=2, cut_innercut=2, cut_ic_pow=2, cut_icgray_p=2)
    rules["0202"] = SettingParam(
        display_rate=3, n_batches=3, batch_size=3, steps=3, skip_steps=3, cut_overview=3, cut_innercut=3, cut_ic_pow=3, cut_icgray_p=3)
    rules["0203"] = SettingParam(
        display_rate=4, n_batches=4, batch_size=4, steps=4, skip_steps=4, cut_overview=4, cut_innercut=4, cut_ic_pow=4, cut_icgray_p=4)

    return rules


def get_setting(style):
    style_int = int(style)
    print("get_setting->style: {}".format(style_int))
    artists_list = styles[style_int]
    print("get_setting->artists_list: {}".format(artists_list))
    index = random.randint(0, len(artists_list) - 1)
    print("get_setting->index: {}".format(index))
    artist = artists_list[index]
    print("get_setting->artist: {}".format(artist))

    rules = get_rules()
    setting_param = rules[artist]
    print("get_setting->setting_param: {}".format(setting_param))
    return setting_param


def make_image(dd_setting):
    print("make_image->start ================================================")
    print("make_image->dd_setting: {}".format(dd_setting))
    print("make_image->complete ---------------------------------------------")


if __name__ == "__main__":
    setting_param = get_setting(style=2)
    make_image(setting_param)
