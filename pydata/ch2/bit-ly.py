import json
from collections import defaultdict
from collections import Counter

path='../data/usagov_bitly_data2012-03-16-1331923249.txt'

records = [json.loads(line) for line in open(path)]
# print(records[0])
time_zones = [record['tz'] for record in records if 'tz' in record]
# print(time_zones)
def get_counts(time_zones):
    time_zone_count={}
    for tz in time_zones:
        if tz in time_zone_count:
            time_zone_count[tz]+=1
        else:
            time_zone_count[tz]=1
    print(time_zone_count)
    return time_zone_count

def get_counts2(time_zones):
    time_zone_count=defaultdict(int)
    for tz in time_zones:
        time_zone_count[tz]+=1
    print(time_zone_count)
    return time_zone_count

def get_top_counts(time_zones,n=10):
    time_zone_count=get_counts2(time_zones)
    value_key_pairs = [(count,tz) for tz,count in time_zone_count.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

def get_top_counts2(time_zones,n=10):
    counts=Counter(time_zones)
    print(counts.most_common(n))

if __name__=="__main__":
    print(get_top_counts2(time_zones))