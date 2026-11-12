#!/usr/bin/env python3
"""Turn feedback records into traceable draft tickets for human review."""
import argparse,csv,json,re
from collections import defaultdict
from pathlib import Path

RULES={"login":r"\b(login|sign.?in|password|authentication)\b","performance":r"\b(slow|latency|timeout|loading|performance)\b","billing":r"\b(bill|invoice|charge|payment|subscription)\b","usability":r"\b(confus|hard to|unclear|navigation|button)\b"}
def classify(text):
 hits=[k for k,p in RULES.items() if re.search(p,text,re.I)]
 return hits[0] if len(hits)==1 else "other"
def build_tickets(feedback):
 groups=defaultdict(list)
 for row in feedback:
  if not isinstance(row,dict) or not row.get("id") or not isinstance(row.get("text"),str): raise ValueError("Each feedback item needs a string id and text")
  groups[classify(row["text"])].append(row)
 out=[]
 for category,items in sorted(groups.items()):
  quotes=[re.sub(r"\s+"," ",x["text"]).strip() for x in items]
  ticket={"title":f"Investigate {category} feedback ({len(items)} report{'s' if len(items)!=1 else ''})","category":category,"source_ids":[str(x["id"]) for x in items],"evidence":quotes,"acceptance_criteria":[f"Reproduce the reported {category} issue using the linked source reports.","Document expected and observed behavior.","Add a regression test for the verified fix."],"questions":[] if all(len(q)>18 for q in quotes) else ["What steps and expected result should be captured for the short report(s)?"],"status":"draft; human review required"}
  out.append(ticket)
 return out
def main():
 p=argparse.ArgumentParser(); p.add_argument("input",type=Path); p.add_argument("--output",type=Path,default=Path("tickets.json")); a=p.parse_args()
 data=json.loads(a.input.read_text()); result=build_tickets(data); a.output.write_text(json.dumps(result,indent=2)+"\n"); print(f"Wrote {len(result)} reviewable tickets to {a.output}")
if __name__=="__main__":main()
