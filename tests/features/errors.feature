Feature: The service shall handle error conditions gracefully

    Scenario: The server returns a 404 for non-existent endpoints
        Given the server is running
        When I make a GET request to the "/non-existent" endpoint
        Then the response status code should be 404
        And the response should raise an error
        And the response body should contain the following key-value pairs
          | key    | value           |
          | detail | Not Found       |
