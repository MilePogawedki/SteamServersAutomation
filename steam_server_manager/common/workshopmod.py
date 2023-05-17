class WorkshopMod:
    def __init__(self, mod_id: int, mod_name: str) -> None:
        self.mod_id = mod_id
        self.mod_name = mod_name

    def __str__(self):
        return f"{self.mod_id}:{self.mod_name}"

    def __repr__(self):
        return str(self)

    @property
    def simplified_mod_name(self) -> str:
        return self.mod_name.translate(
            {
                ord("-"): "_",
                ord(" "): "_",
                ord("("): "_",
                ord(")"): "_",
            }
        )
