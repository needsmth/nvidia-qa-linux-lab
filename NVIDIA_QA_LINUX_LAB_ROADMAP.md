# NVIDIA QA Linux Lab Roadmap

This practical, sequential plan develops Linux QA Automation and Software Verification skill for NVIDIA-oriented requirements: reliable Linux automation, network and performance validation, device and driver evidence, and clear failure analysis. Advance only when the project owner approves completion.

## Progress

| Stage | Focus | Status |
| --- | --- | --- |
| 0 | 0 — Linux Server Foundation | DONE |
| 1 | 1 — Git / GitHub / Development Workflow | CURRENT |
| 2 | 2 — Python + pytest Test Framework | FUTURE |
| 3 | 3 — Linux System Verification | FUTURE |
| 4 | 4 — Linux Networking Fundamentals | FUTURE |
| 5 | 5 — Network QA Automation | FUTURE |
| 6 | 6 — Network Performance Testing | FUTURE |
| 7 | 7 — NIC Offload / RSS / XDP / SR-IOV | FUTURE |
| 8 | 8 — CI/CD | FUTURE |
| 9 | 9 — Containers and Virtualization | FUTURE |
| 10 | 10 — Storage and I/O Verification | FUTURE |
| 11 | 11 — Kernel / Driver / Hardware Debugging | FUTURE |
| 12 | 12 — Observability and Failure Analysis | FUTURE |
| 13 | 13 — Distributed / Large-Scale Testing | FUTURE |
| 14 | 14 — NVIDIA-oriented Capstone | FUTURE |

## Stage 0 — Linux Server Foundation — DONE

- **Objective:** Establish a safe Ubuntu lab and inspect it.
- **Skills:** Shell, permissions, processes, packages, systemd, SSH, resources.
- **Practical exercises:** Record OS, kernel, CPU, memory, storage, interfaces, services, and logs with read-only commands.
- **Expected artifacts:** Sanitized host-inventory notes in docs/.
- **Definition of Done:** The lab is reachable and inventory commands run successfully or have recorded explanations.

## Stage 1 — Git / GitHub / Development Workflow — CURRENT

- **Objective:** Establish a clean, reviewable repository and disciplined Git workflow.
- **Skills:** Status, diff, add, commit, log, branching, merging, remotes, ignore rules, Markdown.
- **Practical exercises:** Document the project; review a small change; practice a feature branch and merge; configure a remote only when approved.
- **Expected artifacts:** README, roadmap, appropriate ignore rules, and workflow notes as needed.
- **Definition of Done:** Documentation describes the lab; status/diff/log are used correctly; a feature branch and pull request are created and reviewed; initial commits contain intentional files only; no credentials are exposed.

## Stage 2 — Python + pytest Test Framework — FUTURE

- **Objective:** Build a maintainable Python foundation for real verification.
- **Skills:** Packaging, pytest fixtures, parametrization, markers, logging, config, assertions, subprocesses.
- **Practical exercises:** Create safe read-only command tests and reusable diagnostic fixtures.
- **Expected artifacts:** Python configuration, tests/, conftest.py, command helper, pytest config, usage docs.
- **Definition of Done:** One command runs the suite; at least three tests verify real Linux behavior with actionable diagnostics.

## Stage 3 — Linux System Verification — FUTURE

- **Objective:** Verify fundamental Linux behavior with useful failure evidence.
- **Skills:** Processes, services, filesystems, CPU, memory, kernel, packages, logs, permissions.
- **Practical exercises:** Check identity, mounts, service state, resources, kernel details, and controlled failure reporting.
- **Expected artifacts:** System test modules, diagnostic fixtures, and a verification guide.
- **Definition of Done:** At least six independent real properties are checked; every failure reports relevant context.

## Stage 4 — Linux Networking Fundamentals — FUTURE

- **Objective:** Understand and safely inspect Linux networking.
- **Skills:** TCP/UDP, Ethernet, L2/L3, addresses, routes, DNS, MTU, VLANs, namespaces, ip, ss, ethtool.
- **Practical exercises:** Inspect state; verify local TCP/UDP and DNS; document topology; capture controlled traffic.
- **Expected artifacts:** Networking guide, inspection commands, topology table or diagram, connectivity procedure.
- **Definition of Done:** Checks distinguish name, route, port, and host failures using evidence.

## Stage 5 — Network QA Automation — FUTURE

- **Objective:** Automate functional network checks with reliable cleanup.
- **Skills:** Sockets, pytest fixtures, namespaces, interface state, matrices, timeouts, retries.
- **Practical exercises:** Automate TCP/UDP, MTU, route, and link-state checks; inject one controlled negative case.
- **Expected artifacts:** Network tests, namespace/socket helpers, test configuration, troubleshooting guide.
- **Definition of Done:** A documented run is repeatable, cleans up resources, and identifies the failing network layer.

## Stage 6 — Network Performance Testing — FUTURE

- **Objective:** Measure performance and identify meaningful regressions.
- **Skills:** Throughput, PPS, latency, jitter, CPU, interrupts, baselines, variance, visualization.
- **Practical exercises:** Run repeated TCP/UDP baselines; correlate throughput, latency, CPU, and interrupts.
- **Expected artifacts:** Benchmark procedure or runner, result data, baseline report, comparison tables or charts.
- **Definition of Done:** Three or more baseline runs report throughput, latency, CPU, parameters, and variance.

## Stage 7 — NIC Offload / RSS / XDP / SR-IOV — FUTURE

- **Objective:** Verify advanced NIC features and their traffic impact.
- **Skills:** ethtool, TSO/GSO/GRO/checksum offload, RSS, IRQ affinity, XDP, SR-IOV, rollback.
- **Practical exercises:** Inventory capabilities; correlate queues and IRQs with traffic; compare approved feature states.
- **Expected artifacts:** NIC inventory, feature tests, RSS/IRQ evidence, before/after reports, rollback runbook.
- **Definition of Done:** Supported features are recorded accurately; approved experiments have baseline, result, and rollback evidence.

## Stage 8 — CI/CD — FUTURE

- **Objective:** Automatically run reliable, appropriately scoped checks.
- **Skills:** Pipelines, runners, test selection, artifacts, reports, caching, secrets hygiene, triage.
- **Practical exercises:** Add portable validation, publish pytest results, and separate hardware-dependent tests.
- **Expected artifacts:** CI configuration, markers, pipeline guide, artifact-retention policy.
- **Definition of Done:** A clean checkout runs portable validation automatically and exposes diagnostics; special tests are clearly routed.

## Stage 9 — Containers and Virtualization — FUTURE

- **Objective:** Use isolated reproducible environments while recognizing hardware differences.
- **Skills:** Docker or Podman, images, volumes, networks, Compose, VMs, environment parity.
- **Practical exercises:** Containerize portable tests; compare host/container observations; build an isolated network scenario.
- **Expected artifacts:** Containerfile, dependency definition, run instructions, virtualization notes, environment matrix.
- **Definition of Done:** Portable tests run from a documented image; the matrix identifies host-only and hardware-only coverage.

## Stage 10 — Storage and I/O Verification — FUTURE

- **Objective:** Verify storage functionality and characterize I/O safely.
- **Skills:** Block devices, filesystems, mounts, fio, IOPS, latency, bandwidth, queue depth, data safety.
- **Practical exercises:** Inspect topology; benchmark approved disposable targets; establish sequential and random baselines.
- **Expected artifacts:** Storage inventory, safe profiles, results, baseline report, safety runbook.
- **Definition of Done:** Write tests use an approved disposable target; baseline reports bandwidth, IOPS, latency, and environment.

## Stage 11 — Kernel / Driver / Hardware Debugging — FUTURE

- **Objective:** Diagnose kernel, driver, and hardware interactions with escalation-quality evidence.
- **Skills:** dmesg, journal, PCIe, modules, device enumeration, parameters, crash evidence, issue reports.
- **Practical exercises:** Map devices to drivers and logs; collect a diagnostic bundle; report a controlled issue.
- **Expected artifacts:** Hardware/driver inventory, diagnostic procedure, issue template, sanitized investigation.
- **Definition of Done:** Workflow maps device, driver, messages, and test results; report includes reproduction, environment, evidence.

## Stage 12 — Observability and Failure Analysis — FUTURE

- **Objective:** Make failures diagnosable through structured telemetry.
- **Skills:** Metrics, logs, traces, correlation, dashboards, hypotheses, failure classification.
- **Practical exercises:** Add timestamps; collect workload metrics; correlate a failure with logs; complete a controlled RCA.
- **Expected artifacts:** Observability schema, diagnostic bundle format, metrics procedure, RCA template and example.
- **Definition of Done:** A failure is reconstructed from artifacts; RCA separates evidence from hypothesis and names next action.

## Stage 13 — Distributed / Large-Scale Testing — FUTURE

- **Objective:** Operate reliable verification across multiple hosts or scale.
- **Skills:** Remote orchestration, inventory, concurrency, synchronization, fault isolation, aggregation.
- **Practical exercises:** Coordinate multi-host connectivity; aggregate outcomes; inject a single-node fault; measure scale.
- **Expected artifacts:** Host inventory format, orchestration configuration, distributed tests, aggregate report.
- **Definition of Done:** A multi-host run identifies every participant and isolates a one-node failure repeatably.

## Stage 14 — NVIDIA-oriented Capstone — FUTURE

- **Objective:** Deliver an end-to-end NVIDIA-adjacent verification project.
- **Skills:** Test strategy, risk analysis, automation architecture, performance, NIC/device diagnostics, CI, communication.
- **Practical exercises:** Choose an approved NIC performance/offload, GPU-adjacent readiness, or distributed-network scenario; automate, baseline, and diagnose a controlled failure.
- **Expected artifacts:** Test strategy, architecture diagram, suite, CI job, comparison report, diagnostics, retrospective.
- **Definition of Done:** Traceable tests produce functional and performance evidence; a controlled failure shows diagnosis; final report states coverage, limits, risks, and improvements.
