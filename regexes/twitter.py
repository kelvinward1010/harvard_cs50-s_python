import re


def info_twitter_1():
    url = input("URL: ").strip()
    #username = url.replace("https://twitter.com/", "")
    
    parttent_1 = r"^https?://(www\.)?twitter\.com/"
    parttent_2 = r"^(https?://)?(www\.)?twitter\.com/"
    parttent_3 = r"^https?://(www\.)?twitter\.com/(.+)$"
    
    username = re.sub(parttent_2, "", url)
    
    print(f"Username: {username}")
    
def info_twitter_2():
    url = input("URL: ").strip()
    
    parttent_3 = r"^https?://(?:www\.)?twitter\.com/(.+)$"
    parttent_4 = r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$"
    
    #matches = re.search(parttent_3, url, re.IGNORECASE)
    
    if matches := re.search(parttent_4, url, re.IGNORECASE):
        print(f"Username: {matches.group(1)}")
    

if __name__ == "__main__":
    info_twitter_2()