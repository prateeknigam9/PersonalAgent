from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import List


def find_similar_person(json_data: List, search_query:str, threshold:float = 0.6):
    valid_entries = [(person, person["name"]) for person in json_data if person["name"]]
    if not valid_entries:
        return None, 0
    
    names = [name for d, name in valid_entries]
    emails = [d['email'] for d, name in valid_entries]
    
    all_contact_details = names + emails
    
    all_contact_details.append(search_query)
    
    vectorizer = CountVectorizer(analyzer='char', lowercase=True)
    vectors = vectorizer.fit_transform(all_contact_details)
    
    similarity_scores = cosine_similarity(vectors[-1:], vectors[:-1])[0]

    best_idx = np.argmax(similarity_scores)
    best_score = similarity_scores[best_idx]
    
    if best_score >= threshold:
        return valid_entries[best_idx][0], best_score
    return None, 0

def update_json_data(data, query):
    updated_data = data.copy()
    
    match_criteria = {k: v for k, v in query.items() if v is not None}
    
    if not match_criteria:
        return updated_data  

    for item in updated_data:
        is_match = False
        for key, value in match_criteria.items():
            if item.get(key) == value:
                is_match = True
                break
            
        if is_match:
            for key, value in query.items():
                if value is not None:
                    item[key] = value
                    
    return updated_data

    

    