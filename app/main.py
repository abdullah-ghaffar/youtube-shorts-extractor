import os
from extractor import extract_shorts_links, save_links_to_file

def main():
    channel_url = input("Enter the YouTube Shorts channel URL: ")  # e.g., https://www.youtube.com/@ChannelName/shorts
    shorts_links = extract_shorts_links(channel_url)

    if shorts_links:
        print(f"\n{len(shorts_links)} Shorts video links found.")
        
        # Set the filename to save
        filename = input("Enter the filename to save the links (e.g., shorts_links.txt): ")
        
        # Construct the full path to save in the current directory
        file_path = os.path.join(os.getcwd(), filename)

        # Ensure the file path is not empty before saving
        if file_path:
            save_links_to_file(shorts_links, file_path)
            print(f"\nAll links have been saved to '{file_path}'.")
        else:
            print("No file path provided. The process has been canceled.")
    else:
        print("No Shorts links found.")

if __name__ == "__main__":
    main()
