from app.classifier import IntentClassifier

classifier = IntentClassifier()


def classifier_node(state):

    result = classifier.classify(state["user_prompt"])

    return {
        "intent": result["intent"]
    }