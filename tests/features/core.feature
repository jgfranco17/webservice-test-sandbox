Feature: The service shall respond to basic health checks

    Scenario: The health endpoint is working
        Given the server is running
        When I make a GET request to the "/healthz" endpoint
        Then the response status code should be 200

    Scenario: The service info endpoint is working
        Given the server is running
        When I make a GET request to the "/service-info" endpoint
        Then the response status code should be 200
