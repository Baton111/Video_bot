import telebot
import yt_dlp
import os

tg_token = '7888913776:AAEB9cJgrdmt1TUxrfsq_6Aq-19s55Xn2fA'
bot = telebot.TeleBot(tg_token)
CHUNK_SIZE = 45 * 1024 * 1024


def split_file(filename, chunk_size):
    chunks = []
    base_name = os.path.splitext(filename)[0]
    with open(filename, 'rb') as f:
        part_num = 1
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            chunk_name = f'{base_name}_part{part_num}.mp4'
            with open(chunk_name, 'wb') as chunk_file:
                chunk_file.write(chunk)
            chunks.append(chunk_name)
            part_num += 1
    return chunks


def download_video(url):
    ydl_options = {
        'format': 'bestvideo[height<=480]+bestaudio/best',
        'outtmpl': 'video.%(ext)s',
        'quiet': True,
        'merge_output_format': 'mp4',
        'postprocessors': [{'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}],
        'ffmpeg_location': r'C:\Users\T-300\Desktop\ffmpeg-2025-03-31-git-35c091f4b7-full_build\bin\ffmpeg.exe',
    }
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Отправь ссылку на YouTube видео')


@bot.message_handler(func=lambda m: True)
def handle_url(message):
    try:
        video_path = download_video(message.text)
        file_size = os.path.getsize(video_path)

        if file_size > CHUNK_SIZE:
            chunks = split_file(video_path, CHUNK_SIZE)
            instructions = (
                "Видео разделено на части.\n\n"
            )
            bot.send_message(message.chat.id, instructions)

            for chunk in chunks:
                with open(chunk, 'rb') as f:
                    bot.send_document(message.chat.id, f, timeout=300)
                os.remove(chunk)
            os.remove(video_path)
        else:
            with open(video_path, 'rb') as video_file:
                bot.send_video(message.chat.id, video_file, timeout=300)
            os.remove(video_path)

    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка: {str(e)}')


bot.infinity_polling()
