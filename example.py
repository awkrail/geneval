import ipdb; ipdb.set_trace() # -> まずは__init__.pyの意図を理解
from geneval.metrics.bleu import BLEUCalculator

def load_files():
    with open("examples/hyp1.txt", "r") as f:
        hyp1 = f.readlines()

    with open("examples/hyp2.txt", "r") as f:
        hyp2 = f.readlines()

    with open("examples/ref1.txt", "r") as f:
        ref1 = f.readlines()

    with open("examples/ref2.txt", "r") as f:
        ref2 = f.readlines()
    return hyp1, hyp2, ref1, ref2

def example():
    hyp1, hyp2, ref1, ref2 = load_files()
    bleu_scorer = BLEUCalculator()
    bleu_scorer.calculate_metrics()
    

if __name__ == "__main__":
    example()