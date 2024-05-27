from pytube import YouTube

from config import LINKS_FILE, DOWNLOADED_PATH, MAX_RESOLUTION

def get_lines_from_txt(txt_file:str) -> list:
    with open(txt_file, 'r') as file:
        lines = []
        for i in file:
            line = i.strip()
            lines.append(line)
        file.close()
    return lines

def main():
    links = get_lines_from_txt(LINKS_FILE)
    print(links)

if __name__ == '__main__':
    main()
