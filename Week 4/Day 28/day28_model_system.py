# 📅 DAY 28 — OOP MINI PROJECT

# 🧠 Project Idea (Think Like ML Engineer)
# 🎯 Model Evaluation System
# This mimics how ML libraries evaluate models.
# Concept
# Base class: Model
# Child classes: LinearModel, TreeModel
# Same method name → different behavior
# Internal data protected
# User interacts only via public methods

class Model:
    def __init__(self, user):
        self.user = user
        self.__accuracy = 0
    def train(self):
        print(f"Training {self.user} model......")
    def set_accuracy(self, acc):
        if 0 <= acc <= 100:
            self.__accuracy = acc
        else:
            print("Invalid accuracy")
    def get_accuracy(self):
        return self.__accuracy
    def evaluate(self):
        print("Evaluating model... (base logic)")
class LinearModel(Model):
    def __init__(self, user):
        super().__init__(user)
    def evaluate(self):
            print(f"{self.user} Evaluation:")
            print("Using linear evaluation method")
            print("Accuracy:", self.get_accuracy(), "%")
    
class TreeModel(Model):
    def __init__(self, user):
        super().__init__(user)
    def evaluate(self):
            print(f"{self.user} Evaluation:")
            print("Using tree-based evaluation")
            print("Accuracy:", self.get_accuracy(), "%")
models = [
    LinearModel("Linear Regression"),
    TreeModel("Decision Tree")
]
models[0].train()
models[0].set_accuracy(82)
models[1].train()
models[1].set_accuracy(90)
print("\n--- MODEL RESULTS ---")
for m in models:
    m.evaluate()
