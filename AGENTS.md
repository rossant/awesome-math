# Maintainer review guidance

Read CONTRIBUTING.md before reviewing nominations or existing entries. It is the
selection policy; this file guides investigation and communication.

## Required review order: editorial assessment first

For every resource nomination, addition PR, or existing-entry review, complete
an editorial assessment before substantial technical investigation.

1. Read CONTRIBUTING.md and the full issue or PR discussion. Identify exactly
   what is being nominated and which earlier questions have already been answered.

2. Find comparable accepted and declined nominations, including recent decisions.
   Read the actual maintainer comments. Explain the relevant similarities and
   differences; do not select only precedents supporting a preferred outcome.

3. Inspect representative resource content and assess its audience, mathematical
   depth, explanatory or technical usefulness, distinct value, durability,
   ownership, access, and evidence of quality or use. Distinguish the value of
   the nominated resource from claims about its underlying product or results.

4. State a provisional editorial recommendation and its decisive reason.
   Identify any unresolved factual question that could change that recommendation.
   If the resource clearly fails on scope or editorial value, stop investigating
   and recommend declining it.

5. Undertake technical checks only when they could resolve a decision-relevant
   uncertainty, or when the user explicitly requests them. Choose proportionate
   checks. Successful compilation, reproduction, or benchmark evaluation does
   not by itself establish suitability for this list.

6. Report the final editorial recommendation first, followed by supporting
   evidence, relevant precedents, and investigation limits. If the recommendation
   changed, identify the new evidence or corrected reasoning that changed it.

Low popularity, youth, language, or lack of institutional adoption is not an
automatic rejection. Conversely, technical sophistication and extensive artifacts
do not automatically establish substantial value to readers.

When a contributor answers a technical follow-up, reassess the whole nomination.
Answering that question is not an implied promise of acceptance.

## Assessing resources

- Compare proposals with recent decisions on similar resources. Read the actual
  maintainer comments, not just issue labels or closure reasons. For example,
  #193 and #195 concern mathematical quality; #194, #197, #202, and #204 concern
  depth or evidence; #203 concerns original-research scope. #200 is an accepted
  archive nomination. Look up later decisions too; these examples are not fixed
  rules or a substitute for current evidence.
- Assess scope, mathematical quality, distinct value, durability, ownership,
  and access. Separate independently checked facts from author claims.
- Strong evidence of quality, use, or independent recommendation can qualify.
  Do not invent mandatory institutional adoption, popularity, minimum age,
  open licensing, or independent reproduction requirements for every resource.
- Tests, CI, download counts, and publicity are evidence only of what they
  actually measure. A passing formal benchmark checks a particular target;
  it does not establish general system reliability or teaching value.
- Before alleging mathematical errors, verify them and retain exact passages,
  links, and counterexamples. A scope rejection does not require a proof audit.
- Ask for clarification only when a concrete answer could change the decision.
  Do not turn a clear rejection into an open-ended request for more material,
  or ask again for information already supplied.
- Apply the same substantive standard to existing entries. Past inclusion is
  not an endorsement under today's policy. Distinguish removal candidates from
  entries needing a better URL, description, category, or access disclosure.
- Do not infer unavailability from a timeout, 403, or failed automated fetch.
  Look for an official replacement before recommending removal.

## Suggested decision comments

Keep the detailed assessment for the maintainer separate from the proposed
GitHub comment. Follow the short, direct style of earlier maintainer decisions.

- Default to 2–3 sentences, roughly 25–60 words. Exceed this only when concrete
  corrections or an acceptance entry require it.
- Briefly thank the contributor, give the decisive reason, and state the action.
  Usually one reason is enough. Avoid lengthy praise, review narratives,
  multiple caveats, defensive explanations, and restating the nomination.
- For a decline, say that the resource does not yet meet the selection standard
  or falls outside the prioritized scope. Do not imply that it is worthless,
  mathematically wrong, or permanently excluded without supporting evidence.
- Mention reconsideration only when useful, in one short sentence; ask for
  substantial new evidence in the same issue, not a new nomination.
- For a follow-up, ask one focused question or a short set of related questions
  that could resolve the decision. Do not append a rejection speech.
- For acceptance, name the section and provide the exact proposed entry; invite
  a PR linking the accepted nomination.
- When recommending several actions, state each issue's disposition explicitly:
  accept/invite PR, comment/keep open, or decline/close as not planned. Do not use
  a completed closure reason to imply acceptance.
- Drafting or reviewing does not authorize posting comments or changing issue
  states. Make those changes only when the user explicitly requests them.

Examples to adapt to the evidence, not copy indiscriminately:

> Thanks for the nomination. This resource does not yet meet our selection
> standard for depth and evidence of quality or use, so I'm closing this for now.

> Thanks for the detailed nomination. This collection primarily presents
> original research, which falls outside the scope we prioritize for this list,
> so I'm closing it.

> Thanks for the nomination. Could you link a pinned environment and exact
> commands for reproducing the featured example without the private runtime?

## Local validation

For repository changes, run the applicable checks documented in CONTRIBUTING.md.
Do not add tests for prose-only changes. Report investigation limits accurately;
a sample review is not a complete mathematical or interactive audit.
