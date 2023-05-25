'''
Main module.
'''
import sys
from modules.request import get_page_content
from modules.functions import (clear_document,
                               clear_text,
                               divide_to_words,
                               lowercase_words,
                               top_words,
                               print_top_words,
                               save_rank)




def main():
    '''
    Main function of the program.
    '''
    # 1. open the page with the given URL.
    # 2. Read the content of the page.
    url = None
    if len(sys.argv) == 2:
        url = sys.argv[1]
        if len(url) < 5:
            url = ""
    if not url:
        url = input("Give URL: ")
    content = get_page_content(url)
    if not content:
        return
    if len(content) == 0:
        print("Can't load content of given URL.")
        return
    # 3. clear the page source of all html, css, js, etc. tags, leaving text that contains human-readable content.
    text_content = clear_document(content)

    # 4. remove all punctuation marks (such as commas, full stops, exclamation marks, etc.) and special characters from the text.

    cleared_text = clear_text(text_content)

    # 5 Divide the text into individual words.
    words = divide_to_words(cleared_text)

    # 6 Calculate the number of occurrences of each word in the text.
    words = lowercase_words(words)
    rank = top_words(words, 10)
    printable_rank = print_top_words(rank)

    # 7. display the 10 most frequent words with their number of occurrences, in descending order.
    print(printable_rank)

    # 8. save this information to a file named &#39;results.txt&#39;.
    save_rank(printable_rank)

if __name__ == '__main__':
    main()
