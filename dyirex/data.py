import pandas


def load(fname):
    df = pandas.read_csv(fname)
    assert df.columns