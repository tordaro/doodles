import csv
from typing import Any

Record = dict[str, Any]

INPUT_FILE = "data.csv"
OUTPUT_FILE = "processed.csv"
OUTPUT_HEADER = ["name", "status", "is_active"]


def read_csv(filename: str) -> list[Record]:
    with open(filename) as f:
        reader = csv.DictReader(f)
        return list(reader)


def process_data(row: Record) -> Record:
    row_copy = row.copy()
    row_copy["is_active"] = row_copy["status"] == "active"
    return row_copy


def write_csv(filename: str, processed_data: list[Record], header: list[str]) -> None:
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(processed_data)


def main() -> None:
    data = read_csv(INPUT_FILE)
    processed_data = [process_data(row) for row in data]
    write_csv(OUTPUT_FILE, processed_data, OUTPUT_HEADER)


if __name__ == "__main__":
    main()
