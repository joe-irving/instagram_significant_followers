# Instagram Follower Data Processing

1. Download follower data using the Instagram data export function, and using the JSON format
2. Place the followers JSON files as described by the input.example folder in a folder called "input"
3. Run `python create_handle_list.py`
4. Upload the handle list to this worker: https://console.apify.com/actors/dSCLg0C3YEZ83HzYX
5. Download the result as a csv, copy it into the base directory and call it "extracted_handles_list.csv"
6. Run `python process_handles.py` to link the handles up to the list of account, and filter for only significant followers