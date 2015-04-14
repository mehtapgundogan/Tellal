#hello.py dosyasından db nesnesi alınacak.Bu kisim degistirilebilir.
from hello import db

class User(db.Model):
    #otomatik artabilecek sekilde ayarlanilacak.	
    userID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.relationship('Mail',backref='user'))
    userStatus = db.Column(db.Boolean)

    def __init__(self, userStatus, email):
        self.email = email
	self.userStatus = userStatus

    def __repr__(self):
        return self.email

class Mail(db.Model):
# mailID otomatik arttirilabilir yapilacak.
    #mailID = db.Column(db.Integer, primary_key=True) Bu kisim boyle mi olmali yukaridaki gibi mi bakilacak.
    mailID = db.Column(db.relationship('Issue',backref='issue'))	
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'))
    mailAdress = db.Column(db.String(50))

class Issue(db.Model):
    issueName = db.Column(db.String(100))
    issueID = db.Column(db.Integer, primary_key=True)
    mailID = db.Column(db.Integer, db.ForeignKey('issue.mailID'))
    issueStatus = db.Column(db.Boolean)
    issueTime = db.Column(db.DateTime)
