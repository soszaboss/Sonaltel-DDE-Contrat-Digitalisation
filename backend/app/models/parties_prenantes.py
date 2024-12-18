from sqlalchemy import Integer, Enum, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from .contrats import BaseTable

class PartiesPrenante(BaseTable):
    __tablename__ = 'parties_prenantes'

    nom_complet = Column(String(50), nullable=False)
    email = Column(String(50), nullable=True)
    numero_enregistrement = Column(String(50), nullable=True)
    adresse = Column(String(50), nullable=False)
    partie_prenante_role = Column(
        Enum('entreprise', 'client', 'acheteur', 'vendeur', name='partie_prenante_role'),
        nullable=False
    )

    signature = relationship("Signature", back_populates="partie_prenante")
