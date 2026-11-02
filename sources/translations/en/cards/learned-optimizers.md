# Learned Optimizers: Learning How to Update Another Model

A gradient describes how a small parameter change affects the loss; an optimizer must still choose the direction and magnitude of each update. Andrychowicz and colleagues train another network to learn this update rule, using gradient history to guide the next training step.

## One model learns to update another

Let θ denote the task model’s parameters and φ the optimizer’s parameters. The optimizer reads task gradients and its historical state, then outputs an update to add to θ. To train the optimizer, the researchers run it for multiple steps on a collection of tasks and adjust φ using the task losses along those trajectories.

Changes to θ train the task model; changes to φ train the optimizer to perform those updates. On a new test task, φ is fixed, while the task parameters and optimizer state continue to change. The outer backpropagation procedure, optimization algorithm, and task distribution are specified by the researchers.

## Comparing update rules and their transfer

The authors train or test optimizers on random quadratic functions, image classification, and neural style transfer, comparing them with conventional methods whose learning rates have been tuned. Replacing the update rule on the same task tests the effectiveness of the learned optimizer.

The paper also varies the number of optimization steps or the task model’s architecture to test whether the update rule remains useful outside its training setting. Evaluation thus covers both optimization on the training problems and transfer across settings.

## Three ways to learn a learning mechanism

Learned optimizers acquire a rule for updating model parameters. [Neural architecture search](neural-architecture-search.md) learns which model structures to propose. [Meta-reinforcement learning](meta-reinforcement-learning.md) allows a network with fixed weights to adapt through its internal state. These approaches use experience to shape update rules, architecture selection, and state changes, respectively.

## Source and reading guide

Andrychowicz et al. (2016), *Learning to learn by gradient descent by gradient descent*, NeurIPS; arXiv v2. See §2, Equations (2)–(3), §3, and the transfer experiments.

[Paper](https://arxiv.org/abs/1606.04474v2) · [Full text](https://arxiv.org/html/1606.04474v2)
