#Another example of webscraping and cleaning the data to readable

def get_recipe_info(recipe_link):
    recipe_dict = dict()
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(recipe_link)
        
        if not response.statuscode == 200:
            return recipe_dict
        
        results_page = BeautifulSoup(response.content, 'lxml')
        ingredient_list=list()
        prep_steps = list()
        for ingredients in results_page.findall('li',class_='ingredient'):
            ingredient_list.append(ingredients.get_text())
        for steps in results_page.findall('li', class_='preparation-step'):
            prep_steps.append(steps.get_text().strip())
        recipe_dict['ingredients']=ingredient_list
        recipe_dict['preparation']=prep_steps
        return recipe_dict
    except:
        return recipe_dict
        
recipe_link = "http://www.epicurious.com/recipes/food/views/spicy-lemongrass-tofu-233844"
get_recipe_info(recipe_link)
