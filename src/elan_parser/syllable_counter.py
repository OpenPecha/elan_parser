import re
from pympi.Elan import Eaf


def get_syllable_count(text, delimiters):
    """Return the number of syllables in a text."""
    pattern = '|'.join(map(re.escape, delimiters))
    syls = re.split(pattern, text)
    return len(syls)

def get_syllable_count_from_eaf(eaf_file, delimiters):
    """Return the number of syllables in a eaf"""
    eaf = Eaf(eaf_file)
    total_syllables = 0

    for tier_name in eaf.get_tier_names():
        tier = eaf.get_annotation_data_for_tier(tier_name)
        for annotation in tier:
            if annotation[2] != "":
                text = annotation[2]
                syl_count = get_syllable_count(text, delimiters)
                total_syllables += syl_count
    return total_syllables