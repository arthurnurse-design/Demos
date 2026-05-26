# Canvas Responsive Prototype — Handoff

## Overview

Two static HTML prototypes demonstrating responsive panel layout behaviour for a chat + canvas application. Both use real browser window resizing (no artificial sliders) and a floating info panel to show current state.

---

## Files

| File | Purpose |
|------|---------|
| `index.html` | Main chat + canvas layout with nav sidebar |
| `skills-settings.html` | Settings page with skills card grid |

---

## index.html — Chat + Canvas Layout

### Panel Structure

```
[ Nav Sidebar ] | resize | [ Chat Area ] | resize | [ Canvas Panel ]
```

### Key Dimensions (constants in JS)

| Panel | Min | Default | Max |
|-------|-----|---------|-----|
| Nav sidebar | 60px (collapsed) | 240px (expanded) | 400px |
| Chat area | 560px | flex (greedy) | unlimited |
| Canvas panel | 260px | 520px | 800px |
| Preview panel | 260px | 540px | 800px |

### Resize Priority

Chat always takes priority. On resize:
1. Canvas shrinks first (down to 260px minimum)
2. If still too tight, nav collapses (240px -> 60px)
3. If still can't fit, canvas auto-closes entirely to preserve chat

### Responsive Behaviours

| Window Width | Nav | Canvas (if open) |
|---|---|---|
| >= 740px + room | Expanded (240px) | Inline |
| < 740px | Collapsed (60px) | Inline if fits, else overlay |
| Too narrow for both | Collapsed (60px) | Auto-closes |

### Draggable Panels

- Yellow resize handles appear between nav/chat and chat/canvas
- Drag nav handle: resizes nav (60–400px), locks sidebar override to "forced open"
- Drag canvas handle: resizes canvas (260–800px)
- Handles hidden when panel is collapsed/closed

### Sidebar Open/Close

- When nav auto-collapses or is closed, a panel icon appears at left of chat header
- Clicking it re-expands the sidebar
- Nav toggle button in sidebar header also toggles collapse
- Info panel "Override Sidebar" button cycles: auto -> forced open -> forced closed -> auto

### Canvas/Preview Modes

- **Inline**: side-by-side with chat when space allows
- **Overlay**: slides over chat with backdrop when too narrow for inline
- **Auto-close**: dismissed entirely on very narrow widths

### Content Max-Width

- Chat messages and input: `max-width: 768px`, centred within chat area

---

## skills-settings.html — Settings Page

### Panel Structure

```
[ Settings Sidebar (240px) ] [ Content Area ]
```

No outer nav sidebar — traffic lights and toggle are embedded in the settings sidebar header.

### Layout

- Settings sidebar: 240px fixed, hides when window < 720px
- Content area: scrollable, with inner wrapper `max-width: 960px`, centred
- Card grid: `auto-fill`, `minmax(260px, 1fr)` — adapts from 3 to 2 to 1 columns

### Responsive Behaviour

| Window Width | Settings Sidebar |
|---|---|
| >= 720px | Visible (240px) |
| < 720px | Hidden |

### Content Structure

```
Breadcrumb
H1 "Skills" + action buttons
Description
Tabs (Discover / My skills / Org skills)
Responsive card grid (12 cards)
```

---

## Info Panel (both pages)

Floating bar at bottom-centre showing:
- Current browser width in px
- Panel states with status dots (green = visible, grey = hidden, amber = overlay)
- Toggle buttons for canvas/preview/sidebar override (index.html)
- Link to navigate between the two pages

---

## Design Tokens (shared)

```css
--color-bg: #ffffff
--color-border: #e8e5e5
--color-text: #1a1a1a
--color-text-secondary: #6b6568
--color-accent: #f5c518
--color-nav-bg: #faf9f9
--color-canvas-bg: #f7f5f5
```

---

## How to Run

Open either HTML file directly in a browser. No build step or dependencies required.

```bash
open canvas-responsive-prototype/index.html
```

Resize the browser window to see responsive behaviours. Use the info panel buttons to toggle canvas/preview/sidebar states.
