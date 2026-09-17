# Restructure notes (2026)

This repo was reorganised around the current 6-session, 12-hour course plan
(2h/session: 1h theory + 1h TP, Session 01 lighter on TP). Grading is 100%
TP-based — no final project.

## New layout

```
sessions/
  01_Introduction/            Session 01 — Introduction & MovieLens
  02_ContentBasedFiltering/   Session 02 — Content-Based Filtering
  03_CollaborativeFiltering/  Session 03 — Collaborative Filtering (neighborhood-based)
  04_EvaluationMetrics/       Session 04 — Evaluation Metrics
  05_HybridRecommenders/      Session 05 — Hybrid Recommender Systems
  06_DeepLearningNCF/         Session 06 — Deep Learning for RecSys (NCF) + wrap-up
utils/                        Shared helpers still in use
tests/                        Tests matching the utils above
archive/
  matrix_factorisation/       Everything tied to SVD/ALS/BPR — explicitly out of scope
  old_lectures/                Superseded material (already marked as such by you)
  FinalProject/                No longer used (grading is 100% TP); data files dropped, READMEs kept
  03bis.ErrorMetrics.ipynb    Generic ML metrics notebook, not RecSys-specific
```
