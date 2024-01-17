from typing import List, Tuple, Set
import pandas as pd
from dminer import *

def self_join(S:Set) -> Set:
    candidates = set()
    frequent = list(S)

    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            candidates.add(tuple(sorted(set(frequent[i]) | set(frequent[j]))))
        #candidates.add(builder_set)

    return candidates


store_data = pd.read_csv('./store_data.csv', header=None)
df = pd.DataFrame(store_data)