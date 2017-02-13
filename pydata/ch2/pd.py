from pandas import DataFrame,Series
import pandas as pd
import numpy as np

import json

path='../data/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]

frame = DataFrame(records)
# print(frame)
# print(frame['tz'].value_counts())
tz=frame['tz']
tz[tz=='']='Unknown'
print(tz)
tz_counts=tz.value_counts()
# print(tz_counts)
tz_counts[:10].plot(kind='barh',rot=0)
