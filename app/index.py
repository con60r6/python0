from flask import Flask
import requests
import console
from console import test
app = Flask(__name__)


#@app.route('/')
#def start():
    #str=test()
    #return str#

#a=0
#b=1
#c=2
#d=3
#e=4
#f=5
#g=6
#h=7
#i=8
#j=9
#print(a, b, c, d, e, f, g, h, i, j)#

x = 1
while x <= 3:
    print(x)
    x += 1


#response = requests.get("https://api.github.com")
    #digit=0
    #string=""
    # while digit<10
    #     string=string+str(digit)
    #     digit=digit+1#

    # return '0 1 2 3 4 5 6 7 8 9'# + str(response.status_code)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
