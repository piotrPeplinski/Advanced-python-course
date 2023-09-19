class AddTags:
    def __init__(self, tag):
        self.__tag = tag

    def __enter__(self):
        print(f'<{self.__tag}>')
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f'</{self.__tag}>')

with AddTags('h1'):
    print('Hello world')
    print('Python is awesome')

print('po con managarze')