# import requests
# from bs4 import BeautifulSoup
class typed_data:
    Ember = {"Hamburger": ["Juicy all beef burger on a soft split bun", 320, 0], \
            "classic hot dog": ["Grilled hot dog on a roll", 310, 0], \
            "grilled herb chicken sandwich":["grilled garlic-herb marinated chicken", 310, 0], \
            "Fresh-Cut French Fries":["House-cut hot and crispy russet French fries", 200, 0], \
            "Grilled BlackBean Burger": ["Grilled black bean burger on a bun", 250, 0], \
            "Classic Grilled Cheese": ["American cheese melted in between slices of crisp white bread", 320, 0], \
            "Crispy French Fries": ["Piping hot crispy French fries", 150, 0], \
            "Crispy Chicken Sandwich": ["Crispy breaded chicken and lettuce on a roll with mayonnaise", 550, 0], \
            "Italian Burger": ["Juicy beef burger, provolone and homemade tomato sauce", 390, 0]
        }
    
    # grubb/ mainline
    Grubb = {
    "Latin Beef Stew": ["Spicy beef stew with tomato, onion, potato, cabbage, corn, squash, peppers, cumin and cilantro", 100, 0], \
    "French Toast": ["Golden brown and fluffy cinnamon-spiced thick-cut French toast", 160, 0], \
    "Roasted Garlic Potatos": ["Oven-roasted red potatoes tossed with roasted garlic", 100, 0], \
    "Turkey Sausage Patty": ["Sizzling hot golden brown turkey sausage patty", 90, 0], \
    "Roasted Veggies": ["Roasted zucchini, tomatoes, red pepper, chickpeas and Kalamata olives with red wine vinaigrette", 60, 0], \
    "Scrambled Eggs": ["Freshly scrambled eggs seasoned with salt and pepper", 180, 0], \
    "Baked Chipotle-Orange Chicken": ["Baked boneless chicken breast coated with a spicy Latin seasoning mix and chipotle-orange glaze", 200, 0], \
    "Spanish RIce": ["Brown rice with tomatoes, onions, garlic and green peppers seasoned with cumin, oregano and sage", 100, 0], \
    "Green Chili": ["Sauteed zucchini with corn and green chilies", 50, 0], \
    "Cajun Baked Chicken": ["Cajun-seasoned baked chicken leg quarter", 230, 0], \
    "ButterMilk": ["Fluffy, golden brown buttermilk pancakes", 160, 0], \
    "Chocolate Chip Buttermilk Pancakes":  ["Fluffy, golden brown buttermilk pancakes with semisweet chocolate chips", 250, 0], \
    "Lyonnaise Potatoes": ["Pan-fried seasoned sliced potatoes and sauteed onions", 120, 0], \
    "Pork Sausage Links": ["Golden brown savory pork sausage link", 240, 0], \
    "Cut Green Beans": ["Steamed green beans tossed with seasonings", 50, 0], \
    "Cajun Baked Chicken": ["Cajun-seasoned baked chicken leg quarter", 230, 0], \
    "Buttermilk Pancakes": ["Fluffy, golden brown buttermilk pancakes", 160, 0], \
    "Chicken Shawarma Platter": ["Yellow rice topped with shawarma-spiced Halal chicken breast, lettuce, tomato", 460, 0], \
    "Buffalo Chicken Mac & Cheese": ["Cavatappi pasta tossed with creamy cheddar sauce, spicy Buffalo chicken and Asiago cheese", 310, 0], \
    "Pork sausage links": ["Golden brown savory pork sausage link", 240, 0], \
    "Swedish Meatballs": ["Juicy meatballs simmered in a rich, creamy sauce, served over egg noodles", 390, 0], \
    "Grilled Ancho Lime Steak": ["Grilled ancho lime marinated steak", 180, 0], \
    "Papas Rancheras": ["Fresh diced potatoes baked in a spicy tomato ranchero sauce", 130, 0], \
    "Pancakes": ["Golden brown gluten-free pancakes", 260, 0], \
    "Crispy Tater Tots": ["Deep-fried seasoned shredded potato bites", 120, 0], \
    "Bacon": ["Crisp, lightly smoked bacon strips", 110, 0], \
    "Macaroni": ["Tender corkscrew pasta in a cheesy cheddar sauce with a buttery Parmesan crumb topping", 360, 0], \
    "Green Been Casserole": ["Green beans and cream of mushroom soup topped with crunchy French fried onions", 100, 0], \
    "Pork, Pulled, Carolina": ["Pulled pork", 260, 0], \
    "Grilled Lemon-Herb Pollock": ["Grilled Pollock seasoned with lemon, garlic and oregano", 150, 0], \
    "Lemon Pepper Rotisserie Chicken": ["Whole rotisserie chicken, lemon pepper seasoning blend", 430, 0], \
    "Nam Tok Pork": ["Grilled pork loin tossed with lime juice, fish sauce, toasted rice, shallot and cilantro", 130, 0], \
    "UCI rice pilaf": ["", 460, 0], \
    "General Tso's Pork": ["Stir-fried pork, bell peppers, water chestnuts and onions in a spicy-sweet sauce", 130, 0], \
    "Crispy Fried Chicken": ["Golden-fried chicken seasoned perfectly with our blend of spices", 470, 0], \
    "Rotisserie Chicken": ["Roasted bone-in chicken rubbed with salt, garlic, onion and paprika", 430, 0], \
    "Chocolate Chip Buttermilk Pancakes": ["Fluffy, golden brown buttermilk pancakes with semisweet chocolate chips", 250, 0], \
    "Grilled Carne Asada Pork Loin": ["Grilled pork loin marinated in a blend of red wine vinegar, orange juice, oregano, cumin and garlic", 170, 0]
    }

    # pizza
    Pizza = {
        "Meatball pizza": ["Sliced Italian meatballs, mozzarella and pizza sauce", 400, 0], \
        "classic cheese pizza": ["Mozzarella cheese and pizza sauce on a golden brown crust", 340, 0], \
        "Pepperoni Pizza": ["Pepperoni, mozzarella and pizza sauce on a golden brown crust", 370, 0], \
        "White Pizza": ["Mozzarella, asiago and ricotta cheese with crushed red pepper and pesto sauce", 400, 0]
    }

    # Soups:
    Soups = {
        "Old Fashioned Oatmeal": ["Homestyle oatmeal cereal", 110, 0], \
        "Chicken Noodle Soup": ["Tender chicken, egg noodles and vegetables simmered in savory chicken stock", 90, 0], \
        "Dinner Roll": ["Soft and delicious white dinner rolls", 60, 0]
    }

    # Vegan:
    Vegan = {
        "Turmeric Tofu Scramble": ["Crumbled tofu sauteed with turmeric, salt and pepper", 220, 0], \
        "Vegan Home-Style Pancakes": ["Warm vegan pancakes made from scratch with soy milk and vanilla", 240, 0], \
        "Hummus Brown Rice Wrap": ["Toasted cumin hummus, roasted vegetables, and brown rice on a wrap", 210, 0], \
        "Scrambled Chick Pea": ["Scrambled seasoned chick pea", 80, 0]
    }

    #Bakery
    Bakery = {
        "Blueberry Mini Muffin": ["Freshly baked miniature muffin with blueberries", 80, 0], \
        "Donut Bites": ["A variety of fresh baked donuts coated with cocoa, cinnamon sugar or powdered sugar", 210, 0], \
        "Oatmeal Raisin Cookie": ["Freshly baked chewy oatmeal cookie with raisins", 120, 0], \
        "Peanut Butter Devil's Food Parait": ["Layers of peanut butter mousse, chocolate pudding and cake topped with whipped topping", 190, 0], \
        "Cranberry Orange Scone": ["Freshly baked scone with fresh cranberries and orange zest drizzled with vanilla icing", 140, 0], \
        "Iced Cinnamon Roll": ["Freshly baked cinnamon roll with cream cheese icing", 220, 0], \
        "Peanut Butter Cookie": ["Freshly baked peanut butter cookie", 120, 0]
    }


if __name__ == "__main__":
    pass
    # html_text = requests.get("https://uci.campusdish.com/LocationsAndMenus/Brandywine").text
    # soup = BeautifulSoup(html_text, 'html.parser')
    # lst = soup.find_all("script")
    # Foods = lst[27]
    # print(len(str(Foods)))
    # str_food = str(Foods)

    # this dictionary is for ember/grill food
    # with the format of key as food name and 
    # and [description, calories, rating] as their name


