from rapidfuzz import fuzz
from ner_evaluator.utils import *


class NerEvaluator:
    def count_matched(
        self, true_entities: tuple, predictions: tuple, label: list
    ) -> tuple:
        """
        This function counts the number of matched entities for a given label.
        To be considered as matched, the entities must share the same start,end,label and text.
        """
        matched = 0

        # Filter by label
        filtered_entities = filter_entities_by_label(true_entities, label)
        filtered_pred = filter_entities_by_label(predictions, label)

        # Try to match the entities and generate a list with matched entities
        matched_entities = []
        for i, v in enumerate(filtered_pred):
            if v in filtered_entities:
                matched += 1
                matched_entities.append(v)

        # Remove the matched entities from the lists
        [
            (filtered_entities.remove(r), filtered_pred.remove(r))
            for r in matched_entities
        ]
        print("\n{} full matches.".format(matched))

        return matched, filtered_entities, filtered_pred

    def get_close_matches(
        self, filtered_entities: list, filtered_pred: list, threshold: float
    ):
        """
        This function counts the number of close matches under a given threshold.
        It compares the entities by their text and returns the number of close matches and the number of wrong matches.
        """

        # Calculate the similarity between the predicted and true entities
        similarities = list(
            map(
                fuzz.token_set_ratio,
                sum([[pred[3]] * len(filtered_entities) for pred in filtered_pred], []),
                [ent[3] for ent in filtered_entities] * len(filtered_pred),
            )
        )

        # Calculate the number of close matches and the number of wrong matches
        correct = len([x for x in sorted(similarities) if x >= threshold])
        wrong = len(filtered_pred) - correct if len(filtered_pred) - correct > 0 else 0
        print(
            "{0} entities matched within the threshold and {1} didn't match.".format(
                correct, wrong
            )
        )
        return correct, wrong

    def evaluate(
        self,
        true_entities: tuple,
        predictions: tuple,
        labels: list,
        threshold: float = 0.85,
    ):
        """
        This function controls the evaluation process running the count_matched and get_close_matches functions.
        Both true_entities and predictions must be tuples with the following structure:
        (START_TOKEN, END_TOKEN, LABEL, ENTITITY_TEXT)
        e.g.: (890, 910, 'SKILL', "utilisation d'un CMS")
        """

        results = {}
        for label in labels:
            print("Label: {}".format(label))
            matched, filtered_entities, filtered_pred = self.count_matched(
                true_entities, predictions, label
            )
            correct, wrong = self.get_close_matches(
                filtered_entities, filtered_pred, threshold * 100
            )

            tp = matched + correct
            fp = wrong
            fn = len(filter_entities_by_label(predictions, label)) - tp

            precision, recall, f1_score = calculate_scores(tp, fp, fn)
            results[label] = {
                "precision": precision,
                "recall": recall,
                "f1_score": f1_score,
            }
            print("{} missed entitie(s)".format(fn))
            print("\n")
        return results
