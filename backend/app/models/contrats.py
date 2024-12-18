from backend.app.extensions import db
from sqlalchemy import Integer, Text, Enum, String, Column, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from .signatures import association_table_contract_signature

# Table d'association pour la relation Many-to-Many
association_table_contract_champs_dynamique = Table(
    'contrat_champs_dynamique',
    db.metadata,
    Column('contrat_id', Integer, ForeignKey('contrats.id')),
    Column('champs_dynamique_id', Integer, ForeignKey('champs_dynamiques.id')),
)

# Classe de base pour centraliser les champs communs
class BaseTable(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

# Modèle pour les contrats
class Contrat(BaseTable):
    __tablename__ = 'contrats'

    numero_contrat = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=False)
    contract_type = Column(
        Enum('commercial', 'fournisseur', name='contract_type'),
        nullable=False
    )
    status_contract = Column(
        Enum('signé', 'brouillon', 'annulé', name='status_contract'),
        nullable=False
    )

    champs_dynamique = relationship(
        "ChampsDynamique",
        secondary=association_table_contract_champs_dynamique,
        back_populates="contrats"
    )

    signatures = relationship(
        "Signature",
        secondary=association_table_contract_signature,
        back_populates="contrats"
    )

    def __repr__(self):
        return f"<Contrat(numero_contrat={self.numero_contrat}, type={self.contract_type})>"
