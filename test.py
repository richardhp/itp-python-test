from src.main import process_registrant
from src.entities import Contact, Lead


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
