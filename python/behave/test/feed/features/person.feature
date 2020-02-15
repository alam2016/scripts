Feature: Person Restful Service operations

  Background: person object setup
    Given person object instantiated in staging

  Scenario Outline: persons credit card request with TransactionCorporateAccountID
    When calling person credit card with <customer_id>, <status>, <person_id> and <tca>
    Then <person_direct_pay_credit_card_id> should return

    Examples: Data
      | customer_id | status | person_id | tca | person_direct_pay_credit_card_id |
      | 5           | ACT    | 327880    | 4   | 68956                            |
      | 5           | ACT    | 1618604   | 4   | 86554                            |
      | 5           | ACT    | 1618604   | 244 | 86559                            |
      | 5           | ACT    | 1618604   | 408 | 86368                            |
      | 5           | ACT    | 1618604   | 615 | 89692                            |

  @wip
  Scenario: test encrypted person lookup request with person_id
    When looking up encrypted person with 327880
    Then person id 327880 should contain in response