from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

# Association Table for many-to-many relationship
user_illness = db.Table('user_illness',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('illness_id', db.Integer, db.ForeignKey('illness.id'), primary_key=True)
)
# Association Table for many-to-many relationship between Illness and Herbs
illness_herbs = db.Table('illness_herbs',
    db.Column('illness_id', db.Integer, db.ForeignKey('illness.id'), primary_key=True),
    db.Column('herbs_id', db.Integer, db.ForeignKey('herbs.id'), primary_key=True)
)
class User(db.Model, SerializerMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, index=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String)

    # Relationship mapping the user to related illnesses
    illnesses = db.relationship(
        'Illness', secondary=user_illness, back_populates='users'
    )

    # Relationship mapping user to related herbs
    herbs = db.relationship(
        'Herbs', back_populates='user', cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f'<User {self.id}, {self.name}, {self.username}, {self.email}>'

class Illness(db.Model, SerializerMixin):
    __tablename__ = "illness"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    body_part = db.Column(db.String(80))
    symptoms = db.Column(db.String(200))
    treatment = db.Column(db.String(200))

    serialize_only = ('id', 'name', 'description', 'body_part', 'symptoms', 'treatment')
    serialize_rules = ('-herbs'),

    # Relationship mapping illness to related users
    users = db.relationship('User', secondary=user_illness, back_populates='illnesses')

    def __repr__(self):
        return f'<Illness {self.id}, {self.name}, {self.description}>'

class Herbs(db.Model, SerializerMixin):
    __tablename__ = "herbs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    health_benefits = db.Column(db.String(200))
    side_effects = db.Column(db.String(200))
    
    # Foreign key for illness
    illness_id = db.Column(db.Integer, db.ForeignKey('illness.id'))
    illnesses = db.relationship('Illness', backref=db.backref('herbs', lazy=True))

    serialize_only = ('id', 'name', 'description', 'health_benefits', 'side_effects', 'illness_id')
    serialize_rules = ('-illness',)

    # Foreign Key for user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='herbs')

    def __repr__(self):
        return f'<Herbs {self.id}, {self.name}, {self.description}>'
