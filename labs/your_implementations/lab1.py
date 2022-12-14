import re
from typing import List

import nltk
from lab_utils import LabPredictor

# pylint: disable=pointless-string-statement
""" Welcome to the first lab!

The comments and TODOs should guide you through the implementation,
but feel free to modify the variables and the overall structure as you see fit.

It is important to ekep the name of the main class: Lab1, as this 
is imported by the `lab_runner.py` file.

You should complete the code for the classes:
- NgramModel (superclass of BigramModel and TrigramModel)
- BigramModel (should be a simple implementation with a few parameters)
- TrigramModel (should be a simple implementation with a few parameters)
- Lab1 (the main logic for parsing input and handling models)
"""

class NgramModel:
    """ The main class for all n-gram models

    Here you will create your model (based on N)
    and complete the predict method to return the most likely words.
    
    """
    def __init__(self, n_gram=1) -> None:
        """ the init method should load/train your model
        Args:
            n_gram (int, optional): 2=bigram, 2=trigram, ... Defaults to 1.
        """
        print(f"Loading {n_gram}-gram model...")
        self.n_gram = n_gram
        self.words_to_return = 4  # how many words to show in the UI

        self.model = None  # TODO: implement the model using built-in NLTK methods
        # take a look at the nltk.collocations module
        # https://www.nltk.org/howto/collocations.html

    def predict(self, tokens: List[str]) -> List[str]:
        """ given a list of tokens, return the most likely next words

        Args:
            tokens (List[str]): preprocessed tokens from the LabPredictor

        Returns:
            List[str]: selected candidates for next-word prediction
        """
        # we're only interested in the last n-1 words.
        # e.g. for a bigram model,
        # we're only interested in the last word to predict the next
        n_tokens = tokens[-(self.n_gram - 1):]

        probabilities = [] # TODO: find the probabilities for the next word(s)
        
        # TODO: apply some filtering to only select the words
        # here you're free to select your filtering methods
        # a simple approach is to simply sort them by probability

        best_matches = []  # TODO: sort/filter to your liking

        # then return as many words as you've defined above
        return best_matches[:self.words_to_return]


class BigramModel(NgramModel):
    def __init__(self) -> None:
        super().__init__(n_gram=2)


class TrigramModel(NgramModel):
    def __init__(self) -> None:
        super().__init__(n_gram=3)


class Lab1(LabPredictor):
    def __init__(self):
        super().__init__()
        self.corpora = None  # TODO: load a corpus from NLTK

        # Define a strategy to select the first words (when there's no input)
        # TODO: this should not be a predefined list
        self.start_words = ["predict", "some", "words"]

    @staticmethod
    def preprocess(text: str) -> List[str]:
        """
        Preprocess the input text as you see fit, return a list of tokens.

        - should you consider parentheses, punctuation?
        - lowercase?
        - find inspiration from the course literature :-)
        """
        # TODO: filters here

        tokens = []  # TODO: tokenize the preprocessed text
        return tokens

    def predict(self, input_text):
        if not bool(input_text):  # if there's no input...
            print("No input, using start words")
            return self.start_words

        tokens = self.preprocess(input_text)

        # make use of the backoff model (e.g. bigram)
        too_few = False  # TODO: check if the input is too short for trigrams

        # select the correct model based on the condition
        model = self.backoff_model if too_few else self.model
        # alternatively, you can switch between the tri- and bigram models
        # based on the output probabilities. This is 100% optional!

        return model.predict(tokens)

    def train(self) -> None:
        """ train or load the models
        add parameters as you like, such as the corpora you selected.
        """
        self.model = TrigramModel()  # TODO: add needed parameters
        self.backoff_model = BigramModel()  # TODO: add needed parameters
