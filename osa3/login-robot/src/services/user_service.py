from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3:
                    raise UserInputError("Username must be at least 3 letters")

        if not re.match("^[a-z]+$", username):
            raise UserInputError("Username invalid, use only letters a-z")

        if len(password) < 8:
            raise UserInputError("Password must be at least 8 letters")

        if not re.match("^.*[^a-zA-Z].*$", password):
            raise UserInputError("Password must contain numbers or special characters")

        
