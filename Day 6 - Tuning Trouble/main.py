from typing import List

DIR_PATH = "Day 6 - Tuning Trouble"

if __name__ == "__main__":
    with open(f"./{DIR_PATH}/input", "r") as fptr:
        datastream = fptr.read()

        NUM_OF_CHARACTERS = 14

        for i in range(0, len(datastream) - NUM_OF_CHARACTERS):
            print(
                datastream[i : i + NUM_OF_CHARACTERS], f" - [{i}:{i+NUM_OF_CHARACTERS}]"
            )
            marker = datastream[i : i + NUM_OF_CHARACTERS]
            if len(set(marker)) == NUM_OF_CHARACTERS:
                break

        print(
            "How many characters need to be processed before the first start-of-packet marker is detected? ",
            i + NUM_OF_CHARACTERS,
        )
