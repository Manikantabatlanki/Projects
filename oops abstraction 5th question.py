from abc import ABC,abstractmethod
class Document(ABC):
    def read(self):
        pass
    @abstractmethod
    def write(self):
        pass
class Letter(Document):
    def write(self):
        return 'letter is writinng'
    def read(self):
        return 'letter is areading'
class Report(Document):
    def write(self):
        return 'report is writing'
    def read(self):
        return 'report is readoing'


documents=[Letter(),Report()]
for document in documents:
    print(document.write())
    print(document.read())
