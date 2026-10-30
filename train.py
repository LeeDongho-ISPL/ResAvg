"""ResAvg train entry point (placeholder)."""
import argparse

from resavg import RELEASE_NOTE


def main() -> None:
    parser = argparse.ArgumentParser(description="ResAvg train (placeholder)")
    parser.add_argument("-s", "--source_path", type=str, default="", help="dataset path")
    parser.add_argument("-m", "--model_path", type=str, default="", help="output path")
    parser.parse_args()
    print(RELEASE_NOTE)


if __name__ == "__main__":
    main()
