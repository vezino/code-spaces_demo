from nlplogic.corenlp import search_wikipedia, sumarize_wikipedia, get_text_blob, get_phrases

def test_get_phrases():
    assert 'golden state' in get_phrases("Golden State Warriors")