class SignUpHandler():
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.message = None

    def register_user(self):
        if not self.is_valid_password():
            return {"error": self.message}, 422
        
        if not self.is_valid_username():
            return {"error": self.message}, 422
        
        if self.user_already_registered():
            return {"error": self.message}, 409
        
        self.create_user(self)
        return {"message": self.message}, 200
    
    def is_valid_password(self) -> bool:
        if not isinstance(self.password, str):
            self.message = "Password must be string"
            return False
        if len(self.password) < 8:
            self.message = "Password must have at least 8 characters"
            return False
        if len(self.password) > 32:
            self.message = "Password must have at most 32 characters"
            return False
        if not any(char.isdigit() for char in self.password):
            self.message = "Password must have at least one digit (0-9)"
            return False
        if not any(not char.isalnum() for char in self.password):
            self.message = "Password must have at least one special characters like !@#$%¨&*()<>: or others"
            return False

    def is_valid_username(self) -> bool:
        if len(self.username) > 0:
            self.message = "Password must have at least 8 characters"

    def user_already_registered(self) -> bool:
        pass

    def create_user(self):
        pass