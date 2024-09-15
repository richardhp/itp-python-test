class Lead:
  def __init__(self, name = None, email = None, phone = None):
    self.name = name
    self.email = email
    self.phone = phone
  
  def __repr__(self):
    return "{name} / {email} / {phone}".format(name = self.name, email = self.email, phone = self.phone)

class Contact:
  def __init__(self, name = None, email = None, phone = None):
    self.name = name
    self.email = email
    self.phone = phone

  def __repr__(self):
    return "{name} / {email} / {phone}".format(name = self.name, email = self.email, phone = self.phone)
