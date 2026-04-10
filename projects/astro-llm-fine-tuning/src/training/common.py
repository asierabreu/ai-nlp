from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, DataCollatorForLanguageModeling, Trainer, TrainingArguments

from src.training.distributed import build_training_args_backend


def read_yaml(path: str) -> dict[str, Any]:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def _load_lm_dataset(path: str):
    return load_dataset("json", data_files={"train": f"{path}/dataset.jsonl"})


def _tokenize_dataset(dataset, tokenizer):
    def _map_fn(batch):
        return tokenizer(batch.get("text", ""), truncation=True, padding="max_length", max_length=512)

    return dataset.map(_map_fn, batched=True)


def run_causal_lm_training(config_path: str, task_name: str) -> None:
    cfg = read_yaml(config_path)
    config_base = Path(config_path).resolve().parent
    model_config_path = (config_base / Path(cfg["model"]["config_file"]).name).as_posix()
    model_cfg = read_yaml(model_config_path)["model"]

    tokenizer = AutoTokenizer.from_pretrained(model_cfg["name_or_path"])
    model = AutoModelForCausalLM.from_pretrained(model_cfg["name_or_path"])

    train_ds = _load_lm_dataset(cfg["data"]["train_path"])["train"]
    eval_ds = _load_lm_dataset(cfg["data"]["eval_path"])["train"]

    tokenized_train = _tokenize_dataset(train_ds, tokenizer)
    tokenized_eval = _tokenize_dataset(eval_ds, tokenizer)

    backend_kwargs = build_training_args_backend(
        cfg["training"]["backend"],
        deepspeed_config="configs/deepspeed_zero2.json",
    )

    args = TrainingArguments(
        output_dir=cfg["experiment"]["output_dir"],
        run_name=cfg["experiment"]["name"],
        per_device_train_batch_size=cfg["training"]["batch_size"],
        per_device_eval_batch_size=cfg["training"]["batch_size"],
        gradient_accumulation_steps=cfg["training"]["gradient_accumulation_steps"],
        learning_rate=float(cfg["training"]["learning_rate"]),
        max_steps=cfg["training"]["max_steps"],
        save_steps=cfg["training"]["save_steps"],
        eval_steps=cfg["training"]["eval_steps"],
        eval_strategy="steps",
        bf16=bool(cfg["training"]["bf16"]),
        gradient_checkpointing=bool(cfg["training"]["gradient_checkpointing"]),
        logging_steps=10,
        report_to=["wandb"] if cfg["tracking"]["use_wandb"] else [],
        **backend_kwargs,
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=tokenized_train,
        eval_dataset=tokenized_eval,
        data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
    )
    trainer.train()
    trainer.save_model()

    Path(cfg["experiment"]["output_dir"]).mkdir(parents=True, exist_ok=True)
    Path(cfg["experiment"]["output_dir"]).joinpath("run_metadata.json").write_text(
        json.dumps({"task": task_name, "config": config_path}, indent=2),
        encoding="utf-8",
    )
