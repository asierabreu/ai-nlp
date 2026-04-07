# Contributing Guidelines

Thank you for considering contributing to the AI/NLP Portfolio!

---

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork: `git clone https://github.com/<your-username>/ai-nlp.git`
3. Create a feature branch: `git checkout -b feature/my-feature`
4. Follow the [setup guide](./setup.md)

---

## Code Style

### Python

- **Formatter**: `black` (line length 88)
- **Linter**: `ruff`
- **Import sorting**: `isort`
- **Type hints**: Required for all public functions

Run locally:

```bash
black projects/ shared/
isort projects/ shared/
ruff check projects/ shared/
```

### TypeScript / JavaScript

- **Linter**: ESLint (`eslint-config-next`)
- **Formatter**: Prettier (via ESLint)

Run locally:

```bash
cd portfolio-website
npm run lint
```

---

## Testing

- Write tests for all new functionality
- Tests live in `tests/` within each project directory
- Use `pytest` for Python, Jest/Vitest for TypeScript

```bash
pytest projects/nlp-knowledge-graph/tests/ -v
```

Aim for **≥ 80% coverage** on new code.

---

## Pull Request Process

1. Ensure all tests pass and linting is clean
2. Update relevant `README.md` and documentation
3. Open a PR against `main` with a clear description
4. Address review feedback promptly

---

## Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(nlp-kg): add relation confidence scores
fix(text2kg-demo): handle empty text input
docs(setup): add Windows instructions
refactor(shared): rename tokenize to tokenize_text
```

---

## Reporting Issues

Use the GitHub issue templates:

- [Bug Report](../.github/ISSUE_TEMPLATE/bug_report.yml)
- [Feature Request](../.github/ISSUE_TEMPLATE/feature_request.yml)

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
