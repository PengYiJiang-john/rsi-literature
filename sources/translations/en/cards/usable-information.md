# Why the same evidence is more usable for some learners

A pattern can be present in data without being accessible to every model. As a simple illustration, let two independent inputs each be equally likely to equal +1 or −1, with their product determining the outcome. A predictor restricted to a linear readout may perform very differently when given the two inputs directly or their product as a feature. The evidence is the same; its usability changes. Xu and colleagues formalize this distinction as usable information.

## Specify who is using the information

Let X be the input, Y the outcome to predict, and 𝒱 the allowed family of predictive models. After observing X, a model f assigns probabilities to the possible values of Y. The expression f(X)(Y) is the probability it assigns to the outcome that actually occurs.

The paper evaluates predictions by log loss. Repeatedly assigning low probability to observed outcomes incurs a large loss. The lowest average loss achievable within the family defines conditional V-entropy:

```math
H_{\mathcal V}(Y\mid X)
=\inf_{f\in\mathcal V}\mathbb E[-\log f(X)(Y)].
```

The infimum is the lowest loss that the family can approach; the expectation averages over the data distribution. Let H𝒱(Y) be the corresponding best loss without observing X. Their difference is the usable information supplied by the input:

```math
I_{\mathcal V}(X\to Y)
=H_{\mathcal V}(Y)-H_{\mathcal V}(Y\mid X).
```

The difference asks how much access to the input can improve prediction for this family. If the family allows a predictor to ignore the input, the old best prediction remains available, so the difference is nonnegative.

## How computation can make information more usable

Deterministic processing of an input cannot increase its Shannon mutual information with the prediction target. Yet the product example shows how processing can put the same pattern into a form that a restricted predictor can use. No new evidence is introduced.

The paper compares information estimators on tasks including synthetic tree-structure recovery. Recovering a structure requires inferring relationships between variables, so how an estimator measures information in those relationships affects the recovered tree.

## Available information and completed learning

The definition uses the best prediction within a model family. A particular training run may not have found that predictor. The gap between current loss and the family optimum concerns training progress; the improvement made possible by a stronger family concerns predictive capacity.

The [merged-staircase property](merged-staircase.md) studies how training can acquire new features. [Compression progress](compression-progress.md) compares actual performance before and after an update. They address how usable information can be learned and how much learning has already changed performance.

## Source and reading locations

Yilun Xu and colleagues (2020), *A Theory of Usable Information under Computational Constraints*, ICLR. [Version used: arXiv v1](https://arxiv.org/abs/2002.10689v1); [full text](https://arxiv.org/html/2002.10689v1).

Checked: Definitions 1–3, Proposition 2, §3.2, Theorem 1, and §6.1.
