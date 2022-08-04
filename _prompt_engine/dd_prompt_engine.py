import random
from collections import namedtuple
from base_prompt_engine import BasePromptEngine

SettingParam = namedtuple(
    "SettingParam", "steps, skip_steps, clip_guidance_scale, cutn_batches, cut_ic_pow, eta, clamp_max")

Artist = namedtuple("Artist", "name, enable")

SentencePattern = namedtuple(
    "SentencePattern", "prefix, artist_code_prefix, key_word, suffix")

FullSettingPara = namedtuple(
    "FullSettingPara", """RN101, RN50, RN50x16, RN50x4, RN50x64, ViTB16, ViTB32, ViTL14, angle, clamp_grad, clamp_max, 
                          clip_denoised, clip_guidance_scale, cut_ic_pow, cut_icgray_p, cut_innercut, cut_overview, cutn_batches, 
                          diffusion_model, diffusion_sampling_mode, diffusion_steps, eta, extract_nth_frame, 
                          far_plane, fov, frames_scale, frames_skip_steps, fuzzy_prompt, height, image_prompts, 
                          init_image, init_scale, interp_spline, key_frames, max_frames, midas_depth_model, midas_weight, 
                          near_plane, padding_mode, perlin_init, perlin_mode, rand_mag, randomize_class, range_scale, 
                          rotation_3d_x, rotation_3d_y, rotation_3d_z, sampling_mode, sat_scale, seed, skip_augs, skip_steps, steps, 
                          text_prompts, translation_x, translation_y, translation_z, turbo_mode, turbo_preroll, turbo_steps, tv_scale, 
                          use_secondary_model, video_init_path, video_init_seed_continuity, width, zoom""")


class DDPromptEngine(BasePromptEngine):
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

    def _get_full_setting_param(self):
        fullSettingParam = FullSettingPara(RN101=True, RN50=False, RN50x16=False, RN50x4=False, RN50x64=False, ViTB16=True,
                                           ViTB32=True, ViTL14=False, angle="0:(0)", clamp_grad=True, clamp_max=0.09,
                                           clip_denoised=False, clip_guidance_scale=5000, cut_ic_pow=10,
                                           cut_icgray_p="[0.2]*400+[0]*600", cut_innercut="[4]*400+[12]*600", cut_overview="[12]*400+[4]*600",
                                           cutn_batches=2, diffusion_model="512x512_diffusion_uncond_finetune_008100",
                                           diffusion_sampling_mode="ddim", diffusion_steps=900, eta=1, extract_nth_frame=2, far_plane=10000,
                                           fov=40, frames_scale=1500, frames_skip_steps="60%", fuzzy_prompt=False, height=1024, image_prompts={},
                                           init_image=None, init_scale=1000, interp_spline="Linear", key_frames=True, max_frames=1,
                                           midas_depth_model="dpt_large", midas_weight=0.3, near_plane=200, padding_mode="border",
                                           perlin_init=False, perlin_mode="mixed", rand_mag=0.05, randomize_class=True, range_scale=150,
                                           rotation_3d_x="0: (0)", rotation_3d_y="0: (0)", rotation_3d_z="0: (0)", sampling_mode="bicubic",
                                           sat_scale=0, seed=2271945961, skip_augs=False, skip_steps=20, steps=150, text_prompts={
                                               "0": [
                                                   "Emerald Birds standing in Maogu"
                                               ],
                                               "100": [
                                                   "This set of prompts start at frame 100",
                                                   "This prompt has weight five:5"
                                               ]
                                           }, translation_x="0: (0)", translation_y="0: (0)", translation_z="0: (10.0)",
                                           turbo_mode=False, turbo_preroll=10, turbo_steps="3", tv_scale=0, use_secondary_model=True,
                                           video_init_path="training.mp4", video_init_seed_continuity=True, width=768, zoom="0: (1), 10: (1.05)")
        return fullSettingParam

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

    def get_generation_config(self, text_prompt, style):
        print("get_generate_config->text_prompt: {}".format(text_prompt))
        print("get_generate_config->style: {}".format(style))

        rule = None
        artist_name = ''
        key_word = ''
        sentence = text_prompt
        sentence_pattern = self._sentence_pattern_list[style]
        print("get_generate_config->sentence_pattern: {}".format(sentence_pattern))

        fullSettingParam = self._get_full_setting_param()

        if sentence_pattern is not None:
            artists_list = self._get_artist_list(
                code_prefix=sentence_pattern.artist_code_prefix)
            if artists_list != None and len(artists_list) > 0:
                print("get_generate_config->artists_list: {}".format(artists_list))
                index = random.randint(0, len(artists_list) - 1)
                print("get_generate_config->index: {}".format(index))
                artist = artists_list[index]
                print("get_generate_config->artist_code: {}".format(artist[0]))
                artist_name = artist[1].name
                print("get_generate_config->artist_name: {}".format(artist_name))
                key_word = sentence_pattern.key_word
                print("get_generate_config->key_word: {}".format(key_word))
                sentence = "{}{}, {}. {}".format(
                    sentence_pattern.prefix, artist_name, text_prompt, self._get_suffix(sentence_pattern))
                rule = self._rule_list[artist[0]]

                fullSettingParam.text_prompts["0"] = [sentence]
                fullSettingParam._replace(steps = rule.steps)
                fullSettingParam._replace(skip_steps = rule.skip_steps)
                fullSettingParam._replace(clip_guidance_scale = rule.clip_guidance_scale)
                fullSettingParam._replace(cutn_batches = rule.cutn_batches)
                fullSettingParam._replace(cut_ic_pow = rule.cut_ic_pow)
                fullSettingParam._replace(eta = rule.eta)
                fullSettingParam._replace(clamp_max = rule.clamp_max)
            else:
                sentence = "{}, {}. {}".format(
                    sentence_pattern.prefix, text_prompt, self._get_suffix(sentence_pattern))

        print("get_generate_config->full prompt: {}".format(sentence))
        print("get_generate_config->rule: {}".format(rule))
        print("get_generate_config->full setting params: {}".format(fullSettingParam))

        return fullSettingParam


if __name__ == "__main__":
    test_style = 5

    prompt_engine = DDPromptEngine()

    fullSettingParam = prompt_engine.get_generation_config(
        text_prompt="a group of small animals are feeding, playing and resting on the grass", style=test_style)
    print("main->sentence: {}".format(fullSettingParam.text_prompts))
    print("main->steps: {}".format(fullSettingParam.steps))
