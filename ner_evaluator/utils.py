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
        precision = round(tp / (tp + fp), 2)
    except ZeroDivisionError:
        precision = 0
    try:
        recall = round(tp / (tp + fn), 2)
    except ZeroDivisionError:
        recall = 0
    try:
        f1_score = round(2 * (precision * recall) / (precision + recall), 2)
    except ZeroDivisionError:
        f1_score = 0
    return precision, recall, f1_score

