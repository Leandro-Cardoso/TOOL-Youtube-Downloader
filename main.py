from pytube import YouTube

from config import LINKS_FILE, MAX_RESOLUTION, OUTPUT_PATH

def get_lines_from_txt(txt_file:str) -> list:
    with open(txt_file, 'r') as file:
        lines = []
        for i in file:
            line = i.strip()
            lines.append(line)
        file.close()
    return lines

def convert_to_filename(name:str, format:str) -> str:
    filename = str(name)
    filename = filename.lower()
    filename = filename.replace(' ', '_')
    valid_chars = 'abcdefghijklmnopqrstuvwxyz0123456789_-'
    valid_filename = ''
    for char in filename:
        if char in valid_chars:
            valid_filename += char
    filename = valid_filename
    if '.' in format:
        filename += str(format)
    else:
        filename += '.' + str(format)
    return filename

def main():
    links = get_lines_from_txt(LINKS_FILE)
    print('\n')
    for link in links:
        try:
            yt = YouTube(link)
            stream = yt.streams.filter(resolution = MAX_RESOLUTION).first()
            title = yt.title
            format = 'mp4'
            filename = convert_to_filename(title, format)
            stream.download(output_path = OUTPUT_PATH, filename = filename)
            print(f'Downloaded: {filename}')
        except Exception as e:
            print(f'Erro: {link} -> {e}')
    print('\n')

if __name__ == '__main__':
    main()
