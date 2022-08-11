from ner_evaluator import NerEvaluator

entities = [
    (795, 835, "SKILL", "comprehension des contextes strategiques"),
    (890, 910, "SKILL", "utilisation d'un CMS"),
    (940, 968, "SKILL", "production de campagne media"),
    (1002, 1009, "SKILL", "digital"),
    (1013, 1022, "SKILL", "Marketing"),
    (1025, 1050, "SKILL", "Culture de la performance"),
    (1052, 1069, "SKILL", "data intelligence"),
    (1078, 1099, "SKILL", "qualite relationnelle"),
    (1106, 1127, "SKILL", "maitrise de Photoshop"),
    (1158, 1194, "SKILL", "sens de la relation client developpe"),
    (1250, 1259, "SKILL", "dynamisme"),
    (1292, 1299, "SKILL", "rigueur"),
    (1307, 1348, "SKILL", "competences organisationnelles et process"),
    (1371, 1385, "SKILL", "parlez anglais"),
]


predictions = [
    (907, 910, "SKILL", "CMS"),
    (923, 939, "SKILL", "a l'aise avec la"),
    (940, 968, "SKILL", "production de campagne media"),
    (1013, 1022, "SKILL", "Marketing"),
    (1025, 1050, "SKILL", "Culture de la performance"),
    (1052, 1069, "SKILL", "data intelligence"),
    (1078, 1099, "SKILL", "qualite relationnelle"),
    (1106, 1127, "SKILL", "maitrise de Photoshop"),
    (1158, 1184, "SKILL", "sens de la relation client"),
    (1250, 1259, "SKILL", "dynamisme"),
    (1292, 1299, "SKILL", "rigueur"),
    (1307, 1348, "SKILL", "competences organisationnelles et process"),
    (1371, 1385, "SKILL", "parlez anglais"),
]

from ner_evaluator import NerEvaluator

eval = NerEvaluator()

print(eval.evaluate(entities, predictions, ["SKILL"]))
