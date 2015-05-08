

def htmlFirst():
    return '''<html xmlns="http://www.w3.org/1999/xhtml">
        <head> <link type="text/static" rel="static" href="/static/style.css"/>
        <style type="text/static">
        <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
        <script type="text/javascript" src="static/scripts.js"></script>
            .label {text-align: right}
            .error {color: red}
        </style>
        <title>Mac Ilcapo</title>
        <body class="mystyle" data-feedly-mini="yes">
            <div id="title"><h1>Mac Ilcapo</h1></div>
            <div id="logoDiv" name="logoDiv">
		        <img src="/static/macilcapo.png" id="logo">
		        </hr>
	        </div>
	        </hr>
            '''


def htmlEnd():
    return '''</body> </html>'''