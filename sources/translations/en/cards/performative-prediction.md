# Performative prediction: how a model changes its next training data

Once a credit-scoring rule is deployed, applicants may adjust what they report, changing the next round of training data. Perdomo and colleagues study this form of performative prediction: deployment affects the environment, and retraining uses the data the environment returns.

## Retraining and deployment optimization

Let φ be the parameters of the deployed model and D(φ) the data distribution it induces. Let θ be the parameters of the model being evaluated, and ℓ(z; θ) its loss on sample z:

```math
R(\theta;\phi)=\mathbb E_{z\sim D(\phi)}[\ell(z;\theta)].
```

The second argument determines the data source; the first determines which model is scored. Retraining collects data induced by the old model θₜ, then selects a new model minimizing R(θ; θₜ). Deployment optimization instead minimizes R(θ; θ): when changing the model, it also accounts for the new data distribution that model will induce.

If retraining stops at θ*, then θ* is best suited to D(θ*). Another model may change people's behavior and achieve lower loss on the resulting distribution. Stability and optimal deployment can therefore differ.

## When retraining converges

The paper requires the loss gradient to be smooth in both parameters and samples: changes in θ or z must change the gradient at a rate bounded by β. The loss must also be γ-strongly convex in its parameters, giving optimization on the current distribution a unique, stable solution.

Deployment-induced distribution changes are measured using Wasserstein-1 distance: the minimum average distance required to transport one distribution into another. A unit change in parameters may change the distribution by at most ε units.

When ε < γ/β, repeated population risk minimization converges to a unique stable point. This bound gives a sufficient condition for stable retraining. “Population” means each round uses the exact distributional expectation; the finite-sample version additionally requires tail conditions and sample sizes that grow with iteration.

## Bringing feedback into the objective

[Outside the Echo Chamber](outside-echo-chamber.md) studies the gap between stability and optimality, estimating the environment's response to deployment in order to optimize performative risk. [Berk–Nash](berk-nash.md) examines how evidence selected by actions supports subjective beliefs.

Performative prediction puts the model's effect on the data distribution directly into the objective. For RSI, evaluating a modification likewise requires accounting for its effects on subsequent feedback.

## Source and reading guide

Perdomo and colleagues, 2020, *Performative Prediction*, ICML. [Paper page](https://proceedings.mlr.press/v119/perdomo20a.html) and [published PDF](https://proceedings.mlr.press/v119/perdomo20a/perdomo20a.pdf).

Risk and stability are defined in §2. Convergence conditions appear in Theorem 3.5; related distinctions appear in Proposition 3.6 and §4.
