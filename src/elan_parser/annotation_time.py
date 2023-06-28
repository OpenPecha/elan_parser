from pympi.Elan import Eaf

def convert_milliseconds_to_minutes(milliseconds):
    minutes = milliseconds / (1000 * 60)
    return minutes

def calculate_total_time_annotated(eaf_file):
    eaf = Eaf(eaf_file)
    total_duration = 0.0

    tier_name = 'Transcription'
    try:
        tier = eaf.get_annotation_data_for_tier(tier_name)
    except:
        print("No transcription tier found")
        return total_duration
    for annotation in tier:
        if annotation[2] != "":
            start_time = annotation[0]
            end_time = annotation[1]
            duration = end_time - start_time
            total_duration += duration
    total_duration = convert_milliseconds_to_minutes(total_duration)
    return total_duration

def calculate_total_time_blank_segment(eaf_file):
    eaf = Eaf(eaf_file)
    total_duration = 0.0

    tier_name = 'Transcription'
    try:
        tier = eaf.get_annotation_data_for_tier(tier_name)
    except:
        print("No transcription tier found")
        return total_duration
    for annotation in tier:
        if annotation[2] == "":
            start_time = annotation[0]
            end_time = annotation[1]
            duration = end_time - start_time
            total_duration += duration
    total_duration = convert_milliseconds_to_minutes(total_duration)
    return total_duration
