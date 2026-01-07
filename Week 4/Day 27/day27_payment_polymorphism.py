class Payment:
    def pay(self, amount):
        print("Processing payment of", amount)
class CashPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using cash")
class CardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using card")
class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")
payments = [
    CashPayment(),
    CardPayment(),
    UPIPayment()
]
for p in payments:
    p.pay(500)



# 1. Why not use if-else everywhere?If you use if-else (or switch) to check for types, you create Rigid Code. Every time you add a new feature, you have to find and modify every single if-else block in your entire codebase.The "Shotgun Surgery" ProblemImagine you have 10 different files in your project that check if animal == "Dog". When you decide to add a "Wolf," you have to go to all 10 files and add an elif animal == "Wolf". If you miss even one, your program crashes or behaves unpredictably.
# 2. How Polymorphism Reduces Future ChangesPolymorphism follows the Open-Closed Principle: Your code should be Open for extension, but Closed for modification.With polymorphism, you don't change existing code; you simply add new code.Scenarioif-else ApproachPolymorphism ApproachAdding a new featureSearch for all if blocks and manually insert new logic.Create a new class that implements the existing methods.Risk of BugsHigh. You might break existing logic while editing old files.Low. You aren't touching the old, working code at all.TestingYou must re-test the entire if-else block.You only need to test the new class you just wrote.
# 3. How this helps ML Frameworks evolveMachine Learning frameworks (like PyTorch, TensorFlow, or Scikit-Learn) rely heavily on polymorphism to allow for rapid innovation.A. Swapping ModelsIn Scikit-Learn, every model (Linear Regression, Random Forest, SVM) has a .fit() and a .predict() method.Because of polymorphism, you can write a single evaluation pipeline:Pythondef evaluate_model(model, data):
#     model.fit(data.x, data.y) # Polymorphic call
#     return model.score(data.test_x, data.test_y)
# You can pass any model into this function. The framework doesn't need to know if the model is a simple line or a complex neural network.B. Pluggable Optimizers and LayersIn PyTorch, all neural network layers inherit from nn.Module.When a researcher invents a new type of layer (like a "Transformer" layer), they just create a new class.Because it follows the nn.Module "form," it immediately works with existing Optimizers, Loss Functions, and GPU accelerators without the PyTorch developers having to rewrite their core engine.C. Hardware Agnostic CodeML frameworks use polymorphism to handle hardware. A "Tensor" object might live on a CPU, a GPU, or a TPU. When you call tensor.add(other), polymorphism ensures the correct low-level C++ or CUDA code runs for that specific hardware, while your Python code remains exactly the same.
