# Model collapse: why learning only from the previous generation loses content

If each generation learns only from its predecessor's samples, how long can rare content survive? Shumailov and colleagues study a repeated process: train a model, sample from it, and train the next model on those samples. Sampling and fitting errors also enter the next generation's data.

## How one omission changes later data

A rare event may be absent from a generation's finite sample. The next model sees only that sample and may assign the event an even lower probability, making it harder to generate later. An omission in one sample can thus change future sampling distributions.

Fitting adds another source of error. Finite data and a given model class only approximate the target distribution, and this approximation becomes the new data source. Each generation inherits upstream bias and adds its own sampling and fitting errors.

## Generational replacement with fixed sample size

The discrete and Gaussian analyses consider a fixed number of samples generated solely by the preceding model at each generation. The discrete analysis shows how finite sampling can eliminate categories.

In the Gaussian process analyzed, covariance tends to zero almost surely, while the expected squared Wasserstein-2 distance from the original distribution diverges. The squared distance measures the minimum average squared displacement needed to match the distributions. A narrowing distribution along a typical trajectory therefore need not become closer to the original distribution in expected distance.

## Comparing data sources in language models

The authors repeatedly fine-tune language models on generated text and compare this with continued inclusion of original data, examining changes in rare content and distributional detail. They also vary the repetition penalty used in generation to examine the effect of sampling choices.

The experiments support retaining original data to mitigate degradation. The two main settings also differ in the number of passes through the training data at each generation—the number of epochs—so the comparison varies both data source and training amount.

## Reading GANs and Berk–Nash through feedback

Comparing the feedback processes, model collapse studies who generates the next round of data. [Berk–Nash](berk-nash.md) studies which world responses actions select and how subjective models interpret them. [Finite-discriminator GAN theory](limited-discriminators.md) studies which differences an evaluator can recognize once samples are available.

[Data accumulation](data-accumulation.md) changes error propagation by retaining original and earlier generated data. [How feedback corrects a learner](../topics/feedback.md) connects data sources, evidence selection, and discriminative capacity, using board games and code to show how effective feedback supports improvement.

## Source and reading guide

Shumailov and colleagues, 2024, *AI models collapse when trained on recursively generated data*, Nature 631, 755–759. [Published full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11269175/).

The process is defined in Definition 2.1. See Theoretical intuition and Theorem 3.1 for the analysis, and the experimental sections for language models and repetition penalties. Conditions for the purely synthetic process follow the [2025 author correction](https://www.nature.com/articles/s41586-025-08905-3).
