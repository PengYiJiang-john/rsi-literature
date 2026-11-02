# How Memento 3 uses a world model to improve the next interaction

When exploring an unfamiliar game, a system must choose its next action after trying only a few possibilities. Memento 3 extracts environmental rules from experience to predict the outcomes of actions it has not yet tried. New execution results then drive revisions to those rules.

## Turning experience into rules and an executable model

The system extracts natural-language rules from interaction records to form a rulebook, then converts them into an executable world model. Given a state and an action, the model predicts the outcome. A planner uses those predictions to select an action for execution in the real environment.

When the result differs from the prediction, the system revises the rules and their implementation. Two checks examine whether the program departs from the written rules and whether it reproduces state changes in past records. The rulebook and executable representation change across rounds; the base language model, revision process, and validation procedures remain fixed.

## Can a rulebook reduce external trial and error?

The authors remove the rulebook as a control while keeping the execution framework, validators, base model, reasoning effort, and other conditions the same. In the selected ablation games, both systems complete the tasks, but the version retaining the rulebook uses fewer environment actions. This supports the rulebook's contribution to interaction efficiency. Game examples further show how particular rules change in response to feedback.

## Moving from agreement with history to new evidence

Two models can explain past experience equally well but predict different outcomes for an untried action. Taking an action that distinguishes those predictions provides an opportunity to discover which explanation is wrong. Committing to one model too early can also steer planning away from such actions.

This connects to [model criticism](bayesian-model-criticism.md): revise an explanation using existing records, then test it against new evidence. Memento 3 implements the first step as an executable rule-revision process and uses the revised model in the next round of action.

## Source and reading guide

Zhao et al., *Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks*, 2026 preprint. This account uses the [arXiv v1 full text](https://arxiv.org/html/2610.11794v1): §2 for the rulebook and validation process; §4, Tables 2–3 for games and the rulebook ablation; §5 for examples; and §1 for the discussion of historical consistency and exploration blind spots.
