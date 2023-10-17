from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def extract_tags(url, tag_type):
    # Setup the ChromeDriver
    service = Service('path_to_chromedriver')  # replace 'path_to_chromedriver' with your chromedriver's path or remove if it's in PATH
    browser = webdriver.Chrome(service=service)
    
    browser.get(url)

    if tag_type == 'img':
        img_elements = browser.find_elements_by_tag_name('img')
        return [img.get_attribute('src') for img in img_elements]
    elif tag_type == 'video':
        a_elements = browser.find_elements_by_tag_name('a')
        return [a.get_attribute('href') for a in a_elements if a.get_attribute('href') and a.get_attribute('href').endswith('.mp4')]
    else:
        return f"Unsupported tag type: {tag_type}"
    finally:
        browser.quit()

if __name__ == "__main__":
    url = input("Enter the URL: ")
    tag_type = input("Which tag would you like to extract (img/video)? ").strip().lower()

    tags = extract_tags(url, tag_type)

    if isinstance(tags, list):
        for idx, tag in enumerate(tags, 1):
            print(f"{idx}. {tag}")
    else:
        print(tags)
