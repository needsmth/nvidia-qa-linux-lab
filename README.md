# NVIDIA QA Linux Lab

## Project purpose

This is a practical, long-term Linux QA Automation and Software Verification
learning lab. It develops NVIDIA-oriented skills through real Linux systems,
networking, automation, CI/CD, performance measurement, and system debugging.
It is an independent learning project, not an NVIDIA product.

## Environment

The primary environment is the Ubuntu Linux host qa-linux-01. Linux is the
primary execution environment. Tools and coverage are introduced progressively
by roadmap stage; system configuration is not changed without explicit approval.

## Current status

- Stage 0 — Linux Server Foundation: **DONE**
- Stage 1 — Git / GitHub / Development Workflow: **CURRENT**
- Stages 2–14: **FUTURE**

Work remains in Stage 1 unless the project owner explicitly advances it. See
[NVIDIA_QA_LINUX_LAB_ROADMAP.md](NVIDIA_QA_LINUX_LAB_ROADMAP.md).

## Repository structure

```text
AGENTS.md                         Repository operating instructions
README.md                         Project overview
NVIDIA_QA_LINUX_LAB_ROADMAP.md    Staged engineering roadmap
docs/                             Notes, runbooks, and findings
scripts/                          Automation utilities (introduced later)
tests/                            Automated verification (introduced later)
```

## Connecting to the Linux lab

From a machine with authorized access, use your assigned account:

```bash
ssh <your-user>@qa-linux-01
```

Use existing SSH configuration. Never store passwords, tokens, or private keys
in this repository. Confirm the host and inspect it non-destructively before an
experiment.

## Development principles

- Work in the active roadmap stage; do not skip ahead without approval.
- Verify real Linux behavior and collect useful diagnostics.
- Keep changes small, reproducible, and reviewable.
- Do not make destructive system or network changes without approval.
- Never commit credentials, private keys, tokens, or unnecessary generated files.
- Before committing, inspect status and diffs, run relevant checks, and commit
  only intentional changes.

## Long-term direction

The project progresses from Linux and Git foundations to a Python/pytest
framework, Linux and network verification, performance and NIC behavior, CI/CD,
containers, storage, driver debugging, observability, distributed testing, and
an NVIDIA-oriented capstone. Each stage produces practical artifacts and
measurable evidence of learning.
