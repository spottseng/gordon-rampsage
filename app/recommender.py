
def parse_recipes(raw_recipes):
    parsed = []
    for resp in raw_recipes:
        cleaned = {
            "id": resp["id"],
            "title": resp["title"],
            "image": resp["image"],
            "used_count": resp["usedIngredientCount"],
            "missed_count": resp["missedIngredientCount"],
            "used_ingredients": [i["name"] for i in resp["usedIngredients"]],
            "missed_ingredients": [{"name": i["name"], "image": i["image"]} for i in resp["missedIngredients"]],
            "likes": resp["likes"]
        }
        parsed.append(cleaned)
    return parsed