import subprocess

class VideoProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def edit_video(self, filters):
        cmd = ['ffmpeg', '-i', self.input_file, '-vf', filters, self.output_file]
        subprocess.run(cmd)

    def overlay_subtitle(self, subtitle_file):
        cmd = ['ffmpeg', '-i', self.input_file, '-vf', f'subtitles={subtitle_file}', self.output_file]
        subprocess.run(cmd)

    def hard_subtitle(self, subtitle_file):
        cmd = ['ffmpeg', '-i', self.input_file, '-vf', f'subtitles={subtitle_file}:force_style="Alignment=10"', self.output_file]
        subprocess.run(cmd)

# Example usage:
# processor = VideoProcessor('input.mp4', 'output.mp4')
# processor.edit_video('scale=1280:720')
# processor.overlay_subtitle('sub.srt')
# processor.hard_subtitle('sub.srt')