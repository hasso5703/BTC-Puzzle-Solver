import multiprocessing
import pandas as pd

from constants import DATA_FILE

DF = pd.read_csv(DATA_FILE)
PUZZLES_LIST = sorted(set(DF.puzzle_number.values.tolist()))
NB_THREAD = multiprocessing.cpu_count()
