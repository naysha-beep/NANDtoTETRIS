# assembler.py

import sys

symbols = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576
}

for i in range(16):
    symbols[f"R{i}"] = i

dest_table = {
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}

jump_table = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

comp_table = {
    "0":"0101010",
    "1":"0111111",
    "-1":"0111010",
    "D":"0001100",
    "A":"0110000",
    "M":"1110000",
    "!D":"0001101",
    "!A":"0110001",
    "!M":"1110001",
    "-D":"0001111",
    "-A":"0110011",
    "-M":"1110011",
    "D+1":"0011111",
    "A+1":"0110111",
    "M+1":"1110111",
    "D-1":"0001110",
    "A-1":"0110010",
    "M-1":"1110010",
    "D+A":"0000010",
    "D+M":"1000010",
    "D-A":"0010011",
    "D-M":"1010011",
    "A-D":"0000111",
    "M-D":"1000111",
    "D&A":"0000000",
    "D&M":"1000000",
    "D|A":"0010101",
    "D|M":"1010101"
}


def clean_lines(filename):
    lines = []

    with open(filename, "r") as f:
        for line in f:
            line = line.split("//")[0].strip()
            if line:
                lines.append(line)

    return lines


def first_pass(lines):
    rom = 0

    for line in lines:
        if line.startswith("("):
            label = line[1:-1]
            symbols[label] = rom
        else:
            rom += 1


def second_pass(lines):
    result = []
    next_var = 16

    for line in lines:

        if line.startswith("("):
            continue

        if line.startswith("@"):
            symbol = line[1:]

            if symbol.isdigit():
                value = int(symbol)

            else:
                if symbol not in symbols:
                    symbols[symbol] = next_var
                    next_var += 1

                value = symbols[symbol]

            result.append(format(value, "016b"))

        else:
            dest = ""
            jump = ""
            comp = line

            if "=" in line:
                dest, comp = line.split("=")

            if ";" in comp:
                comp, jump = comp.split(";")

            try:
                binary = (
                   "111"
                    + comp_table[comp]
                    + dest_table[dest]
                 + jump_table[jump]
                         )
            except KeyError:
                print(f"Line: Invalid instruction -> {line}")
                return

            result.append(binary)

    return result


def main():

    asm_file = sys.argv[1]

    lines = clean_lines(asm_file)

    first_pass(lines)

    binary = second_pass(lines)

    out_file = asm_file.replace(".asm", ".hack")

    with open(out_file, "w") as f:
        for line in binary:
            f.write(line + "\n")

    print("Generated:", out_file)


if __name__ == "__main__":
    main()