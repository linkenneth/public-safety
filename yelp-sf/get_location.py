# load unique restaurants from u.csv
# u = pd.read_csv('u.csv', index_col=0)

# load yelp api function calls

rests = []
for k, id_ in u['id'].iteritems():
    print k, id_
    s = get_business(id_)['location']['coordinate']
    rests.append( (id_, s['longitude'], s['latitude']) )

df = pd.DataFrame.from_records
