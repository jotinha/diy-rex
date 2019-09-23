import pandas

def load(fname):
    print(f"Loading {fname}")
    df = pandas.read_csv(fname)

    if not set(df.columns) == {'date','user','item'}:
        raise ValueError("Invalid columns")

    df = df.astype({
        'date': 'datetime64[ns]',
        'user': 'category',
        'item': 'category'
    })
    return df


def stats(df):
    n = len(df)
    nusers = df.user.nunique()
    nitems = df.item.nunique()

    print(n, "lines")
    print(nusers, "users")
    print(nitems, "items")
    print("Density:", n / (nusers*nitems))