from Models.Category import Category
from Log.Logger import Logger

logger = Logger()

def find_ranking_by_categories(data):
    rankings = []

    for category in data['createdCategories']:
        category_name = category['categoryName']
        slider_values = category['sliderValues']

        new_category = Category(category_name, slider_values)
        ranking = new_category.player_ranking_for_category()
        rankings.append(ranking)

    return ranking_by_score(rankings)


def ranking_by_score(rankings):
    player_scores, category_scores = collect_raw_scores(rankings)
    normalized_category_scores = normalize_category_scores(category_scores)

    result_players = normalize_player_scores(player_scores, normalized_category_scores)
    result_players.sort(key=lambda x: x['total_score'], reverse=True)

    return result_players


def find_player_score(player_id, data):
    ranking = find_ranking_by_categories(data)
    
    found_player = None
    for player in ranking:
        if player['_id'] == player_id:
            found_player = player
            break
    
    return found_player


#region player_helpers    
def create_player_data_structure(player_id, player_result):
    return {
        "_id": player_id,
        "name": player_result['name'],
        "categories": [],
        "total_score": 0.0
    }

def add_category_data(player_data, category_name, total_score):
    player_data['categories'].append({
        "name": category_name,
        "score": total_score
    })

    player_data['total_score'] += total_score


def collect_raw_scores(rankings):
    player_scores = {}
    category_scores = {}

    for ranking in rankings:
        for player_result in ranking:
            player_id = player_result['_id']
            total_score = player_result['total_category_score']

            if player_id not in player_scores:
                player_scores[player_id] = create_player_data_structure(player_id, player_result)

            add_category_data(player_scores[player_id], player_result['category_name'], total_score)

            category_name = player_result['category_name']
            if category_name not in category_scores:
                category_scores[category_name] = []
            category_scores[category_name].append(total_score)

    return player_scores, category_scores


def normalize_category_scores(category_scores):
    normalized_category_scores = {}

    for category_name, scores in category_scores.items():
        min_score = min(scores)
        max_score = max(scores)

        if max_score != min_score:
            normalized_scores = [(score - min_score) / (max_score - min_score) for score in scores]
        else:
            normalized_scores = [0] * len(scores)

        normalized_category_scores[category_name] = normalized_scores

    return normalized_category_scores


def normalize_player_scores(player_scores, normalized_category_scores):
    for player_id in player_scores:
        categories = player_scores[player_id]['categories']

        for category in categories:
            category_name = category['name']
            category_score = normalized_category_scores[category_name].pop(0)
            category['score'] = category_score

        total_normalized_score = sum(category['score'] for category in categories) / len(categories)
        player_scores[player_id]['total_score'] = total_normalized_score

    return list(player_scores.values())
#endregion
