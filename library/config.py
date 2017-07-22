"""Config file."""

port = 8124

# library config

media_folder = "/media/hdd1/TV"
root_items = [{"name": "The-Flash", "target": "/media/hdd1/TV/The-Flash"},
              {"name": "Test", "target": "/home/alexander/tmp/test-media"},
              {"name": "TBBT", "target": "/media/hdd1/TV/The-Big-Bang-Theory"}]


# transcoder config

ffmpeg = "ffmpeg"

types = {
    "mp3": "audio",
    "jpg": "image",
    "mp4": "video"}


transcode_mime = {
    "*": "video/mp4",
    "mp3": "audio/mp3",
    "jpg": "image/jpg"}


ffmpeg_transcode_args_2 = {
    "*": ["-f", "mp4", "-strict", "experimental", "-preset", "ultrafast", "-movflags", "frag_keyframe+empty_moov+faststart", "pipe:1"],
    "mp3": ["-f", "mp3", "-codec", "copy", "pipe:1"]}

ffmpeg_transcode_args = {
    "*": " -ss {} -i {} -f {} -vcodec {} -acodec {} -strict experimental -preset ultrafast -movflags frag_keyframe+empty_moov+faststart pipe:1",
    "mp3": ["-f", "mp3", "-codec", "copy", "pipe:1"]}

ffmpeg_poster_args = ["-f", "mjpeg", "-vf", "scale=512x512", "pipe:1"]
# "-noaccurate_seek"
