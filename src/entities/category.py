class Category:
    """Luokka, joka määrittelee aihenkategorian.

    Attributes:
        title: Merkkijonoarvo, joka kuvaa kategorian nimeä.
    """
    def __init__(self, title):
        """Luokan konstruktori, joka luo uuden kategorian.

        Args:
            title: Merkkijonoarvo, joka kuvaa kategorian nimeä.
        """

        self.title = title

    def __repr__(self):
        return f"{self.title}"
