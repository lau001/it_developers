def htmlFirst():
    return '''<html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <link type="text/style" rel="stylesheet" href="/stylesheet/style.css"/>
            <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
            <script type="text/javascript" src="/javascript/scripts.js"></script>
            <title>Mc Ilcapo</title>
        </head>
        <body class="mystyle" data-feedly-mini="yes">
            <div id="logoDiv" name="logoDiv">
		        <img src="/images/logo.png" id="logo" width="500px"/>
	        </div>
	        </hr>
            '''

def htmlEnd():
    return '''</body></html>'''
