Feature: MyInfo - Personal Details

  Scenario: Verify ESS user is able to view Personal Details page
    Given the user is logged into OrangeHRM as an ESS user with username "virat123" and password "Virat123"
    When the user clicks on the My Info tab
    Then the user should be redirected to the Personal Details section