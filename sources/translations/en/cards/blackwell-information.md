# Blackwell on how information improves decisions

Suppose you use temperature to decide whether to switch on a machine. One sensor reports the exact temperature; another reports only whether it exceeds a threshold. A decision based on the threshold can also be made using the exact reading: convert the number into a threshold result, then apply the same decision rule. This illustrates the starting point of Blackwell's comparison: can one signal reproduce the decisions supported by another?

## Simulating a coarser signal

Let w be the unknown state. Channel A produces signal x, and channel B produces signal z. Suppose a fixed processing rule K can turn x into a signal with the same distribution as B, by discarding detail or adding randomness:

```math
Q_B(z\mid w)=\sum_x K(z\mid x)Q_A(x\mid w).
```

The two Q terms describe each channel's signal distribution when the state is w. K(z|x) is the probability of producing z after receiving x. Crucially, K can use only the signal, not the unknown state w; otherwise, the processing step could introduce additional information.

Take any decision rule that uses B. A decision maker with access to A can first generate z using K, then apply that rule, reproducing its performance. A therefore preserves every decision rule available under B. With the same prior and payoff function, no acquisition cost, and optimal use of information, A cannot yield a lower optimal expected payoff.

## When additional information changes the outcome

The conclusion is a weak improvement, not necessarily a strict one. If switching on the machine requires only a threshold judgment, the exact temperature may add no value. Extra detail can improve the outcome only if it changes which action is worth taking. The decision value of information therefore depends on the task.

This argument allows the decision maker to simulate the old channel freely and choose the best rule. Learning also involves acquisition costs and limits on using information. [Usable information](usable-information.md) studies how much evidence a restricted predictor can exploit; [dual control](dual-control.md) studies how actions determine the evidence available later.

## Source and verification scope

David Blackwell (1953), *Equivalent Comparisons of Experiments*, Annals of Mathematical Statistics 24: 265–272. [Published paper](https://doi.org/10.1214/aoms/1177729032); [scholarly profile and abstract](https://celebratio.org/Blackwell_DH/article/255/).

Verification was limited to the bibliographic record and abstract. This note explains only the direct implication from signal processing to nondecreasing decision value; the paper's full equivalence theorem was not verified.
