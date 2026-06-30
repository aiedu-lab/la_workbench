# Instructor Preflight Checklist

Complete every step and its validation before students arrive.
Time required: approximately 60 minutes.

> **One-time repo hygiene:** before running this checklist for the
> first time, complete [repo.md](repo.md) to enable branch
> protection on `main` and confirm CODEOWNERS + PR review workflow.

> **Class ID convention:** choose a short unique identifier for
> this class run (e.g. `2026-spring`, `2026-fall-hs`). Replace
> every occurrence of `<CLASS_ID>` below with your chosen value.
> This prevents name collisions when the same instructor runs
> multiple cohorts.

---

## Section 1 — Collect Student Roster (5 min)

Student roster data is collected via a Google Form filled in by
students at the end of the Introduction session. Responses are
private — only the form owner (you) can see them.

### Google Form Setup (one-time — reused across all cohorts)

1. Go to `forms.google.com` → create a blank form.
   Title: `AI Workbench Lab Roster`
2. Add four **Short Answer** questions:
   Full Name, Email, GitHub username, Discord username
3. Responses tab → **Link to Sheets** → create new spreadsheet.
4. Settings → **Get pre-filled link** → copy the base URL
   (remove everything from `?entry.` onward).
   Set `GOOGLE_FORM_URL` in
   `setup/labenv.yaml` to this URL.

### Per-cohort — Extract Roster CSV

Responses tab → ⋮ → **Download responses (.csv)** → save as
`roster.csv` (never commit — contains PII).

Use the roster for provisioning:

**GitHub repo access** — add each student as a collaborator:

```bash
while IFS=, read -r name email github discord; do
  gh api repos/OWNER/REPO/collaborators/"$github" \
    -X PUT -f permission=push && echo "Added: $github"
done < <(tail -n +2 roster.csv)
```

**Discord invites** — send the server invite link (Section 2)
to each student's email address from the roster CSV.

### Roster Reference Table

Before provisioning anything, verify one row per student exists:

| Full name   | GitHub username | Discord username | Laptop OS   | Admin? |
|-------------|-----------------|------------------|-------------|--------|
| Alice Smith | `alicesmith`    | `@alice`         | Win11+WSL2  | yes    |
| Bob Jones   | `bobjones42`    | `@bob`           | macOS 14    | yes    |

**GitHub username** — validate each one resolves:

```bash
# Replace USERNAME with each student's handle
curl -s https://api.github.com/users/USERNAME \
  | python3 -c "import sys,json; d=json.load(sys.stdin); \
    print('OK:', d['login']) if 'login' in d \
    else print('NOT FOUND')"
```

**Discord username** — new-format handles are `@username` (no
discriminator). Old-format: `username#1234`. Confirm each student
has a Discord account before inviting (Section 2).

**Laptop OS** — accept only `Win11+WSL2` or `macOS 13+`. Students
on older OS versions must upgrade before the lab.

**Admin/sudo** — required for tool installation.
Students without admin access cannot complete the exercises.

---

*The roster table above is a local tracking aid — never commit it.
The Google Form CSV is the authoritative source.*

---

## Section 2 — Discord Server Setup and Student Invite (15 min)

Reference: https://support.discord.com/hc/en-us/articles/204849977

- Choose your `<CLASS_ID>` (e.g. `2026-spring`)
- Create a new Discord server named `la-workbench-<CLASS_ID>`
  - Server Settings → Overview → Server Name
  - Do NOT reuse a previous class server — keep cohorts isolated
- Create a text channel `#general` for class discussion and
  coordination (questions, announcements, study groups)
- Invite each student by Discord username:
  - Server Settings → Invites → Create Invite (no expiry)
  - Or: right-click `#general` → Invite People
  - Send the invite link to each student via a shared doc or
    class chat before the lab day
- Confirm every student has joined and can read `#general`:
  - Each student posts a test message: "ready: <their name>"
  - Do not proceed until all students appear in the member list

---

## Section 3 — Student Laptop Preflight (10 min per student)

> Students complete platform and tool setup independently using
> [Development Workbench Setup](dev_workbench.md) before the lab
> day. This section covers the instructor's validation gate only.

**Instructor validation — confirm all students show PASS:**

```bash
python3 setup/preflight_check.py
```

Every item must show `PASS` before the lab begins.

---

## Section 4 — Student Platform Architecture

Students arrive on one of two platforms. Both produce an identical
Ubuntu shell.

> "Students on Win11 use VSCode → Remote-WSL → Ubuntu. Students on
> macOS use VSCode → Dev Containers → Ubuntu. Both produce an
> identical Ubuntu shell." 

| Layer | Win11 | macOS |
|-------|-------|-------|
| Frontend | VSCode native | VSCode native |
| Dev environment | WSL2 Ubuntu | Dev Container Ubuntu |

Validate student platform before the lab:

```bash
# On each student laptop — confirm Ubuntu shell is active:
uname -a   # must show Linux
python3 --version  # must be >= 3.10
```

---

## Teaching Philosophy

Each lesson follows the same structure:

1. **Start with a real-world problem.**
2. **Explain why the problem is difficult.**
3. **Introduce the mathematical idea that solves it.**
4. **Visualize the concept whenever possible.**
5. **Connect it to modern AI.**

### Linear Algebra

**Reinforce the idea with a short NumPy/PyTorch exercise.**

#### Learning Outcomes

By the end of this session, students should be able to explain:

* What a machine learning model is and how it differs from a traditional program.
* Why vectors are an effective representation of information.
* Why embeddings capture semantic similarity.
* Why cosine similarity is widely used.
* Why a neural network layer is a matrix transformation.
* Why inference consists primarily of repeated matrix multiplication and nonlinear activation functions.
* Why backpropagation computes gradients efficiently.
* Why GPUs and TPUs are optimized for matrix operations.
* How these concepts prepare them for the mathematics presented in Gilbert Strang's lectures and the geometric intuition developed in 3Blue1Brown's *Essence of Linear Algebra*.

