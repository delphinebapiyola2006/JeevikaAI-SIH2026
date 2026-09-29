import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

EDU_ORDER = {"No formal education":0,"8th":1,"10th":2,"12th":3,"ITI":3,"Diploma":4,"Graduate":5}

def education_score(profile_edu, minimum):
    p = EDU_ORDER.get(profile_edu, 3)
    m = EDU_ORDER.get(minimum, 0)
    return 1.0 if p >= m else max(0.0, p / max(1, m))

def recommend(profile, roles, opportunity_counts):
    profile_text = " ".join([str(x) for x in (
        profile.get("skills", []) + profile.get("interests", []) +
        [profile.get("current_occupation",""), profile.get("family_occupation","")]
    ) if x]).lower()

    role_texts = [r.get("keywords","") for r in roles]
    corpus = [profile_text] + role_texts
    matrix = TfidfVectorizer(stop_words="english").fit_transform(corpus)
    sims = cosine_similarity(matrix[0:1], matrix[1:]).flatten()
    out = []

    for role, sim in zip(roles, sims):
        sim = float(sim)
        edu = education_score(profile.get("education",""), role.get("education_min","8th"))
        pref = profile.get("employment_preference","Either")
        pref_match = 1.0 if pref == "Either" or pref == role.get("employment_mode") or role.get("employment_mode") == "Both" else 0.45
        local = min(1.0, opportunity_counts.get(role["role_id"],0)/3.0)
        score = sim*0.55 + edu*0.15 + 1.0*0.15 + local*0.10 + 0.05
        score *= (0.92 + 0.08*pref_match)
        terms = set(re.findall(r"[a-zA-Z]+", profile_text))
        role_terms = set(re.findall(r"[a-zA-Z]+", role.get("keywords","").lower()))
        gaps = [x for x in sorted(role_terms-terms) if len(x)>2][:5]
        reasons = []
        if sim > 0.15: reasons.append("Your skills/interests overlap with this role.")
        if edu >= 0.9: reasons.append("Your education meets the prototype threshold.")
        if local > 0: reasons.append("A demo local-opportunity signal exists.")
        if pref_match >= 0.9: reasons.append("The employment mode matches your preference.")
        if not reasons: reasons.append("This role is a candidate pathway for further assessment.")
        out.append({
            "role_id": role["role_id"], "job_role": role["job_role"], "sector": role["sector"],
            "qp_code": role["qp_code"], "nsqf_level": role["nsqf_level"],
            "score": round(min(1,score)*100,1), "reasons": reasons[:4],
            "skill_gaps": gaps or ["Role-specific competencies to be validated"],
            "pathway": ["Confirm eligibility","Complete skill-gap training","Assessment/certification where applicable","Explore verified local employment or enterprise opportunities"]
        })
    return sorted(out,key=lambda x:x["score"],reverse=True)
