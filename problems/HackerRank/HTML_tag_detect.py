from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"{tag}")
        for attr, value in attrs:
            print(f'-> {attr} > {value}')
        
    def handle_startendtag(self, tag, attrs):
        print(f"{tag}")
        for attr, value in attrs:
            print(f'-> {attr} > {value}')


my_parser = myHTMLParser()

N = int(input())
for _ in range(N):
    my_parser.feed(input())