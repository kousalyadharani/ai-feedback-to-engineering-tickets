import unittest
from feedback_tickets import build_tickets
class FeedbackTests(unittest.TestCase):
 def test_traceable_grouped_output(self):
  ts=build_tickets([{"id":"1","text":"Login is slow"},{"id":"2","text":"Login is slow again"}]); self.assertEqual(ts[0]["source_ids"],["1","2"]); self.assertTrue(ts[0]["acceptance_criteria"])
 def test_rejects_missing_source(self):
  with self.assertRaises(ValueError):build_tickets([{"text":"broken"}])
if __name__=="__main__":unittest.main()
