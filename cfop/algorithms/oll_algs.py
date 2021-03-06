"""
Gets a whole bunch of OLL algorithms from:

    https://www.speedsolving.com/wiki/index.php/OLL

And creates a dict, where each entry is one OLL case
"""
import re

from bs4 import BeautifulSoup
from requests import get


ALG_CHARS = "ULFRBDulfrbdxyzMES()'23456789w "
# These have the tag: This alg was written but doesn't solve the OLL
BAD_ALGS = ["(y') l U2 L U L' U' L U L' U' l'",
            "(y) l' U2 L U L' U' L U L' U' l",
            "(y') R' U' R x U' R' U y R U y' R U' x'",
            "(y') (L F' L' F)2 L U' L' U L U' L"]

def _parse(tag):
    """
    Used by the BeautifulSoup parser to get the wanted tags
    """
    # Return if it's the title of the OLL Alg which are h2s with the tag
    # OLL_* where * goes from 1 to 57
    if tag.has_attr('id'):
        return tag['id'].startswith('OLL_')
    # Return if it's an actual alg which are a tags with the following classes
    elif tag.name == 'a' and tag.has_attr('class'):
        return tag['class'] == ['external', 'text']
    # Otherwise don't return anything
    return False

def _get_tags():
    """
    Gets the appropriate tags from the website.
    """
    soup = BeautifulSoup(
        get('https://www.speedsolving.com/wiki/index.php/OLL').content,
        'html.parser'
    )
    return soup.find_all(_parse)

def _get_alg_dict(alg_tags):
    """
    Turns the tags into a dictionary of {OLL Case: List of Algs}.
    """
    algs_dict = {}
    for tag in alg_tags:
        text = tag.text
        # Remove the bad algs that don't work
        if text in BAD_ALGS:
            continue
        # Find the OLL case numbers and make an empty list as the value
        if re.search(r'^OLL \d{1,2}$', text):
            last_oll = text
            algs_dict[text] = []
        # Fill that empty list the algs for it
        elif re.search(r'^[{}]*$'.format(ALG_CHARS), text):
            algs_dict[last_oll].append(text)

    return algs_dict

def _make_algs_readable(algs_dict):
    """
    Changes the format of the algs slightly so that they can be read by the
    code used here.
    """
    # Make the algs readable
    for case, algs in algs_dict.items():
        new_algs = []
        # For each alg in each OLL case...
        for n, alg in enumerate(algs):
            # Find the parentheses with a digit after them
            parens = re.findall(r'\([^)]*\)\d', alg)
            # If we have them, distribute it out
            if parens:
                for paren in parens:
                    mult = int(re.findall(r'\d*$', paren)[0])
                    alg = alg.replace(paren, paren[:-1*len(str(mult))] * mult)
            # Remove everything unnecessary
            for char in "() ":
                alg = alg.replace(char, '')
            new_algs.append(alg)
        # Replace with new algs
        algs_dict[case] = new_algs

    return algs_dict


def get_algs():
    """
    Does everything and returns the readable algs
    """
    # 1) Gets the tags from the HTML
    alg_tags = _get_tags()
    # 2) Turns these tags into a usable dictionary
    algs_dict = _get_alg_dict(alg_tags)
    # 3) Turns the dictionary into a readable dictionary
    algs_dict_readable = _make_algs_readable(algs_dict)

    return algs_dict_readable
