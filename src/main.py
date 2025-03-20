import argparse
from datetime import datetime
import time

from magi_network import MagiNetwork


def main(args):

    level = args.level
    query = args.text
    trials = args.number_of_trials
    magi_network = MagiNetwork(level)
    magi_network.set_query(query)
    result = None
    results = []

    print(f"\nQuery: {query}")
    print(f"\n{level} levels of decision making")
    print(f"{3 ** level} decision makers")
    print(f"{trials} trials")

    start = datetime.now()

    if trials > 1:
        print(f"\nRunning multiple trials with {level} levels of decision making")
        for i in range(trials):

            current_result = magi_network.decide()
            print(f"\nTrial {i + 1}: {current_result}")
            results.append(magi_network.decide())
        result = max(set(results), key=results.count)
        print(f"\nResults: {results}")
    else:
        result = magi_network.decide()
        print("\nDecision Tree Structure:")
        print(magi_network.get_tree_representation())



    print(f"\nFinal Result: {result}")

    print("\nRequests:")
    print(f"{level} level{"s" if level > 1 else ""} of decision making")
    print(f"{3 ** level} decision maker{"s" if 3 ** level > 1 else ""}")
    print(f"{trials} trial{"s" if trials > 1 else ""}")

    end = datetime.now()
    elapesed_time = end - start
    print("\nTime Elapsed:")
    print(f"{elapesed_time.total_seconds()} s")
    print(f"{elapesed_time.total_seconds() * 1000} ms")
    print(f"{elapesed_time.total_seconds() * 1_000_000} µs")
    print(f"{elapesed_time.total_seconds() * 1_000_000_000} ns")

    
    # You can now get the tree representation again without recalculating


def get_args():
    description = "Submit a question to the machina"
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("text", type=str, help="The text to submit to the machina")
    parser.add_argument("-l", "--level", type=int, default=1, help="The level of thinking")
    parser.add_argument("-n", "--number_of_trials", type=int, default=1, help="The number of trials to run")
    return parser.parse_args()


if __name__ == '__main__':
    # Get arguments
    args = get_args()

    main(args)



