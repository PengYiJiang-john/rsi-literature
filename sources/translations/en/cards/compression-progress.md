# Choosing experience through compression progress

Revisiting a familiar pattern usually teaches little, while observing pure noise may never reveal a pattern. What should a learner seek between these extremes? Schmidhuber proposes seeking experiences that produce learning progress, measured by improvements in compression.

## Learning a pattern can shorten a description

A compressor that discovers a pattern can describe data through the pattern and its exceptions, rather than recording every detail separately. Learning can therefore be assessed by comparing the cost of encoding the same history before and after an update.

Let h be a fixed history, C_old and C_new the compressors before and after learning, and L(C,h) the cost of encoding h with compressor C. A progress reward can be written as:

```math
r_{\mathrm{progress}}
=L(C_{\mathrm{old}},h)-L(C_{\mathrm{new}},h).
```

A positive difference means that the new compressor describes the same experiences at lower cost. Both must be evaluated on the same history: comparing an old compressor on difficult data with a new one on easy data would not isolate learning.

## Using progress to choose the next action

The system gives this reward to a controller that selects actions. The controller seeks experiences likely to improve compression. After the compressor learns from them, the measured improvement provides feedback to the controller. Learning thus changes where the system goes and what it observes; those observations, in turn, change what it learns.

Familiar data may be easy to compress but offer no further progress. Pure noise keeps changing but usually supplies no stable, reusable patterns. The reward is intended to favor material that the learner has not mastered but can potentially learn.

Progress is relative to the current learner. Structured data may produce no progress signal when compressor training fails or its capacity is insufficient. The reward measures the observed change between two versions.

## How this differs from other information measures

[Usable information](usable-information.md) asks how much observing an input can improve prediction within a model family. [Epiplexity](epiplexity.md) characterizes the structure needed to describe data under a computational constraint. Compression progress compares old and new compressors on the same history, using completed learning to guide the choice of future experience.

The article develops the framework and formalization and reviews existing implementations. The loop can operate with a fixed compressor update rule.

## Source and reading locations

Jürgen Schmidhuber (2008 draft, revised 2009), *Driven by Compression Progress: A Simple Principle Explains Essential Aspects of Subjective Beauty, Novelty, Surprise, Interestingness, Attention, Curiosity, Creativity, Art, Science, Music, Jokes*. [Version used: arXiv v2](https://arxiv.org/abs/0812.4360v2); [full text](https://arxiv.org/html/0812.4360v2).

Checked: §1.2–1.3, §3, and Appendices A.5–A.7, especially equations (5)–(6).
