from dataclasses import dataclass

@dataclass
class Connessione:
    user1: str
    user2: str
    peso: int

    def __str__(self):
        return f"{self.user1} ,{self.user2}, {self.peso}"

    def __repr__(self):
        return f"{self.user1} ,{self.user2}, {self.peso}"

    def __hash__(self):
        return hash((self.user1, self.user2))

