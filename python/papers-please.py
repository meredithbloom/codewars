# Paper, Please - 3 kyu
# https://www.codewars.com/kata/59d582cafbdd0b7ef90000a0/train/python

'''
Papers, Please is an indie video game where the player takes on a the role of a border crossing immigration officer in the fictional dystopian Eastern Bloc-like country of Arstotzka in the year 1982. As the officer, the player must review each immigrant and returning citizen's passports and other supporting paperwork against a list of ever-increasing rules using a number of tools and guides, allowing in only those with the proper paperwork, rejecting those without all proper forms, and at times detaining those with falsified information.

# ** OBJECTIVE
Your task is to create a constructor function (or class) and a set of instance methods to perform the tasks of the border checkpoint inspection officer. The methods you will need to create are as follow:

# TODO: Method: receiveBulletin
Each morning you are issued an official bulletin from the Ministry of Admission. This bulletin will provide updates to regulations and procedures and the name of a wanted criminal.
The bulletin is provided in the form of a string. It may include one or more of the following:

#* Updates to the list of nations (comma-separated if more than one) whose citizens may enter (begins empty, before the first bulletin):

example 1: Allow citizens of Obristan
example 2: Deny citizens of Kolechia, Republia

#* Updates to required documents:

example 1: Foreigners require access permit
example 2: Citizens of Arstotzka require ID card
example 3: Workers require work pass

#* Updates to required vaccinations:

example 1: Citizens of Antegria, Republia, Obristan require polio vaccination
example 2: Entrants no longer require tetanus vaccination

#* Update to a currently wanted criminal:

example 1: Wanted by the State: Hubert Popovic

# TODO: Method: inspect

Each day, a number of entrants line up outside the checkpoint inspection booth to gain passage into Arstotzka. The inspect method will receive an object representing each entrant's set of identifying documents. This object will contain zero or more properties which represent separate documents. Each property will be a string value. These properties may include the following:

#* Applies to all entrants:

passport
certificate_of_vaccination
Applies only to citizens of Arstotzka
ID_card
Applies only to foreigners:
access_permit
work_pass
grant_of_asylum
diplomatic_authorization

# *The inspect method will return a result based on whether the entrant passes or fails inspection:

#* Conditions for passing inspection

All required documents are present
There is no conflicting information across the provided documents
All documents are current (ie. none have expired) -- a document is considered expired if the expiration date is November 22, 1982 or earlier
The entrant is not a wanted criminal
If a certificate_of_vaccination is required and provided, it must list the required vaccination
A "worker" is a foreigner entrant who has WORK listed as their purpose on their access permit
If entrant is a foreigner, a grant_of_asylum or diplomatic_authorization are acceptable in lieu of an access_permit. In the case where a diplomatic_authorization is used, it must include Arstotzka as one of the list of nations that can be accessed.


#* If the entrant passes inspection, the method should return one of the following string values:

If the entrant is a citizen of Arstotzka: Glory to Arstotzka.
If the entrant is a foreigner: Cause no trouble.

#! If the entrant fails the inspection due to expired or missing documents, or their certificate_of_vaccination does not include the necessary vaccinations, return Entry denied: with the reason for denial appended.

Example 1: Entry denied: passport expired.
Example 2: Entry denied: missing required vaccination.
Example 3: Entry denied: missing required access permit.

#! If the entrant fails the inspection due to mismatching information between documents (causing suspicion of forgery) or if they're a wanted criminal, return Detainment: with the reason for detainment appended.

If due to information mismatch, include the mismatched item. e.g.Detainment: ID number mismatch.
If the entrant is a wanted criminal: Detainment: Entrant is a wanted criminal.
NOTE: One wanted criminal will be specified in each daily bulletin, and must be detained when received for that day only. For example, if an entrant on Day 20 has the same name as a criminal declared on Day 10, they are not to be detained for being a criminal.
Also, if any of an entrant's identifying documents include the name of that day's wanted criminal (in case of mismatched names across multiple documents), they are assumed to be the wanted criminal.

In some cases, there may be multiple reasons for denying or detaining an entrant. For this exercise, you will only need to provide one reason.

If the entrant meets the criteria for both entry denial and detainment, priority goes to detaining.
For example, if they are missing a required document and are also a wanted criminal, then they should be detained instead of turned away.
In the case where the entrant has mismatching information and is a wanted criminal, detain for being a wanted criminal.

#* TEST EXAMPLE

bulletin = """Entrants require passport
Allow citizens of Arstotzka, Obristan"""

inspector = Inspector()
inspector.receive_bulletin(bulletin)

entrant1 = {
    "passport": """ID#: GC07D-FU8AR
    NATION: Arstotzka
    NAME: Guyovich, Russian
    DOB: 1933.11.28
    SEX: M
    ISS: East Grestin
    EXP: 1983.07.10"""
}

inspector.inspect(entrant1) #=> 'Glory to Arstotzka.'

#* INPUT NOTES

Inputs will always be valid.
There are a total of 7 countries: Arstotzka, Antegria, Impor, Kolechia, Obristan, Republia, and United Federation.
Not every single possible case has been listed in this Description; use the test feedback to help you handle all cases.
The concept of this kata is derived from the video game of the same name, but it is not meant to be a direct representation of the game.

'''
import re

class Inspector:
    def __init__(self):
        self.wanted_criminals = []
        self.country_details = {
            'arstotzka': {
                'status': 'native',
                'allowance': True,
                'documents': [],
                'vaccinations': [],
                'worker_docs': [],
                'worker_vax': []
            },
            'antegria': {
                # country will have allowance key added
                'status': 'foreign',
                'documents': [],
                'vaccinations': [],
                'worker_docs': [],
                'worker_vax': []
            },
            'impor': {
                'status': 'foreign',
                'documents': [],
                'vaccinations': [],
                'worker_docs': [],
                'worker_vax': []
            },
            'kolechia': {
                'status': 'foreign',
                'documents': [],
                'vaccinations': [],
                'worker_docs': [],
                'worker_vax': []
            },
            'obristan': {
                'status': 'foreign',
                'documents': [],
                'vaccinations': [],
                'worker_docs': [],
                'worker_vax': []
            },
            'republia': {
                'status': 'foreign',
                'documents': [],
                'vaccinations': [],
                'worker_docs': [],
                'worker_vax': []
            },
            'united federation': {
                'status': 'foreign',
                'documents': [],
                'vaccinations': [],
                'worker_docs': [],
                'worker_vax': []
            }
        }
        self.citizen_docs = ['passport', 'certificate of vaccination','id card']
        self.foreigner_docs = ['passport', 'certificate of vaccination', 'access permit', 'work pass', 'grant of asylum', 'diplomatic authorization']
        self.all_countries = ['arstotzka','antegria','impor','kolechia','obristan','republia','united federation']
    
    
    # function to break out countries from a string
    def find_countries(self, string):
        relevant_countries = []
        for country in self.all_countries:
            if country in string:
                relevant_countries.append(country)
        print(f'find countries function test: {relevant_countries}\n')
        return relevant_countries
    
    
    def update_country_allowances(self, update):
        # method to process updates dedicated to allowing/denying citizens from specified countries
        # need to break out countries from allow/deny
        # split update into words then filter only country words
        action = update.split(' ')[0]
        countries = self.find_countries(update)
        for country in countries:
            if action == 'allow':
                self.country_details[country]['allowance'] = True
            elif action == 'deny':
                self.country_details[country]['allowance'] = False
        #print(self.country_details, end="\n\n")
        
    
    def update_required_documents(self, update):
        # method to process updates dedicated to updating required documents for each group (foreigners, citizens, workers)
        # need to identify which group from which country (if applicable)
        # need to identify which documents
        # * for new requirements
        if 'no longer require' not in update: 
            split_index = update.index('require')
            document = update[split_index+7:].strip()
            # if the change applies to specific countries, we need to identify those countries
            if 'citizens of' in update:
                countries = self.find_countries(update)
                for country in countries:
                    self.country_details[country]['documents'].append(document)
                #print(f'citizens of {countries} now require {document}\n')
            elif 'workers of' in update:
                countries = self.find_countries(update)
                for country in countries:
                    self.country_details[country]['worker_docs'].append(document)
                print(f'workers of {countries} now require {document}\n')
            # if the change applies to neither citizens nor workers of a specific country, we do not need to check for specific list of countries to change status of
            else:
                target_group = update[:split_index].strip() 
                #print(f'{target_group} now require {document}\n')
                if target_group == 'entrants':
                    # need to update status of all countries
                    for country in self.country_details.keys():
                        self.country_details[country]['documents'].append(document)
                elif target_group == 'foreigners':
                    for country in self.country_details.keys():
                        if self.country_details[country]['status'] == 'foreign':
                            self.country_details[country]['documents'].append(document)

                    
        #* removing old requirements
        if 'no longer require' in update:
            split_index = update.index('no longer require')
            document = update[split_index+17:].strip()
            # if the change applies to specific countries, we need to identify those countries
            if 'citizens of' in update:
                countries = self.find_countries(update)
                for country in countries:
                    self.country_details[country]['documents'].remove(document)
                print(f'citizens of {countries} no longer require {document}\n')
            elif 'workers of' in update:
                countries = self.find_countries(update)
                for country in countries:
                    self.country_details[country]['worker_docs'].remove(document)
                print(f'workers of {countries} no longer require {document}\n')
            else:
                target_group = update[:split_index].strip()
                print(f'{target_group} do not require {document}')
                if target_group == 'entrants':
                    # need to update dictionary document status of all countries
                    for country in self.country_details.keys():
                        self.country_details[country]['documents'].remove(document)                
                elif target_group == 'foreigners':
                    for country in self.country_details.keys():
                        if self.country_details[country]['status'] == 'foreign':
                            self.country_details[country]['documents'].remove(document)
        #print(self.country_details)
               
           
    def update_vaccination_reqs(self, update):
        #* for new requirements
        if 'no longer require' not in update:
            split_index = update.index('require')
            vaccines = update[split_index+7:].strip()
            countries = self.find_countries(update)
            # we know the string has to include either citizens of or workers of if there are any specific countries mentioned
            if len(countries) > 0:
                if 'citizens of' in update:
                    countries = self.find_countries(update)
                    for country in countries:
                        self.country_details[country]['vaccinations'].append(vaccines)
                    #print(f'citizens of {countries} now require {vaccines}\n')
                elif 'workers of' in update:
                    countries = self.find_countries(update)
                    for country in countries:
                        self.country_details[country]['worker_vax'].append(vaccines)
                    #print(f'workers of {countries} now require {vaccines}\n')
            else:
                if 'entrants' in update:
                    for country in self.country_details.keys():
                        self.country_details[country]['vaccinations'].append(vaccines)       
                elif 'foreigners' in update:
                    for country in self.country_details.keys():
                        if self.country_details[country]['status'] == 'foreign':
                            self.country_details[country]['vaccinations'].append(vaccines)
            #print(vaccines, countries)
        
        #* for removing old requirements    
        elif 'no longer require' in update:
            split_index = update.index('no longer require')
            vaccines = update[split_index+17:].strip()
            countries = self.find_countries(update)
            # we know the string has to include either citizens of or workers of if there are any specific countries mentioned
            if len(countries) > 0:
                if 'citizens of' in update:
                    countries = self.find_countries(update)
                    for country in countries:
                        self.country_details[country]['vaccinations'].remove(vaccines)
                    #print(f'citizens of {countries} no longer require {vaccines}\n')
                elif 'workers of' in update:
                    countries = self.find_countries(update)
                    for country in countries:
                        self.country_details[country]['worker_vax'].remove(vaccines)
                    #print(f'workers of {countries} no longer require {vaccines}\n')
            else:
                if 'entrants' in update:
                    for country in self.country_details.keys():
                        self.country_details[country]['vaccinations'].remove(vaccines)       
                elif 'foreigners' in update:
                    for country in self.country_details.keys():
                        if self.country_details[country]['status'] == 'foreign':
                            self.country_details[country]['vaccinations'].remove(vaccines)
            #print(vaccines, countries)
        #print(self.country_details)
            
    def update_wanted_criminal(self, update):
        split_index = update.index(':')
        criminal = update[split_index+2:].strip()
        self.wanted_criminals.append(criminal)
        #print(self.wanted_criminals)
      
    def receive_bulletin(self, bulletin):
        updates = bulletin.split('\n')      
        # reinitialize sorting of updates every day
        for update in updates:
            # make everything lowercase for ease of string matching
            update = update.lower()
            if "allow" in update or "deny" in update:
                self.update_country_allowances(update)
            elif "vaccination" in update:
                self.update_vaccination_reqs(update)
            elif "require" in update and "vaccination" not in update:
                self.update_required_documents(update)
            elif "wanted" in update:
                self.update_wanted_criminal(update)
        print(self.country_details)
              
    
    # ! INSPECT method
    # TODO: need to take in each document and store information to be reviewed
    
    def inspect(self, entrant):
        # need to store all information about potential entrant across all documents
        entrant_details = {}
        documents = []
        # need to move through each document that the potential entrant has
        for doc, value in entrant.items():
            details = value.split('\n')
            # need to keep track of documents
            documents.append(doc)
            for val in details:
                split_index = val.index(':')
                attribute, info = val[:split_index].strip(), val[split_index+1:].strip().lower()
                #print(attribute, info)
                #* adding new information to profile
                if attribute not in entrant_details.keys():
                    entrant_details[attribute] = info
                # if information is already present in profile, we need to cross reference
                else:
                    # function to compare new information to existing information
                    if self.compare_entrant_detail(entrant_details[attribute], info) == False:
                        self.return_rejection(attribute, 'mismatch')
                    else:
                        pass
            print(documents, entrant_details)
        #print(f'going to check if applicant has all required docs')
        self.has_all_docs(entrant_details, documents)
    
    
    #* compare specific attribute values - existing vs new. if mismatch, return false/error
    def compare_entrant_detail(self, existing_attr, new_attribute):
        # pass existing and new attribute values as strings OR date objects, if relevant
        return True if existing_attr == new_attribute else False

    # country detail dict structure
    
    # 'united federation': {
    #             'status': 'foreign',
    #             'documents': [],
    #             'vaccinations': [],
    #             'worker_docs': [],
    #             'worker_vax': []
    #         }
    
    # TODO: assess if applicant meets requirements
    
    #* does the applicant have the right documents needed
    def has_all_docs(self, entrant, entrant_documents):
        print(f'testing if applicant has required documents')
        print(entrant_documents)
        # need to check citizenship of entrant
        # need to check work status of entrant
        # need to cross reference dictionary of countries to see if entrant has all required docs based on their citizenship and work status
        print(entrant)
        nation = entrant['NATION']
        if 'PURPOSE' in entrant.keys():
            worker = True if entrant['PURPOSE'] == 'WORK' else False
            if worker:
                worker_docs, worker_vax = self.country_details[nation]['worker_docs'], self.country_details[nation]['worker_vax']
        all_docs, all_vax = self.country_details[nation]['documents'], self.country_details[nation]['vaccinations']
        
        # need to check list of documents to see if it matches required list 
        print(entrant_documents)
    
    #* is the information across the applicant's documents consistent
    def compare_documents(self, entrant):
        pass
    
    #* is the document expired
    def check_expiration(self, document):
        pass
    
    def return_rejection(self, attribute, reason):
        pass
    
                    
   
    
    # TODO: decide if the applicant is accepted or not
    # also needs to return string depending on whether applicant is native citizen                
    def final_decision(self, entrant):
        pass     
    
    
    
inspector = Inspector()
# bulletin = """Entrants require passport
# Allow citizens of Arstotzka, Obristan
# Deny citizens of United Federation
# Workers require work permit
# Workers no longer require work permit
# Citizens of Arstotzka require ID card
# Foreigners require access permit"""

bulletin = """Citizens of Arstotzka, United Federation require ID card
Citizens of Antegria, Republia, Obristan require polio vaccination
Entrants require tetanus vaccination
Foreigners no longer require tetanus vaccination
Wanted by the State: Hubert Popovic
"""
josef = {
	"passport": 'ID#: GC07D-FU8AR\nNATION: Arstotzka\nNAME: Costanza, Josef\nDOB: 1933.11.28\nSEX: M\nISS: East Grestin\nEXP: 1983.03.15'
}

guyovich = {
	"access_permit": 'NAME: Guyovich, Russian\nNATION: Obristan\nID#: TE8M1-V3N7R\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 159cm\nWEIGHT: 60kg\nEXP: 1983.07.13'
}

roman = {
	"passport": 'ID#: WK9XA-LKM0Q\nNATION: United Federation\nNAME: Dolanski, Roman\nDOB: 1933.01.01\nSEX: M\nISS: Shingleton\nEXP: 1983.05.12',
	"grant_of_asylum": 'NAME: Dolanski, Roman\nNATION: United Federation\nID#: Y3MNC-TPWQ2\nDOB: 1933.01.01\nHEIGHT: 176cm\nWEIGHT: 71kg\nEXP: 1983.09.20'
}

inspector.receive_bulletin(bulletin)
print("\n\n")
inspector.inspect(roman)