# Bienvenue au BecomTech d'Octobre 2019

Le but de cet exercice est de créer une API pour réaliser l'inférence d'un modèle ML. Le modèle en question est un SVM entraîné sur le MNIST Dataset. Le modèle est disponible au format `pickle`.

## 0. Setup

Tout d'abord crée un virtualenv et active le.

```(sh)
virtualenv venv
source venv/bin/activate
```

Ensuite, installe les packages nécessaires à l'application. Installe également l'application en mode éditable.

```(sh)
pip install -r requirements.txt
pip install -e .
```

> Tips: pour vérifier l'installation des packages tu peux faire un `pip freeze`.

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

> N'oublie pas de mettre à jour les packages installés dans `requirements.txt`

## II. Le serveur Flask

En utilisant la classe que tu as créée dans l'exercice précédent, développe une API qui prend en requête POST une image et renvoie la prédiction du modèle.

Si le temps le permet, tu peux toi-même coder le serveur Flask mais ce n'est pas le point de cette séance. Une autre team a déjà développé cette feature dans la branch `2-flask`.

Pour faciliter le developpement, lance le server Flask en mode dev (qui inclus le hot reloading):

```(sh)
export FLASK_APP=mnist
export FLASK_ENV=development
flask run --host=0.0.0.0
```

Tu peux utliser un outil comme **Postman** pour tester l'API.

Attention, cette feature a été développée en parallèle du modèle et donc le code n'est plus à jour avec `master`. Pense à rebase ;) .
