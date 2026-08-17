# NVIDIA QA Linux Lab — Codex Instructions

## Project

This repository is a practical QA automation and Linux systems verification laboratory.

The long-term goal is to build NVIDIA-oriented Software Verification / QA Automation skills through real Linux, networking, automation, CI/CD, performance and system-debugging work.

## Current Roadmap Stage

Stage 1 — GitHub / Git workflow

Do not advance to later roadmap stages unless explicitly instructed.

The roadmap is maintained in:

`NVIDIA_QA_LINUX_LAB_ROADMAP.md`

## Working Principles

1. Prefer practical engineering tasks over toy examples.
2. Do not skip learning stages.
3. Do not redesign the roadmap without explicit approval.
4. Explain important architectural or implementation decisions.
5. Keep changes small and reviewable.
6. Run relevant tests after making changes.
7. Do not hide failures.
8. Do not modify system configuration unnecessarily.
9. Never expose secrets, private SSH keys, passwords or access tokens.
10. Keep the Linux environment as the primary execution environment.

## QA Engineering

The project should progressively develop:

- Python
- pytest
- test framework architecture
- fixtures
- parametrization
- logging
- configuration
- Linux system testing
- networking
- network automation
- performance testing
- CI/CD
- Docker
- virtualization
- API testing
- storage testing
- kernel/driver debugging
- observability
- distributed testing
- failure analysis

## Testing Philosophy

Tests should verify real system behavior.

Prefer tests that:

- execute real commands;
- inspect real system state;
- validate expected behavior;
- collect useful diagnostics;
- produce reproducible results.

Avoid creating artificial tests whose only purpose is to make the test suite appear larger.

## Linux

The project runs primarily on Ubuntu `qa-linux-01`.

Do not make destructive system changes without explicit approval.

Do not disable security controls merely to make a test pass.

## Networking

Networking is a major project track.

Future work includes:

- TCP/UDP
- L2/L3
- routing
- VLAN
- network automation
- traffic generation
- throughput
- packets/sec
- latency
- CPU utilization
- interrupts
- NIC behavior
- TSO
- GSO
- GRO
- checksum offload
- RSS
- XDP where practical
- SR-IOV where practical

## Performance

Performance experiments must establish a baseline and compare measurable results.

Where applicable collect:

- throughput
- packets/sec
- latency
- CPU utilization
- interrupts
- memory
- I/O

## Git

Use clear commits.

Do not commit:

- passwords
- tokens
- private SSH keys
- credentials
- unnecessary generated files

Before committing:

1. inspect `git status`;
2. review the diff;
3. run relevant tests;
4. commit only intentional changes.

## Codex Role

Codex is an implementation assistant.

Codex may:

- create and modify code;
- create tests;
- refactor code;
- run commands;
- investigate failures;
- improve documentation.

The human/project owner decides:

- what stage to work on;
- what the next learning objective is;
- architectural direction;
- whether a stage is complete.

Do not automatically move the project to the next roadmap stage.

## Definition of Done

A task is not complete merely because code was written.

Where applicable, completion requires:

- implementation;
- test execution;
- successful result or documented failure;
- reviewable Git diff;
- documentation;
- clear explanation of what was learned.