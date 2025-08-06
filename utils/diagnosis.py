def match_symptoms(input_symptoms, diseases):
    results = []

    for disease in diseases:
        match_count = len(set(disease["symptoms"]).intersection(input_symptoms))
        if match_count > 0:
            results.append({
                "name": disease["name"],
                "description": disease["description"],
                "match": match_count,
                "total": len(disease["symptoms"])
            })

    results.sort(key=lambda x: x["match"], reverse=True)
    return results
