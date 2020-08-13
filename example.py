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

def split_sentences(sentences):
    """
    split sentences into array by " ".
    example
    "this is a library for evaluating nlg system" -> ["this", "is", "a", "libary", "for", "evaluating", "nlg", "system"]
    """
    return [
        sentence.strip().split(" ")
        for sentence in sentences
    ]

def print_dict(score_dict):
    for score_name, score in score_dict.items():
        print(score_name, ": ", score)

def example():
    """
    The input of the system should be
        - hyp: [[hyp1], [hyp2], ....]
        - ref: [[ref1a, ref1b, ...], [ref2a, ref2b, ...]]
    """
    hyp1, hyp2, ref1, ref2 = load_files()
    hyp1 = split_sentences(hyp1)
    hyp2 = split_sentences(hyp2)
    hyp1, hyp2 = hyp1[0], hyp2[0]
    ref1 = split_sentences(ref1)
    ref2 = split_sentences(ref2)

    hyps = [hyp1, hyp2]
    refs = [ref1, ref2]

    bleu_scorer = BLEUCalculator()
    bleu_score_dict = bleu_scorer.calculate_metrics(hyps, refs)
    print_dict(bleu_score_dict)
    

if __name__ == "__main__":
    example()