import config
startapp = config.htmlFirst() + \
        ''' <div> Hello there! </div>
            <form>
                <div> <a href=\"/logout\">logout</a></br> </div>

            </form>
        ''' + config.htmlEnd()