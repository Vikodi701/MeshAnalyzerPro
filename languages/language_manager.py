"""
MeshAnalyzer Pro
Language Manager
"""

from core.config import Config

from languages.tr import TEXT as TR_TEXT
from languages.en import TEXT as EN_TEXT


class LanguageManager:

    LANGUAGES = {
        "tr": TR_TEXT,
        "en": EN_TEXT,
    }

    @staticmethod
    def current_language():
        config = Config()
        language = config.get("language")

        if language not in LanguageManager.LANGUAGES:
            language = "tr"

        return language

    @staticmethod
    def text(key):
        language = LanguageManager.current_language()
        dictionary = LanguageManager.LANGUAGES.get(language, TR_TEXT)

        return dictionary.get(key, key)

    @staticmethod
    def set_language(language):
        if language not in LanguageManager.LANGUAGES:
            language = "tr"

        config = Config()
        config.set("language", language)

    @staticmethod
    def available_languages():
        return {
            "tr": "Türkçe",
            "en": "English",
        }