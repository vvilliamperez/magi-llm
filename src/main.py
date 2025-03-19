import argparse
import openai

from magi_network import MagiNetwork


def main(args):
    level = args.level
    query = args.text
    magi_network = MagiNetwork(level)
    magi_network.set_query(query)
    result = magi_network.decide()

    print(result)


def get_args():
    description = "Submit a question to the machina"
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("text", type=str, help="The text to submit to the machina")
    parser.add_argument("-l", "--level", type=int, default=1, help="The level of thinking")
    return parser.parse_args()


if __name__ == '__main__':
    # Get arguments
    args = get_args()

    main(args)



