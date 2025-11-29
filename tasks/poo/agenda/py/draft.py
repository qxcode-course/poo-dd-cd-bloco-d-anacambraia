class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def isValid(self) -> bool:
        valid = "0123456789()."
        return all(c in valid for c in self.number)

    def __str__(self):
        return f"{self.id}:{self.number}"

    def toString(self) -> str:
        return self.__str__()

class Contact:
    def __init__(self, name : str):
        self.name = name
        self.favorited = False
        self.fones: list[Fone] = []

    def addFone(self, id: str, number: str):
        f = Fone(id, number)
        if f.isValid():
            self.fones.append(f)
        else:
            print("fail: número inválido")

    def rmFone(self, index: int):
        if 0 <= index < len(self.fones):
            self.fones.pop(index)
        else:
            print("fail: índice inválido")

    def toggleFavorited(self):
        self.favorited = not self.favorited

    def isFavorited(self) -> bool:
        return self.favorited

    def getName(self) -> str:
        return self.name

    def getFones(self):
        return self.fones

    def __str__(self):
        prefix = "@" if self.favorited else "-"
        fones_str = ", ".join(str(f) for f in self.fones)
        return f"{prefix} {self.name} [{fones_str}]"

    def toString(self):
        return self.__str__()

class Agenda:
    def __init__(self):
        self.contacts : list[Contact] = []

    def findPosByName(self, name: str) -> int:
        for i, c in enumerate(self.contacts):
            if c.getName() == name:
                return i

        return -1

    def addContact(self, name: str, fones: list[Fone]):
        pos = self.findPosByName(name)

        if pos == -1:
            c = Contact(name)
            self.contacts.append(c)
            self.contacts.sort(key=lambda x: x.getName())
            pos = self.findPosByName(name)

        for f in fones:
            if f.isValid():
                self.contacts[pos].addFone(f.id, f.number)
            else:
                print("fail: número inválido")
    def getContact(self, name: str):
        pos = self.findPosByName(name)
        return self.contacts[pos] if pos != -1 else None

    def rmContact(self, name: str):
        pos = self.findPosByName(name)
        if pos == -1:
            print("fail: contato não existe")
            return
        self.contacts.pop(pos)

    def search(self, pattern: str):
        result = []
        for c in self.contacts:
            if pattern in c.getName():
                result.append(c)
                continue

            for f in c.getFones():
                if pattern in f.id or pattern in f.number:
                    result.append(c)
                    break

        return result

    def getFavorited(self):
        return [c for c in self.contacts if c.isFavorited()]

    def getContacts(self):
        return self.contacts

    def __str__(self):
        return "\n".join(str(c) for c in self.contacts)

    def toString(self):
        return self.__str__()

def main():
    agenda = Agenda()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "add":
            name = args[1]
            fones = []
            for item in args[2:]:
                id, num = item.split(":")
                fones.append(Fone(id, num))
            agenda.addContact(name, fones)
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "rmFone":
            name = args[1]
            index = int(args[2])
            contact = agenda.getContact(name)
            contact.rmFone(index)
        elif args[0] == "rm":
            agenda.rmContact(args[1])
        elif args[0] == "search":
            pattern = args[1]
            res = agenda.search(pattern)
            for c in res:
                print(c)
        elif args[0] == "tfav":
            c = agenda.getContact(args[1])
            c.toggleFavorited()

main()