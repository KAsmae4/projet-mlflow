"""Produit reports/champion.md et sa matrice de confusion."""

from pathlib import Path

import mlflow
from mlflow import MlflowClient

mlflow.set_tracking_uri("sqlite:///mlflow.db")

v = MlflowClient().get_model_version_by_alias(
    "cancer-sein", "champion"
)
run = mlflow.get_run(v.run_id)

Path("reports").mkdir(exist_ok=True)

mlflow.artifacts.download_artifacts(
    run_id=v.run_id,
    artifact_path="matrice_confusion.png",
    dst_path="reports",
)

lignes = [
    f"# Modèle champion : cancer-sein, version {v.version}",
    "",
    f"Run `{run.info.run_name}` (C = {run.data.params['C']})",
    "",
    "| Métrique | Valeur |",
    "|---|---|",
]

lignes += [
    f"| {k} | {x} |"
    for k, x in sorted(run.data.metrics.items())
]
lignes += ["", "![Matrice de confusion](matrice_confusion.png)"]

rapport = Path("reports/champion.md")
rapport.write_text("\n".join(lignes) + "\n", encoding="utf-8")

print(rapport.read_text(encoding="utf-8"))