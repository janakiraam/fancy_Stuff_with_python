#install moviepy library and run this code GIF will be generated

from moviepy.editor import VideoFileClip
clip=VideoFileClip('video.mp4')
clip.write_gif("mygif.gif")