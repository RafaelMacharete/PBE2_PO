class ContactList():
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.contact_list = []
        pass

    def add_contact(self, contact_name, contact_phone):
        self.contact = {'contact name': contact_name, 'contact phone': contact_phone}
        self.contact_list.append(self.contact)
        return self.contact_list

    def edit_contact(self, contact_name, new_contact_name):
        for contact in self.contact_list:
            if contact['contact name'] == contact_name:
                self.contact['contact name'] = new_contact_name
                print(contact)
                return 'Contact updated'
        return 'Contact not found'
    
    def remove_contact(self, contact_name):
        for contact in self.contact_list:
            if contact['contact name'] == contact_name:
                self.contact_list.remove(contact)
                return self.contact_list
        return 'Contact not found'
contact_list1 = ContactList('Rafael')

contact_list1.add_contact('Lucas', 123)
contact_list1.add_contact('Rafael', 223)
contact_list1.add_contact('Leafar', 222)


print(contact_list1.remove_contact('Leafar'))