import os
from collections import defaultdict


def load_log_files(directory):
    log_data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.log'):
            with open(os.path.join(directory, filename), 'r') as file:
                log_data[filename] = set(line.strip()
                                         for line in file if line.strip())
    return log_data


def find_common_in_all(log_data):
    if not log_data:
        return set()

    common_elements = set.intersection(*log_data.values())
    return common_elements


def write_results_to_file(common_elements, output_file):
    with open(output_file, 'w') as file:
        file.write("Elements found in all files:\n")
        for element in sorted(common_elements):
            file.write(f"{element}\n")


def main():
    directory = '/Users/dean/dev/gsoc'  # Replace with your directory path
    output_file = 'common_in_all_files.txt'  # Name of the output file

    log_data = load_log_files(directory)
    common_elements = find_common_in_all(log_data)

    write_results_to_file(common_elements, output_file)
    print(f"Results have been written to {output_file}")
    print(f"Number of common elements found in all files: {len(common_elements)}")


if __name__ == "__main__":
    main()
