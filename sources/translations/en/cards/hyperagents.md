# How HyperAgents makes the improvement process editable

A stronger task program does not necessarily imply a stronger program for modifying it. HyperAgents separates the task program from the improvement program and allows both to be edited. The system can change how it solves a task and how it searches for better solutions.

## How the improvement program enters the next round

The improvement program can edit task code as well as the code for diagnosing errors, proposing changes, and organizing later modifications. New versions undergo task evaluation and remain available for search. Their improvement programs can then perform the next round of modification.

[DGM](darwin-godel-machine.md) already allows descendants to make modifications, while keeping the outer process that generates modification instructions fixed. HyperAgents exposes more of that process as editable code. The base language model, external task scoring, and version-selection rule in the main experiments remain fixed.

## Testing improvement ability separately

During evaluation, the improvement program is held fixed while it modifies a given task program and candidates already generated. A validation set selects a version, and a test set measures its performance relative to the starting task program. This tests how much improvement a particular version can produce. The number of candidates is limited, although attempts can still have different computational costs.

The paper also freezes the improvement program, removes the historical archive, and compares with DGM to examine self-modification and the retention of search branches.

## Transferring experience with modification

The authors transfer systems developed on paper reviewing and robotics reward design to grading mathematical solutions. Under the same evaluation rules and candidate limit, the transferred versions produce larger improvements than a system starting with the initial task and improvement programs. The improvement program stays fixed during this evaluation.

Both parts of the code transfer together, so the result supports the usefulness of the combined system on the new task. Improvements also include repairing output formatting so that the grading process runs correctly; they cannot all be attributed to the improvement program or to mathematical understanding.

[STOP](stop.md) directly optimizes an improvement program through its downstream modifications. HyperAgents includes both task and improvement code in the search and evaluates the effects of transferring them together.

## Source and reading guide

Zhang et al., *Hyperagents*, 2026 preprint. This account uses the [arXiv v1 full text](https://arxiv.org/html/2603.19461v1): §§3–5, especially the improvement-ability evaluation in §5.2. Appendices C.4, D.3–D.4, E.3, and E.5 provide scoring, candidate-selection, and system details.
