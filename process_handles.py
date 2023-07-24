import os
import pandas as pd

followers = pd.read_csv("./extracted_handles_list.csv")


def assign_account(row, followers):
    if row['username'] in followers:
        return True
    else:
        return False


sig_followers = followers.loc[(
    (followers['followersCount'] > 10000) | (followers['verified'] == True))]


for folder in os.listdir("input"):
    followers_file_path = os.path.join("input", folder, "followers.txt")
    if not os.path.isfile(followers_file_path):
        continue
    print(followers_file_path)
    with open(followers_file_path) as followers_file:
        followers = followers_file.read().split('\n')
        sig_followers[f"{folder}_follower"] = sig_followers.apply(
            lambda row: assign_account(row, followers), axis=1)


sig_followers.to_csv("./extracted_significant_followers.csv", index=False)
