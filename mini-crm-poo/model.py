from datetime import date


class Lead:

    def __init__(self,
                 name: str,
                 company: str,
                 email: str,
                 stage: str,
                 created_at: str = None):
        self.name = name
        self.company = company
        self.email = email
        self.stage = stage
        self.created_at = created_at or date.today().isoformat()

    def is_valid(self) -> bool:
        return bool(self.name) and bool(self.email) and ("@" in self.email)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "create": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Lead":
        return cls(
            name=data.get("name", ""),
            company=data.get("company", ""),
            email=data.get("email", ""),
            stage=data.get("stage", ""),
            created_at=data.get("create"),
        )

    def __repr__(self) -> str:
        return f"Lead(name='{self.name}', company='{self.company}', email='{self.email}', stage='{self.stage}')"