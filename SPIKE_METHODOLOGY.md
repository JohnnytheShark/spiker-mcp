Specification: The S.P.I.K.E.R. Methodology
Version: 1.1.0

Status: Production-Ready

Framework: Japanese Precision Engineering for Software Systems

1. Philosophy: The "Zero-Entropy" Goal
S.P.I.K.E.R. is a methodology designed to prevent Technical Sepsis. In the same way that the Ikejime method stops biological decay at the moment of harvest, S.P.I.K.E.R. stops technical debt at the moment of commit. We treat "Stress" (ambiguity, tight coupling, and bloat) as a toxin that ruins the "meat" (logic) of the application.

2. The S.P.I.K.E.R. Pillars
[S] Systemic Spiking (Intent Precision)
Definition: Destroying ambiguity before the first line of code.

The Rule: If you cannot explain the "Success State" and "Failure State" in one sentence, the "brain" is still alive and struggling.

Documentation: Architecture Decision Records (ADRs) must be finalized here.

[P] Peripheral Purge (Minimalist Hygiene)
Definition: Immediate removal of "Sanguineous Logic" (dead code, logs, and "just-in-case" parameters).

The Rule: Refactor during the flow, not as a future ticket. If it doesn't serve the core intent, it is "blood" and must be drained.

[I] Isolation of Nerves (Structural Decoupling)
Definition: Severing the spinal cord between unrelated modules.

The Rule: Use interfaces to ensure that a "twitch" in the UI or Database does not propagate to the Business Logic.

Design Pattern: Dependency Injection and strict API boundaries.

[K] Kinetic Hygiene (Dependency Purity)
Definition: Avoiding "Tap Water" (impure external dependencies).

The Rule: Be aggressively protective of the environment. Every external library is a potential point of contamination. Use native solutions where possible.

[E] Enzymatic Aging (Extensibility)
Definition: Designing code that matures and develops "Umami."

The Rule: Code is written for the next person. It should be stable enough to be extended without being rewritten.

Documentation: Diataxis "Explanation" and "Reference" sections.

[R] Rigorous Refinement (Quality Verification)
Definition: The final "Kensha" (Inspection).

The Rule: Use Zero-Signal Testing. Tests must fail loudly and pass silently. A "sharp" test suite verifies that the "Spike" worked and the "Nerves" are isolated.

Action: Automated Unit, Integration, and Contract testing.

3. Mapping to Diataxis Documentation
   
|Pillar|Documentation Type|Focus |
|--|--|--|
|Spike|Explanation / ADR |The "Why" behind the architecture.|
|Purge|Tutorials| The cleanest, most direct path to implementation.|
|Isolate|Reference| Technical API specs and boundary definitions.|
|Kinetic| How-to Guides| Solving specific tasks with zero bloat.|
|Age/Refine|Testing Docs|Validation of long-term stability.|

4. LLM Implementation (System Prompt)
Copy and paste this into an LLM context or MCP Resource description:

"Act as a S.P.I.K.E.R. Methodology Consultant. Evaluate the provided codebase or technical proposal against the six S.P.I.K.E.R. pillars. Identify 'Systemic Ambiguity' (S), 'Sanguineous Logic' (P), 'Nerve Propagation' (I), 'Tap Water Bloat' (K), and 'Rot-prone Design' (E). Finally, suggest 'Rigorous Refinement' (R) through specific testing strategies. Format output as an ADR and organize supporting docs via Diataxis."

5. Glossary
Ikejime-Code: Software that was killed (completed) cleanly and can be aged (maintained) for years.

Lactic Acid: The "sour" taste in a codebase caused by rushing, stress, and poor initial requirements.

The Spike: The definitive moment logic is solved, before the keyboard is touched.