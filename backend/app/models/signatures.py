from backend.app.extensions import db
from sqlalchemy import Integer, Column, ForeignKey, LargeBinary, Table
from sqlalchemy.orm import relationship
from .contrats import BaseTable

# Table d'association pour la relation Many-to-Many
association_table_contract_signature = Table(
    'contrat_signature',
    db.metadata,
    Column('contrat_id', Integer, ForeignKey('contrats.id')),
    Column('signature_id', Integer, ForeignKey('signatures.id')),
)

class Signature(BaseTable):
    __tablename__ = 'signatures'

    signature_image = Column(LargeBinary, nullable=False)
    partie_prenante_id = Column(Integer, ForeignKey('parties_prenantes.id'), nullable=False)
    partie_prenante = relationship("PartiesPrenante", back_populates="signature")

    contrats = relationship(
        "Contrat",
        secondary=association_table_contract_signature,
        back_populates="signatures"
    )
