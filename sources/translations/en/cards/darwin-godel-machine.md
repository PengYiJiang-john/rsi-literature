# How DGM lets descendant programs continue self-modification

After a coding agent modifies itself, can the new version help make further changes? The Darwin Gödel Machine (DGM) lets descendant programs participate in self-modification and retains several past versions for later search.

## One program performs two jobs

During task evaluation, the program fixes issues in code repositories or solves programming tasks. During self-modification, it reads a modification request and changes its own tools and workflow. The system selects a starting version from its history, makes changes, and evaluates the new version on programming tasks.

Usable programs are retained as code in an archive. A version that is not currently best may still contain useful tools or procedures, so keeping it preserves a starting point for further changes. The base language model, the outer process that generates modification instructions, and the version-selection rule remain fixed. The program carrying out those instructions can be a descendant produced earlier.

## Freezing the modifier and removing the archive

One control always uses the initial program to make modifications, preventing descendants from taking over. Its later gains level off sooner, supporting the value of allowing descendants to participate in modification on the tested coding tasks.

A second control removes the archive and continues only from the latest working version. Poor modifications more readily obstruct this process, while the full system can return to another branch. This comparison tests the value of preserving search paths, complementing the first comparison's test of changes to the modifier.

## How coding ability can support self-modification

DGM draws on the overlap between solving programming tasks and editing its own implementation. [HyperAgents](hyperagents.md) makes more of the improvement process editable and evaluates transfer across domains.

DGM evaluates candidates through task experiments and keeps multiple branches for further search. The original Gödel machine requires a proof that a modification is beneficial. The two approaches use empirical evaluation and formal proof, respectively, as the basis for modification.

## Source and reading guide

Zhang, Hu, Lu, Lange, and Clune, *Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents*, first released in 2025. This account uses the [arXiv v3 full text](https://arxiv.org/html/2505.22954v3): §3 and Algorithms 1–3 for the procedure; §§4.1–4.4 and Appendices E.2–E.3 for tasks and ablations.
