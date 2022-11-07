import sys
import glob
import argparse
import pathlib
import pandas as pd


def combine_csv(root_dir=None):
    csv_files = glob.glob(f"{root_dir}/*/*.csv")
    return pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        type=pathlib.Path,
        required=True,
        metavar="DIR",
        help="Relative or absolute path to input directory from which all csv files should be merged.",
    )
    args = parser.parse_args()
    sys.stdout.write(combine_csv(args.input).to_csv())
