import requests
from decouple import config


class EdamamInfo:
    def __init__(self):
        self.api_key = config("EDAMAM_API_KEY")
        self.app_id = config("EDAMAM_APPLICATION_ID")
        self.base_url = "https://api.edamam.com"

    def build_recipe(title, ingredients):
        return {"title": title, "ingr": ingredients}

    def get_nutrition_details(self, title, ingredients):
        url = self.base_url + "/api/nutrition-details"
        url += f"?app_id={self.app_id}&app_key={self.api_key}"
        # print(EdamamInfo.build_recipe(title, ingredients))
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        response = requests.post(
            url, json=EdamamInfo.build_recipe(title, ingredients), headers=headers
        ).json()

        labels = {
            "ENERC_KCAL": "Calorias",
            "CHOCDF": "Carbohidratos",
            "PROCNT": "Proteinas",
            "SUGAR": "Azucar",
            "FIBTG": "Fibra",
            "FAMS": "Grasas Saturadas",
            "FAPU": "Grasas Polinsaturadas",
        }
        nutrition = {}
        total_nutrients = response.get("totalNutrients", {})
        for key, label in labels.items():
            if key in total_nutrients:
                nutrition[label] = (
                    f"{total_nutrients[key]['quantity']:.2f} {total_nutrients[key]['unit']}"
                )
            else:
                nutrition[label] = 0
        return nutrition


# object_info = EdamamInfo()


# test = object_info.get_nutrition_details(
#     "pizza", ['3 zucchini', 'Olive oil, enough to brush on the boats', '1-2 tsp. garlic, minced', '15 grape tomatoes, halved', 'Bread crumbs', '1-2 cups mozzarella cheese, shredded', 'Chopped fresh or dried basil, enough to sprinkle on top', 'Parmesan cheese, enough to sprinkle on top', 'Salt and pepper, to taste']
# )
# print(test)
