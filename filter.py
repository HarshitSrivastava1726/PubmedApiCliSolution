def is_non_academic(affiliation: str) -> bool:
    """Return True if affiliation looks non-academic."""
    academic_keywords = ["university", "college", "school", "hospital", "institute"]
    if not affiliation:
        return False
    lower_aff = affiliation.lower()
    return not any(keyword in lower_aff for keyword in academic_keywords)
