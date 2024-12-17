from reportlab.platypus import Paragraph, Image
from reportlab.lib.styles import ParagraphStyle
from datetime import datetime
from reportlab.lib.units import inch
import os

from backend.app.contrats.commercial.styles import PageStyles
from backend.app.contrats.commercial.utils.functions import validate_keys, validate_file_path


class PageComponents:
    def __init__(self):
        """
        Initialise la classe avec les clés nécessaires et les styles de paragraphes.
        """
        # Clés nécessaires pour chaque section
        self.intro_keys = ['company_name', 'company_status', 'company_jurisdiction',
                           'company_address', 'client_name', 'client_jurisdiction', 'client_address']
        self.termination_keys = ['termination_notice', 'termination_remedy']
        self.law_keys = ['applicable_law', 'arbitration_rules']

        # Styles des paragraphes
        self.signature_styles = PageStyles().get_signature_styles()


    def intro(self, intro_data: dict, styles):
        """
        Crée l'introduction du contrat avec les données dynamiques fournies.

        :param intro_data: Dictionnaire contenant les informations de l'introduction.
        :param styles: Dictionnaire des styles pour formater les paragraphes.
        :return: Liste d'objets Paragraph.
        :raises ValueError: Si les données nécessaires sont absentes.
        """
        validate_keys(intro_data, self.intro_keys, "Intro")

        today = datetime.today()
        formatted_date = today.strftime("%d/%m/%Y")
        
        items = [
            Paragraph(f"Ce Contrat Commercial (« Contrat ») est conclu à ce <b>{formatted_date}</b> ...", styles['IntroStyle']),
            Paragraph(f"<b>{intro_data['company_name']}</b>, une <b>{intro_data['company_status']}</b> organisée selon les lois de "
                      f"<b>{intro_data['company_jurisdiction']}</b> avec son principal lieu d'activité à "
                      f"<b>{intro_data['company_address']}</b> (« Votre entreprise »),", styles['IntroStyle']),
            Paragraph("et", styles['IntroStyle']),
            Paragraph(f"<b>{intro_data['client_name']}</b>, une <b>{intro_data['client_status']}</b> organisée selon les lois de "
                      f"<b>{intro_data['client_jurisdiction']}</b> avec son principal établissement à "
                      f"<b>{intro_data['client_address']}</b> (« Client »)", styles['IntroStyle'])
        ]
        return items

    def services_section(self, ser: str):
        """
        Création de la section des services avec les données dynamiques.
        :param ser: Description des services.
        :return: Texte formaté pour la section des services.
        """
        if not ser:
            raise ValueError("services_data is empty")
        return f"""
        Votre Société s'engage à fournir les services suivants au Client : <b>{ser}</b>.
        """

    def termination_section(self, termination_data: dict):
        """
        Création de la section de termination avec les données dynamiques fournies.
        :param termination_data: Dictionnaire contenant les informations de termination.
        :return: Texte formaté pour la section de termination.
        """
        validate_keys(termination_data, self.termination_keys, "Termination")
        return f"""
        Chacune des parties peut résilier le présent Contrat moyennant un préavis de 
        <b>{termination_data['termination_notice']} jours</b>. En cas de manquement, l'autre partie disposera de 
        <b>{termination_data['termination_remedy']} jours</b> pour remédier au problème.
        """

    def generate_signatures_section(self, signatures_data: dict, styles):
        """
        Génère les paragraphes pour la section des signatures.
        :param signature_image_path: Chemin de l'image de la signature.
        :param signatures_data: Dictionnaire contenant les données de l'entreprise et du client.
        :param styles: Dictionnaire des styles.
        :return: Liste de Paragraphs et Images.
        """
        signature_image_path = "../../assets/images/signatures/signature-40127.png"
        validate_keys(signatures_data,
                           ['company_name', 'company_email', 'company_address', 
                            'company_registration', 'client_name', 'client_email', 'client_address'], 
                           "Signatures")
        validate_file_path(signature_image_path)

        signature_image = Image(signature_image_path, width=1.5 * inch, height=0.5 * inch)
        items = []

        # Section Entreprise
        items.append(Paragraph("<b>ENTREPRISE</b>", styles['SubtitleStyle']))
        items.append(Paragraph(f"<u>{signatures_data['company_name']}</u>", self.signature_styles['UnderlineStyle']))
        items.append(Paragraph(f"Par: <u>_________________________</u>", self.signature_styles['DefaultStyle']))
        items.append(signature_image)
        items.append(Paragraph(f"Signature: <u>___________________________________________</u>", self.signature_styles['DefaultStyle']))
        items.append(Paragraph(f"E-mail: <u>{signatures_data['company_email']}</u>", self.signature_styles['DefaultStyle']))
        items.append(Paragraph(f"Adresse: <u>{signatures_data['company_address']}</u>", self.signature_styles['DefaultStyle']))
        items.append(Paragraph(" ", self.signature_styles['DefaultStyle']))

        # Section Client
        items.append(Paragraph("<b>CLIENT</b>", styles['SubtitleStyle']))
        items.append(Paragraph(f"Nom du Client: <u>{signatures_data['client_name']}</u>", self.signature_styles['DefaultStyle']))
        items.append(Paragraph(f"Signature: <u>_________________________</u>", self.signature_styles['DefaultStyle']))
        items.append(Paragraph(f"E-mail: <u>{signatures_data['client_email']}</u>", self.signature_styles['DefaultStyle']))
        items.append(Paragraph(f"Adresse: <u>{signatures_data['client_address']}</u>", self.signature_styles['DefaultStyle']))
        items.append(Paragraph(" ", self.signature_styles['DefaultStyle']))

        return items

    def compensation_section(self, compensation: str):
        """
            Création de la section de compensation,
            avec les données dynamiques fournies par l'utilisateur.
        """
        
        if not compensation:
            raise ValueError("compensation is empty")
        return f"""
            Le Client s'engage à verser à Votre Société la rémunération suivante 
            pour les services rendus : <b>{compensation}</b>.
            """
    
    def confidentiality_section(self):
        """
            Création de la section de confidentialité.
        """
        
        return """
            Votre Société et le Client reconnaissent que pendant la durée du présent Contrat, 
            ils peuvent avoir accès aux informations confidentielles de l'autre partie. 
            Les deux parties conviennent de maintenir la confidentialité de ces informations 
            et de ne pas les divulguer à des tiers sans le consentement écrit préalable de l'autre partie, sauf si la loi l'exige.
            """
    
    def intellectual_property_section(self):
        """
            section propriété intellectuelle
        """
        
        return """
            Toute propriété intellectuelle créée par Votre Société dans le cadre de la fourniture 
            des services en vertu du présent contrat restera la propriété de Votre Société, sauf accord écrit contraire. 
            Le Client disposera d'une licence non exclusive et non transférable pour utiliser cette propriété intellectuelle 
            uniquement aux fins pour lesquelles les services sont fournis.
            """

    def term_section(self, term: str):
        if not term:
            raise ValueError("term is empty")
        return f"""
            La durée du présent contrat sera de <b>{term}</b>, 
            à compter de la date d'entrée en vigueur, à moins qu'il ne soit résilié plus tôt 
            conformément aux termes du présent contrat.
            """
    
    def law_section(self,law_content: dict):
        """
            Création de la section de loi, avec les données dynamiques fournies par l'utilisateur.
            :param applicable_law: string contenant les lois applicables
            :param arbitration_rules: string contenant les lois d'arbitrage
            :return: Texte formaté pour la section de loi
            :raises ValueError: Si les données indispensables sont manquantes

        """
        validate_keys(law_content, self.law_keys, "Lois")
        return f"""
            Ce Contrat sera régi et interprété conformément aux lois de <b>{law_content['applicable_law']}</b>. 
            Tout litige découlant de ou lié au présent Contrat sera résolu par arbitrage conformément aux règles de 
            <b>{law_content['arbitration_rules']}</b>, et le jugement sur la sentence rendue par le ou les arbitres pourra être 
            inscrit devant tout tribunal compétent.
            """
    
    def limitation_responsabilite_section(self):
        """
            Création de la section de limitation de responsabilité.
            :return: str
        """
        
        return """
        En aucun cas, l'une ou l'autre des parties ne pourra être tenue responsable envers l'autre partie de tout dommage indirect, 
        accidentel, consécutif, spécial ou punitif découlant de ou lié au présent Contrat, même si la partie a été informée de la 
        possibilité de tels dommages.
        """
    
    def affectation_section(self):
        """
            Création de la section d'affectation.
            :return: str
        """
        
        return """
                Aucune des parties ne peut céder ce Contrat ou tout droit ou obligation en vertu des présentes sans le consentement écrit préalable de l'autre partie, sauf que votre Société peut céder ce Contrat à toute société affiliée ou ayant cause sans un tel consentement.
            """
    
    def divisibilite_section(self):
        """
            Création de la section de divisibilité.
            :return: Texte
        """
        
        return """
                Si une disposition de ce Contrat est jugée invalide, illégale ou inapplicable, les autres dispositions de ce Contrat ne seront pas affectées, et ce Contrat sera interprété comme si une telle disposition invalide, illégale ou inapplicable n'avait jamais été contenue dans les présentes. 
            """

    def accord_integral_section(self):
        """
        Création de la section Accord légal.
        :return: Texte
        """
        return """
                    Ce Contrat contient l'intégralité de l'accord des parties en ce qui concerne l'objet des présentes et remplace tous les accords et ententes antérieurs et contemporains, qu'ils soient oraux ou écrits. Le présent Contrat ne peut être amendé ou modifié que par écrit signé par les deux parties.
                """