## 0.49.0 (2025-02-04)

### Feat

- Support limiting row count and offsets in Oracle queries (#754)
- Support creating/dropping indices on tables (#753)
- add missing join query builder methods
- add table level alias for select, insert and update

### Fix

- README.rst (#801)
- **doc**: update PseudoColumn module import. (#698)
- **terms**: fixed EmptyCriterion bug with ComplexCriterion (#732)
- Typing hint for builder decorator (#740)
- remove duplicated method
- mysql create/drop tables
- #264: add documentation and example
- GIT-264: fix select alias to use table object directly

### Refactor

- move the repository to neopika, uv and mkdocs
- CI (#752)
