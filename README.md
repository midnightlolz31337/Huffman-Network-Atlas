# Huffman Network Atlas

A federated, evidence-backed map of the Huffman Systems ecosystem, repositories, capabilities, dependencies, and provenance.

## Mission
Make a distributed research ecosystem understandable without pretending that a directory is an authority. The Atlas indexes projects; each repository remains authoritative for its own code, documentation, releases, and security posture.

## Ecosystem accounts
| Account | Role in this map | Evidence status |
|---|---|---|
| [HuffmanMainNode](https://github.com/HuffmanMainNode) | Systems, protocols, OSINT and agent experimentation | Prior project audit; refresh required |
| [HuffmanRepositories](https://github.com/HuffmanRepositories) | Ecosystem navigation and interoperability | Prior project audit; refresh required |
| [PCakes303](https://github.com/PCakes303) | OSINT registries, collection, evidence and graph prototypes | Prior project audit; refresh required |
| [LoLz / CIPHER](https://github.com/midnightlolz31337) | ELITE coordination and shared infrastructure | Account/repository snapshot |

## ELITE project set
- [ELITE Protocol](https://github.com/midnightlolz31337/ELITE-Protocol) — evidence exchange, provenance and trust boundaries.
- [ELITE Ingestion Core](https://github.com/midnightlolz31337/ELITE-Ingestion-Core) — bounded ingestion, validation and quarantine.
- [ELITE Agent Commons](https://github.com/midnightlolz31337/ELITE-Agent-Commons) — machine-readable discovery and task routing.
- [Huffman Network Atlas](https://github.com/midnightlolz31337/Huffman-Network-Atlas) — federated ecosystem index.
- [Private research vault](https://github.com/midnightlolz31337/ELITE-Research-Vault2) — private planning; do not mirror its contents here.

## Evidence discipline
Distinguish verified facts, attributed claims, inferences, and unknowns. Repository existence does not establish code quality, safety, originality, maintenance, or production readiness. Counts are dated snapshots, not timeless facts.

## Quick start
Python 3.10+:
```bash
python tools/validate_registry.py
python tools/render_summary.py
```

## Status
Initial public catalogue scaffold. It is not yet a complete audit of every repository in the four-account ecosystem. See [DATA_MODEL](docs/DATA_MODEL.md) and [RESEARCH_METHOD](docs/RESEARCH_METHOD.md).
