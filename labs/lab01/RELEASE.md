# Релиз лабораторной работы №1

## Общая информация

Лабораторная работа №1 посвящена численному решению модели экспоненциального роста на Julia и первичной настройке воспроизводимого проекта. В состав релиза входят исходные материалы, собранный отчёт, собранная презентация и рабочие файлы проекта.

## Состав релиза

- `report/` — исходники и собранные версии отчёта.
- `presentation/` — исходники и собранные версии презентации.
- `project/` — проект DrWatson с кодом, сценариями и тестами.
- `setup_project.jl` — вспомогательный скрипт подготовки проекта.
- `linear_regression.jl` — отдельный скрипт с учебным примером вычислений.

## Материалы отчёта

- `report/simulation-modeling--lab01--report.qmd` — исходный Quarto-файл отчёта.
- `report/_output/simulation-modeling--lab01--report.html` — HTML-версия отчёта.
- `report/_output/simulation-modeling--lab01--report.docx` — DOCX-версия отчёта.
- `report/_output/simulation-modeling--lab01--report.pdf` — PDF-версия отчёта.
- `report/bib/` — библиография.
- `report/image/` — иллюстрации и скриншоты, используемые в отчёте.

## Материалы презентации

- `presentation/simulation-modeling--lab01--presentation.qmd` — исходный Quarto-файл презентации.
- `presentation/_output/simulation-modeling--lab01--presentation.html` — HTML-версия презентации.
- `presentation/_output/simulation-modeling--lab01--presentation.pdf` — PDF-версия презентации.
- `presentation/image/` — иллюстрации и скриншоты для слайдов.

## Проект моделирования

Каталог `project/` содержит воспроизводимую структуру Julia-проекта:

- `project/src/` — исходный код модели и служебные файлы.
- `project/scripts/` — сценарии запуска и обработки результатов.
- `project/markdown/` — текстовые материалы проекта.
- `project/test/` — тестовый набор.
- `project/Project.toml` — зависимости проекта.
- `project/README.md` — инструкция по запуску.

## Итог

Релиз включает полный набор материалов по лабораторной работе №1: исходники Quarto, собранные `pdf/html/docx`, проект Julia и вспомогательные скрипты.
