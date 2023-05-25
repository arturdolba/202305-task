from .parsers import RemoveHTMLCode
from .wordrank import WordRank
from .clear import ClearText


def clear_document(content):
    '''
    Clears document from HTML/CSS/JS content.
    '''
    content = content.strip()
    if len(content) == 0:
        return content
    parser = RemoveHTMLCode(content)
    text_content = parser.get_text()
    return text_content


def clear_text(content):
    '''
    Clears document from special characters and entities.
    '''
    clear = ClearText(content)
    return clear.get_clear_text()


def divide_to_words(content):
    '''
    Divides content into words (space is separator)
    '''
    words = content.split(" ")
    response = []
    for word in words:
        clear_word = word.strip()
        if clear_word:
            response.append(clear_word)
    return response


def lowercase_words(words):
    '''
    Change strings in list to lowercase.
    '''
    response = []
    for word in words:
        response.append(word.lower())
    return response


def top_words(words, top_counter):
    '''
    Generates rank of top n words
    '''
    rank = WordRank(words, top_counter)
    return rank.get_result()


def print_top_words(rank):
    '''
    Prints top words from rank.
    '''
    response = ""
    for element in rank:
        response+="%s : %d\n" % (element[0], element[1])
    return response

def save_rank(data):
    '''
    Save rank to file results.txt
    '''
    with open('results.txt', "w", encoding="utf-8") as file_write:
        file_write.write(data)
