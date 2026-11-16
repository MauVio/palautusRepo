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
        if len(username) <3:
            raise UserInputError("Username should be atleat 3 chars long")
       
        if re.search(r"[åäöÅÄÖ]", username):
            raise UserInputError("Username can only contain letters a-z")

        if not ((re.search(r"[A-Za-z]", password) and (re.search(r"[0-9]", password)))):
            raise UserInputError("Password should have letters and numbers")

        if len(password) <8:
            raise UserInputError("Password should be atleast 8 chars long")


        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
