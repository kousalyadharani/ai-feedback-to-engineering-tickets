# AI Customer Feedback to Engineering Tickets

Reconstructed from the portfolio's classification/grouping, source-linked ticket generation, Pydantic validation, manual-label evaluation, and Streamlit review workflow. This implementation uses explainable keyword rules and standard-library validation; no LLM endpoint or customer data is bundled.

## Run

`python3 feedback_tickets.py sample_feedback.json --output tickets.json`

Input JSON records require `id` and `text`. Output groups records into draft tickets with evidence IDs, acceptance criteria, missing-information questions, and an explicit human-review status. Categories can be extended in `RULES`.

The portfolio also describes a planned telecom-support extension and planned discovery/pilot activities. Those items remain plans here; no customer interviews, pilot, or commercial impact is represented as completed.

## Verify

`python3 -m unittest -v`
