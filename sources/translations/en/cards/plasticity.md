# Why continual learning also requires plasticity

Does a network remain able to learn new tasks as training continues? Dohare and colleagues find that accumulated training can make later problems harder to learn. The ability to keep learning from new experience is called plasticity.

## Failing to learn new tasks and forgetting old ones

Forgetting research asks how much old knowledge survives after learning a new task. Plasticity research asks how well the network can still learn the new task. The paper trains networks on a sequence of changing tasks and evaluates each one. Performance on later tasks can deteriorate even when retaining earlier tasks is not required.

## Resetting low-utility units to preserve learning ability

In settings including sequences of image tasks, the authors compare standard backpropagation, regularization or perturbation methods, and continual backpropagation. Alongside gradient updates, continual backpropagation tracks units' utility. Units that have trained for some time but still contribute little can be reset, giving subsequent learning room to adjust.

The groups face the same task sequences. In the tested sequences, resetting units reduces the decline in later performance. This indicates that changes caused by prior training contribute to the decline, and that changing the update method can help preserve learning ability. The rules for selecting and resetting units are designed by the researchers and remain fixed during training.

## Feedback must still be learnable after it arrives

A system can receive new feedback while becoming less able to turn it into capability. Plasticity research addresses this failure, separately from a lack of corrective evidence.

[Learned optimizers](learned-optimizers.md) use another model to learn parameter-update rules, while [meta-reinforcement learning](meta-reinforcement-learning.md) uses training across tasks to shape adaptation through internal state. These lines change how a system updates and adapts; maintaining plasticity helps it continue to use later learning opportunities.

## Source and reading guide

The journal article is Dohare et al., *Loss of plasticity in deep continual learning*, Nature, 2024. The method description here follows the authors' preprint v3, titled *Maintaining Plasticity in Deep Continual Learning*. Its title and some of its organization differ from the journal version. The relevant sections are §§2 and 5, Algorithm 1, and the sequential-task experiments.

[Journal record](https://doi.org/10.1038/s41586-024-07711-7) · [Author version used](https://arxiv.org/abs/2306.13812v3) · [PDF](https://arxiv.org/pdf/2306.13812v3)
