import pandas

def load(fname, cols):
    print(f"Loading {fname}")
    df = pandas.read_csv(fname)

    if not set(df.columns) == set(cols):
        raise ValueError("Invalid columns")

    dtypes = {
        'date': 'datetime64[ns]',
        'user': 'category',
        'item': 'category',
        'feature': 'category'
    }
    for col in cols:
        if col in dtypes:
            df[col] = df[col].astype(dtypes[col])

    return df

def stats(df):
    n = len(df)
    nusers = df.user.nunique()
    nitems = df.item.nunique()

    print(n, "lines")
    print(nusers, "users")
    print(nitems, "items")
    print("Density:", n / (nusers*nitems))