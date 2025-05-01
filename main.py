import subprocess as sub
import requests


def main():
    with open("modlist.md", "r") as file:
        line = file.readline()
        while line:
            url = line.strip().split("(")[1].replace(")", "")
            r = requests.head(url, allow_redirects=True)
            print(f"Checking {r.url}...")
            if 'modrinth' in url:
                command = f"packwiz modrinth install {url} -y"
                sub.run(command, shell=True)
            elif 'curseforge' in url:
                command = f"packwiz curseforge install {url} -y"
                sub.run(command, shell=True)
            line = file.readline()
    print("All mods installed successfully!")


if __name__ == "__main__":
    main()
