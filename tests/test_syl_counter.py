from elan_parser.syllable_counter import get_syllable_count_from_eaf


def test_get_syllable_count_from_eaf():
    eaf_file = "tests/data/test.eaf"
    delimiters=['་', '།']
    total_syllables = get_syllable_count_from_eaf(eaf_file, delimiters)
    assert total_syllables == 42
