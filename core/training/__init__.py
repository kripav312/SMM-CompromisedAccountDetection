from .decision_tree import train_classifier as train_decision_tree


type_classifier_mapping = {
    'decision_tree': train_decision_tree
}


def train_classifier(samples, labels, classifier_type):
    if len(samples) != len(labels):
        raise ValueError('Number of samples has to equal number of labels!')
    if classifier_type not in type_classifier_mapping:
        raise ValueError('Invalid classifier_type!')

    training_callable = type_classifier_mapping[classifier_type]
    return training_callable(samples, labels)