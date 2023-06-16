from elan_parser.annotation_time import calculate_total_time_annotated


def test_calculate_total_time_annotated():
    eaf_file = "tests/data/test.eaf"
    total_time_annotated = calculate_total_time_annotated(eaf_file)
    assert total_time_annotated == 0.8144166666666667


