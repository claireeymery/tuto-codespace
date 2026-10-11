"""Ce module fournit une fonction pour calculer une moyenne de valeurs."""

from rich.markdown import Markdown
from rich.console import Console


def moyenne(valeurs):
    """
    # Calcule la moyenne des valeurs.

    **Paramètres**
    - `valeurs` : valeurs dont on veut calculer la moyenne

    **Retour**
    - la moyenne des valeurs

    **Exceptions**
    - `ValueError` : si la liste est vide
    """
    return sum(valeurs) / len(valeurs)


if __name__ == "__main__":
    Console().print(Markdown(moyenne.__doc__))
    print("moyenne([10, 20, 15]) :", end=" ")
    print(moyenne([10, 20, 15]))
    