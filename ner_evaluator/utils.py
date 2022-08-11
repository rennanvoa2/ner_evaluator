def filter_entities_by_label(entities: tuple, label: str) -> list:
    """
    This function filters the results by label.
    """
    return [ent for ent in entities if ent[2] == label]


def calculate_scores(tp: int, fp: int, fn: int) -> tuple:
    """
    This function calculates the precision,recall and f1_score.
    """
    try:

        precision = tp + fp and round(tp / (tp + fp), 2)
    except Exception as e:
        print(e)
        print("Tp: {}, Fp: {}, Fn: {}".format(tp, fp, fn))

    recall = tp + fn and round(tp / (tp + fn), 2)

    f1_score = precision + recall and round(2 * (precision * recall) / (precision + recall), 2)

    return precision, recall, f1_score

