import nltk

class BLEUCalculator:
    def __init__(self):
        pass
    
    def calculate_metrics(self, gts, refs):
        """
        gts: generated sentences
        refs: reference sentences
        """
        bleu1 = nltk.translate.bleu_score.corpus_bleu(refs, gts, weights=[1.0, 0, 0, 0])
        bleu2 = nltk.translate.bleu_score.corpus_bleu(refs, gts, weights=[0.5, 0.5, 0, 0])
        bleu3 = nltk.translate.bleu_score.corpus_bleu(refs, gts, weights=[1/3, 1/3, 1/3, 0])
        bleu4 = nltk.translate.bleu_score.corpus_bleu(refs, gts)
        
        return {
            "bleu1" : bleu1,
            "bleu2" : bleu2,
            "bleu3" : bleu3,
            "bleu4" : bleu4
        }