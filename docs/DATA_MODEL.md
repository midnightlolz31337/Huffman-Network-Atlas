# Atlas data model

A repository record is a time-bounded observation about a GitHub repository, not a guarantee of its quality.

## Required fields

- `id`: stable Atlas-local identifier; do not derive identity from display name alone.
- `url`: canonical HTTPS GitHub URL.
- `owner`, `name`: GitHub owner and repository name at observation time.
- `visibility`: public, private, internal, or unknown.
- `description`: exact repository description when verified; otherwise label as attributed or omit.
- `status`: scaffolded, prototype, experimental, maintained, archived, or planning.
- `evidence_level`: how the record was established.

## Evidence labels

- `repository_metadata_verified`: metadata was directly checked against GitHub.
- `file_content_verified`: named files were directly inspected.
- `prior_audit_snapshot`: information comes from an earlier audit and needs refresh.
- `owner_assertion`: supplied by a project owner but not independently checked.
- `inferred`: reasoned interpretation; never present as a fact.

## Rules

1. Include `last_verified` for direct checks.
2. Preserve snapshot dates and scope.
3. Do not copy private repository contents into this public index.
4. Never interpret repository presence as proof of active maintenance, security, authorship of every file, or production readiness.
5. Prefer links and provenance over copied source material.
