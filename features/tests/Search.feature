Feature: Search for stays on Booking.com

Scenario: Perform a search for a stay
    Given Open Booking page
    When User clicks on Search Stays button
    And User enters the destination "Paris" in the search field
    And User selects the dates for the stay from "15" to "25"
    And User clicks on Search button
    Then The search results should include properties in Paris
