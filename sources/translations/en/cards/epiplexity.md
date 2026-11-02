# Epiplexity and structure accessible under limited computation

Data can be difficult to predict because it is close to random or because it contains complex patterns the learner has not understood. Both can produce large prediction errors, but they offer different learning opportunities. Finzi and colleagues introduce epiplexity through a computationally constrained coding problem that separates describable structure from the remaining unpredictable content.

## Describing both the model and what it leaves unexplained

Choose a probability model P, then use it to encode data X. The total cost has two parts: the bits needed to specify the program for P, and the bits still needed to encode the data using P. Among programs satisfying a runtime limit, the paper selects one minimizing the total:

```math
P^\star\in\arg\min_{P\in\mathcal P_T}
\left\{|P|+\mathbb E[-\log_2P(X)]\right\}.
```

Here 𝒫ₜ contains programs that can perform the required sampling and probability calculations within time T. The term |P| is the program's description length; the expectation is the average remaining data-encoding cost. P★ is a program achieving the best total code. Epiplexity is the first component, |P★|; the associated time-bounded entropy is the second.

Program length measures the cost of specifying a model. The runtime constraint determines which models are eligible.

## Why structure differs from pure noise

For random data without exploitable patterns, a complex program may not reduce the remaining code enough to justify its description cost. For some structured data, a longer program can capture many regularities and shorten the total description. Epiplexity measures the part of this optimal description allocated to the model, rather than the entire prediction error.

The quantity depends on the computational budget and coding scheme. Relaxing the constraint can turn content previously recorded as a remainder into structure that a program can explain.

## Testing whether the structure helps a task

The authors arrange the same chess information into two pretraining sequences: board then moves, or moves then board. The first ordering has higher estimated epiplexity. After fine-tuning, the resulting models perform similarly on chess puzzles, while the first is better at predicting numerical position evaluations.

This comparison shows that the organization of the same information affects what a bounded learner can extract, with benefits that depend on the downstream task. Experimental epiplexity is estimated approximately through training and coding.

## Structure and progress are different quantities

[Compression progress](compression-progress.md) measures how much an update reduces coding cost. Epiplexity characterizes the structural part of the best description under a constraint. [V-information](usable-information.md) measures how much an input helps with a specified prediction target.

## Source and reading locations

Marc Finzi and colleagues (2026), *From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence*, preprint. [Version used: arXiv v2](https://arxiv.org/abs/2601.03220v2); [full PDF](https://arxiv.org/pdf/2601.03220v2).

Checked: Definitions 7–8 and Theorems 9–10 in §3, §4, Figure 7 in §6.1, and Appendix C.4.
