#!/usr/bin/env python

from src import app

# print(dir(src.main))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
