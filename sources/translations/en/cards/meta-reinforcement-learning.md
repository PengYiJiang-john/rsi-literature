# Meta-Reinforcement Learning: Adaptation with Fixed Weights

A network with fixed weights can still adjust its actions after a recent success or failure. Wang and colleagues locate this rapid adaptation in a recurrent network’s internal state: weights encode a learned way of adapting, while state changes with experience in the current task.

## Training across tasks and adapting within a task

During training, the network repeatedly encounters related tasks. After acting, it receives rewards and other interaction information, updates its internal state, and selects its next action. Outer reinforcement learning adjusts the weights to improve returns across the interaction sequence, thereby shaping how state responds to feedback.

On a new test task, weights remain fixed while the network continues to receive feedback, update its state, and act. For example, when returns change, recent experience can alter its choices. Rapid adaptation thus occurs through state changes without retraining the weights.

## Testing how the network adapts

The paper uses tasks with correlated options, fluctuating returns, and two-stage choices. In volatile environments, the authors compare the network with classical exploration strategies and fixed-learning-rate rules. They also analyze its behavior to estimate the weight it places on recent feedback.

These tasks make a fixed action inadequate over time. Behavioral analysis examines whether adaptation changes with environmental volatility. The experiments therefore assess both task performance and the way feedback is used.

## Learning through state and through parameters

At test time, new experiences change the state; how those experiences are retained and used has already been learned during outer training. [Learned optimizers](learned-optimizers.md) explicitly produce updates to another model’s parameters, whereas this approach adapts through the task network’s state. Both make a learning method the product of learning, with the outer training process still specified by the researchers.

## Source and reading guide

Wang et al., *Learning to reinforcement learn*. First preprint 2016; this account uses arXiv v3 from 2017. See §2.3, §3.1.3–3.1.4, §3.2, and the behavioral analyses.

[Paper](https://arxiv.org/abs/1611.05763v3) · [Full text](https://arxiv.org/html/1611.05763v3)
