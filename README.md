# Subscription Service Mock

This is a mock API for a subscription service that can receive and respond to SOAP requests. It was built using Python and the Flask web framework.

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Usage

To start the API server, run the following command:

```
python app.py
```

This will start the server on `http://localhost:5000/`.

To send a SOAP request to the API, use a tool like SoapUI or Postman and send a request to the endpoint `http://localhost:5000/getSubscriptionList`. The request should be in the same format as the example request provided in the code.

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork this repository.
2. Create a new branch with your changes: `git checkout -b my-feature-branch`.
3. Commit your changes: `git commit -m "Add some feature"`.
4. Push your changes to your fork: `git push origin my-feature-branch`.
5. Submit a pull request to this repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project was inspired by the need for a mock API for testing purposes. Thanks to Flask and the developers of the libraries used in this project.
