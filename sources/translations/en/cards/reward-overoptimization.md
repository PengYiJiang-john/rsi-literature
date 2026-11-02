# Reward overoptimization: why proxy scores rise while reference scores fall

A scoring model can help a system find better answers, yet steer it in the wrong direction when optimized repeatedly. Gao, Schulman, and Hilton ask how a fixed reference model evaluates outputs as a generation policy works harder to maximize a proxy score.

## Optimization favors overvalued outputs

The proxy score only approximates the target evaluation. Initially, raising the proxy score can also raise the reference score. As search intensifies, however, the system becomes more likely to find outputs that the proxy overvalues. If overvaluation puts an answer above its competitors, that answer becomes more likely to be selected. A consistently overvalued class of answers can then become a direction the policy favors.

Small scoring errors on randomly sampled answers can produce larger distortions when selecting the highest-scoring answer. Optimization changes the output distribution and, with it, which evaluation errors the system encounters.

## Use two evaluators to track divergence

The experiment fixes a reference reward model, uses it to score answers, and trains a smaller proxy reward model on those labels. During optimization, the generation system receives only proxy scores. The reference model remains frozen and evaluates the resulting answers.

The authors compare two methods: generate several candidate answers and select the highest proxy score, or update the policy with reinforcement learning so that high-scoring outputs become more likely. They also vary reward-model size and training-data volume, tracking both scores as optimization increases.

The proxy score can keep rising while the reference score first rises and then falls. Better proxy models generally delay or reduce this divergence. The proxy guides improvement over a range, while continued optimization exposes its errors.

## How optimization amplifies evaluation errors

[Limited-discriminator theory](limited-discriminators.md) studies which differences an evaluator cannot detect. Reward overoptimization asks how those omissions and errors shape outputs when an optimizer specifically pursues the evaluator's highest scores.

In [Berk–Nash](berk-nash.md), evidence selected by actions feeds back into beliefs. Reward overoptimization can occur with a completely frozen evaluator. For RSI, this motivates checking whether a modification concentrates behavior on outputs the current evaluator overvalues, and evaluating those outputs against a fixed reference standard.

## Source and reading guide

Gao, Schulman, and Hilton, 2023, *Scaling Laws for Reward Model Overoptimization*, ICML. [Paper page](https://proceedings.mlr.press/v202/gao23h.html) and [published PDF](https://proceedings.mlr.press/v202/gao23h/gao23h.pdf).

See §2.1 for models and data; §§3.1–3.6 for the two optimization methods, empirical curves, and model-size comparisons; §4.5 for further discussion.
