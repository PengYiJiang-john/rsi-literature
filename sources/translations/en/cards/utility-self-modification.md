# Which Objective Should Evaluate a Change of Objective?

A system could replace “success means completing the task” with “every outcome counts as success.” Its self-evaluation would improve without any improvement in behavior. Everitt and colleagues ask which objective should evaluate a modification when an agent can change its own goals.

## Three evaluation rules

The first rule evaluates outcomes using the modified utility function. Under this rule, adopting a utility function that assigns maximal utility to every outcome can itself be an optimal modification.

The second keeps the current utility function but predicts future behavior as though the modification had not occurred. It retains the original criterion while ignoring how the change affects subsequent actions.

The third uses the current utility function and predicts the behavior that the modification would actually produce. The paper calls this *realistic* evaluation: what would the modified agent do, and would those actions be better under its present objective?

## Conditions for preserving optimality under the original objective

For the third rule, the paper proves that behavior along the realized history can remain optimal for the original objective, provided the initial policy is optimal and the beliefs and initial utility satisfy modification independence and the other stated conditions.

Modification independence means that, with external actions and observations held fixed, utility and beliefs about the environment cannot change merely because the record of internal program modifications differs. Modifications can still affect outcomes through future actions. The theorem preserves behavioral optimality under the original objective; it does not require the utility code to remain textually unchanged.

## How this differs from rewriting training rewards

[Eureka](eureka.md) changes training rewards while evaluating policies against a fixed task criterion. It compares different means of pursuing the same objective. Utility self-modification allows that criterion to change as well. Evaluation rules and predictions of future behavior must therefore be specified together to distinguish better behavior from a change in how behavior is scored.

## Source and reading guide

Everitt, Filan, Daswani, and Hutter (2016), *Self-Modification of Policy and Utility Function in Rational Agents*, AGI; arXiv v1. See §3, Assumption 8, Definitions 9–12, and Theorems 14–16.

[Paper](https://arxiv.org/abs/1605.03142v1) · [Full text](https://arxiv.org/html/1605.03142v1)
