import audiosegment
import numpy as np


def audiosegment_to_librosawav(audio_segment):
    channel_sounds = audio_segment.split_to_mono()
    return channels_to_librosawav(channel_sounds)


def channels_to_librosawav(channel_sounds):
    samples = [s.get_array_of_samples() for s in channel_sounds]

    fp_arr = np.array(samples).T.astype(np.float32)
    fp_arr /= np.iinfo(samples[0].typecode).max
    fp_arr = fp_arr.reshape(-1)

    return fp_arr
