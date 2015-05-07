

def htmlFirst():
    return '''<html xmlns="http://www.w3.org/1999/xhtml">
        <head> <link type="text/stylesheet" rel="stylesheet"href="/stylesheet/style.stylesheet"/>
        <style type="text/stylesheet">
        <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
        <script type="text/javascript" src="count/counter.js"></script>
        <script type="text/javascript" src="scripts.js"></script>
            .label {text-align: right}
            .error {color: red}
        </style>
        <title>Mac Ilcapo</title>
        <body class="mystyle" data-feedly-mini="yes">
            <div id="logoDiv" name="logoDiv">
		        <img src="/stylesheet/macilcapo.png" id="logo">
		        </hr>
	        </div>
            '''


def htmlEnd():
    return '''</body> </html>'''