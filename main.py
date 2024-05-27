from pytube import YouTube

from config import LINKS_FILE, DOWNLOADED_PATH, MAX_RESOLUTION

def main():
    with open(LINKS_FILE, 'r') as file:
        links = []
        for line in file:
            link = line.strip()
            links.append(link)
        file.close()
    print(links)

if __name__ == '__main__':
    main()
