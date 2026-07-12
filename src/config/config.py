"""import os

# Project Root
ROOT_DIR = os.getcwd()

# Data
RAW_DATA_PATH = os.path.join(ROOT_DIR, "data", "raw", "creditcard.csv")
BALANCED_DATA_PATH = os.path.join(ROOT_DIR, "data", "processed", "credit_card_balanced.csv")

# Model
MODEL_PATH = os.path.join(ROOT_DIR, "models", "logistic_regression.pkl")"""


"""
Level 1 — Beginner (Learning Stage)
At this stage, config.py only stores file paths.
"""


# config.py
#beginner level..

RAW_DATA_PATH = "data/raw/creditcard.csv"

PROCESSED_DATA_PATH = "data/processed/credit_card_balanced.csv"

# MODEL_PATH = "models/model.pkl"

#Used in

"""from src.config.config import RAW_DATA_PATH

df = pd.read_csv(RAW_DATA_PATH)"""

######################################################################################################

""" Level 2 — Intermediate (Portfolio Projects)

Now your project becomes bigger.

You also store project settings.
"""

# config.py
"""
import os

ROOT_DIR = os.getcwd()

# Data
RAW_DATA_PATH = os.path.join(ROOT_DIR, "data", "raw", "creditcard.csv")
PROCESSED_DATA_PATH = os.path.join(ROOT_DIR, "data", "processed", "creditcard_clean.csv")

# Model
MODEL_PATH = os.path.join(ROOT_DIR, "models", "model.pkl")

# Training
RANDOM_STATE = 42
TEST_SIZE = 0.2

# Target
TARGET_COLUMN = "Class"

# Logging
LOG_FILE = os.path.join(ROOT_DIR, "logs", "training.log")

Used in
from src.config.config import TEST_SIZE

train_test_split(
    X,
    y,
    test_size=TEST_SIZE
)"""