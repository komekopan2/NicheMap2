def select_path_icon(path):
    """
    pathに応じたアイコンを返す
    :param path: str
    :return: str
    """
    path_icons = {
        "popular_searches": 'bi bi-star-fill me-3 text-primary',
        "user_rating_count_searches": 'bi bi-people-fill me-3 text-secondary',
        "niche_searches": 'bi bi-map-fill me-3 text-success'
    }

    return path_icons[path]

def select_cuisine_icon(cuisine):
    """
    cuisineに応じたアイコンを返す
    :param cuisine: str
    :return: str
    """
    cuisine_icons = {
        "restaurant": 'fa-solid fa-house me-3 text-success',
        "ramen_restaurant": 'fa-solid fa-trophy me-3 text-primary',
        "fast_food_restaurant": 'fa-solid fa-hamburger me-3 text-warning',
        "chinese_restaurant": 'fa-solid fa-fire me-3 text-danger',
        "french_restaurant": 'fa-solid fa-wine-glass me-3 text-success',
        "japanese_restaurant": 'fa-solid fa-lemon me-3 text-warning',
        "pub": 'fa-solid fa-beer me-3 text-warning',
        "sushi_restaurant": 'fa-solid fa-fish me-3 text-primary',
        "steak_house": 'fa-solid fa-drumstick-bite me-3 text-danger',
        "bakery": 'fa-solid fa-bread-slice me-3 text-warning',
        "cafe": 'fa-solid fa-coffee me-3 text-success',
        "bar": 'fa-solid fa-glass-martini me-3 text-danger',
        "meal_takeaway": 'fa-solid fa-box me-3 text-primary'
    }

    return cuisine_icons[cuisine]
