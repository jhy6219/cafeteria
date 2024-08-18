import re
from tqdm import tqdm
import numpy as np
import pandas as pd
import ast
# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process

import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

# pd.set_option('display.max_columns', None)
tqdm.pandas()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample

from xgboost import XGBClassifier

import scipy.stats as stats