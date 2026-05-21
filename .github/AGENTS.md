# Custom Agents

This repository includes custom VS Code agents for common review workflows.

## secure-code-review

- **Name:** `secure-code-review`
- **Location:** `.github/agents/secure-code-review.agent.md`
- **Use when:** anyone asks for a secure code review of this repository
- **Focus:** repository-wide application and script review, dependency and supply chain analysis, OWASP Top 10, DISA Application Security and Development STIGs, NIST 800-53 r5, and secure software development best practices.
- **Output expectations:** validated findings, proof-of-concept reasoning when applicable, and concrete remediation steps.

To use the agent in VS Code, ask for a secure code review or invoke the `secure-code-review` agent if your Copilot/agent interface supports it.

## threat-model

- **Name:** `threat-model`
- **Location:** `.github/agents/threat-model.agent.md`
- **Use when:** anyone asks for threat modeling, architecture risk analysis, or secure design review
- **Focus:** system decomposition, data flows, trust boundaries, attacker capabilities, STRIDE threat enumeration, and mitigation design guidance.
- **Output expectations:** a timestamped markdown threat model artifact in `output/` with sections suitable as compliance evidence (Overview, System Decomposition, Assets, Data Flows, Trust Boundaries, Threats, Risk Prioritization, Mitigations, Evidence, Control Mapping, Generated-By).

To use the agent in VS Code, ask for a threat model review or invoke the `threat-model` agent if your Copilot/agent interface supports it.
