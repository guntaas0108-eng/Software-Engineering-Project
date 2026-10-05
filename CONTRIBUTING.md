# Contributing to EstatePulse (UCS503P)

Thank you for contributing to the **Real Estate Price Prediction and Marketplace Platform**. To maintain high software quality and time-to-value delivery, please follow our collaborative git workflow.

---

## 🔀 Branching Strategy

We follow a feature-branch workflow:
- `main` / `master`: Stable, tested, deployable code.
- `feature/<feature-name>`: New capabilities (e.g. `feature/ml-regression-update`, `feature/payment-webhook`).
- `bugfix/<issue-name>`: Bug fixes (e.g. `bugfix/chat-timestamp-timezone`).
- `docs/<topic>`: Documentation updates.

---

## 💻 Development Workflow

1. **Pull the latest changes:**
   ```powershell
   git checkout master
   git pull origin master
   ```

2. **Create your feature branch:**
   ```powershell
   git checkout -b feature/your-feature-name
   ```

3. **Activate environment & install packages:**
   ```powershell
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Verify tests before committing:**
   ```powershell
   pytest code/backend/tests -v
   ```

5. **Commit with conventional messages:**
   - `feat: add duplicate check endpoint`
   - `fix: resolve appointment calculation edge case`
   - `docs: update API endpoints documentation`
   - `test: add unit test for regression MSE`

6. **Submit a Pull Request (PR):**
   - Fill out the PR template.
   - Ensure the CI pipeline passes.
   - Request review from at least one peer team member.
