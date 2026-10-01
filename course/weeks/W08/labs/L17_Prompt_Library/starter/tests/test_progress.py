"""Lab 17 progress tests."""
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_library_exists_with_8_prompts():
    p = HERE / "my_prompt_library.md"
    assert p.exists(), "my_prompt_library.md not written"
    text = p.read_text()
    assert text.count("##") >= 8                        # 8+ prompt entries

def test_five_part_structure():
    p = HERE / "my_prompt_library.md"
    text = p.read_text().lower()
    for part in ["role", "context", "schema", "constraint", "example"]:
        assert part in text, f"prompt library missing: {part}"
