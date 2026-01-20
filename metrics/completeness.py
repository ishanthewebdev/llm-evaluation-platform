def completeness(question:str,answer:str)->dict:
     """
    Measures whether the answer covers all important parts of the question.
    """
     question=question.lower()
     answer=answer.lower()

     required_aspects=[]
    
     if "what is" in question:
        required_aspects.append("definition")

     if "why" in question:
        required_aspects.append("reason")

     if "how" in question:
        required_aspects.append("process")

     if "where" in question or "applications" in question:
        required_aspects.append("applications")
     if not required_aspects:
        # If we can't infer aspects, assume complete
        return {
            "complete": True,
            "coverage_score": 1.0,
            "missing_aspects": []
        }
     covered=[]
     missing=[]
     for aspect in required_aspects:
        if aspect == "definition" and len(answer.split()) > 5:
            covered.append(aspect)
        elif aspect == "reason" and any(w in answer for w in ["because", "helps", "allows"]):
            covered.append(aspect)
        elif aspect == "process" and any(w in answer for w in ["step", "process", "works"]):
            covered.append(aspect)
        elif aspect == "applications" and any(w in answer for w in ["used", "applications", "industry"]):
            covered.append(aspect)
        else:
            missing.append(aspect)    
     score = len(covered) / len(required_aspects)

     return {
        "complete": score >= 0.7,
        "coverage_score": round(score, 2),
        "missing_aspects": missing
    }