from html.parser import HTMLParser

class myHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        
        for attr, value in attrs:
            print(f"-> {attr} > {value}")
        
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")

        for attr, value in attrs:
            print(f"-> {attr} > {value}")

    # def handle_data(self, data):
    #     print(f"Data : {data}")

parser = myHTMLParser()
# parser.feed("<html><head><title>HTML Parser - I</title></head>"
#             "<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>")

N = int(input())
for _ in range(0, N):
    parser.feed(input())
    
