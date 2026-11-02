# Why Internal Rewards Can Differ from the Final Objective

If obtaining food first requires learning to open boxes, should training reward only eating, or also opening boxes? Singh and colleagues show why a signal that helps a bounded learner acquire a skill can differ from the criterion used to evaluate it.

## The objective served by a training reward

One grid-world experiment initially provides no food. A learner trained only on food rewards receives little guidance; an internal reward for opening boxes can develop behavior useful when food later becomes available. Internal reward guides learning along the way, while external fitness evaluates returns over the learner’s lifetime.

Let r denote an internal reward, A a specified learning algorithm, and A(r) the resulting policy. If J evaluates lifetime performance, reward design seeks an r that improves J(A(r)). The same reward can work differently for learners with different capabilities, memories, or learning speeds. Its value depends on how it helps the particular learner.

## Comparing reward designs

The authors search a specified reward space and compare the selected internal rewards with training directly on external fitness. Learning to open boxes in advance helps subsequent food collection: behavior without an immediate external return can improve lifetime returns. A second set of partially observable foraging experiments examines rewards that depend on the learner’s internal state.

The learner and reward-search procedure remain fixed. The experiments compare how different training signals help achieve the external objective.

## From internal rewards to automated reward design

[Eureka](eureka.md) adopts this reward-design formulation: a language model writes rewards, policies are trained, and feedback informs revised rewards. Both approaches retain a fixed external criterion. [Utility self-modification](utility-self-modification.md) asks a further question: if that criterion can also change, which objective should determine whether a modification is better?

## Source and reading guide

Singh, Lewis, Barto, and Sorg (2010), *Intrinsically Motivated Reinforcement Learning: An Evolutionary Perspective*. See the journal version, §IV, Equation (1), §V, and the experimental figures and tables.

[Journal record](https://doi.org/10.1109/TAMD.2010.2051031) · [Author PDF](https://www.ece.uvic.ca/~bctill/papers/ememcog/Singh_etal_2010.pdf)
