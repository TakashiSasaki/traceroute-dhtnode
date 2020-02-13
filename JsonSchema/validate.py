#!/usr/bin/python3
import jsonschema
import json

def main():
    schema = json.load(open("schema.json", "r"))
    document = json.load(open("bookmarks.json", "r"))
    jsonschema.validate(document, schema)

if __name__ == "__main__":
    main()

