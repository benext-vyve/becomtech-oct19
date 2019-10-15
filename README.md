# Bienvenue au BecomTech d'Octobre 2019

Tout d'abord crée un virtualenv et active le.

```(sh)
virtualenv venv
source venv/bin/activate
```

Ensuite, install les requirements nécessaires à l'application. Installe également l'application en mode éditable.

```(sh)
pip install -r requirements.txt
pip install -e .
```

> Tips: pour vérifier l'installatiom des packages tu peux faire un `pip freeze`.

## I. Implémente la classe _Model_

Écrit une classe qui représente le modèle de l'application afin de faciliter l'intégration e celui-ci dans une application complète. Cette classe pourrait être utilisé par d'autres data scientist et data engineer.

Le début est dans `mnist/model.py`. Cette classe devra prendre contenir:

1. Un modèle sckit-learn en attribut.
2. Une méthode _predict_ qui prendra en input en input une image et retournera la prédiction du modèle.
3. (Optionel) Une Méthode de classe qui prend en input le pickle du modèle et qui retourne une instance de la classe.

Pour compléter, tu peux rajouter les tests unitaires. Il y a déjà un début de test de créé. Tu peux t'en inspirer pour les tiens. Tu dois installer `pytest` et `pytest-cov` (pour afficher le coverage).

```(sh)
pip install pytest pytest-cov
pytest --cov=mnist
```
