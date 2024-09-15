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

from .entities import Contact, Lead
ATTRIBUTE_LIST = ["name", "email", "phone"]

# Only update contact details if they are missing
def update_contact(contact, registrant_data):
  for attribute in ATTRIBUTE_LIST:
    if getattr(contact, attribute) is None:
      setattr(contact, attribute, registrant_data[attribute]) 

# Attempt a match
def check_for_match(object_list, registrant_data, attribute):
  for o in object_list:
    if registrant_data[attribute] == getattr(o, attribute) and registrant_data[attribute] is not None:
      return o
  return None

# Copy across
def add_lead_to_contacts(ContactsList, LeadsList, lead):
  new_contact = Contact()
  for attribute in ATTRIBUTE_LIST:
    setattr(new_contact, attribute, getattr(lead, attribute))
  LeadsList.remove(lead)
  ContactsList.append(new_contact)

# This function will process a single registrant json object
def process_registrant(ContactsList, LeadsList, registrant):
  registrant_data = registrant["registrant"]
  # Match email first
  matching_contact = check_for_match(ContactsList, registrant_data, "email")
  if matching_contact is not None:
    print("Matched contact on email")
    update_contact(matching_contact, registrant_data)
    return
  # Next attempt to match on phone
  matching_contact = check_for_match(ContactsList, registrant_data, "phone")
  if matching_contact is not None:
    print("Matched contact on phone")
    update_contact(matching_contact, registrant_data)
    return
  # Now try and match lead by email
  matching_lead = check_for_match(LeadsList, registrant_data, "email")
  if matching_lead is not None:
    print("Matched lead on email")
    update_contact(matching_lead, registrant_data)
    add_lead_to_contacts(ContactsList, LeadsList, matching_lead)
    return 
  # And by phone
  matching_lead = check_for_match(LeadsList, registrant_data, "phone")
  if matching_lead is not None:
    print("Matched lead on phone")
    update_contact(matching_lead, registrant_data)
    add_lead_to_contacts(ContactsList, LeadsList, matching_lead)
    return 
  # Otherwise add to contacts
  print("No match, creating new")
  new_contact = Contact()
  update_contact(new_contact, registrant_data)
  ContactsList.append(new_contact)
