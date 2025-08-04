# Video DRM Downloader Bot

A Telegram bot that can download and process DRM-protected videos, split large files, and handle various video formats.

## Features
- Appx Zip Video Downloader 
- Appx Signed Url Downloader
- Classplus Automatic Token Generator Added
- Classplus /Study IQ New DRM Downloader
- Download with Multiple Task at 1 time
- Upload Video From Log Database 
- Topic Name Defined in Caption
- Utkarsh + Youtube Code Added
- Download DRM-protected videos from various sources
- Support for m3u8, mpd, and other streaming formats
- Automatic video splitting for files larger than 2GB
- Custom watermark overlay support
- Thumbnail generation
- Progress tracking during uploads
- Premium user system
- Admin controls

## Requirements

- Python 3.8+
- FFmpeg
- N_m3u8DL-RE
- aria2c
- yt-dlp

## Installation

1. Clone the repository:

```

2. Install dependencies:

```

3. Configure environment variables in `config.py`:


## Deploy to Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?&template=https://github.com/username/reponame)

## Usage

1. Start the bot:

2. Send video URLs to the bot in any of these formats:
- Direct video links
- m3u8 links
- MPD streams
- Encrypted URLs (m3u8://:encrypted_url)

3. For files larger than 2GB, the bot will automatically:
- Split the video into 1GB parts
- Upload each part separately
- Add part numbers to captions
- Clean up temporary files

## Supported Platforms

- Regular video hosting sites
- DRM-protected streams
- M3U8 streams
- DASH/MPD streams
- Zoom recordings
- Appx Zip+Encrypted URLs(Uhs 2.00 and 3.00)
- Appx Encrypted PDF (All)
- Classplus DRM and Non-DRM content
- PhysicsWallah DRM content
- CareerWill and PDF content
- Khan GS content
- Study IQ DRM content
- APPX and APPX Encrypted PDF
- Brightcove protected content
- Visionias protected content
- Utkarsh content (Video + PDF)
- Non-DRM and AES Encrypted URLs
- MPD URLs with known keys
- Custom platforms with encryption

## Commands

### User Commands
- `/start` - Start the bot and check subscription status
- `/stop` - Stop the bot (Premium/Admin only)
- `/txt` - Access premium features (Premium users)
- `/myplan` - View your premium plan details and remaining time
- `/id` - Get your chat ID

### Admin Commands
- `/admin` - Access admin controls (Admin only)
- `/auth [user_id] [days]` - Add premium access for a user
- `/remove [user_id]` - Remove premium access from a user
- `/authlist` - List all premium users and their expiry dates
- `/status` - Get total number of subscribers
- `/broadcast [message]` - Send message to all subscribers
- `/broadcast -v` - Broadcast video/photo to all subscribers

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
```

This README provides:

1. A clear description of what the bot does
2. Key features list
3. Installation instructions
4. Deployment options
5. Usage instructions
6. Supported platforms
7. Available commands
8. Contributing guidelines
9. License information

You can customize this further by:
- Adding specific setup instructions for your environment
- Including screenshots or examples
- Adding troubleshooting guides
- Listing any specific dependencies or requirements
- Adding contact information or support channels

Let me know if you'd like me to modify any section or add more details!
```

</rewritten_file>