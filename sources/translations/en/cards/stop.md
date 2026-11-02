# How STOP evaluates a program that produces improvements

Can a program that edits code become better at editing code by rewriting itself? STOP distinguishes a task program from an improvement program. The task program solves a problem; the improvement program takes task code and a scoring function, then calls a language model to propose changes. Its value is measured by how well the modified task programs perform.

## Evaluating self-modification through downstream performance

The researchers first use the same improvement program to modify a set of task programs and calculate their average utility after modification. During self-modification, the current improvement program edits its own source code to produce a new version. That version receives the same downstream evaluation. Better-performing versions can take over subsequent self-modification.

The base language model, task utilities, and budget mechanism remain researcher-specified. Recursion occurs in the code that organizes language-model calls, and evaluation depends on the changes that code actually produces.

## Testing whether the improvement program becomes more useful

One task is learning parity with noisy labels: the task program must learn a parity relation among bits from examples whose labels may be wrong. The authors compare the self-modified improvement program with the initial program, single-pass generation, and greedy iteration. They evaluate the resulting task programs on independent test instances. Experiments on other tasks examine whether the modification methods transfer.

Self-modification improves average performance with some base models, but can reduce it with weaker models. The experiments therefore support recursive improvement under particular model and task conditions.

## Connections to DGM and HyperAgents

[DGM](darwin-godel-machine.md) uses one program for both problem solving and self-modification, retaining past versions for further search. STOP directly optimizes an improvement program through its downstream results. [HyperAgents](hyperagents.md) also distinguishes task and improvement programs and allows both to be edited. Its transfer experiments move both parts together and evaluate how the combined system helps on a new task.

## Source and reading guide

Zelikman, Lorch, Mackey, and Kalai, *Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation*, COLM 2024. This account uses the [arXiv v3 PDF](https://arxiv.org/pdf/2310.02304v3): §§3–4 and Algorithm 1 for improvement programs and recursion; §§5.1–5.3, Figure 4, and Table 1 for task comparisons and transfer experiments.
