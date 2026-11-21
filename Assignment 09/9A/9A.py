"""Assignment 9A - Detect a direct contradiction between research sources.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Add a fourth source, S4, whose claim directly contradicts S1's hallucination-reduction figure (e.g. reporting no measurable improvement in a different evaluation). Update `compare()` and `synthesize()` to report this as a genuine conflict — not a gap — and to state a plausible reason for the disagreement (different evaluation methodology, different domain, different dataset size).
"""
SOURCES = {
    "S1": {"claim": "RAG reduced hallucinations by 41% in a medical QA benchmark.", "result": "reduction", "method": "200 held-out medical questions"},
    "S2": {"claim": "RAG improved grounding in a domain QA evaluation.", "result": "improvement", "method": "retrieval evaluation"},
    "S3": {"claim": "RAG performance depends on retrieval quality.", "result": "conditional", "method": "error analysis"},
    "S4": {"claim": "A separate evaluation found no measurable hallucination reduction.", "result": "no_improvement", "method": "different domain and larger test set"},
}

def compare(sources):
    s1, s4 = sources["S1"], sources["S4"]
    return {"conflict": s1["result"] == "reduction" and s4["result"] == "no_improvement",
            "source_a": "S1", "source_b": "S4", "kind": "direct contradiction",
            "claims": [s1["claim"], s4["claim"]]}

def synthesize(sources):
    conflict = compare(sources)
    return ("The evidence is conflicting: S1 reports a 41% reduction, while S4 reports no measurable improvement. "
            "This is a genuine contradiction, not missing information. A plausible explanation is that the studies "
            "used different evaluation methodologies, domains, and dataset sizes. The 41% figure should not be "
            "generalized beyond the conditions in which it was measured.")

if __name__ == "__main__":
    for sid, source in SOURCES.items(): print(f"{sid}: {source['claim']} | Method: {source['method']}")
    print("\nComparison:", compare(SOURCES))
    print("\nSynthesis:", synthesize(SOURCES))
