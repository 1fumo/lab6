from flask import Flask 
#all_records = [
 #{
  # "name" : "Radiohead",
   #"albums" : [ 
    #        { 
     #     "title" :"The King of Limbs",
      #                     "Songs":[    
#				    ...
 # 				   ],
#				   "description":"..."
#			   }, 
#		           {
#			   	    "title":"OK Computer"
 #                          	    "songs":[]
  #                         	    "description":"..."
   #                        }
#		]
 #   },
  #  {
#}


#]



app = Flask(__name__)

@app.route('/')
def hello():
	return('<h1>Hello World!</h1>')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80)

