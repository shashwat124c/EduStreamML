# backend/ml/classifier.py

def dummy_classify_difficulty(resources):
    """
    A temporary rule-based classifier. 
    Will be replaced by Scikit-learn (Naive Bayes/Logistic Regression) in Phase 3.
    """
    classified_path = {
        "beginner": [],
        "intermediate": [],
        "advanced": []
    }

    for res in resources:
        text_to_analyze = (res['title'] + " " + res['description']).lower()

        # Simple keyword matching for Phase 1
        if any(word in text_to_analyze for word in ['beginner', 'intro', 'basics', 'crash course', '101']):
            res['difficulty'] = 'beginner'
            classified_path["beginner"].append(res)
            
        elif any(word in text_to_analyze for word in ['advanced', 'deep dive', 'architecture', 'expert', 'scale']):
            res['difficulty'] = 'advanced'
            classified_path["advanced"].append(res)
            
        else:
            res['difficulty'] = 'intermediate'
            classified_path["intermediate"].append(res)

    return classified_path