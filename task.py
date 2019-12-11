import sys
import linecache


def handler(first_file: str, second_file: str):
    with open("out.txt", "w") as output:
        with open(first_file) as file:
            for line in file:
                name, positions = line.strip().split()
                positions = [int(num) for num in positions.split(",")]
                restoraunts = []
                for position in positions:
                    restoraunt = linecache.getline(second_file, position).strip().split(" ", 1)[1]
                    restoraunts.append(restoraunt)
                output.write(f"{name} {', '.join(restoraunts)}\n")


if __name__ == '__main__':
    handler(sys.argv[1], sys.argv[2])
