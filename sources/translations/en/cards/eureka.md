# Eureka: Improving Reward Programs through Training Feedback

Giving a robot a task objective still leaves the problem of designing rewards that help it learn. Eureka uses a language model to revise reward code, guided by the results of policy training.

## Changing the training signal while keeping evaluation fixed

A reward program guides policy training; an external task score evaluates the trained policy. Policies produced by different rewards are compared under this fixed criterion. The objective is to improve F(A(R)), where R is a reward program, A(R) the policy trained with it, and F the task evaluation. This follows the distinction between [internal rewards and external objectives](internal-rewards.md).

## How feedback informs the next revision

The language model reads the task description and environment code, then generates candidate reward programs. A reinforcement learning algorithm trains a policy with each reward, recording task performance and training statistics for individual reward components.

The language model reads this feedback alongside the reward code. Task performance indicates which designs are worth pursuing; the magnitudes and trends of reward components help connect training behavior to the code and guide subsequent revisions.

## What the two comparisons establish

Simply generating more candidates could also yield better rewards. The authors therefore compare one-shot generation with generation over successive rounds, using the same total number of candidates. The latter uses feedback from earlier training and performs better. This supports the contribution of feedback-driven iteration beyond the number of attempts; matching candidate counts does not match all computational costs.

A second comparison retains task scores but removes detailed feedback on reward components. Performance declines, indicating that these statistics provide additional help beyond task scores in the tested tasks and search procedure.

The loop revises reward code while keeping the base language model, reinforcement learning algorithm, task evaluation, and search framework fixed. Eureka connects training feedback to better training signals. [Utility self-modification](utility-self-modification.md) instead examines how to evaluate changes to the objective itself.

## Source and reading guide

Ma et al. (2024), *Eureka: Human-Level Reward Design via Coding Large Language Models*, ICLR; arXiv v2. See Definition 2.1, §3.2–3.3, §4.1–4.3, and the feedback ablations.

[Paper](https://arxiv.org/abs/2310.12931v2) · [Full text](https://arxiv.org/html/2310.12931v2)
