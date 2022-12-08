if __name__ == "__main__":
    with open("./Day 4 - Camp Cleanup/input", "r") as fptr:
        pairs = fptr.readlines()

        total_inherit = 0

        for pair in pairs:
            sections = pair.strip().split(",")

            s = []
            for section in sections:
                series = section.split("-")
                s.append([i for i in range(int(series[0]), int(series[1]) + 1)])

            # Overlaps part 1:
            # They have all the section inherit the other pair
            # if not set(s[0]) - set(s[1]) or not set(s[1]) - set(s[0]):
            #     total_inherit += 1

            # Overlaps part 2:
            # If there some part inherit the other pair
            if set(s[0]) & set(s[1]):
                total_inherit += 1

        print(total_inherit)
