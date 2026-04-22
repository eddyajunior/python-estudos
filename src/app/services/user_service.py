from app.models.user import UserCreate

class UserService:

    def create_user(self, user: UserCreate):
        # aqui entraria regra real (validação, integração, etc.)
        return {
            "message": f"Usuário {user.name} criado com sucesso!",
            "data": user
            } 