# AUTHOR: Michael Partridge <mcp292@nau.edu>
#
# Sources:
# https://docs.python.org/3/library/sqlite3.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html

import argparse
import sqlite3 as sql
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="This program converts a SQL "
                                     "tabel to a pandas dataframe.")
    parser.add_argument("db",
                    help="The SQL database to convert.")
    parser.add_argument("-t", "--table", type=str, nargs='+',
                    help="The list of tables to convert. Format: table1 table2 "
                        "table3.")
    parser.add_argument("-m", "--manual", action="store_true",
                    help="Drop into an interactive shell to manually inspect "
                        "dataframes.")
    args = parser.parse_args()

    # TODO: Automatically write to csvs
    # TODO: Have switch to read in from csv that you can pair with
    # manual (can't exist without -m)
    
    con = sql.connect(args.db)

    if args.table:              # if table provided
        # TODO: for each table in list, extract (right now only single entry support)
        query = f"SELECT * FROM {args.table[0]}"
    else:
        # TODO: for each table, select all, append to df list
        pass

    df = pd.read_sql(query, con) # can only be single table or table subset
    filename = f"{args.table[0]}.csv"
    df.to_csv(filename)

    if args.manual:
        breakpoint()


if __name__ == "__main__":
    main()
