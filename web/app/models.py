from flask import current_app
from . import db


class Permission:
    SUBMIT_PUZZLE = 0x01
    EDIT_PUZZLE = 0x02
    ADMINISTER = 0x80


class Role(db.Model):
    """Model the different roles in the system."""
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        """Initializes user roles."""
        roles = {
            'Student': (0, True),
            'Moderator' : (Permission.SUBMIT_PUZZLE |
                           Permission.EDIT_PUZZLE, False),
            'Administrator': (0xff, False)
        }

        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role {}>'.format(self.name)


class User(db.Model):
    """Model the user accounts."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True, index=True)
    screen_name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128), default=None)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, **kwargs):
        """Assign the user proper roles."""
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, permissions):
        """Check if user has the given permissions."""
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        """Check if user has the ADMINISTER permission."""
        return self.can(Permission.ADMINISTER)

    def __repr__(self):
        return '<User {}>'.format(self.email)
