from requests import Request, Session


class PersonController:

    def __init__(self, domain):
        self.domain = domain
        self.url = 'person.' + domain + '.pool.mycompany.com'
        self.session = Session()

    def get_personscreditcard_using_person_id_and_transaction_corporate_account(
            self, customer_id, status, person_id, tca):
        net_loc = '/persons/creditCard/'
        headers = {'content-type': 'application/json'}
        req = Request('GET',
                      "http://"
                      + self.url
                      + net_loc
                      + '?customerId='
                      + str(customer_id)
                      + '&status='
                      + status
                      + '&personId='
                      + str(person_id)
                      + '&transactionCorporateAccountId='
                      + str(tca),
                      headers=headers)
        prepped = req.prepare()
        response = self.session.send(prepped)
        return response

    def get_eplu_using_person_id(self, customer_id, person_id):
        net_loc = '/persons/creditCard/encryptedPersonLookup/'
        headers = {'content-type': 'application/json'}
        req = Request('GET',
                      "http://" + self.url + net_loc + '?customerId=' + str(customer_id) +
                      '&personId=' + str(person_id),
                      headers=headers)
        prepped = req.prepare()
        response = self.session.send(prepped)
        return response