# How Toolformer learns to use existing tools

For an arithmetic problem, a language model can answer directly or call a calculator first. Toolformer lets the model generate its own training examples to learn which tool to call, when to call it, how to prepare its input, and how to use the result.

## The model proposes calls and a filter tests their usefulness

The researchers provide tool interfaces and a few examples. The model inserts candidate calls into ordinary text. The system executes them, puts their results back into the text, and checks whether they reduce the prediction error for subsequent words. Examples that pass this filter enter the fine-tuning data, teaching the model those uses.

The positions of tool calls need no individual human annotation. Researchers specify the tools, initial examples, and loss-based filter. Fine-tuning changes the model's calling behavior; the tool implementations and training-example generation process remain fixed.

## Separating the effects of training and execution

One control is trained on the same corpus without tool calls, testing the effect of additional text training. Another disables tool calls at test time, testing the effect of executing a tool.

On arithmetic tasks, the version allowed to call a calculator outperforms the version with calls disabled. Both retain the same trained parameters; the difference is whether the calculator can actually run. Some of the gain therefore comes from tool execution.

## Tools can supply facts or perform calculations

A lookup tool can provide facts absent from the input, while a calculator can evaluate an expression already given. Toolformer learns when to delegate these operations to existing interfaces. [Voyager](voyager.md) instead saves action programs it has written as callable skills: Toolformer learns to use existing tools, while Voyager adds reusable tool content.

## Source and reading guide

Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*, NeurIPS 2023. This account uses the [arXiv v1 full text](https://arxiv.org/html/2302.04761v1): §2 for the method, §4.1 and Table 4 for experiments. The focus is the generation, execution, and filtering of tool-call examples, and the controls using the same training corpus or disabling tool calls.
