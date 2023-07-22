# translator.py
"""
Module for translation between English and French using MyMemoryTranslator.
"""

from deep_translator import MyMemoryTranslator


def english_to_french(text, source_language='en'):
    """
    Translate English text to French.

    Args:
        text (str): The text in English to be translated.
        source_language (str): The source language code. Default is 'en'.

    Returns:
        str: The translated text in French.
    """
    french_text = MyMemoryTranslator(source=source_language, target='fr').translate(text)
    return french_text


def french_to_english(text, source_language='fr'):
    """
    Translate French text to English.

    Args:
        text (str): The text in French to be translated.
        source_language (str): The source language code. Default is 'fr'.

    Returns:
        str: The translated text in English.
    """
    english_text = MyMemoryTranslator(source=source_language, target='en').translate(text)
    return english_text
