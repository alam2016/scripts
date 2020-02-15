import json
import sys
from behave import given, when, then
from app.core.personController import PersonController


@given(u'person object instantiated in {test_env}')
def step_impl(context, test_env):
    context.person = PersonController(test_env)


@when(u'calling person credit card with {customer_id}, {status}, {person_id} and {tca}')
def step_impl(context, customer_id, status, person_id, tca):
    persons_credit_card_tca_response = \
        context.person.get_personscreditcard_using_person_id_and_transaction_corporate_account(
            customer_id,
            status,
            person_id,
            tca)
    try:
        context.json_cc_response_person_id_tca = json.loads(persons_credit_card_tca_response.content)
    except Exception, e:
        print('No response from get_cc_using_person_id')
        print('Exception: %s' % str(e))
        sys.exit(1)


@then(u'{person_direct_pay_credit_card_id} should return')
def step_impl(context, person_direct_pay_credit_card_id):
    assert context.json_cc_response_person_id_tca[0]['personDirectPayCreditCardID'] == int(person_direct_pay_credit_card_id)


@when(u'looking up encrypted person with {person_id}')
def step_impl(context, person_id):
    eplu_person_id_response = context.person.get_eplu_using_person_id('5', person_id)
    try:
        context.json_eplu_response_person_id = json.loads(eplu_person_id_response.content)
    except Exception, e:
        print('No response from get_cc_using_person_id')
        print('Exception: %s' % str(e))
        sys.exit(1)


@then(u'person id {person_id} should contain in response')
def step_impl(context, person_id):
    assert context.json_eplu_response_person_id[0]['personID'] == int(person_id)


