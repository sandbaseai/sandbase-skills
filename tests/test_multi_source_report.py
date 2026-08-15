import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research" / "multi-source-search" / "scripts" / "validate_report.py"
EXAMPLE = ROOT / "examples" / "verifiable-research-report.json"


def report():
    return {
        "question": "Does the result replicate independently?",
        "searched_at": "2026-08-15",
        "providers": ["tavily_search", "exa_search", "scholar_search_mixed"],
        "unavailable_providers": [],
        "sources": [
            {"id": "s1", "url": "https://example.org/a", "publisher": "A", "source_type": "primary"},
            {"id": "s2", "url": "https://example.net/b", "publisher": "B", "source_type": "secondary"},
            {"id": "s3", "url": "https://example.com/c", "publisher": "C", "source_type": "primary"},
        ],
        "claims": [{
            "id": "c1", "text": "Three independent sources report the result.",
            "kind": "sourced", "confidence": "high", "source_ids": ["s1", "s2", "s3"],
            "independent_source_count": 3, "conflict": False,
        }],
        "gaps": ["Raw benchmark data is not public."],
    }


class MultiSourceReportTests(unittest.TestCase):
    def run_report(self, payload):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            return subprocess.run([sys.executable, str(SCRIPT), str(path)], text=True, capture_output=True, check=False)

    def test_valid_report(self):
        result = self.run_report(report())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "VALID: 3 source(s), 1 claim(s), 3 provider(s)")

    def test_committed_example(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(EXAMPLE)],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "VALID: 3 source(s), 1 claim(s), 3 provider(s)")

    def test_rejects_inflated_confidence(self):
        payload = report()
        payload["claims"][0]["independent_source_count"] = 2
        result = self.run_report(payload)
        self.assertEqual(result.returncode, 1)
        self.assertIn("requires at least 3 independent sources", result.stderr)

    def test_rejects_unknown_and_unused_sources(self):
        payload = copy.deepcopy(report())
        payload["claims"][0]["source_ids"][2] = "missing"
        result = self.run_report(payload)
        self.assertIn("unknown source id: missing", result.stderr)
        self.assertIn("source is not referenced by any claim: s3", result.stderr)

    def test_rejects_duplicate_urls(self):
        payload = copy.deepcopy(report())
        payload["sources"][2]["url"] = payload["sources"][0]["url"]
        result = self.run_report(payload)
        self.assertIn("duplicate source URL", result.stderr)

    def test_rejects_high_confidence_conflict(self):
        payload = report()
        payload["claims"][0]["conflict"] = True
        result = self.run_report(payload)
        self.assertIn("cannot be high confidence", result.stderr)


if __name__ == "__main__":
    unittest.main()
