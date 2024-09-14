data = {
    "Name": "Ilya",
    "age": 30,
    "email": "text@gmail.com"
}

class Data:
    name: str
    age: int
    email: str

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.validate()

    def validate(self):
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("Имя должно быть не пустой строкой")

        if not isinstance(self.age, int) or not 0 <= self.age <= 100:
            raise ValueError("Возраст должен быть целым числом от 0 до 100")

        if not isinstance(self.email, str):
            try:
                mail, domain = self.email.split("@")
                subdomain, postdomain = domain.split(".")
            except Exception as e:
                raise ValueError("Некорректная почта")


d = Data("Ilya", -10, "text@gmail.com")