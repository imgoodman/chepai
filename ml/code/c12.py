from collections import defaultdict

def map_word_count(document_id, document):
    counts = defaultdict(int)
    for word in document.split(" "):
        counts[word] += 1
    
    for word in counts:
        yield (word, counts[word])

def shuffle_words(results):
    records = defaultdict(list)