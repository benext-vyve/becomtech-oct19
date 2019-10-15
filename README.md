# Bienvenue au BecomTech d'Octobre 2019

First of all, create a virtualenv and activate it.

```(sh)
virtualenv venv .
source venv/bin/activate
```

Then you need to install the requirements and the application

```(sh)
pip install -r requirements.txt
```

## I. Implémente la classe _Model_

Écrit une classe qui représente le modèle de l'application afin de faciliter l'intégration e celui-ci dans une application complète. Cette classe pourrait être utilisé par d'autres data scientist et data engineer.

Le début est dans `mnist/model.py`. Cette classe devra prendre contenir:

1. Un modèle sckit-learn en attribut.
2. Une méthode _predict_ qui prendra en input ....

Pour compléter, tu peux rajouter les tests unitaires. Il y a déjà un début de test de créé. Tu peux t'en inspirer pour les tiens. Tu dois installer `pytest` et `pytest-cov` (pour afficher le coverage).

```(sh)
pip install pytest pytest-cov
pytest --cov=mnist
```
