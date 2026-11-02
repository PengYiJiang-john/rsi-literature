# Finite discriminators: indistinguishable distributions need not be identical

A generative adversarial network trains a generator to produce samples and a discriminator to distinguish them from real data. Arora and colleagues ask: when the discriminator cannot tell them apart, has the generator learned the real distribution, or merely satisfied the checks available to that discriminator?

## Discriminative capacity determines the measure of closeness

Let P be the real distribution, Q the generated distribution, and 𝓕 the allowed class of discriminator functions. Each function f assigns a score to a sample. The following distance takes the largest difference in average scores that an allowed function can detect:

```math
d_{\mathcal F}(P,Q)=\sup_{f\in\mathcal F}
\left|\mathbb E_P f-\mathbb E_Q f\right|.
```

The expectations are over real and generated samples respectively. A small distance means this class of discriminators has difficulty separating the distributions. Differences in structures the discriminators cannot test may go undetected.

## Generalization can coexist with missing diversity

A failure to distinguish training samples might simply reflect too little data. Under conditions including a bounded measuring function and smooth dependence on network parameters, the paper shows that finite samples can estimate the corresponding neural-network distance. Closeness as judged by the restricted discriminators can therefore generalize from samples to population distributions.

The authors also construct distributions with very small support that are difficult for finite discriminators to distinguish from the real distribution, despite missing much of its diversity. More data can improve estimation of the restricted distance; the discriminator class still determines what is being tested.

The paper also experiments with mixtures of generators and discriminators on images, comparing sample quality and generation metrics. The theoretical construction explains why finite discriminative capacity permits omissions; the experiments examine the mixture-based training method.

## Reading Berk–Nash and model collapse through feedback

Comparing the feedback processes, finite-discriminator theory studies what can be recognized after samples arrive. [Berk–Nash](berk-nash.md) studies how actions select evidence and subjective models interpret it. [Model collapse](model-collapse.md) studies how omissions and errors propagate when a previous model becomes the data source.

[Reward overoptimization](reward-overoptimization.md) further examines how pursuing the current score changes outputs. For RSI, evaluators' discriminative capacity affects which improvements can be recognized and retained. [How feedback corrects a learner](../topics/feedback.md) connects these steps and uses board games and code to illustrate effective feedback.

## Source and reading guide

Arora and colleagues, 2017, *Generalization and Equilibrium in Generative Adversarial Nets (GANs)*, ICML. [Paper page](https://proceedings.mlr.press/v70/arora17a.html) and [published PDF](https://proceedings.mlr.press/v70/arora17a/arora17a.pdf).

Generalization: §3.3, Theorem 3.1. Small-support construction: §3.4, Corollary 3.1. Image experiments: §6. The displayed formula uses a linear measuring function to explain the restricted distance; the paper allows more general measuring functions.
