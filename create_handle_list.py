import os
import json
from datetime import datetime

INPUT = "input"
OUTPUT = "output"


def process_folder(folder):
    followers = []
    for filename in os.listdir(folder):
        if filename[:9] != "followers" or filename[-4:] != "json":
            continue
        followers.extend(file_to_list(os.path.join(folder, filename)))
    # pd.DataFrame(followers).to_csv(os.path.join(folder, "followers.csv"), index=False))
    followers_string = '\n'.join(followers)
    with open(os.path.join(folder, "followers.txt"), 'w+') as file:
        file.write(followers_string)
    # List files in dir
    # if start with followers and and with json then process
    # output as csv file in folder
    return followers


def file_to_list(file):
    follower_list = json.load(open(file))
    return [f["string_list_data"][0]["value"] for f in follower_list]


all_followers = []

for folder in os.listdir(INPUT):
    all_followers.extend(process_folder(os.path.join(INPUT, folder)))

followers_deduplicated = list(dict.fromkeys(all_followers))

output_base = os.path.join(
    f"{OUTPUT}", f"{int(datetime.now().timestamp())}_all_follower_handles")


with open(f"{output_base}.txt", 'w+') as file:
    file.write('\n'.join(followers_deduplicated))

with open(f"{output_base}.json", 'w+') as file:
    file.write(json.dumps(followers_deduplicated))
