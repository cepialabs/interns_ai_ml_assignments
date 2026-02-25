import re
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class TextStatsTransformer(BaseEstimator, TransformerMixin):
    """
    Creates numeric features from raw text:
    length, word_count, uppercase_ratio, exclamations, digits, links count
    """
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.Series(X).fillna("").astype(str)

        lengths = X.str.len().to_numpy()
        word_count = X.str.split().str.len().fillna(0).to_numpy()

        upper_count = X.apply(lambda s: sum(1 for c in s if c.isupper())).to_numpy()
        alpha_count = X.apply(lambda s: sum(1 for c in s if c.isalpha())).to_numpy()
        uppercase_ratio = np.where(alpha_count == 0, 0.0, upper_count / alpha_count)

        num_excl = X.str.count("!").to_numpy()
        num_digits = X.apply(lambda s: sum(1 for c in s if c.isdigit())).to_numpy()

        # crude link counter
        num_links = X.apply(lambda s: len(re.findall(r"(http|www\.)", s.lower()))).to_numpy()

        feats = np.column_stack([lengths, word_count, uppercase_ratio, num_excl, num_digits, num_links])
        return feats