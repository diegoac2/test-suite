To run:
python/path path/to/test-suite
For example:
/usr/local/bin/python3.7 /Users/user/Documents/GitHub/test-suite/flaskr/app.py

Then go to http://0.0.0.0:8080/ui/#/Pets to see the documentation.

To run connexion's mock go to /test-suite/flaskr/ and run the command:
---
$ connexion run ../data.yaml --mock=all -v
---

A more thorough implementation fo the example: https://github.com/hjacobs/connexion-example/blob/master/app.py
