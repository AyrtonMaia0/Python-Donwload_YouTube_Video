#AYRTON MAIA

# To import the library pytubeflix
# In terminal : pip install pytubefix
# Run script

from pytubefix import YouTube
try:
    # Request Video URL
    yt = YouTube(str(input('Video URL: ')))

    # Check Video Availability
    yt.check_availability()

    # Print the Video Title
    print("Title:", yt.title)

    # Print the Thumbnail URL
    print("Thumbnail URL:", yt.thumbnail_url)

    # Get The Stream With The Best Resolution
    stream = yt.streams.get_highest_resolution()
    
    # Download The Video
    stream.download()
    print("Download completed successfully.")

except Exception as e:
    print("An error occurred:", e)