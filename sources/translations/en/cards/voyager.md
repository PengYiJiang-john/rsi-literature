# How Voyager turns accumulated skills into resources for later learning

After succeeding at a task, can an agent reuse the steps it has already solved on a related task? Voyager saves successful action programs in a skill library in Minecraft, where they can later be retrieved, called, and combined.

## Turning execution into a reusable skill

The system selects tasks based on the environment state and its existing abilities, then asks a language model to write code for executing them. The environment returns state changes and execution errors, which guide code revision. A separate language-model-based self-verification step judges whether the task is complete.

Successful code enters the skill library. For a new task, the system retrieves relevant skills and gives them to the language model, allowing new code to focus on differences between tasks and on skill combinations. The base language model's weights remain frozen. The rules for task selection, retrieval, writing to memory, and self-verification also stay fixed; skill content accumulates.

## What removing the skill library tests

The authors remove the skill library to test whether task selection and code generation within the current attempt can sustain exploration. Exploration stalls earlier in this version, supporting the contribution of storing and calling earlier skills. The paper also tests skill transfer to tasks in a new world, extending evaluation beyond the original successful experience.

## Skills and world models support later rounds in different ways

[Toolformer](toolformer.md) learns when to call supplied interfaces. Voyager adds its own programs to the set of callable tools. Earlier skills enter later combinations, allowing learning outcomes to support subsequent action directly.

[Memento 3](memento-3.md) stores environmental rules for predicting actions not yet taken. A skill program provides steps for completing a task; a world model predicts an action's consequences. They accumulate reusable procedures and understanding of the environment, respectively.

## Source and reading guide

Wang et al., *Voyager: An Open-Ended Embodied Agent with Large Language Models*, first released in 2023, TMLR 2024. This account uses the [arXiv v2 full text](https://arxiv.org/html/2305.16291v2): §§2.1–2.3 for the curriculum, skill library, and feedback process; §§3.2–3.4 and Figures 1 and 9 for comparisons.
