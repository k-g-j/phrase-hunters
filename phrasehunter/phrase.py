class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.correct_letters = list(set(self.phrase.replace(" ", "")))
        self.guessed_letters = []

    def display(self):
        split_phrase = list(self.phrase)
        phrase_display = list('_' * len(split_phrase))
        for index, letter in enumerate(split_phrase):
            if letter == ' ':
                phrase_display[index] = ' '
            if letter in self.guessed_letters:
                phrase_display[index] = letter
        return print(f"Current Progress:\n{''.join(phrase_display)}")

    def check_letter(self, letter):
        return letter in self.correct_letters

    def check_complete(self):
        return set(self.correct_letters) == set(self.guessed_letters)


# if __name__ == '__main__':
#     # python3 phrasehunter/phrase.py
#     phrase = Phrase('Hello World')
#     print(phrase.display())
#     print(phrase.check_letter('w'))
#     print(phrase.check_complete())
