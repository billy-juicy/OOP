from wsgiref.validate import validator


class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserValidator:

    def valid_username(self, username):
        if not username:
            raise ValueError("Username не должен быть пустым!")
        if len(username) < 3:
            raise ValueError("Username должен состоять из более 3 символов!")
        if " " in username:
            raise ValueError("Username не должен содержать пробелов!")
        return True

    def valid_email(self, email):
        if not email:
            raise ValueError("Email не должен быть пустым!")
        if "@" not in email or "." not in email:
            raise ValueError("Неверный формат email!")
        return True


class UserRepository:

    def save_user(self, user):
        print(f"Сохранение пользователя {user.username} в базу данных!")

    def get_user_by_id(self, user_id):
        print(f"Получение юзера по {user_id}")


class EmailService:

    def send_welcome_email(self, user):
        print(f"Отправить приветственное письмо на почту {user.email}")


def register_user(username, email):
    user = User(username, email)

    validator = UserValidator()
    repository = UserRepository()
    email_service = EmailService()

    try:
        validator.valid_username(user.username)
        validator.valid_email(user.email)
        repository.save_user(user)
        email_service.send_welcome_email(user)
        print("Успешная регистрация пользователя!")
        return user
    except ValueError as e:
        print(f"Регистрация провалена: {e}")
        return None

good_user = register_user("John_Long", "cranton@gmail.com")
print()
bad_user = register_user("Joe", "clanton.email.com")
