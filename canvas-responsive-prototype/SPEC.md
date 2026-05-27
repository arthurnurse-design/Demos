# Canvas Responsive Layout Spec

## Chat + Canvas Layout

| Panel | Min | Default | Max |
| --- | --- | --- | --- |
| Nav sidebar | 60px (collapsed) / 200px (drag) | 240px | 400px |
| Chat area | 560px | flex greedy | — |
| Chat content | — | 768px (centred) | 768px |
| Canvas | 260px | 520px | 800px |

## Responsive Behaviour

| Window condition | Nav | Canvas |
| --- | --- | --- |
| ≥ 740px, no canvas | Expanded 240px | Off |
| < 740px, no canvas | Collapsed 60px | Off |
| Canvas open, enough space | Stays as-is | Inline |
| Canvas open, tight | Auto-collapses to 60px | Inline if fits |
| Canvas open, very tight | Collapsed 60px | Auto-closes |

## Shrink Priority

| Order | Action |
| --- | --- |
| 1 | Canvas shrinks (→ 260px min) |
| 2 | Nav collapses (240px → 60px) |
| 3 | Canvas auto-closes |

## Settings Layout

| Panel | Width | Responsive |
| --- | --- | --- |
| Settings sidebar | 240px fixed | Hides < 720px |
| Content area | flex, max 960px centred | — |
| Card grid | minmax(260px, 1fr) | 3 → 2 → 1 cols |
