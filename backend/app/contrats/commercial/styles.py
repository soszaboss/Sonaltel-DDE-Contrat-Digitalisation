from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

from backend.app.contrats.commercial.utils.functions import initialise_font


class PageStyles:
    """
    Classe contenant les styles et ParagraphStyles.
    """

    def __init__(self):
        self.styles = self.initialise_styles()




    def initialise_styles(self):

        styles = getSampleStyleSheet()

        # Initialiser les fonts s'ils ne sont pas initialisés
        initialise_font()

        # Titre principal
        title_style = self.get_title_style(bold=True)
        styles.add(title_style)

        # Sous-titres
        subtitle_style = self.get_subtitle_style(bold=True, space_before=32, space_after=32)
        styles.add(subtitle_style)

        # Texte normal (paragraphe)
        text_style = self.get_text_style(space_after=0, space_before=0, line_spacing=1.5, font_size=14)
        styles.add(text_style)

        # Intro style
        intro_style = self.get_intro_style()
        styles.add(intro_style)

        return styles

    @staticmethod
    def get_title_style(
        font_name: str = "Arial-Bold",
        font_size: int = 18,
        font_color: str = "black",
        alignment: int = 1,  # 0 = left, 1 = center, 2 = right
        line_spacing: float = 1.15,
        space_after: int = 24,
        space_before: int = 12,
        bold: bool = True,
    ) -> ParagraphStyle:
        """
        Définit le style des titres principaux du document.

        :param font_name: Nom de la police (par défaut Arial-Bold).
        :param font_size: Taille de la police (par défaut 18 points).
        :param font_color: Couleur de la police (par défaut noir).
        :param alignment: Alignement du texte (0 = gauche, 1 = centre, 2 = droite).
        :param line_spacing: Interligne relatif (par défaut 1.15).
        :param space_after: Espace après le titre (par défaut 24 points).
        :param space_before: Espace avant le titre (par défaut 12 points).
        :param bold: Mettre le texte en gras (par défaut True).
        :return: Style ParagraphStyle pour les titres.
        """
        return ParagraphStyle(
            name="TitleStyle",
            fontName=font_name,
            fontSize=font_size,
            textColor=font_color,
            alignment=alignment,
            leading=font_size * line_spacing,
            spaceAfter=space_after,
            spaceBefore=space_before,
            fontWeight="bold" if bold else "normal",
        )

    @staticmethod
    def get_subtitle_style(
        font_name: str = "Arial-Bold",
        font_size: int = 14,
        font_color: str = "black",
        alignment: int = 0,  # Alignement à gauche
        line_spacing: float = 1.15,
        space_after: int = 12,
        space_before: int = 12,
        bold: bool = True,
    ) -> ParagraphStyle:
        """
        Définit le style des sous-titres du document.

        :param font_name: Nom de la police (par défaut Arial-Bold).
        :param font_size: Taille de la police (par défaut 14 points).
        :param font_color: Couleur de la police (par défaut noir).
        :param alignment: Alignement du texte (0 = gauche, 1 = centre, 2 = droite).
        :param line_spacing: Interligne relatif (par défaut 1.15).
        :param space_after: Espace après le sous-titre (par défaut 12 points).
        :param space_before: Espace avant le sous-titre (par défaut 12 points).
        :param bold: Mettre le texte en gras (par défaut True).
        :return: Style ParagraphStyle pour les sous-titres.
        """
        return ParagraphStyle(
            name="SubtitleStyle",
            fontName=font_name,
            fontSize=font_size,
            textColor=font_color,
            alignment=alignment,
            leading=font_size * line_spacing,
            spaceAfter=space_after,
            spaceBefore=space_before,
            fontWeight="bold" if bold else "normal",
        )

    @staticmethod
    def get_text_style(
        font_name: str = "Arial",
        font_size: int = 12,
        font_color: str = "black",
        alignment: int = 0,  # Alignement à gauche
        line_spacing: float = 1.15,
        space_after: int = 6,
        space_before: int = 12,
        bold: bool = False,
    ) -> ParagraphStyle:
        """
        Définit le style du texte normal dans le document.

        :param font_name: Nom de la police (par défaut Arial).
        :param font_size: Taille de la police (par défaut 12 points).
        :param font_color: Couleur de la police (par défaut noir).
        :param alignment: Alignement du texte (0 = gauche, 1 = centre, 2 = droite).
        :param line_spacing: Interligne relatif (par défaut 1.15).
        :param space_after: Espace après le texte (par défaut 6 points).
        :param space_before: Espace avant le texte (par défaut 12 points).
        :param bold: Mettre le texte en gras (par défaut False).
        :return: Style ParagraphStyle pour le texte.
        """
        return ParagraphStyle(
            name="TextStyle",
            fontName=font_name,
            fontSize=font_size,
            textColor=font_color,
            alignment=alignment,
            leading=line_spacing * font_size,
            spaceAfter=space_after,
            spaceBefore=space_before,
            fontWeight="bold" if bold else "normal",
        )

    @staticmethod
    def get_intro_style():
        """
            Définit le style du texte normal dans le document.
            :return: Style ParagraphStyle pour le texte.
        """
        return ParagraphStyle(
            name="IntroStyle",
            fontName="Arial",
            fontSize=14,
            textColor="black",
            alignment=0,
            leading=1.5 * 14,
            spaceAfter=6,
            spaceBefore=12,
            fontWeight="normal",
        )

    @staticmethod
    def get_signature_styles():
        return {
            'DefaultStyle': ParagraphStyle(
                name='Default',
                fontName='Arial',
                fontSize=12,
                leading=15,
                spaceAfter=12
            ),
            'SignatureDefaultStyle': ParagraphStyle(
                name='SignatureDefault',
                fontName='Arial',
                fontSize=12,
                leading=15,
                spaceAfter=0
            ),
            'UnderlineStyle': ParagraphStyle(
                name='Underline',
                fontName='Arial',
                fontSize=12,
                leading=15,
                spaceAfter=12
            )
        }