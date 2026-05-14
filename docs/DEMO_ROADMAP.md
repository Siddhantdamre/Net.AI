# Demo Upgrade Roadmap

Goal: make Net.AI safely reviewable with synthetic traffic data, clear anomaly charts, and no need for live packet capture.

## Current State

- GitHub Pages surface is live.
- README now explains the ML/security workflow and repository map.
- The repo includes capture, preprocessing, training, API, dashboard, and pipeline files.

## Highest-Impact Improvements

| Priority | Upgrade | Recruiter value |
| --- | --- | --- |
| P0 | Add `examples/` with synthetic traffic samples. | Makes the project reproducible and safe. |
| P0 | Add a one-command demo mode using sample data. | Removes setup friction. |
| P1 | Add Streamlit dashboard screenshots. | Makes anomaly results visible. |
| P1 | Add Docker or a pinned requirements file. | Improves reproducibility. |
| P2 | Add an ethical-use note and clarify no live capture is required for demo mode. | Signals responsible security framing. |

## Suggested Demo Shape

- Streamlit dashboard backed by synthetic CSV/JSON traffic features.
- Views: traffic summary, anomaly scores, suspicious sessions, model explanation.
- Optional API mode for deeper review.

## Definition Of Done

- Reviewer can run the demo without sniffing real traffic.
- Dashboard shows at least one normal and one anomalous case.
- README includes screenshots and a safe-use note.
