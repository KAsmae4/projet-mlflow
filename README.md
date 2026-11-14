# projet-mlflow
## Suivi des expériences (MLflow)

Jeu : Breast Cancer Wisconsin (Diagnostic), fourni par scikit-learn.
Expérience MLflow : `cancer-sein`.
Modèle enregistré : `cancer-sein`.

### Commandes

- Entraîner : `python src/train.py 3.0`
- Chercher C : `python src/tune.py`
- Résumer les runs : `python scripts/runs.py`
- Interface : `mlflow ui --backend-store-uri sqlite:///mlflow.db`
- Enregistrer le champion : `python src/register.py`
- Générer le rapport : `python scripts/report.py`

### Résultats

[Rapport du modèle champion](reports/champion.md)