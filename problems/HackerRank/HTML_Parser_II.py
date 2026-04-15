from html.parser import HTMLParser

class myHTMLParsar(HTMLParser):
    
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
        else:
            print('>>> Single-line Comment')
            print(data)

    def handle_data(self, data):
        if data.stripe():
            print(">>> Data")
            print(data)

parsar = myHTMLParsar()
N = int(input())
for _ in range(0, N):
    line = input()
    parsar.feed(line)
