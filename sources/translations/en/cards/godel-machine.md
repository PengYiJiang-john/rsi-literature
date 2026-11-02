# The Gödel Machine’s Criterion for Self-Modification

After finding a potentially useful modification, should a program apply it immediately or keep searching for a better one? The Gödel machine uses a proof condition to decide when to stop searching and modify itself.

## The acceptance condition

The system uses axioms to describe its own operation, its environment, and its utility objective. A proof-search program seeks candidate modifications and attempts to prove that executing one now has greater expected future utility than continuing the current search process.

Once such a proof is found, the system executes the modification. Replaceable components include the programs that search for modifications and proofs. A modification can therefore change how subsequent modifications are proposed, checked, and implemented.

## Why the alternative is continued search

Continuing to search includes the possibility of finding other proposals later. Comparing a candidate only with “never change the current program” would not explain why the system should stop searching now. The acceptance condition accounts for waiting, search, and future self-modifications, combining the stopping decision and the modification decision in one utility comparison.

The optimality result is relative to the system’s axioms. A useful modification may be unprovable within them, and an existing proof may not be found in time. The result therefore governs the choice to modify once the required proof has been obtained.

## Acceptance by proof and evaluation by experiment

[Metareasoning](metareasoning.md) also connects computational costs to eventual choices; the Gödel machine additionally allows changes to the computing program itself. The modern reward-design system [Eureka](eureka.md) instead trains policies with candidate rewards and uses task performance to guide further revisions. The former accepts modifications through proof, while the latter evaluates candidates through training experiments. They provide, respectively, a formal acceptance criterion and an executable feedback process.

## Source and reading guide

Schmidhuber, *Gödel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements*. First draft 2003; this account uses v5 from 2006. See §2.4, Theorem 4.1, and §4.3.

[Paper](https://arxiv.org/abs/cs/0309048v5) · [Full text](https://arxiv.org/html/cs/0309048v5)
