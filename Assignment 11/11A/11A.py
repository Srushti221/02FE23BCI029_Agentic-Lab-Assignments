"""Assignment 11A - Process two stories and preserve artifact lineage.
Name: Srushti Bandi | SRN: 02FE23BCI029

Assignment question: Add a second story (e.g. "export to PDF in addition to CSV") processed through the same pipeline. Extend the lineage trace so it correctly attributes each design/code/test artifact to the right story when two stories exist side by side.
"""
STORIES = [
    {"id": "ST-01", "title": "Export filtered records to CSV", "format": "CSV"},
    {"id": "ST-02", "title": "Export filtered records to PDF", "format": "PDF"},
]

def design_agent(story): return {"story_id": story["id"], "artifact_type": "design", "name": f"{story['format']} export design"}
def coding_agent(story, design): return {"story_id": story["id"], "artifact_type": "code", "name": f"{story['format']} export implementation", "based_on": design["name"]}
def testing_agent(story, code): return {"story_id": story["id"], "artifact_type": "test", "name": f"{story['format']} export tests", "tests_code": code["name"]}

def run_pipeline(stories):
    lineage = []
    for story in stories:
        design = design_agent(story); code = coding_agent(story, design); tests = testing_agent(story, code)
        lineage.extend([design, code, tests])
    return lineage

if __name__ == "__main__":
    lineage = run_pipeline(STORIES)
    print("Stories processed:")
    for story in STORIES: print(story["id"], "-", story["title"])
    print("\nArtifact lineage:")
    for artifact in lineage: print(artifact)
    expected = {story["id"] for story in STORIES}
    valid = len(lineage) == 6 and all(item["story_id"] in expected for item in lineage)
    for story_id in expected:
        valid = valid and {x["artifact_type"] for x in lineage if x["story_id"] == story_id} == {"design", "code", "test"}
    print("Lineage validation:", "PASS" if valid else "FAIL")
