# 0a
a = ""
length = 0
q0.a.check()

# 0b
b = "it's ok"
length = 7
q0.b.check()

# 0c
c = 'it\'s ok'
length = 7
q0.c.check()

# 0d
d = """hey"""
length = 3
q0.d.check()

# 0e 
e = '\n'
length = 1
q0.e.check()

# 1
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return zip_code.isdigit() and len(zip_code) == 5
    pass

# Check your answer
q1.check()

# 2 
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    result = []
    keyword = keyword.lower()
    
    for index, doc in enumerate(doc_list):
        doc = doc.lower().replace(".", "").replace(",", "")
        words = doc.split()
        if keyword in words:
            result.append(index)
            
    return result
    pass

# Check your answer
q2.check()

# 3
def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    search_results = {}
    
    for keyword in keywords:
        indices = word_search(doc_list, keyword)
        search_results[keyword] = indices
        
    return search_results
    pass

# Check your answer
q3.check()



