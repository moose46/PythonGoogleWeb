import csv
from collections import namedtuple
from pathlib import Path

DATE_FORMAT = '%m-%d-%Y'
file_path = Path.cwd() / "data"
file_path_new = Path.cwd() / "data1"
# when running on python anywhere
print(f"{file_path}\n{file_path_new}")
if not file_path.exists():
    file_path = Path.cwd() / "beerme" / "data"
    log_file = Path.cwd() / 'files_log.txt'
print(f"{file_path}\n{file_path_new}")
# exit()

for src in file_path.glob("results*.txt"):
    race_track = src.stem.split('_')[1]
    race_date = src.stem.split("_")[2]
    mdy = src.stem.split("_")[2]
    year = mdy.split("-")[2]
    day = mdy.split("-")[1]
    month = mdy.split("-")[0]
    # print(f"{race_track}_{year}{month}{day}")
    dst_filename = race_track + "_" + year + month + day + ".txt"

    with open(Path(f'{src.parent}/{src.name}'), 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        # csv file must have header
        rawResult = namedtuple("rawResult", next(reader), rename=True)
        # Result = namedtuple('Result', [*rawResult._fields, 'picked_by', 'race_date', 'race_track'])
        file_path_new = Path.cwd().joinpath("data1", dst_filename)
        delim = "\t"
        try:
            with open(file_path_new, "w") as fid:
                for row in reader:
                    fid.write(delim.join(row) + "\n")
                    result = rawResult(*row)
                    print(result)
        except Exception as e:
            print(e)
            exit(-1)
