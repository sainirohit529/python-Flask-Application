from flask import Flask, render_template

app = Flask(__name__)


@app.route('/render_content/',methods = ["GET"])
@app.route('/render_content/<file_name>/',defaults = {'start' : None , 'end' : None})
@app.route('/render_content/<file_name>/<start>/<end>/',methods = ["GET"])
def hello(file_name = 'file1.txt',start=None,end=None):
	try:
		final = []
		if (start==None and end==None):
			text = open(file_name, 'r+' , encoding = "latin1")
			for content in text:
				final.append(content)
			text.close()
		else:
			out = []
			if file_name == 'file2.txt':
				text = open(file_name, 'r+', encoding = "UTF-16")
			else:
				text = open(file_name, 'r+', encoding = "latin1")
			for content in text:
				out.append(content)	
			text.close()
			reset = 1
			for element in out:
				if (element.find(start) != -1 or reset == 0):
					final.append(element)
					reset = 0
					if(element.find(end) != -1 and reset == 0):
						reset=1
						break;
			final.pop(0)
			final.pop(len(final)-1)
		return render_template('content.htm', text=final)
	except Exception as e:
	    print(str(e))

if __name__ == '__main__':
    app.run(debug=True)