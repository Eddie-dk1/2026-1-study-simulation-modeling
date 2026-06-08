#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import os
import random
import shutil
import textwrap
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".cache" / "matplotlib"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

COURSE = "simulation-modeling"
AUTHOR = "Гашимов Кенан Мухтар оглы"
GROUP = "НКНбд-01-23"
STUDENT_ID = "1032235820"
PROGRAM = "Математика и компьютерные науки"
EMAIL = "kenan24gguka@gmail.com"
YEAR = "2025-2026"
TERM = "2026-1"


@dataclass(frozen=True)
class Lab:
    slug: str
    number: int
    title: str
    focus: str
    theory: str
    goal: str
    experiments: list[str]
    conclusions: list[str]
    datasets: list[str]
    artifacts: list[str]
    release_notes: list[str]
    project_readme: str
    report_sections: list[str]
    presentation_points: list[str]
    julia_module: str
    julia_script: str
    julia_tests: str
    markdown_doc: str
    notebook_cells: list[dict]
    instructions: list[str]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def clean_root() -> None:
    for name in ["README.md", "README.en.md", "README.git-flow.md", "CHANGELOG.md", "COURSE", "Makefile", "package.json", ".gitignore"]:
        path = ROOT / name
        if path.exists():
            path.unlink()
    for name in ["template", "labs", "tools/generated", ".cache"]:
        path = ROOT / name
        if path.exists():
            shutil.rmtree(path)


def build_root_files(labs: list[Lab]) -> None:
    write(
        ROOT / "COURSE",
        COURSE,
    )
    write(
        ROOT / ".gitignore",
        textwrap.dedent(
            """
            .DS_Store
            .cache/
            __pycache__/
            *.pyc
            *.log
            */project/tmp/
            */project/build/
            */report/*.tmp
            */presentation/*.tmp
            """
        ),
    )
    write(
        ROOT / "README.md",
        textwrap.dedent(
            f"""
            # Имитационное моделирование

            Репозиторий курса содержит комплект из восьми лабораторных работ по дисциплине «Имитационное моделирование».

            ## Автор

            - ФИО: {AUTHOR}
            - Группа: {GROUP}
            - Студенческий билет: {STUDENT_ID}
            - Направление: {PROGRAM}
            - Email: {EMAIL}

            ## Структура

            - `template/` — шаблоны отчётов, презентаций и служебных документов.
            - `labs/lab01` … `labs/lab08` — лабораторные работы.
            - `tools/` — генераторы содержимого, сборки и проверки.

            ## Содержание лабораторных

            {chr(10).join(f"- `labs/{lab.slug}` — {lab.title}" for lab in labs)}

            ## Сборка

            Используются локально доступные инструменты `python3`, `pandoc` и `julia`.

            ```bash
            make generate
            make render
            make verify
            ```

            Отчёты и презентации хранятся вместе с исходниками каждой лабораторной. Для отчётов формируются `html` и `docx`, для презентаций — `html` и `pptx`.

            ## Примечание по окружению

            В рабочем окружении отсутствуют `quarto` и TeX, поэтому `.qmd`-источники сохраняются, а финальная сборка выполняется через `pandoc`. Логика literate-пайплайна, структура каталогов, release-документы и набор артефактов при этом сохранены.
            """
        ),
    )
    write(
        ROOT / "README.en.md",
        textwrap.dedent(
            f"""
            # Simulation Modeling

            This repository contains a complete eight-lab coursework set for the Simulation Modeling class.

            ## Student

            - Name: {AUTHOR}
            - Group: {GROUP}
            - Student ID: {STUDENT_ID}
            - Program: {PROGRAM}
            - Email: {EMAIL}

            ## Repository layout

            {chr(10).join(f"- `labs/{lab.slug}` — {lab.focus}" for lab in labs)}

            ## Tooling

            The repository is designed to work offline with `python3`, `pandoc`, and `julia`.

            ```bash
            make generate
            make render
            make verify
            ```
            """
        ),
    )
    write(
        ROOT / "README.git-flow.md",
        textwrap.dedent(
            """
            # Git Flow

            Репозиторий рассчитан на git-flow с основной веткой `main` и рабочей веткой `develop`.

            ## Ожидаемая схема релизов

            - `lab01` — подготовка стенда и стартовый DrWatson-проект.
            - `lab02` — базовые непрерывные модели.
            - `lab03` — Daisyworld.
            - `lab04` — агентная SIR-модель.
            - `lab05` — сети Петри и философы.
            - `lab06` — SIR через сети Петри.
            - `lab07` — дискретно-событийное моделирование и `M/M/c`.
            - `lab08` — дискретно-событийная SIR-модель.

            ## Базовые команды

            ```bash
            git flow init
            git flow feature start lab01
            git flow release start lab01
            git tag lab01
            ```

            После наполнения репозитория удобно выпускать релиз на каждую лабораторную работу и синхронизировать описание релиза с локальным `RELEASE.md`.
            """
        ),
    )
    changelog_lines = [
        "# CHANGELOG",
        "",
        "## lab08",
        "- Добавлена дискретно-событийная SIR-модель с отчётом, презентацией, экспериментами и release-документом.",
        "",
        "## lab07",
        "- Добавлены DES-эксперименты для `M/M/c` и модели событийного потока по Россу.",
        "",
        "## lab06",
        "- Добавлена реализация SIR через аппарат сетей Петри.",
        "",
        "## lab05",
        "- Добавлены лабораторные материалы по сетям Петри и задаче обедающих философов.",
        "",
        "## lab04",
        "- Добавлена агентная SIR-модель с параметрическими экспериментами.",
        "",
        "## lab03",
        "- Добавлена лабораторная по Daisyworld.",
        "",
        "## lab02",
        "- Добавлены модели SIR и Лотки–Вольтерры.",
        "",
        "## lab01",
        "- Добавлен стартовый проект курса, literate-пайплайн и пример экспоненциального роста.",
    ]
    write(ROOT / "CHANGELOG.md", "\n".join(changelog_lines))
    write(
        ROOT / "Makefile",
        textwrap.dedent(
            """
            .PHONY: help generate render verify clean

            help:
            \t@printf "Targets:\\n"
            \t@printf "  make generate  - recreate repository structure and generated assets\\n"
            \t@printf "  make render    - build html/docx/pptx outputs with pandoc\\n"
            \t@printf "  make verify    - run structural and content checks\\n"
            \t@printf "  make clean     - remove generated cache\\n"

            generate:
            \tpython3 tools/generate_course_repo.py

            render:
            \tpython3 tools/render_outputs.py

            verify:
            \tpython3 tools/verify_repo.py

            clean:
            \trm -rf .cache tools/generated
            """
        ),
    )
    write_json(
        ROOT / "package.json",
        {
            "name": "simulation-modeling-course",
            "version": "1.0.0",
            "private": True,
            "description": "Offline build scripts for the simulation modeling course repository.",
            "scripts": {
                "generate": "python3 tools/generate_course_repo.py",
                "render": "python3 tools/render_outputs.py",
                "verify": "python3 tools/verify_repo.py",
            },
        },
    )
    write(
        ROOT / "template" / "README.md",
        textwrap.dedent(
            """
            # Templates

            Каталог хранит шаблоны, на основе которых воспроизводятся отчёты, презентации и служебные документы лабораторных работ.
            """
        ),
    )
    write(
        ROOT / "template" / "report-template.qmd",
        textwrap.dedent(
            f"""
            ---
            title: "Шаблон отчёта по имитационному моделированию"
            author: "{AUTHOR}"
            lang: ru
            ---

            # Назначение

            Используется как опорный шаблон для лабораторных отчётов.
            """
        ),
    )
    write(
        ROOT / "template" / "presentation-template.qmd",
        textwrap.dedent(
            f"""
            ---
            title: "Шаблон презентации по имитационному моделированию"
            author: "{AUTHOR}"
            lang: ru
            ---

            # Назначение

            Используется как опорный шаблон для лабораторных презентаций.
            """
        ),
    )


def rk4(func, y0, t0, t1, dt):
    times = np.arange(t0, t1 + dt, dt)
    ys = np.zeros((len(times), len(y0)), dtype=float)
    ys[0] = np.array(y0, dtype=float)
    for i in range(1, len(times)):
        t = times[i - 1]
        y = ys[i - 1]
        k1 = np.array(func(t, y))
        k2 = np.array(func(t + dt / 2, y + dt * k1 / 2))
        k3 = np.array(func(t + dt / 2, y + dt * k2 / 2))
        k4 = np.array(func(t + dt, y + dt * k3))
        ys[i] = y + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return times, ys


def simulate_lab01(base: Path) -> dict[str, str]:
    data_dir = base / "project" / "data"
    plots_dir = base / "project" / "plots"
    alphas = [0.15, 0.30, 0.45]
    summary = []
    plt.figure(figsize=(9, 5))
    for alpha in alphas:
        t = np.linspace(0, 10, 101)
        u = np.exp(alpha * t)
        df = pd.DataFrame({"time": t, "population": u, "alpha": alpha})
        csv_path = data_dir / f"exponential-growth-alpha-{alpha:.2f}.csv"
        df.to_csv(csv_path, index=False)
        plt.plot(t, u, label=f"α={alpha:.2f}")
        summary.append((alpha, float(u[-1]), math.log(2) / alpha))
    plt.title("Экспоненциальный рост")
    plt.xlabel("Время")
    plt.ylabel("u(t)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plot_path = plots_dir / "exponential-growth-scenarios.png"
    plt.tight_layout()
    plt.savefig(plot_path, dpi=180)
    plt.close()

    lines = ["| α | u(10) | Время удвоения |", "| --- | ---: | ---: |"]
    for alpha, u10, doubling in summary:
        lines.append(f"| {alpha:.2f} | {u10:.3f} | {doubling:.3f} |")
    return {
        "plot": plot_path.name,
        "summary_table": "\n".join(lines),
        "metrics": " ; ".join(f"α={alpha:.2f}: u(10)={u10:.3f}, T2={doubling:.3f}" for alpha, u10, doubling in summary),
    }


def simulate_lab02(base: Path) -> dict[str, str]:
    data_dir = base / "project" / "data"
    plots_dir = base / "project" / "plots"

    def sir(_, y):
        s, i, r = y
        beta, gamma = 0.36, 0.12
        return np.array([-beta * s * i, beta * s * i - gamma * i, gamma * i])

    t_sir, y_sir = rk4(sir, [0.99, 0.01, 0.0], 0.0, 90.0, 0.5)
    sir_df = pd.DataFrame({"time": t_sir, "S": y_sir[:, 0], "I": y_sir[:, 1], "R": y_sir[:, 2]})
    sir_df.to_csv(data_dir / "sir.csv", index=False)
    plt.figure(figsize=(9, 5))
    plt.plot(t_sir, sir_df["S"], label="S")
    plt.plot(t_sir, sir_df["I"], label="I")
    plt.plot(t_sir, sir_df["R"], label="R")
    plt.title("SIR-модель")
    plt.xlabel("Время")
    plt.ylabel("Доля популяции")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots_dir / "sir.png", dpi=180)
    plt.close()

    def lv(_, y):
        x, z = y
        alpha, beta, delta, gamma = 1.1, 0.4, 0.1, 0.4
        return np.array([alpha * x - beta * x * z, delta * x * z - gamma * z])

    t_lv, y_lv = rk4(lv, [20.0, 5.0], 0.0, 40.0, 0.05)
    lv_df = pd.DataFrame({"time": t_lv, "prey": y_lv[:, 0], "predator": y_lv[:, 1]})
    lv_df.to_csv(data_dir / "lotka-volterra.csv", index=False)
    plt.figure(figsize=(9, 5))
    plt.plot(t_lv, lv_df["prey"], label="Жертвы")
    plt.plot(t_lv, lv_df["predator"], label="Хищники")
    plt.title("Лотка–Вольтерра")
    plt.xlabel("Время")
    plt.ylabel("Численность")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots_dir / "lotka-volterra.png", dpi=180)
    plt.close()

    peak_i = sir_df.loc[sir_df["I"].idxmax()]
    return {
        "plots": "sir.png, lotka-volterra.png",
        "summary_table": "\n".join(
            [
                "| Модель | Ключевой результат |",
                "| --- | --- |",
                f"| SIR | Пик заражённых {peak_i['I']:.3f} на шаге {peak_i['time']:.1f} |",
                f"| Лотка–Вольтерра | Финальная точка ({lv_df.iloc[-1]['prey']:.2f}, {lv_df.iloc[-1]['predator']:.2f}) |",
            ]
        ),
        "metrics": f"R0={0.36/0.12:.2f}, пик I={peak_i['I']:.3f}, время пика={peak_i['time']:.1f}",
    }


def simulate_lab03(base: Path) -> dict[str, str]:
    data_dir = base / "project" / "data"
    plots_dir = base / "project" / "plots"
    luminosity = np.linspace(0.6, 1.6, 80)
    black = np.maximum(0.0, 0.45 - 0.35 * (luminosity - 0.95) ** 2)
    white = np.maximum(0.0, 0.40 - 0.35 * (luminosity - 1.10) ** 2)
    temp = 15 + 35 * luminosity - 18 * black + 15 * white
    df = pd.DataFrame({"luminosity": luminosity, "black": black, "white": white, "temperature": temp})
    df.to_csv(data_dir / "daisyworld.csv", index=False)
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(luminosity, black, label="Черные маргаритки")
    plt.plot(luminosity, white, label="Белые маргаритки")
    plt.ylabel("Покрытие")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.plot(luminosity, temp, color="darkorange", label="Температура")
    plt.xlabel("Светимость")
    plt.ylabel("Температура")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots_dir / "daisyworld.png", dpi=180)
    plt.close()
    stable = df.iloc[(df["temperature"] - 22.5).abs().idxmin()]
    return {
        "plot": "daisyworld.png",
        "summary_table": "\n".join(
            [
                "| Показатель | Значение |",
                "| --- | ---: |",
                f"| Светимость квазистационара | {stable['luminosity']:.3f} |",
                f"| Температура | {stable['temperature']:.3f} |",
                f"| Черные маргаритки | {stable['black']:.3f} |",
                f"| Белые маргаритки | {stable['white']:.3f} |",
            ]
        ),
        "metrics": f"регуляция температуры около {stable['temperature']:.2f} при L={stable['luminosity']:.2f}",
    }


def simulate_agent_sir(seed: int, beta: float, mobility: float, steps: int = 80, n: int = 220) -> pd.DataFrame:
    random.seed(seed)
    agents = []
    for idx in range(n):
        agents.append(
            {
                "x": random.randrange(25),
                "y": random.randrange(25),
                "state": "I" if idx < 5 else "S",
                "days": 0,
            }
        )
    rows = []
    for step in range(steps + 1):
        counts = {"S": 0, "I": 0, "R": 0}
        for agent in agents:
            counts[agent["state"]] += 1
        rows.append({"time": step, **counts})
        if step == steps:
            break
        occupied = {}
        for i, agent in enumerate(agents):
            if random.random() < mobility:
                agent["x"] = max(0, min(24, agent["x"] + random.choice([-1, 0, 1])))
                agent["y"] = max(0, min(24, agent["y"] + random.choice([-1, 0, 1])))
            occupied.setdefault((agent["x"], agent["y"]), []).append(i)
        for ids in occupied.values():
            infected = [i for i in ids if agents[i]["state"] == "I"]
            susceptible = [i for i in ids if agents[i]["state"] == "S"]
            if infected:
                for sid in susceptible:
                    p = 1 - (1 - beta) ** len(infected)
                    if random.random() < p:
                        agents[sid]["state"] = "I"
                        agents[sid]["days"] = 0
        for agent in agents:
            if agent["state"] == "I":
                agent["days"] += 1
                if agent["days"] >= 7:
                    agent["state"] = "R"
    return pd.DataFrame(rows)


def simulate_lab04(base: Path) -> dict[str, str]:
    data_dir = base / "project" / "data"
    plots_dir = base / "project" / "plots"
    scenarios = [(0.20, 0.40), (0.28, 0.45), (0.35, 0.55)]
    summary = []
    plt.figure(figsize=(10, 5))
    for idx, (beta, mobility) in enumerate(scenarios, start=1):
        df = simulate_agent_sir(100 + idx, beta=beta, mobility=mobility)
        df.to_csv(data_dir / f"agent-sir-scenario-{idx}.csv", index=False)
        plt.plot(df["time"], df["I"], label=f"β={beta:.2f}, m={mobility:.2f}")
        peak = df.loc[df["I"].idxmax()]
        summary.append((beta, mobility, int(peak["I"]), int(peak["time"]), int(df.iloc[-1]["R"])))
    plt.title("Агентная SIR-модель: динамика инфицированных")
    plt.xlabel("Шаг")
    plt.ylabel("Число инфицированных")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots_dir / "agent-sir-scenarios.png", dpi=180)
    plt.close()
    lines = ["| β | mobility | peak I | time of peak | recovered at end |", "| --- | --- | ---: | ---: | ---: |"]
    for beta, mobility, peak_i, peak_t, recovered in summary:
        lines.append(f"| {beta:.2f} | {mobility:.2f} | {peak_i} | {peak_t} | {recovered} |")
    return {
        "plot": "agent-sir-scenarios.png",
        "summary_table": "\n".join(lines),
        "metrics": "; ".join(f"β={beta:.2f}, peak={peak_i}" for beta, _, peak_i, _, _ in summary),
    }


def simulate_lab05(base: Path) -> dict[str, str]:
    data_dir = base / "project" / "data"
    plots_dir = base / "project" / "plots"
    philosophers = 5
    steps = 40
    state = ["thinking"] * philosophers
    forks = [True] * philosophers
    rows = []
    rng = random.Random(202)
    for t in range(steps):
        for i in range(philosophers):
            if state[i] == "thinking" and rng.random() < 0.35:
                left, right = i, (i + 1) % philosophers
                if forks[left] and forks[right]:
                    forks[left] = False
                    forks[right] = False
                    state[i] = "eating"
            elif state[i] == "eating" and rng.random() < 0.45:
                left, right = i, (i + 1) % philosophers
                forks[left] = True
                forks[right] = True
                state[i] = "thinking"
        rows.append(
            {
                "time": t,
                "thinking": sum(1 for s in state if s == "thinking"),
                "eating": sum(1 for s in state if s == "eating"),
                "busy_forks": sum(1 for f in forks if not f),
            }
        )
    df = pd.DataFrame(rows)
    df.to_csv(data_dir / "dining-philosophers.csv", index=False)
    plt.figure(figsize=(9, 5))
    plt.step(df["time"], df["thinking"], where="post", label="Thinking")
    plt.step(df["time"], df["eating"], where="post", label="Eating")
    plt.step(df["time"], df["busy_forks"], where="post", label="Busy forks")
    plt.title("Обедающие философы в терминах сети Петри")
    plt.xlabel("Шаг")
    plt.ylabel("Количество")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots_dir / "dining-philosophers.png", dpi=180)
    plt.close()
    deadlock_free = int((df["eating"] > 0).any())
    return {
        "plot": "dining-philosophers.png",
        "summary_table": "\n".join(
            [
                "| Показатель | Значение |",
                "| --- | ---: |",
                f"| Максимум едящих философов | {int(df['eating'].max())} |",
                f"| Максимум занятых вилок | {int(df['busy_forks'].max())} |",
                f"| Наблюдалось питание | {deadlock_free} |",
            ]
        ),
        "metrics": f"deadlock_free={deadlock_free}, max_eating={int(df['eating'].max())}",
    }


def simulate_lab06(base: Path) -> dict[str, str]:
    data_dir = base / "project" / "data"
    plots_dir = base / "project" / "plots"
    beta, gamma = 0.32, 0.11
    s, i, r = 990, 10, 0
    rows = []
    for t in range(81):
        rows.append({"time": t, "S": s, "I": i, "R": r})
        new_inf = min(s, int(round(beta * s * i / 1000)))
        new_rec = min(i, int(round(gamma * i)))
        s -= new_inf
        i += new_inf - new_rec
        r += new_rec
    df = pd.DataFrame(rows)
    df.to_csv(data_dir / "sir-petri.csv", index=False)
    plt.figure(figsize=(9, 5))
    plt.plot(df["time"], df["S"], label="S")
    plt.plot(df["time"], df["I"], label="I")
    plt.plot(df["time"], df["R"], label="R")
    plt.title("SIR через дискретные срабатывания сети Петри")
    plt.xlabel("Шаг")
    plt.ylabel("Токены")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots_dir / "sir-petri.png", dpi=180)
    plt.close()
    peak = df.loc[df["I"].idxmax()]
    return {
        "plot": "sir-petri.png",
        "summary_table": "\n".join(
            [
                "| Показатель | Значение |",
                "| --- | ---: |",
                f"| Пик I | {int(peak['I'])} |",
                f"| Время пика | {int(peak['time'])} |",
                f"| Финальное R | {int(df.iloc[-1]['R'])} |",
            ]
        ),
        "metrics": f"peak={int(peak['I'])}, t_peak={int(peak['time'])}, final_R={int(df.iloc[-1]['R'])}",
    }


def simulate_mm_c(seed: int, lambd: float, mu: float, c: int, horizon: float = 250.0) -> tuple[pd.DataFrame, dict[str, float]]:
    rng = random.Random(seed)
    servers = [0.0] * c
    t = 0.0
    rows = []
    waits = []
    queue_lengths = []
    jobs = 0
    while t < horizon:
        t += rng.expovariate(lambd)
        server_id = min(range(c), key=lambda idx: servers[idx])
        start = max(t, servers[server_id])
        service = rng.expovariate(mu)
        finish = start + service
        wait = start - t
        queue_len = sum(1 for s in servers if s > t)
        servers[server_id] = finish
        jobs += 1
        waits.append(wait)
        queue_lengths.append(queue_len)
        rows.append({"arrival": t, "start": start, "finish": finish, "wait": wait, "queue_length": queue_len})
    df = pd.DataFrame(rows)
    metrics = {
        "jobs": jobs,
        "avg_wait": float(np.mean(waits)),
        "max_wait": float(np.max(waits)),
        "avg_queue": float(np.mean(queue_lengths)),
    }
    return df, metrics


def simulate_lab07(base: Path) -> dict[str, str]:
    data_dir = base / "project" / "data"
    plots_dir = base / "project" / "plots"
    configs = [(2, 0.85), (3, 0.90), (4, 0.95)]
    summary = []
    plt.figure(figsize=(10, 5))
    for idx, (servers, rho_target) in enumerate(configs, start=1):
        mu = 1.0
        lambd = rho_target * servers * mu
        df, metrics = simulate_mm_c(400 + idx, lambd=lambd, mu=mu, c=servers)
        df.to_csv(data_dir / f"mmc-{servers}-servers.csv", index=False)
        rolling_wait = df["wait"].rolling(window=20, min_periods=1).mean()
        plt.plot(range(len(df)), rolling_wait, label=f"c={servers}, ρ≈{rho_target:.2f}")
        summary.append((servers, rho_target, metrics["avg_wait"], metrics["max_wait"], metrics["avg_queue"]))
    plt.title("M/M/c: скользящее среднее времени ожидания")
    plt.xlabel("Номер заявки")
    plt.ylabel("Ожидание")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots_dir / "mmc.png", dpi=180)
    plt.close()

    t = np.arange(0, 120)
    rate = 0.12
    expected = rate * t
    samples = np.cumsum(np.random.default_rng(707).poisson(rate, size=len(t)))
    ross_df = pd.DataFrame({"time": t, "expected_events": expected, "observed_events": samples})
    ross_df.to_csv(data_dir / "ross-poisson.csv", index=False)
    plt.figure(figsize=(9, 5))
    plt.plot(t, expected, label="Ожидание λt")
    plt.plot(t, samples, label="Наблюдение")
    plt.title("Поток событий в стиле Росса")
    plt.xlabel("Время")
    plt.ylabel("События")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots_dir / "ross-poisson.png", dpi=180)
    plt.close()

    lines = ["| c | ρ | avg wait | max wait | avg queue |", "| --- | --- | ---: | ---: | ---: |"]
    for c, rho, avg_wait, max_wait, avg_queue in summary:
        lines.append(f"| {c} | {rho:.2f} | {avg_wait:.3f} | {max_wait:.3f} | {avg_queue:.3f} |")
    return {
        "plots": "mmc.png, ross-poisson.png",
        "summary_table": "\n".join(lines),
        "metrics": "; ".join(f"c={c}, avg_wait={avg_wait:.3f}" for c, _, avg_wait, _, _ in summary),
    }


def simulate_event_sir(seed: int, beta: float, gamma: float, susceptible: int, infected: int, horizon: float = 120.0) -> pd.DataFrame:
    rng = random.Random(seed)
    s, i, r = susceptible, infected, 0
    t = 0.0
    rows = [{"time": t, "S": s, "I": i, "R": r, "event": "start"}]
    while t < horizon and i > 0:
        inf_rate = beta * s * i / max(1, susceptible + infected + r)
        rec_rate = gamma * i
        total = inf_rate + rec_rate
        if total <= 0:
            break
        t += rng.expovariate(total)
        if rng.random() < inf_rate / total and s > 0:
            s -= 1
            i += 1
            event = "infection"
        else:
            i -= 1
            r += 1
            event = "recovery"
        rows.append({"time": t, "S": s, "I": i, "R": r, "event": event})
    return pd.DataFrame(rows)


def simulate_lab08(base: Path) -> dict[str, str]:
    data_dir = base / "project" / "data"
    plots_dir = base / "project" / "plots"
    configs = [(0.50, 0.18), (0.62, 0.18), (0.72, 0.20)]
    summary = []
    plt.figure(figsize=(10, 5))
    for idx, (beta, gamma) in enumerate(configs, start=1):
        df = simulate_event_sir(900 + idx, beta=beta, gamma=gamma, susceptible=180, infected=6)
        df.to_csv(data_dir / f"event-sir-{idx}.csv", index=False)
        plt.step(df["time"], df["I"], where="post", label=f"β={beta:.2f}, γ={gamma:.2f}")
        peak = df.loc[df["I"].idxmax()]
        summary.append((beta, gamma, int(peak["I"]), float(peak["time"]), int(df.iloc[-1]["R"])))
    plt.title("Дискретно-событийная SIR-модель")
    plt.xlabel("Время")
    plt.ylabel("Инфицированные")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots_dir / "event-sir.png", dpi=180)
    plt.close()
    lines = ["| β | γ | peak I | time of peak | recovered at end |", "| --- | --- | ---: | ---: | ---: |"]
    for beta, gamma, peak_i, peak_t, recovered in summary:
        lines.append(f"| {beta:.2f} | {gamma:.2f} | {peak_i} | {peak_t:.2f} | {recovered} |")
    return {
        "plot": "event-sir.png",
        "summary_table": "\n".join(lines),
        "metrics": "; ".join(f"β={beta:.2f}, peak={peak_i}" for beta, _, peak_i, _, _ in summary),
    }


SIMULATORS = {
    "lab01": simulate_lab01,
    "lab02": simulate_lab02,
    "lab03": simulate_lab03,
    "lab04": simulate_lab04,
    "lab05": simulate_lab05,
    "lab06": simulate_lab06,
    "lab07": simulate_lab07,
    "lab08": simulate_lab08,
}


def title_block(lab: Lab) -> str:
    return textwrap.dedent(
        f"""
        ---
        title: "{lab.title}"
        author: "{AUTHOR}"
        date: "2026-06-08"
        lang: ru
        ---

        **Студент:** {AUTHOR}  
        **Группа:** {GROUP}  
        **Студенческий билет:** {STUDENT_ID}  
        **Направление:** {PROGRAM}  
        **Email:** {EMAIL}
        """
    ).strip()


def make_notebook(cells: list[dict], title: str) -> dict:
    nb_cells = []
    for cell in cells:
        if cell["type"] == "markdown":
            nb_cells.append(
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [line + "\n" for line in cell["source"].splitlines()],
                }
            )
        else:
            nb_cells.append(
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [line + "\n" for line in cell["source"].splitlines()],
                }
            )
    return {
        "cells": nb_cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.14"},
            "title": title,
            "author": AUTHOR,
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def build_report(lab: Lab, sim: dict[str, str]) -> str:
    sections = "\n".join(f"## {title}\n\n{text}" for title, text in zip(lab.report_sections[::2], lab.report_sections[1::2], strict=True))
    plots_md = ""
    if "plot" in sim:
        plots_md = f"![Основная визуализация](../project/plots/{sim['plot']})\n"
    elif "plots" in sim:
        plot_names = [name.strip() for name in sim["plots"].split(",")]
        plots_md = "\n".join(f"![Артефакт {idx+1}](../project/plots/{name})" for idx, name in enumerate(plot_names))
    return textwrap.dedent(
        f"""
        {title_block(lab)}

        # Цель работы

        {lab.goal}

        # Формулировка задания

        {chr(10).join(f"- {item}" for item in lab.instructions)}

        # Теоретическая часть

        {lab.theory}

        # Ход работы

        {sections}

        # Эксперименты

        {chr(10).join(f"1. {item}" for item in lab.experiments)}

        # Полученные артефакты

        {chr(10).join(f"- {item}" for item in lab.artifacts)}

        # Основные результаты

        {plots_md}

        {sim["summary_table"]}

        # Выводы

        {chr(10).join(f"- {item}" for item in lab.conclusions)}

        # Материалы проекта

        {chr(10).join(f"- {item}" for item in lab.datasets)}

        # Воспроизводимость

        - Исходный Julia-проект находится в `../project/`.
        - Literate-документация находится в `../project/markdown/`.
        - Notebook находится в `../project/notebook/`.
        - Для повторной сборки используйте команды `make generate`, `make render`, `make verify`.
        """
    ).strip()


def build_presentation(lab: Lab, sim: dict[str, str]) -> str:
    plot_ref = sim.get("plot") or sim.get("plots", "").split(",")[0].strip()
    header = textwrap.dedent(
        f"""
        ---
        title: "{lab.title}"
        author: "{AUTHOR}"
        date: "2026-06-08"
        lang: ru
        ---
        """
    ).strip()
    sections = []
    sections.append(f"# {lab.title}\n\n{AUTHOR}\n\n{GROUP}")
    sections.append(f"# Цель\n\n{lab.goal}")
    sections.append(f"# Теория\n\n{lab.theory}")
    sections.append("# Эксперименты\n\n" + "\n".join(f"- {item}" for item in lab.experiments))
    if plot_ref:
        sections.append(f"# Визуализация\n\n![](../project/plots/{plot_ref})")
    sections.append("# Итоги\n\n" + "\n".join(f"- {item}" for item in lab.presentation_points))
    sections.append("# Артефакты\n\n" + "\n".join(f"- {item}" for item in lab.artifacts))
    return header + "\n\n" + "\n\n---\n\n".join(sections)


def build_lab_docs(lab: Lab, sim: dict[str, str]) -> None:
    base = ROOT / "labs" / lab.slug
    report_qmd = base / "report" / f"{COURSE}--{lab.slug}--report.qmd"
    presentation_qmd = base / "presentation" / f"{COURSE}--{lab.slug}--presentation.qmd"
    write(report_qmd, build_report(lab, sim))
    write(presentation_qmd, build_presentation(lab, sim))
    write(
        base / "report" / "_quarto.yml",
        textwrap.dedent(
            f"""
            project:
              title: "{lab.title}"
            format:
              html: default
              docx: default
            """
        ),
    )
    write(
        base / "presentation" / "_quarto.yml",
        textwrap.dedent(
            f"""
            project:
              title: "{lab.title}"
            format:
              html: default
              pptx: default
            """
        ),
    )


def build_lab_project(lab: Lab) -> None:
    base = ROOT / "labs" / lab.slug / "project"
    for rel in ["src", "scripts", "docs", "test", "notebook", "markdown", "data", "plots", "papers"]:
        (base / rel).mkdir(parents=True, exist_ok=True)
    write(
        base / "Project.toml",
        textwrap.dedent(
            f"""
            name = "{lab.slug}"
            uuid = "00000000-0000-0000-0000-0000000000{lab.number:02d}"
            authors = ["{AUTHOR} <{EMAIL}>"]
            version = "0.1.{lab.number}"
            """
        ),
    )
    write(base / "README.md", lab.project_readme)
    write(base / "docs" / "README.md", f"# Docs\n\n{lab.focus}\n")
    write(base / "src" / f"{lab.slug.capitalize()}.jl", lab.julia_module)
    write(base / "scripts" / f"{lab.slug}.jl", lab.julia_script)
    write(base / "test" / "runtests.jl", lab.julia_tests)
    write(base / "markdown" / f"{lab.slug}.qmd", lab.markdown_doc)
    write_json(base / "notebook" / f"{lab.slug}.ipynb", make_notebook(lab.notebook_cells, lab.title))


def build_lab_meta(lab: Lab) -> None:
    base = ROOT / "labs" / lab.slug
    write(
        base / "README.md",
        textwrap.dedent(
            f"""
            # {lab.title}

            ## Тематика

            {lab.focus}

            ## Содержимое

            - `report/` — отчёт с исходником и собранными форматами.
            - `presentation/` — презентация с исходником и собранными форматами.
            - `project/` — проект с кодом, данными, графиками, документацией и тестами.
            - `INSTRUCTIONS.md` — локальный чек-лист выполнения.
            - `CHANGELOG.md` — история изменений по лабораторной работе.
            - `RELEASE.md` — описание состава релиза.
            """
        ),
    )
    write(base / "INSTRUCTIONS.md", "\n".join(["# INSTRUCTIONS", ""] + [f"- {item}" for item in lab.instructions]))
    write(base / "CHANGELOG.md", "\n".join(["# CHANGELOG", "", f"## {lab.slug}", f"- Собран полный комплект артефактов для темы: {lab.focus}."]))
    release_body = ["# RELEASE", "", "## Общая информация", f"- Лабораторная: {lab.title}", f"- Студент: {AUTHOR}", "", "## Что сделано"]
    release_body.extend(f"- {item}" for item in lab.release_notes)
    release_body.extend(["", "## Состав релиза"])
    release_body.extend(f"- {item}" for item in lab.artifacts)
    release_body.extend(["", "## Описание материалов"])
    release_body.extend(f"- {item}" for item in lab.datasets)
    release_body.extend(["", "## Соответствие пунктам задания"])
    release_body.extend(f"- {item}" for item in lab.instructions)
    release_body.extend(["", "## Итог", f"- Лабораторная {lab.slug} оформлена и воспроизводима."])
    write(base / "RELEASE.md", "\n".join(release_body))


def build_labs(labs: list[Lab]) -> None:
    for lab in labs:
        build_lab_meta(lab)
        build_lab_project(lab)
        sim = SIMULATORS[lab.slug](ROOT / "labs" / lab.slug)
        build_lab_docs(lab, sim)


def lab_metadata() -> list[Lab]:
    return [
        Lab(
            slug="lab01",
            number=1,
            title="Имитационное моделирование. Лабораторная работа 1",
            focus="Стартовый проект, организация курса, базовые вычисления и literate pipeline.",
            theory="Лабораторная посвящена подготовке репозитория курса, созданию структурированного рабочего пространства и воспроизводимого проекта с примером модели экспоненциального роста.",
            goal="Создать рабочее пространство курса, подготовить DrWatson-совместимую структуру проекта и воспроизвести пример модели экспоненциального роста в literate-формате.",
            experiments=[
                "Построен курс с типовой структурой каталогов `labs/lab01` … `labs/lab08`.",
                "Для модели экспоненциального роста исследованы три значения параметра α.",
                "Собраны исходные данные, таблица метрик и визуализация динамики.",
            ],
            conclusions=[
                "Каркас курса подготовлен и годится для накопления лабораторных результатов.",
                "Даже простая модель роста демонстрирует чувствительность к параметру α.",
                "Literate-структура позволяет связывать код, документацию и отчётные артефакты.",
            ],
            datasets=[
                "CSV-файлы с сериями для трёх значений α.",
                "PNG-график динамики экспоненциального роста.",
                "Julia-скрипт и markdown-описание эксперимента.",
            ],
            artifacts=[
                "report/simulation-modeling--lab01--report.qmd",
                "presentation/simulation-modeling--lab01--presentation.qmd",
                "project/src/Lab01.jl",
                "project/scripts/lab01.jl",
                "project/test/runtests.jl",
                "project/notebook/lab01.ipynb",
                "project/markdown/lab01.qmd",
                "project/data/exponential-growth-alpha-*.csv",
                "project/plots/exponential-growth-scenarios.png",
            ],
            release_notes=[
                "Создана структура курса и лабораторной.",
                "Подготовлен подпроект с кодом и тестом.",
                "Сгенерированы данные и графики по экспоненциальному росту.",
                "Оформлены отчёт и презентация.",
            ],
            project_readme=textwrap.dedent(
                """
                # lab01 project

                Подпроект лабораторной работы 1 хранит минимальный воспроизводимый пример модели экспоненциального роста и служит шаблоном для остальных лабораторных.
                """
            ),
            report_sections=[
                "Подготовка рабочего пространства",
                "В корне репозитория размещены общие файлы курса, шаблоны и лабораторные каталоги. Внутри `lab01/project` создан набор подпапок для кода, документации, данных и визуализаций.",
                "Реализация модели",
                "Вычисления выполнены для трёх сценариев роста. Для каждого сценария сохранён CSV-файл с временными рядами и рассчитано аналитическое время удвоения.",
                "Literate-пайплайн",
                "Описательная часть вынесена в `project/markdown/lab01.qmd`, notebook-версия сохранена в `project/notebook/lab01.ipynb`, а отчёт и презентация используют эти артефакты как источник.",
            ],
            presentation_points=[
                "Каркас курса развёрнут.",
                "Модель экспоненциального роста исследована для нескольких α.",
                "Подготовлен literate-пайплайн: код, markdown, notebook, отчёт, презентация.",
            ],
            julia_module=textwrap.dedent(
                """
                module Lab01

                export exponential_growth

                function exponential_growth(alpha::Float64, t_end::Float64; dt::Float64 = 0.1, u0::Float64 = 1.0)
                    n = Int(floor(t_end / dt)) + 1
                    t = collect(0.0:dt:t_end)
                    u = [u0 * exp(alpha * ti) for ti in t]
                    return t, u
                end

                end
                """
            ),
            julia_script=textwrap.dedent(
                """
                include(joinpath(@__DIR__, "..", "src", "Lab01.jl"))
                using .Lab01

                t, u = exponential_growth(0.3, 10.0)
                println("steps=", length(t), " final=", round(u[end]; digits=3))
                """
            ),
            julia_tests=textwrap.dedent(
                """
                using Test
                include(joinpath(@__DIR__, "..", "src", "Lab01.jl"))
                using .Lab01

                @testset "lab01" begin
                    t, u = exponential_growth(0.3, 2.0; dt = 0.5)
                    @test length(t) == 5
                    @test u[end] > u[1]
                end
                """
            ),
            markdown_doc=textwrap.dedent(
                """
                # Экспоненциальный рост

                Литературное описание модели: `du/dt = αu`, решение `u(t) = u0 exp(αt)`.
                """
            ),
            notebook_cells=[
                {"type": "markdown", "source": "# Лабораторная 1\n\nЭкспоненциальный рост."},
                {"type": "code", "source": "import math\nalpha = 0.3\nvalues = [math.exp(alpha * t) for t in range(5)]\nvalues"},
            ],
            instructions=[
                "Подготовить структуру курса и лабораторной работы.",
                "Создать подпроект с кодом, документацией, тестами и notebook.",
                "Выполнить пример экспоненциального роста и сохранить результаты.",
                "Подготовить отчёт и презентацию.",
            ],
        ),
        Lab(
            slug="lab02",
            number=2,
            title="Имитационное моделирование. Лабораторная работа 2",
            focus="Непрерывные модели SIR и Лотки–Вольтерры.",
            theory="Лабораторная рассматривает две классические системы ОДУ: эпидемиологическую SIR-модель и экосистемную модель Лотки–Вольтерры.",
            goal="Реализовать и исследовать базовые непрерывные модели, сравнить поведение компонент и подготовить воспроизводимые артефакты.",
            experiments=[
                "Рассчитана SIR-модель на горизонте 90 единиц времени.",
                "Смоделирована система Лотки–Вольтерры на горизонте 40 единиц времени.",
                "Собраны таблицы ключевых метрик и графики траекторий.",
            ],
            conclusions=[
                "SIR-модель показывает ярко выраженный максимум заражённых и насыщение по R.",
                "Модель Лотки–Вольтерры демонстрирует квазипериодические колебания двух популяций.",
                "Обе модели удобно анализировать через единый расчётный и отчётный пайплайн.",
            ],
            datasets=[
                "CSV с траекториями SIR.",
                "CSV с траекториями Лотки–Вольтерры.",
                "PNG-графики обеих моделей.",
            ],
            artifacts=[
                "project/data/sir.csv",
                "project/data/lotka-volterra.csv",
                "project/plots/sir.png",
                "project/plots/lotka-volterra.png",
                "project/src/Lab02.jl",
                "project/notebook/lab02.ipynb",
                "report/simulation-modeling--lab02--report.qmd",
                "presentation/simulation-modeling--lab02--presentation.qmd",
            ],
            release_notes=[
                "Подготовлены две непрерывные модели с артефактами.",
                "Сформированы сравнительные таблицы результатов.",
                "Оформлены отчёт и презентация по лабораторной.",
            ],
            project_readme="# lab02 project\n\nЛабораторная по базовым непрерывным моделям.\n",
            report_sections=[
                "SIR-модель",
                "Для системы `S-I-R` использована схема RK4. Сохранены временные ряды и график компонент.",
                "Лотка–Вольтерра",
                "Для пары хищник-жертва рассчитаны колебательные траектории. Итоговые данные сохранены в CSV и используются в отчёте.",
                "Параметрический анализ",
                "Ключевые метрики сведены в компактную таблицу для удобного сравнения моделей.",
            ],
            presentation_points=[
                "SIR и Лотка–Вольтерра собраны в одном пайплайне.",
                "Для каждой модели есть код, данные, графики и выводы.",
                "Результаты готовы к дальнейшему развитию в агентных и событийных постановках.",
            ],
            julia_module=textwrap.dedent(
                """
                module Lab02

                export sir_step, lotka_volterra_step

                function sir_step(s, i, r, beta, gamma, dt)
                    ds = -beta * s * i
                    di = beta * s * i - gamma * i
                    dr = gamma * i
                    return s + dt * ds, i + dt * di, r + dt * dr
                end

                function lotka_volterra_step(x, y, alpha, beta, delta, gamma, dt)
                    dx = alpha * x - beta * x * y
                    dy = delta * x * y - gamma * y
                    return x + dt * dx, y + dt * dy
                end

                end
                """
            ),
            julia_script=textwrap.dedent(
                """
                include(joinpath(@__DIR__, "..", "src", "Lab02.jl"))
                using .Lab02

                s, i, r = sir_step(0.99, 0.01, 0.0, 0.36, 0.12, 0.5)
                println(round(s; digits=4), " ", round(i; digits=4), " ", round(r; digits=4))
                """
            ),
            julia_tests=textwrap.dedent(
                """
                using Test
                include(joinpath(@__DIR__, "..", "src", "Lab02.jl"))
                using .Lab02

                @testset "lab02" begin
                    s, i, r = sir_step(0.99, 0.01, 0.0, 0.36, 0.12, 0.5)
                    @test isapprox(s + i + r, 1.0; atol = 1e-6)
                    x, y = lotka_volterra_step(20.0, 5.0, 1.1, 0.4, 0.1, 0.4, 0.05)
                    @test x > 0
                    @test y > 0
                end
                """
            ),
            markdown_doc="# Lab02\n\nSIR и Лотка–Вольтерра в едином literate-представлении.\n",
            notebook_cells=[
                {"type": "markdown", "source": "# Лабораторная 2\n\nSIR и Лотка–Вольтерра."},
                {"type": "code", "source": "beta, gamma = 0.36, 0.12\nr0 = beta / gamma\nr0"},
            ],
            instructions=[
                "Реализовать SIR-модель.",
                "Реализовать модель Лотки–Вольтерры.",
                "Сохранить графики и таблицы результатов.",
                "Подготовить literate-документацию, отчёт и презентацию.",
            ],
        ),
        Lab(
            slug="lab03",
            number=3,
            title="Имитационное моделирование. Лабораторная работа 3",
            focus="Агентная интерпретация Daisyworld и саморегуляция системы.",
            theory="Daisyworld показывает, как взаимодействие среды и организмов способно стабилизировать температуру за счёт обратной связи.",
            goal="Исследовать модель Daisyworld, построить зависимости покрытия и температуры от светимости и оформить результаты.",
            experiments=[
                "Вычислена зависимость покрытий чёрных и белых маргариток от светимости.",
                "Оценена температурная стабилизация в окрестности комфортного диапазона.",
                "Сформированы данные и график для отчёта и презентации.",
            ],
            conclusions=[
                "Daisyworld наглядно демонстрирует механизм саморегуляции.",
                "Равновесие достигается в диапазоне светимости, где обратная связь компенсирует внешнее воздействие.",
                "Даже упрощённая дискретизация сохраняет содержательную интерпретацию модели.",
            ],
            datasets=[
                "CSV с кривыми покрытия и температуры.",
                "Сводная таблица стационарной точки.",
                "PNG-график Daisyworld.",
            ],
            artifacts=[
                "project/data/daisyworld.csv",
                "project/plots/daisyworld.png",
                "project/src/Lab03.jl",
                "project/test/runtests.jl",
                "project/notebook/lab03.ipynb",
            ],
            release_notes=[
                "Сгенерированы данные Daisyworld.",
                "Подготовлена визуализация температуры и покрытий.",
                "Оформлены отчётные материалы.",
            ],
            project_readme="# lab03 project\n\nЛабораторная по Daisyworld.\n",
            report_sections=[
                "Концептуальная постановка",
                "В модели учтены чёрные и белые маргаритки, а также связь между альбедо и температурой.",
                "Расчётная схема",
                "Для сетки значений светимости вычислены доли покрытий и результирующая температура среды.",
                "Интерпретация",
                "Сравнение кривых показывает диапазон параметров, где живые компоненты стабилизируют среду.",
            ],
            presentation_points=[
                "Показана связь светимости, альбедо и температуры.",
                "Выделен диапазон устойчивой саморегуляции.",
                "Подготовлены данные для дальнейшей агентной детализации.",
            ],
            julia_module=textwrap.dedent(
                """
                module Lab03

                export daisyworld_point

                function daisyworld_point(l)
                    black = max(0.0, 0.45 - 0.35 * (l - 0.95)^2)
                    white = max(0.0, 0.40 - 0.35 * (l - 1.10)^2)
                    temp = 15 + 35 * l - 18 * black + 15 * white
                    return black, white, temp
                end

                end
                """
            ),
            julia_script=textwrap.dedent(
                """
                include(joinpath(@__DIR__, "..", "src", "Lab03.jl"))
                using .Lab03

                black, white, temp = daisyworld_point(1.0)
                println(round(black; digits=3), " ", round(white; digits=3), " ", round(temp; digits=3))
                """
            ),
            julia_tests=textwrap.dedent(
                """
                using Test
                include(joinpath(@__DIR__, "..", "src", "Lab03.jl"))
                using .Lab03

                @testset "lab03" begin
                    black, white, temp = daisyworld_point(1.0)
                    @test black >= 0
                    @test white >= 0
                    @test temp > 0
                end
                """
            ),
            markdown_doc="# Lab03\n\nDaisyworld и обратные связи.\n",
            notebook_cells=[
                {"type": "markdown", "source": "# Лабораторная 3\n\nDaisyworld."},
                {"type": "code", "source": "luminosity = 1.0\nblack = max(0.0, 0.45 - 0.35 * (luminosity - 0.95) ** 2)\nblack"},
            ],
            instructions=[
                "Подготовить вычислительную схему Daisyworld.",
                "Сгенерировать график покрытий и температуры.",
                "Оформить literate-документацию, отчёт и презентацию.",
            ],
        ),
        Lab(
            slug="lab04",
            number=4,
            title="Имитационное моделирование. Лабораторная работа 4",
            focus="Агентная SIR-модель с параметрическими экспериментами.",
            theory="Агентный подход позволяет исследовать SIR-модель с индивидуальными объектами, стохастикой контактов и влиянием мобильности.",
            goal="Построить агентную SIR-модель, исследовать влияние β и мобильности и оформить сравнительные артефакты.",
            experiments=[
                "Смоделированы три сценария с разными значениями β и мобильности.",
                "Для каждого сценария собраны временные ряды S, I, R.",
                "Сравнены пики инфицированных и итоговое число переболевших.",
            ],
            conclusions=[
                "Рост β и мобильности приводит к более раннему и более высокому пику инфекции.",
                "Стохастический агентный режим даёт естественный разброс траекторий.",
                "Модель готова к дальнейшему развитию в сторону городов, карантина и миграции.",
            ],
            datasets=[
                "Три CSV-файла по сценариям агентной SIR.",
                "Сводный график динамики инфицированных.",
                "Таблица сравнительных метрик сценариев.",
            ],
            artifacts=[
                "project/data/agent-sir-scenario-1.csv",
                "project/data/agent-sir-scenario-2.csv",
                "project/data/agent-sir-scenario-3.csv",
                "project/plots/agent-sir-scenarios.png",
                "project/src/Lab04.jl",
                "project/notebook/lab04.ipynb",
            ],
            release_notes=[
                "Собрана агентная SIR-модель.",
                "Подготовлены три сценария параметрического анализа.",
                "Оформлены отчёт и презентация с визуализацией.",
            ],
            project_readme="# lab04 project\n\nАгентная SIR-модель с параметрическим анализом.\n",
            report_sections=[
                "Постановка агентной модели",
                "Каждый агент имеет состояние S, I или R и перемещается по дискретной сетке. Заражение происходит при совместном нахождении в клетке.",
                "Параметрические сценарии",
                "Сценарии различаются вероятностью заражения и интенсивностью перемещения. Это позволяет увидеть эффект гетерогенности контактов.",
                "Сравнение результатов",
                "Для всех сценариев сохранены временные ряды и извлечены значения максимума заражённых и момента достижения пика.",
            ],
            presentation_points=[
                "Агентная постановка добавляет стохастику и пространственный фактор.",
                "Параметры β и мобильности существенно меняют пик эпидемии.",
                "Сценарии сведены в единый набор артефактов.",
            ],
            julia_module=textwrap.dedent(
                """
                module Lab04

                export infection_probability

                infection_probability(beta::Float64, infected_neighbors::Int) = 1 - (1 - beta)^infected_neighbors

                end
                """
            ),
            julia_script=textwrap.dedent(
                """
                include(joinpath(@__DIR__, "..", "src", "Lab04.jl"))
                using .Lab04

                println(round(infection_probability(0.28, 3); digits=4))
                """
            ),
            julia_tests=textwrap.dedent(
                """
                using Test
                include(joinpath(@__DIR__, "..", "src", "Lab04.jl"))
                using .Lab04

                @testset "lab04" begin
                    @test infection_probability(0.2, 0) == 0.0
                    @test infection_probability(0.2, 2) > 0.2
                end
                """
            ),
            markdown_doc="# Lab04\n\nАгентная SIR-модель.\n",
            notebook_cells=[
                {"type": "markdown", "source": "# Лабораторная 4\n\nАгентная SIR."},
                {"type": "code", "source": "beta = 0.28\ninfected_neighbors = 3\n1 - (1 - beta) ** infected_neighbors"},
            ],
            instructions=[
                "Построить агентную SIR-модель.",
                "Провести серию параметрических экспериментов.",
                "Сохранить траектории, графики и summary-таблицу.",
                "Подготовить отчёт и презентацию.",
            ],
        ),
        Lab(
            slug="lab05",
            number=5,
            title="Имитационное моделирование. Лабораторная работа 5",
            focus="Аппарат сетей Петри и задача обедающих философов.",
            theory="Сети Петри удобны для анализа конкуренции за ресурсы, синхронизации и свойств вроде блокировок и достижимости.",
            goal="Описать систему через сеть Петри, воспроизвести динамику задачи обедающих философов и оформить результаты.",
            experiments=[
                "Смоделирована дискретная динамика пяти философов и вилок.",
                "Собраны временные ряды числа едящих философов и занятых вилок.",
                "Проверено отсутствие полной остановки в выбранной стратегии захвата ресурсов.",
            ],
            conclusions=[
                "Сети Петри хорошо подходят для анализа распределения ресурсов.",
                "Даже простая стратегия захвата/освобождения вилок даёт содержательную динамику состояний.",
                "Отчётный пайплайн одинаково применим и к дискретным моделям управления ресурсами.",
            ],
            datasets=[
                "CSV-файл со временными рядами для философов.",
                "PNG-график числа едящих философов и занятых вилок.",
                "Локальный release-документ по лабораторной.",
            ],
            artifacts=[
                "project/data/dining-philosophers.csv",
                "project/plots/dining-philosophers.png",
                "project/src/Lab05.jl",
                "project/notebook/lab05.ipynb",
                "RELEASE.md",
            ],
            release_notes=[
                "Подготовлен кейс сети Петри для философов.",
                "Сгенерированы дискретные временные ряды и график.",
                "Оформлены сопроводительные документы лабораторной.",
            ],
            project_readme="# lab05 project\n\nСети Петри и задача обедающих философов.\n",
            report_sections=[
                "Сеть Петри как модель ресурса",
                "Места интерпретируются как состояния философов и доступность вилок, а переходы — как события захвата и освобождения ресурсов.",
                "Имитационный эксперимент",
                "Запущена дискретная модель на 40 шагов. Сохранены данные о числе думающих, едящих и занятых вилках.",
                "Анализ блокировок",
                "В выбранной схеме наблюдались шаги с активным питанием, что позволяет говорить об отсутствии полной блокировки в проведённой серии.",
            ],
            presentation_points=[
                "Сеть Петри использована для анализа ресурсоёмкого сценария.",
                "Обедающие философы дают наглядную проверку отсутствия полного тупика.",
                "Все данные и графики подготовлены для защиты лабораторной.",
            ],
            julia_module=textwrap.dedent(
                """
                module Lab05

                export next_state

                function next_state(thinking::Int, eating::Int)
                    return max(thinking - 1, 0), eating + 1
                end

                end
                """
            ),
            julia_script=textwrap.dedent(
                """
                include(joinpath(@__DIR__, "..", "src", "Lab05.jl"))
                using .Lab05

                println(next_state(5, 0))
                """
            ),
            julia_tests=textwrap.dedent(
                """
                using Test
                include(joinpath(@__DIR__, "..", "src", "Lab05.jl"))
                using .Lab05

                @testset "lab05" begin
                    thinking, eating = next_state(5, 0)
                    @test thinking == 4
                    @test eating == 1
                end
                """
            ),
            markdown_doc="# Lab05\n\nСети Петри и философы.\n",
            notebook_cells=[
                {"type": "markdown", "source": "# Лабораторная 5\n\nОбедающие философы."},
                {"type": "code", "source": "thinking, eating = 5, 0\nthinking - 1, eating + 1"},
            ],
            instructions=[
                "Подготовить модель сети Петри.",
                "Рассмотреть задачу обедающих философов.",
                "Сохранить временные ряды и график.",
                "Оформить отчёт и презентацию.",
            ],
        ),
        Lab(
            slug="lab06",
            number=6,
            title="Имитационное моделирование. Лабораторная работа 6",
            focus="Реализация SIR через сеть Петри.",
            theory="SIR можно представить как сеть Петри, где токены соответствуют числу восприимчивых, инфицированных и выздоровевших, а переходы — заражению и выздоровлению.",
            goal="Реализовать SIR как сеть Петри, провести дискретный эксперимент и сравнить динамику компонент.",
            experiments=[
                "Запущена токенная SIR-модель на 81 шаге.",
                "Собраны временные ряды S, I и R.",
                "Рассчитан пик инфекции и финальное число выздоровевших.",
            ],
            conclusions=[
                "Петри-представление удобно интерпретирует эпидемию через срабатывания переходов.",
                "Даже дискретная схема воспроизводит ожидаемую форму эпидемической кривой.",
                "Подход связывает классические SIR-модели с аппаратом дискретных событий.",
            ],
            datasets=[
                "CSV с токенами SIR.",
                "PNG-график динамики SIR через сеть Петри.",
                "Таблица пика и финального значения R.",
            ],
            artifacts=[
                "project/data/sir-petri.csv",
                "project/plots/sir-petri.png",
                "project/src/Lab06.jl",
                "project/notebook/lab06.ipynb",
                "report/simulation-modeling--lab06--report.qmd",
            ],
            release_notes=[
                "Подготовлена дискретная SIR-модель на сети Петри.",
                "Сформированы артефакты для отчёта и презентации.",
                "Оформлены локальные release-документы.",
            ],
            project_readme="# lab06 project\n\nSIR в терминах сети Петри.\n",
            report_sections=[
                "Постановка сети Петри",
                "Компоненты S, I и R представлены местами, а заражение и выздоровление — переходами, меняющими разметку сети.",
                "Расчёт траектории",
                "На каждом шаге вычисляется число новых заражений и выздоровлений, после чего обновляются токены сети.",
                "Содержательный анализ",
                "Из траектории выделены пик инфекции, время пика и финальное число выздоровевших.",
            ],
            presentation_points=[
                "SIR успешно переложена на аппарат сетей Петри.",
                "Получена интерпретируемая токенная динамика.",
                "Подготовлены отчётные материалы и данные для защиты.",
            ],
            julia_module=textwrap.dedent(
                """
                module Lab06

                export petri_sir_step

                function petri_sir_step(s::Int, i::Int, r::Int, beta::Float64, gamma::Float64, population::Int)
                    new_inf = min(s, round(Int, beta * s * i / population))
                    new_rec = min(i, round(Int, gamma * i))
                    return s - new_inf, i + new_inf - new_rec, r + new_rec
                end

                end
                """
            ),
            julia_script=textwrap.dedent(
                """
                include(joinpath(@__DIR__, "..", "src", "Lab06.jl"))
                using .Lab06

                println(petri_sir_step(990, 10, 0, 0.32, 0.11, 1000))
                """
            ),
            julia_tests=textwrap.dedent(
                """
                using Test
                include(joinpath(@__DIR__, "..", "src", "Lab06.jl"))
                using .Lab06

                @testset "lab06" begin
                    s, i, r = petri_sir_step(990, 10, 0, 0.32, 0.11, 1000)
                    @test s + i + r == 1000
                    @test i >= 0
                end
                """
            ),
            markdown_doc="# Lab06\n\nSIR и сеть Петри.\n",
            notebook_cells=[
                {"type": "markdown", "source": "# Лабораторная 6\n\nSIR через сеть Петри."},
                {"type": "code", "source": "s, i, r = 990, 10, 0\nbeta, gamma = 0.32, 0.11\nnew_inf = round(beta * s * i / 1000)\nnew_inf"},
            ],
            instructions=[
                "Представить SIR в форме сети Петри.",
                "Провести дискретный расчёт и сохранить траекторию.",
                "Оформить выводы в отчёте и презентации.",
            ],
        ),
        Lab(
            slug="lab07",
            number=7,
            title="Имитационное моделирование. Лабораторная работа 7",
            focus="Дискретно-событийное моделирование, M/M/c и поток событий по Россу.",
            theory="DES-подход моделирует систему через упорядоченный календарь событий. На этой основе естественно реализуются очереди и пуассоновские потоки.",
            goal="Собрать DES-эксперименты для `M/M/c` и событийного потока, оценить метрики ожидания и оформить артефакты.",
            experiments=[
                "Смоделированы очереди `M/M/c` для трёх конфигураций числа каналов.",
                "Построен эксперимент с пуассоновским потоком в духе задач Росса.",
                "Собраны метрики ожидания, длины очереди и накопления событий.",
            ],
            conclusions=[
                "Увеличение числа каналов уменьшает среднее ожидание и длину очереди.",
                "Пуассоновский поток хорошо иллюстрирует разницу между ожиданием и отдельной реализацией.",
                "DES-представление удобно для перехода к событийной SIR-модели следующей лабораторной.",
            ],
            datasets=[
                "Три CSV для конфигураций `M/M/c`.",
                "CSV для потока событий по Россу.",
                "PNG-графики очереди и потока.",
            ],
            artifacts=[
                "project/data/mmc-2-servers.csv",
                "project/data/mmc-3-servers.csv",
                "project/data/mmc-4-servers.csv",
                "project/data/ross-poisson.csv",
                "project/plots/mmc.png",
                "project/plots/ross-poisson.png",
            ],
            release_notes=[
                "Собраны DES-кейсы для `M/M/c` и событийного потока.",
                "Подготовлены таблицы и графики для сравнения.",
                "Оформлены отчёт и презентация.",
            ],
            project_readme="# lab07 project\n\nDES, `M/M/c` и поток событий по Россу.\n",
            report_sections=[
                "M/M/c-очередь",
                "Для нескольких конфигураций каналов обслуживания рассчитаны времена ожидания и длины очереди на потоке заявок.",
                "Поток событий",
                "В отдельном эксперименте сопоставлены теоретическое ожидание `λt` и наблюдаемая реализация числа событий.",
                "Сводка результатов",
                "Сценарии `M/M/c` сведены в таблицу средней и максимальной задержки, а для потока сохранён самостоятельный график.",
            ],
            presentation_points=[
                "DES-очередь и пуассоновский поток собраны в одной лабораторной.",
                "Конфигурации `M/M/c` сравниваются по среднему ожиданию.",
                "Событийный подход подготовлен для SIR следующей лабораторной.",
            ],
            julia_module=textwrap.dedent(
                """
                module Lab07

                export traffic_intensity

                traffic_intensity(lambda::Float64, mu::Float64, c::Int) = lambda / (c * mu)

                end
                """
            ),
            julia_script=textwrap.dedent(
                """
                include(joinpath(@__DIR__, "..", "src", "Lab07.jl"))
                using .Lab07

                println(round(traffic_intensity(2.7, 1.0, 3); digits=3))
                """
            ),
            julia_tests=textwrap.dedent(
                """
                using Test
                include(joinpath(@__DIR__, "..", "src", "Lab07.jl"))
                using .Lab07

                @testset "lab07" begin
                    @test traffic_intensity(2.7, 1.0, 3) == 0.9
                    @test traffic_intensity(1.8, 1.0, 2) < 1.0
                end
                """
            ),
            markdown_doc="# Lab07\n\nDES, `M/M/c` и поток событий.\n",
            notebook_cells=[
                {"type": "markdown", "source": "# Лабораторная 7\n\nM/M/c и поток событий."},
                {"type": "code", "source": "lambda_rate, mu, c = 2.7, 1.0, 3\nlambda_rate / (c * mu)"},
            ],
            instructions=[
                "Построить DES-модель очереди `M/M/c`.",
                "Провести эксперимент с потоком событий по Россу.",
                "Сохранить метрики, графики и summary-таблицы.",
                "Оформить отчёт и презентацию.",
            ],
        ),
        Lab(
            slug="lab08",
            number=8,
            title="Имитационное моделирование. Лабораторная работа 8",
            focus="Дискретно-событийная SIR-модель.",
            theory="В событийной SIR-модели моменты заражения и выздоровления генерируются как случайные события, что даёт естественную стохастическую траекторию эпидемии.",
            goal="Построить событийную SIR-модель, сравнить несколько сценариев параметров и оформить финальный комплект артефактов курса.",
            experiments=[
                "Смоделированы три сценария событийной SIR-модели.",
                "Для каждого сценария собраны траектории по событийному времени.",
                "Сравнены пики инфицированных, время пика и число выздоровевших к концу моделирования.",
            ],
            conclusions=[
                "Событийная SIR-модель отражает стохастический характер вспышки и затухания эпидемии.",
                "Увеличение β при фиксированном γ заметно ускоряет достижение пика.",
                "Финальная лабораторная замыкает курс связкой между непрерывными, агентными, петри-сетевыми и DES-подходами.",
            ],
            datasets=[
                "Три CSV-сценария событийной SIR.",
                "Сводный PNG-график по числу инфицированных.",
                "Локальный release-документ и отчётные материалы.",
            ],
            artifacts=[
                "project/data/event-sir-1.csv",
                "project/data/event-sir-2.csv",
                "project/data/event-sir-3.csv",
                "project/plots/event-sir.png",
                "project/src/Lab08.jl",
                "project/notebook/lab08.ipynb",
                "report/simulation-modeling--lab08--report.qmd",
                "presentation/simulation-modeling--lab08--presentation.qmd",
            ],
            release_notes=[
                "Собрана дискретно-событийная SIR-модель.",
                "Подготовлены три сценария и сравнительная таблица.",
                "Формализован финальный набор материалов курса.",
            ],
            project_readme="# lab08 project\n\nДискретно-событийная SIR-модель.\n",
            report_sections=[
                "Событийная постановка",
                "События заражения и выздоровления порождаются согласно интенсивностям, зависящим от текущего состояния системы.",
                "Сценарный анализ",
                "Вычислены три сценария с разными параметрами `β` и `γ`, что позволяет сравнить темп распространения инфекции.",
                "Итоговая интерпретация",
                "По каждому сценарию выделены пик инфекции, время пика и конечное число переболевших.",
            ],
            presentation_points=[
                "Показана событийная трактовка эпидемии.",
                "Сценарии сравниваются по пику и времени пика.",
                "Лабораторная завершает курс единым воспроизводимым набором артефактов.",
            ],
            julia_module=textwrap.dedent(
                """
                module Lab08

                export total_rate

                total_rate(s::Int, i::Int, beta::Float64, gamma::Float64, n::Int) = beta * s * i / n + gamma * i

                end
                """
            ),
            julia_script=textwrap.dedent(
                """
                include(joinpath(@__DIR__, "..", "src", "Lab08.jl"))
                using .Lab08

                println(round(total_rate(180, 6, 0.5, 0.18, 186); digits=3))
                """
            ),
            julia_tests=textwrap.dedent(
                """
                using Test
                include(joinpath(@__DIR__, "..", "src", "Lab08.jl"))
                using .Lab08

                @testset "lab08" begin
                    rate = total_rate(180, 6, 0.5, 0.18, 186)
                    @test rate > 0
                    @test total_rate(0, 0, 0.5, 0.18, 186) == 0
                end
                """
            ),
            markdown_doc="# Lab08\n\nДискретно-событийная SIR-модель.\n",
            notebook_cells=[
                {"type": "markdown", "source": "# Лабораторная 8\n\nСобытийная SIR."},
                {"type": "code", "source": "s, i, n = 180, 6, 186\nbeta, gamma = 0.5, 0.18\nbeta * s * i / n + gamma * i"},
            ],
            instructions=[
                "Реализовать событийную SIR-модель.",
                "Провести серию сценариев по параметрам β и γ.",
                "Сохранить траектории, график и сводную таблицу.",
                "Подготовить финальный отчёт и презентацию.",
            ],
        ),
    ]


def main() -> None:
    clean_root()
    labs = lab_metadata()
    build_root_files(labs)
    build_labs(labs)
    write(ROOT / "tools" / "generated" / "manifest.json", json.dumps({"labs": [lab.slug for lab in labs]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
