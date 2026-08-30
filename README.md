# PRMM LLM Code — Reliability Model Comparison Plots

Generates comparison plots for a research paper, showing a reference reliability
model `R_r(t)` against reliability models `R_g(t)` produced by different LLMs
(Claude, Copilot, DeepSeek).

## Project Structure

```
graphics/
├── r_diff_claude.xlsx       # Reference vs. Claude-generated data
├── r_diff_copilot.xlsx      # Reference vs. Copilot-generated data
├── r_diff_deepseek.xlsx     # Reference vs. DeepSeek-generated data
├── plot_claude.py           # Generates final_plot_claude.png
├── plot_copilot.py          # Generates final_plot_copilot.png
├── plot_deep_seek.py        # Generates final_plot_deepseek.png
├── final_plot_claude.png
└── final_plot_copilot.png
```

Each `.xlsx` file provides three columns (in order): time, reference reliability,
and the LLM-generated reliability. Each script reads its matching spreadsheet,
plots both curves, and saves a high-resolution PNG (300 DPI) suitable for
publication.

## Requirements

- Python 3
- pandas
- matplotlib
- openpyxl (for reading `.xlsx` files)

A `.venv` with these dependencies is already set up in this repo.

## Usage

From the `graphics/` directory, run the script for the model you want to plot:

```bash
cd graphics
python plot_claude.py
python plot_copilot.py
python plot_deep_seek.py
```

Each run displays the plot and saves it as `final_plot_<model>.png` in the
`graphics/` directory.

## Plot Style

- Reference model: solid black line
- Generated model: dashed red line
- Axes: Time (`t`) vs. Reliability `R(t)`
- Legend: upper right, framed
- Output: 300 DPI PNG for print quality
