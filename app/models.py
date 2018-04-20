from . import db



class User(db.Model):
    ''' Users create a user model'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128) , unique=True )
    phone  =  db.Column(db.String(128) , unique=True )
    bankno = db.Column(db.String(128) , unique=True)
    
    national_id = db.Column(db.String(30) , nullable=False , unique=True)

    is_approved = db.Column(db.Boolean , default=True)
    
    age = db.Column(db.Integer , unique=False)
    
    location = db.Column(db.String(128))
    photo = db.Column(db.String(128) , default='avatar.png')

    
    service_id =  db.Column(db.Integer, db.ForeignKey('services.id'),
        nullable=True)


    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def __str__(self):
        return self.name 

    def __repr__(self):
        return '<User: {}>'.format(self.name)

    

class Service(db.Model):
    ''' Users create a user model'''
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    
    cost = db.Column(db.Float)

    photo = db.Column(db.String(128) , default='avatar.png')
    
    users = db.relationship('User', backref='service', lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()


    def to_dict(self):
        services = {
            'id':self.id,
            'name':self.name,
            'photo':self.photo
        }
        return services


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(128))
    phone  = db.Column(db.String(30))

    def save(self):
        db.session.add(self)
        db.session.commit()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employer_id = db.Column(db.Integer , db.ForeignKey('users.id'))
    client_id = db.Column(db.Integer , db.ForeignKey('clients.id'))
    service_id = db.Column(db.Integer , db.ForeignKey('clients.id'))
    # cost  = db.Column(db.Float)
    is_paid = db.Column(db.Boolean, default=False)
    is_complete = db.Column(db.Boolean , default=False)

    task_id = db.Column(db.String(128) , unique=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __str__(self):
        return self.task_id

    def __repr__(self):
        return '<Task {}>'.format(self.task_id)
    

















