from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import os

def page_footer(canvas, doc):
    """
    Ajoute un numéro de page dans le pied de page.

    :param canvas: Le canevas utilisé pour dessiner sur la page.
    :param doc: Le document en cours de génération.
    """
    # Numéro de page actuel
    page_num = canvas.getPageNumber()

    # Dimensions de la page (largeur en points)
    page_width = A4[0]

    # Positionnement du texte (centré au bas de la page, 20 points du bas)
    canvas.drawCentredString(page_width / 2, 20, f"Page {page_num}")


def initialise_font():
    """
    Enregistre les polices Arial si elles ne sont pas déjà enregistrées.
    """
    # Liste des polices à vérifier et enregistrer
    fonts = [
        ('Arial', 'arial.ttf'),
        ('Arial-Bold', 'arialbd.ttf'),  # Gras
        ('Arial-Italic', 'ariali.ttf'),  # Italique
        ('Arial-BoldItalic', 'arialbi.ttf')  # Gras Italique
    ]

    for font_name, font_file in fonts:
        # Vérifie si la police est déjà enregistrée
        if font_name not in pdfmetrics.getRegisteredFontNames():
            try:
                # Enregistrer la police si non présente
                pdfmetrics.registerFont(TTFont(font_name, font_file))
            except Exception as e:
                print(f"Erreur lors de l'enregistrement de la police '{font_name}': {e}")


def validate_keys(data: dict, required_keys: list, section_name: str):
    """
    Vérifie que toutes les clés nécessaires sont présentes dans les données.
    :param data: Le dictionnaire de données à valider.
    :param required_keys: Liste des clés obligatoires.
    :param section_name: Nom de la section (pour les messages d'erreur).
    :raises ValueError: Si une clé est manquante.
    """
    if not data:
        raise ValueError(f"{section_name} data is empty")
    for key in required_keys:
        if key not in data:
            raise ValueError(f"{key} is missing in {section_name} data")

def validate_file_path(file_path: str):
    """
    Vérifie que le fichier existe et que le chemin est valide.
    :param file_path: Chemin du fichier à valider.
    :raises FileNotFoundError: Si le fichier n'existe pas.
    """
    if not file_path or not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

