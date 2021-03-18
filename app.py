from flask import Flask 

all_records = [
{
"name" : "Radiohead",
"albums" : [ 
        { 
       "title":"The king of Limbs", 
		     "songs":[
			      ...
			     ],
			     "description":"..."
			},
		        {
			    "title":"OK Computer",
			    "songs":[],
			    "desciption":"..."  
			}
		  ]
	},
	{
		  "name":"Portishead"
		   "albums":[
			   {
				"title":"Dummy"
				"songs"[]
				"description":"..."
			    },

			    {
				"title":"Third",
				"songs":[],
				"description":"..."
			    }
		   ]
	}
]


app = Flask(__name__)

@app.route('/')
def hello():
	 return "<h1>Hello, World!</h1>"

@app.route('/records/', methods=['GET'])
def get_records():
	return(all_records)

if __name__ =='__main__':
	app.run(host='0.0.0.0',port=80,debug=True)
