# Neural Architecture Search: Learning to Propose Better Models

Trying many architectures at random can also produce a good network. Zoph and Le train an architecture controller to test whether feedback from previously trained candidates helps it propose better networks.

## How the controller uses candidate performance

The controller generates symbols describing a network, such as layer settings or connections within a recurrent cell. The system builds the candidate, trains its weights, and evaluates it on validation data. The controller uses this evaluation as a reward and learns, through reinforcement learning, to adjust the probabilities of proposing different architectures.

Each round therefore contains two learning processes: candidate networks learn the task, while the controller learns to propose networks. The former updates weights; the latter updates the distribution over architecture proposals.

## What the random-search comparison supports

The authors search for convolutional architectures in image classification and recurrent cells in language modeling. The language-modeling experiment compares controller-based search with random search, examining both the best candidate and the average performance of leading candidates.

The controller outperforms random search in these comparisons, supporting the use of training feedback to improve subsequent proposals. Performance across several strong candidates provides evidence beyond a single best result; it does not require every proposal to outperform its predecessor.

## Architecture search and update rules

The controller learns within a search space specified by the designers; its own architecture and update algorithm remain fixed. [Learned optimizers](learned-optimizers.md) change how a given model is trained, while architecture search changes which model is proposed. Both turn a component of producing task capability into a mechanism that can learn from experience.

## Source and reading guide

Zoph and Le (2017), *Neural Architecture Search with Reinforcement Learning*, ICLR; arXiv v2. See §3.1–3.2, §4.1–4.2, and the random-search comparison.

[Paper](https://arxiv.org/abs/1611.01578v2) · [Full text](https://arxiv.org/html/1611.01578v2)
