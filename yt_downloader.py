import yt_dlp
import cv2

url = ""

def get_youtube_cap(url, format_id='22'):  # Default to '22' which is often 720p
    # Set up yt-dlp options to select a specific format by format_id
    ydl_opts = {
        'format': format_id,  # Use specific format ID
        'noplaylist': True,  # Avoid playlist download if a playlist URL is provided
        'quiet': True,  # Suppress output to keep it clean
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Get video information
        info_dict = ydl.extract_info(url, download=False)
        
        # Get the URL of the selected format
        video_url = next(
            (stream['url'] for stream in info_dict['formats'] if stream['format_id'] == format_id),
            None
        )
    
    if video_url is None:
        raise ValueError(f"Could not find a valid video stream with format_id {format_id}")
    
    # Open the video URL with OpenCV
    return cv2.VideoCapture(video_url)

#check_available formats
options = {
    'listformats': True,         # print a list of the formats to stdout and exit
}
with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])

# Example usage: Specify a format_id like '22' (typically 720p)
format_id = '22'  # You can change this to any valid format_id
cap = get_youtube_cap(url, format_id)

ret, frame = cap.read()

cap.release()