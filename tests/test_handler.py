
import importlib.util
import json
import unittest
from pathlib import Path

# Load the existing Lambda handler.
handler_path = (
    Path(__file__).resolve().parents[1]
    / "lambda"
    / "handler.py"
)

spec = importlib.util.spec_from_file_location(
    "handler_module", handler_path
)
handler_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(handler_module)

lambda_handler = handler_module.lambda_handler


class TestLambdaHandler(unittest.TestCase):

    def test_default_name(self):
        event = {"queryStringParameters": None}

        response = lambda_handler(event, None)

        self.assertEqual(response["statusCode"], 200)

        body = json.loads(response["body"])
        self.assertEqual(body["message"], "Hello, World!")
        self.assertEqual(body["status"], "success")

    def test_custom_name(self):
        event = {
            "queryStringParameters": {
                "name": "Ajara"
            }
        }

        response = lambda_handler(event, None)

        self.assertEqual(response["statusCode"], 200)

        body = json.loads(response["body"])
        self.assertEqual(body["message"], "Hello, Ajara!")


if __name__ == "__main__":
    unittest.main()
