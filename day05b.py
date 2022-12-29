"""
--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of
determining whether a string is naughty or nice. None of the old rules
apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice
    in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa),
    but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter
    between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj)
    and a letter that repeats with exactly one letter between them (zxz).

    xxyxx is nice because it has a pair that appears twice and a letter
    that repeats with one between, even though the letters used by each
    rule overlap.

    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat
    with a single letter between them.

    ieodomkazucvgmuy is naughty because it has a repeating letter with one
    between (odo), but no pair that appears twice.

How many strings are nice under these new rules?
"""


def main():
    with open("data/day5input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            line = line.strip()

            # It contains a pair of any two letters that appears at least twice in
            # the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but
            # not like aaa (aa, but it overlaps).
            nice = False
            for i in range(len(line)-2):
                a = line[i:i+2]
                for j in range(i+2, len(line)-1):
                    b = line[j:j+2]
                    if a == b:
                        nice = True
                if nice:
                    break

            # It contains at least one letter which repeats with exactly one letter
            # between them, like xyx, abcdefeghi (efe), or even aaa.
            if nice:
                for i in range(len(line)-2):
                    a = line[i]
                    b = line[i+2]
                    if line[i] == line[i+2]:
                        break
                else:
                    nice = False

            if nice:
                count += 1
                print(line)
        print(count)


if __name__ == "__main__":
    main()
