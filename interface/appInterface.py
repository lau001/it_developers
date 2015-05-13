import config
def add_element_gui():
    return config.htmlFirst() + '''
            <form method="post">
                <h1>Add Element</h1>
                <table>
                    <tr>
                        <td>Name:</td>
                        <td><input type="text" id="name"/></td>
                    </tr>
                    <tr>
                        <td>Price:</td>
                        <td><input type="text" id="price"/></td>
                    </tr>
                    <tr>
                        <td>Photo: </td>
                        <td><input type="file" id="photo" accept="image/*"/></td>
                    </tr>
                    <tr>
                        <td>Type: </td>
                        <td>
                            <select>
                                <option value="food">Food</option>
                                <option value="dessert">Dessert</option>
                                <option value="drink">Drink</option>
                            </select>
                        </td>
                    </tr>
                </table>
                <div> <a href="/foodmenu">Food Menu</a><div>
            </form>''' + config.htmlEnd()

def see_all_elements_gui():
    result = config.htmlFirst() + '''
        <form method="post">
            <h1>Menu</h1>
            <table border="1">'''
    # elementos = Element.query()
    # for elemento in elementos:
    #     result = result + '''
    #             <tr>
    #                 <td>''' + elemento +'''</td>
    #                 <td>''' + elemento +''' </td>
    #                 <td>''' + elemento +'''</td>
    #                 <td>''' + elemento +'''</td>
    #             </tr>'''
    result1 = result + '''
            </table>
        </form>''' + config.htmlEnd()
    return result1
