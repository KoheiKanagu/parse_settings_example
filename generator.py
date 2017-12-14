import string
import random
import json
import argparse


def gen(n=64) -> str:
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])


parser = argparse.ArgumentParser(description='Generater')
parser.add_argument(
    "-m", "--mountPath",
    default="/your_mountPath",
    type=str
)
parser.add_argument(
    "-p", "--port",
    default=1340,
    type=int
)
parser.add_argument(
    "-ps", "--publicServerURL",
    default="https://example.com/your_parse",
    type=str
)
parser.add_argument(
    "-s", "--serverURL",
    default="https://example.com/your_parse",
    type=str
)
parser.add_argument(
    "-d", "--databaseURI",
    default="mongodb://localhost:27017/your_db",
    type=str
)

# push config
parser.add_argument(
    "--push",
    action="store_true"
)
parser.add_argument(
    "--senderId",
    default="senderId",
    type=str
)
parser.add_argument(
    "--apiKey",
    default="apiKey",
    type=str
)
parser.add_argument(
    "--pfx",
    default="your/p12/full/path/hoge.p12",
    type=str
)
parser.add_argument(
    "--bundleId",
    default="com.example.parse",
    type=str
)

arg = parser.parse_args()
results = {
    "appId": gen(),
    "masterKey": gen(),
    "clientKey": gen(),
    "javascriptKey": gen(),
    "restAPIKey": gen(),
    "fileKey": gen(),
    "mountPath": arg.mountPath,
    "port": arg.port,
    "serverURL": arg.serverURL,
    "publicServerURL": arg.publicServerURL,
    "databaseURI": arg.databaseURI,
    "logLevel": "info",
    "maxUploadSize": "128mb"
}

if arg.push:
    results["push"] = {
        "android": {
            "senderId": arg.senderId,
            "apiKey": arg.apiKey
        },
        "ios": {
            "pfx": arg.pfx,
            "bundleId": arg.bundleId,
            "production": True
        }
    }


print(json.dumps(results, indent=4))
