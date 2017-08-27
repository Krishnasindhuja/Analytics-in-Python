#using HTML request response, getting data from an example page 

def get_recipes(keywords):
    recipe_list = list()
    import requests
    from bs4 import BeautifulSoup
    url = "http://www.epicurious.com/search/" + keywords
    response = requests.get(url)
    if not response.status_code == 200:
        print("failure")
        return recipe_list
    try:
        result_page = BeautifulSoup(response.content, 'lxml')
        recipes = result_page.find_all('article', class_='recipe-content-card')
        for recipe in recipes:
            recipe_name = recipe.find('a').get_text()
            recipe_link = "http://www.epicurious.com" + recipe.find('a').get('href')
            recipe_desc = recipe.find('p', class_='dek').get_text()
            print(recipe_name, recipe_link, recipe_desc)
        
    except:
        return recipe_list
    
    return recipe_list
    
get_recipes("Tofu chili")
