import pandas
from tqdm import trange

PROJECT_ID = "mistakes-42c6d"

def get_listenbrainz_data(month, year):

    df  = pandas.read_gbq("""
        select 
            listened_at, user_name, artist_name, release_name, track_name, tags
        from `listenbrainz.listenbrainz.listen`
        where 
            extract(MONTH from listened_at) = {}
            and extract(YEAR from listened_at) = {}
        """.format(month, year), project_id=PROJECT_ID)
    df.to_csv('{:02d}_{}.csv'.format(month,year), index=False)

if __name__ == "__main__":
    for month in trange(1,7):
        get_listenbrainz_data(month,2018)




