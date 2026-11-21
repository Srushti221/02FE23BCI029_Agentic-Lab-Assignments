"""Assignment 9B - Weight conflicting sources by quality tier.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Add a source-quality tier to each source (e.g. peer-reviewed > independent benchmark > vendor blog) and use it in `synthesize()` to state which claim the synthesis leans toward when two sources conflict — while still explicitly disclosing that a lower-tier source's claim was down-weighted, not discarded.
"""
SOURCES = [
    {"id": "S1", "tier": "peer-reviewed", "claim": "RAG reduced hallucinations in the tested medical QA domain."},
    {"id": "S4", "tier": "independent benchmark", "claim": "No measurable reduction was found in a different evaluation."},
    {"id": "S5", "tier": "vendor blog", "claim": "RAG always removes hallucinations."},
]
QUALITY_RANK = {"peer-reviewed": 3, "independent benchmark": 2, "vendor blog": 1}

def synthesize(sources):
    ordered = sorted(sources, key=lambda source: QUALITY_RANK[source["tier"]], reverse=True)
    strongest = ordered[0]
    lower_tier_claims = [s for s in ordered[1:] if s["claim"] != strongest["claim"]]
    print("Quality-weighted synthesis leans toward", strongest["id"], f"({strongest['tier']}).")
    for source in lower_tier_claims:
        print(f"Disclosure: {source['id']} ({source['tier']}) claims: {source['claim']}")
        print("This claim is down-weighted because of its lower source-quality tier, not discarded.")
    print("The sources still conflict; source quality alone cannot prove which result is universally correct.")
    print("Different domains, datasets, and methods require further comparable replication.")
    return strongest["id"]

if __name__ == "__main__":
    for source in SOURCES: print(source["id"], "|", source["tier"], "|", source["claim"])
    print("\nSynthesis:")
    preferred = synthesize(SOURCES)
    print("Preferred source:", preferred)
