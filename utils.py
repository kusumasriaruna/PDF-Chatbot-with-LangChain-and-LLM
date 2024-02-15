import numpy as np
import re


def split_text_into_paragraphs(text):
  """Splits a text into paragraphs.

  Args:
    text: The text to split.

  Returns:
    A list of paragraphs.
  """

  paragraphs = re.split(r"\n\n", text)
  return paragraphs



def calculate_similarity_between_texts(text1, text2):
  """Calculates the similarity between two texts.

  Args:
    text1: The first text.
    text2: The second text.

  Returns:
    A similarity score between 0 and 1, where 1 is the most similar.
  """

  # Convert the texts to lowercase.
  text1 = text1.lower()
  text2 = text2.lower()

  # Remove punctuation.
  text1 = re.sub(r"[^\w\s]", "", text1)
  text2 = re.sub(r"[^\w\s]", "", text2)

  # Split the texts into words.
  text1_words = text1.split()
  text2_words = text2.split()

  # Calculate the cosine similarity between the two texts.
  cosine_similarity = np.dot(text1_words, text2_words) / (np.linalg.norm(text1_words) * np.linalg.norm(text2_words))

  return cosine_similarity
