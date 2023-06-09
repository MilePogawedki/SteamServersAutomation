from typing import Optional


class WorkshopMod:
    def __init__(self, mod_id: int, mod_name: Optional[str] = None) -> None:
        self.mod_id = mod_id
        self.mod_name = mod_name

    def __str__(self):
        return f"{self.mod_id}:{self.mod_name}"

    def __repr__(self):
        return str(self)
