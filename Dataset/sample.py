import os
import pandas as pd

def main():
    here = os.path.dirname(__file__)
    path = os.path.join(here, "MalwareData.csv")
    df = pd.read_csv(path)
    print(df.head(5))

if __name__ == '__main__':
    main()
