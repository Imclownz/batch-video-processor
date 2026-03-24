# Batch Video Processor

## Usage Examples

### Example 1: Basic Usage
```bash
python batch_video_processor.py --input input_video.mp4 --output output_video.mp4
```

### Example 2: Specify Format
```bash
python batch_video_processor.py --input input_video.mp4 --output output_video.avi --format avi
```

## Configuration Examples

### Example Configuration File
```json
{
  "video_quality": "1080p",
  "output_format": "mp4",
  "max_threads": 4
}
```

### Setting Environment Variables
```bash
export VIDEO_QUALITY=1080p
export OUTPUT_FORMAT=mp4
export MAX_THREADS=4
```
