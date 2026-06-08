# Релиз лабораторной работы №6

## Общая информация

Лабораторная работа №6 посвящена реализации SIR-модели в подходе сетей Петри. В релиз включены проект Julia с моделями и экспериментами, а также собранные версии отчёта и презентации.

## Состав релиза

- `report/` — исходники и собранные версии отчёта.
- `presentation/` — исходники и собранные версии презентации.
- `lab_06_SIR_petri/` — проект DrWatson с моделью, данными и производными материалами.

## Материалы отчёта

- `report/simulation-modeling--lab06--report.qmd` — исходный Quarto-файл отчёта.
- `report/_output/simulation-modeling--lab06--report.html` — HTML-версия отчёта.
- `report/_output/simulation-modeling--lab06--report.docx` — DOCX-версия отчёта.
- `report/_output/simulation-modeling--lab06--report.pdf` — PDF-версия отчёта.
- `report/bib/` — библиография.
- `report/image/` — графики, таблицы и скриншоты отчёта.

## Материалы презентации

- `presentation/simulation-modeling--lab06--presentation.qmd` — исходный Quarto-файл презентации.
- `presentation/_output/simulation-modeling--lab06--presentation.html` — HTML-версия презентации.
- `presentation/_output/simulation-modeling--lab06--presentation.pdf` — PDF-версия презентации.
- `presentation/image/` — изображения для слайдов.

## Проект моделирования

Каталог `lab_06_SIR_petri/` содержит:

- `lab_06_SIR_petri/src/` — исходный код модели и служебные модули.
- `lab_06_SIR_petri/scripts/` — сценарии базового запуска, параметрического анализа, анимации и отчётов.
- `lab_06_SIR_petri/docs/` — Markdown-материалы, сгенерированные из literate-скриптов.
- `lab_06_SIR_petri/notebook/` — Jupyter notebooks по сценариям лабораторной работы.
- `lab_06_SIR_petri/data/` — CSV-результаты вычислительных экспериментов.
- `lab_06_SIR_petri/plots/` — графики и анимации.
- `lab_06_SIR_petri/test/` — тесты проекта.
- `lab_06_SIR_petri/Project.toml` — зависимости Julia-проекта.
- `lab_06_SIR_petri/README.md` — инструкция по воспроизведению.

## Итог

Релиз лабораторной работы №6 объединяет проект модели SIR в сетях Петри и собранные `pdf/html/docx`-материалы по отчёту и презентации.
