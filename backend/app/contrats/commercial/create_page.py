import uuid

from reportlab.lib.pagesizes import A4
from reportlab.platypus import Frame, PageTemplate, Paragraph, Spacer, BaseDocTemplate

from backend.app.contrats.commercial.components import PageComponents
from backend.app.contrats.commercial.page_space_marge_and_frame import PageSpacePaddingFrame
from backend.app.contrats.commercial.styles import PageStyles
from backend.app.contrats.commercial.utils.functions import page_footer
from faker import Faker

class CreatePage:

    def __init__(self, **kwargs):
        """
        Initialise un document de contrat avec des données dynamiques.

        :param kwargs: Données dynamiques pour les différentes sections du contrat.
            - intro_data (dict, optionnel) : Données pour l'introduction.
            - services_data (str, optionnel) : Données pour la section des services.
            - terme_data (str, optionnel) : Données pour les termes du contrat.
            - compensation_data (str, optionnel) : Données pour la compensation.
            - confidentiality_data (str, optionnel) : Données pour la confidentialité.
            - termination_section_data (dict, optionnel) : Données pour la section de résiliation.
            - law_data (dict, optionnel) : Données pour la section de loi applicable.
            - signatures_data (dict, optionnel) : Données pour la section des signatures.
            - signature_image_path (str, optionnel) : Chemin vers l'image de la signature.

        """
        self.elements = []
        self._styles = PageStyles().styles
        self._components = PageComponents()
        self.intro_data = kwargs.get('intro_data', None)
        self.services_data = kwargs.get('services_data', None)
        self.terme_data = kwargs.get('terme_data', None)
        self.compensation_data = kwargs.get('compensation_data', None)
        self.termination_section_data = kwargs.get('termination_section_data', None)
        self.law_data = kwargs.get('law_data', None)
        self.signatures_data = kwargs.get('signatures_data', None)
        self.signature_image_path = kwargs.get('signature_image_path', None)
        self.create_sections()

    @staticmethod
    def create_page_template(frames, a4_format=False, **kwargs):
        """
        Crée un PageTemplate avec des cadres (Frames) spécifiés et un pied de page.

        Arguments :
            frames (Frame ou list[Frame]) : Un ou plusieurs objets Frame à inclure dans le PageTemplate.
            a4_format (bool) : Si True, utilise le format A4 pour la taille de la page.
            **kwargs : Taille personnalisée de la page (pagesize=(width, height)).

        Retourne :
            PageTemplate : Un objet PageTemplate configuré.

        Exceptions :
            ValueError : Si frames ou pagesize est invalide.
        """
        # Générer un identifiant unique pour le modèle de page
        page_template_id = str(uuid.uuid4())  # Utilisation de uuid native

        # Valider les frames
        if isinstance(frames, (list, tuple)):
            for frame in frames:
                if not isinstance(frame, Frame):
                    raise ValueError("All frames must be instances of Frame.")
        elif not isinstance(frames, Frame):
            raise ValueError("Frame must be of type Frame.")

        # Si le format A4 est demandé
        if a4_format:
            return PageTemplate(id=page_template_id, frames=frames, onPage=page_footer, pagesize=A4)

        # Vérifier la taille de page personnalisée
        page_size = kwargs.get('pagesize', None)
        if not isinstance(page_size, (tuple, list)) or len(page_size) != 2 or not all(
                isinstance(x, (float, int)) for x in page_size):
            raise ValueError("Page size must be a tuple or list of two numbers (width, height).")

        # Retourner le PageTemplate avec la taille personnalisée
        return PageTemplate(id=page_template_id, frames=frames, onPage=page_footer, pagesize=page_size)


    def add_section(self, title, content, subtitle_style, text_style):
        """
        Ajoute une section au PDF.

        Arguments :
            title (str) : Titre de la section.
            content (str) : Contenu de la section.
            subtitle_style : Style pour le titre de la section.
            text_style : Style pour le contenu de la section.
        """
        self.elements.append(Paragraph(title, subtitle_style))
        self.elements.append(Paragraph(content, text_style))

    def create_sections(self):
        self._styles = self._styles
        # Titre Principal
        self.elements.append(Paragraph(
            "Contrat Commercial",
            self._styles['TitleStyle']
        ))

        # Ajouter une ligne sous le texte avec des tirets
        self.elements.append(Paragraph("<u>_________________________________________________________</u>", self._styles['TextStyle']))

        # Ajouter un espacement
        self.elements.append(Spacer(1, 24))

        # Introduction
        intro_data = self.intro_data
        introduction = self._components.intro(intro_data, self._styles)
        self.elements.extend(introduction)

        # Ajouter une ligne sous le texte avec des tirets
        self.elements.append(Paragraph("<u>_________________________________________________________</u>", self._styles['TextStyle']))

        # Ajouter un espacement
        self.elements.append(Spacer(1, 24))

        # Services
        services_data = self.services_data
        services = self._components.services_section(services_data)
        self.add_section("SERVICES", services, self._styles['SubtitleStyle'], self._styles['TextStyle'])

        # Terme
        terme_data = self.terme_data
        terme = self._components.term_section(terme_data)
        self.add_section("TERME", terme, self._styles['SubtitleStyle'], self._styles['TextStyle'])

        # Compensation
        compensation_data = self.compensation_data
        compensation = self._components.compensation_section(compensation_data)
        self.add_section("COMPENSATION", compensation, self._styles['SubtitleStyle'], self._styles['TextStyle'])

        # Confidentialité
        confidentiality_data = self._components.confidentiality_section()
        self.add_section("CONFIDENTIALITÉ", confidentiality_data, self._styles['SubtitleStyle'], self._styles['TextStyle'])

        # Propriété Intellectuelle
        intellectual_property_data = self._components.intellectual_property_section()
        self.add_section("PROPRIÉTÉ INTELLECTUELLE", intellectual_property_data, self._styles['SubtitleStyle'],
                    self._styles['TextStyle'])

        # Terminaison
        termination_section_data = self.termination_section_data
        termination_data = self._components.termination_section(termination_section_data)
        self.add_section("TERMINAISON", termination_data, self._styles['SubtitleStyle'], self._styles['TextStyle'])

        # Limitation de Responsabilité
        limitation_responsabilite_data = self._components.limitation_responsabilite_section()
        self.add_section("LIMITATION DE RESPONSABILITÉ", limitation_responsabilite_data, self._styles['SubtitleStyle'],
                    self._styles['TextStyle'])

        # Loi Applicable
        law_data = self.law_data
        law_data_content = self._components.law_section(law_data)
        self.add_section("LOI APPLICABLE", law_data_content, self._styles['SubtitleStyle'], self._styles['TextStyle'])

        # Accord Intégral
        accord_integral_data = self._components.accord_integral_section()
        self.add_section("ACCORD INTÉGRAL", accord_integral_data, self._styles['SubtitleStyle'], self._styles['TextStyle'])

        # Affectation
        affectation_data = self._components.affectation_section()
        self.add_section("AFFECTATION", affectation_data, self._styles['SubtitleStyle'], self._styles['TextStyle'])

        # Divisibilité
        divisibilite_data = self._components.divisibilite_section()
        self.add_section("DIVISIBILITÉ", divisibilite_data, self._styles['SubtitleStyle'], self._styles['TextStyle'])

        # Générer les paragraphes pour les signatures
        signature_image_path = self.signature_image_path
        signatures_data = self.signatures_data
        signature_paragraphs = self._components.generate_signatures_section(signatures_data, self._styles)

        # Ajouter les paragraphes au document
        return self.elements.extend(signature_paragraphs)

    def generate_contrat(self):
        page_space = PageSpacePaddingFrame()
        padding_values = page_space.padding(left_padding=1, right_padding=1, top_padding=1, bottom_padding=1.3)
        frames = page_space.create_frame(padding_values, True)
        page_template = self.create_page_template(frames, True)
        base_doc = BaseDocTemplate("contrat_comercial.pdf", pageTemplates=[page_template])
        base_doc.build(self.elements)


"""
    fake = Faker()

data = {
"termination_section_data" : {
    'termination_notice': 30,
    'termination_remedy': 15
},

"signatures_data" : {
    'company_name': 'XYZ Corp',
    'company_email': 'contact@xyzcorp.com',
    'company_address': '123 rue de Paris, 75001 Paris, France',
    'company_registration': 'FR123456789',
    'client_name': 'John Doe',
    'client_email': 'johndoe@example.com',
    'client_address': '456 avenue de Lyon, 69000 Lyon, France'
},

"law_data" : {
    'applicable_law': "France",
    'arbitration_rules': "CCI (Chambre de Commerce Internationale)"
},
"intro_data" : {
    'company_name': fake.company(),
    'company_status': "Société Anonyme (SA)",
    'company_jurisdiction': fake.country(),
    'company_address': fake.address(),
    'client_name': fake.company(),
    'client_status': "SA",
    'client_jurisdiction': fake.country(),
    'client_address': fake.address()
},
"compensation_data" : "une rémunération mensuelle de 5000 € pour les services fournis.",
"services_data" : "Assistance informatique, conseils stratégiques.",
"terme_data" : " 1 an",


}

create_page = CreatePage(**data)
create_page.generate_contrat()
"""
