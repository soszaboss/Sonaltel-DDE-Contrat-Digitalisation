from typing import Union
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Frame

class PageSpacePaddingFrame:
    """
    Classe contenant les styles et configurations pour les marges et paddings.
    """

    @staticmethod
    def padding(
        left_padding: Union[int, float] = 0.5,
        right_padding: Union[int, float] = 0.5,
        top_padding: Union[int, float] = 0.5,
        bottom_padding: Union[int, float] = 0.5,
    ) -> dict:
        """
        Définit les paddings du document en pouces.

        :param left_padding: Padding gauche (par défaut 0.5 pouce).
        :param right_padding: Padding droit (par défaut 0.5 pouce).
        :param top_padding: Padding haut (par défaut 0.5 pouce).
        :param bottom_padding: Padding bas (par défaut 0.5 pouce).
        :return: Dictionnaire des paddings en points (72 points = 1 pouce).
        """
        return {
            "leftPadding": left_padding * inch,
            "rightPadding": right_padding * inch,
            "topPadding": top_padding * inch,
            "bottomPadding": bottom_padding * inch,
        }

    @staticmethod
    def margins(
        left_margin: Union[int, float] = 0.75,
        right_margin: Union[int, float] = 0.75,
        top_margin: Union[int, float] = 1.0,
        bottom_margin: Union[int, float] = 1.0,
    ) -> dict:
        """
        Définit les marges du document en pouces.

        :param left_margin: Marge gauche (par défaut 0.75 pouce).
        :param right_margin: Marge droite (par défaut 0.75 pouce).
        :param top_margin: Marge haute (par défaut 1.0 pouce).
        :param bottom_margin: Marge basse (par défaut 1.0 pouce).
        :return: Dictionnaire des marges en points (72 points = 1 pouce).
        """
        return {
            "leftMargin": left_margin * inch,
            "rightMargin": right_margin * inch,
            "topMargin": top_margin * inch,
            "bottomMargin": bottom_margin * inch,
        }

    @staticmethod
    def create_frame(padding_values: dict, a4_format: bool = False, **kwargs):
        """
        Crée un cadre (Frame) avec des valeurs de padding et des dimensions personnalisées ou A4.

        Arguments :
            padding_values (dict) : Dictionnaire contenant les paddings (left, right, top, bottom).
            a4_format (bool) : Utilise le format A4 si True.
            **kwargs : Dimensions personnalisées pour width et height si a4_format est False.

        Retourne :
            Frame : Objet Frame avec les dimensions et padding spécifiés.

        Exceptions :
            ValueError : Si width/height manquent ou padding_values n'est pas correctement formaté.
        """
        if not padding_values:
            raise ValueError("padding_values is missing or empty.")

        if a4_format:
            # Utilise le format A4
            return Frame(0, 0, *A4, **padding_values)
        else:
            # Dimensions personnalisées
            width = kwargs.get('width')
            height = kwargs.get('height')

            if width is None or height is None:
                raise ValueError("Height or width is missing.")

            if not isinstance(width, (float, int)) or not isinstance(height, (float, int)):
                raise ValueError("Width and height must be of type float or int.")

            return Frame(0, 0, width, height, **padding_values)


