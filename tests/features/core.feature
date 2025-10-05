Feature: Verify the core endpoints

    Scenario: The health endpoint is working
        Given the server is running
        When I make a GET request to the "/healthz" endpoint
        Then the response status code should be 200
