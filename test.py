from src.main import process_registrant
from src.entities import Contact, Lead

"""
CONTACTS:

Alice Brown / None / 1231112223
Bob Crown / bob@crowns.com / None
Carlos Drew / carl@drewess.com / 3453334445
Doug Emerty / None / 4564445556
Egan Fair / eg@fairness.com / 5675556667

LEADS:

None / kevin@keith.com / None
Lucy / lucy@liu.com / 3210001112
Mary Middle / mary@middle.com / 3331112223
None / None / 4442223334
None / ole@olson.com / None


REGISTRANTS (these should be read as JSON mentioned above)

Lucy Liu / lucy@liu.com / None
Doug / doug@emmy.com / 4564445556
Uma Thurman / uma@thurs.com / None

{
  "registrant": 
  {
    "name": "Tom Jones", 
    "email": "tom@jones.com",
    "phone": "3211234567",
  }
}

"""

ContactsList = []
ContactsList.append(Contact("Alice Brown", None, "1231112223"))
ContactsList.append(Contact("Doug Emerty", None, "4564445556"))

LeadsList = []
LeadsList.append(Lead(None, "kevin@keith.com", None))
LeadsList.append(Lead("Lucy", "lucy@liu.com", "3210001112"))

Registrants = []
Registrants.append({
  "registrant": {
    "name": "Lucy Liu",
    "email": "lucy@liu.com",
    "phone": None,
  }
})
Registrants.append({
  "registrant": {
    "name": "Doug",
    "email": "doug@emmy.com ",
    "phone": "4564445556",
  }
})

for registrant in Registrants:
  process_registrant(ContactsList, LeadsList, registrant)

print(ContactsList)
print(LeadsList)
