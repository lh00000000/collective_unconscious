import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from functools import partial
import google

def html_to_plaintext(html):
    soup = BeautifulSoup(html, 'html.parser')
    return ''.join(soup.findAll(text=True))

def _what_(thing, to_be):
    question = "what {} {}".format(to_be, thing)
    answer_prefix = "{} {}".format(thing, to_be)
    default_answer = "idk"

    top_url = next(google.search(question, stop=1))
    top_text = html_to_plaintext(requests.get(top_url).text)
    is_answer = lambda line: answer_prefix in line.strip().lower()
    return next(
        filter(is_answer, sent_tokenize(top_text)),
        default_answer)

what_is = partial(_what_, to_be="is")
what_are = partial(_what_, to_be="are")

"""
Example
>>> print(what_is("the point"))
So here I come to what the point is: the point is to bring about more consciousness.
"""
