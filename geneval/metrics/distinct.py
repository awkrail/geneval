class DistinctCalculator:
    def __init__(self):
        pass
    
    def calculate_metrics(self, gts, refs=None):
        """
        gts: generated sentences
        Distinct-N aims to calculate distinct percentage of n-gram, thus reference sentences are not necessesary.
        """
        distinct_1 = sum(self.calculate_distinct_n(gt, ngram=1) for gt in gts) / len(gts)
        distinct_2 = sum(self.calculate_distinct_n(gt, ngram=2) for gt in gts) / len(gts)
        return {
            "distinct1" : distinct_1,
            "distinct2" : distinct_2
        }

    def calculate_distinct_n(self, sentence, ngram):
        if len(sentence) == 0:
            return 0
        distinct_ngrams = set(self.ngram(sentence, ngram))
        return len(distinct_ngrams) / len(sentence)
    
    def ngram(self, sentence, ngram):
        sequence = iter(sentence)
        history = []
        
        while ngram > 1:
            history.append(next(sequence))
            ngram -= 1
        
        for item in sequence:
            history.append(item)
            yield tuple(history)
            del history[0]