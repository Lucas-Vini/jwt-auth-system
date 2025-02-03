class SignUpHandler():
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.message = None

    def register_user(self):
        if not self.is_strong_password():
            return {"error": self.message}, 422
        
        if not self.is_valid_username():
            return {"error": self.message}, 422
        
        if self.user_already_registered():
            return {"error": self.message}, 409
        
        self.create_user(self)
        return {"message": self.message}, 200
    
    def is_strong_password(self) -> bool:
        pass

    def is_valid_username(self) -> bool:
        pass

    def user_already_registered(self) -> bool:
        pass

    def create_user(self):
        pass