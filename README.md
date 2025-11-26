# 🧠 Mémoire de travail – Séquences de chiffres

Ce projet propose des exercices simples et rapides pour entraîner sa **mémoire de travail** au quotidien.

Ce module constitue la première partie d’un ensemble d’exercices :

- Séquences de chiffres ✅
- Séquences de prénoms 🟡 (en cours)
- Autres types de mémorisation 🔜

---

## ✅ Structure du projet

```

/
README.md
modules/
├─ chiffres.py
└─ prenoms.py   (TODO)
data/

````

---

## ▶️ Comment lancer le script

Depuis la racine du projet, exécute :

```bash
python modules/chiffres.py
````

Si tu ne donnes aucun paramètre, les valeurs par défaut sont :

* longueur de la suite : 9 chiffres
* temps d’affichage : 10 secondes
* répétitions : 30 essais

---

### 🛠️ Paramètres disponibles

Tu peux personnaliser l'exercice :

```bash
python modules/chiffres.py -l 7 -t 8 -n 20
```

| option                | description                        | valeur par défaut |
| --------------------- | ---------------------------------- | ----------------- |
| `-l`, `--length`      | longueur de la suite de chiffres   | 9                 |
| `-t`, `--time`        | temps d’affichage (secondes)       | 10                |
| `-n`, `--repetitions` | nombre d’exercices dans la session | 30                |

---

## 💾 Données enregistrées

À chaque lancement, un dossier `data/` est créé s’il n’existe pas.

Il contient :

* `memoire_summary.csv`
  → résumé global des sessions
* `memoire_detail_YYYY-MM-DD_HH-MM-SS_attemptX.csv`
  → détails par essai

Tu peux ainsi suivre ta progression au fil du temps.

---

## 🟡 Module "Prénoms" (TODO)

Un deuxième module sera ajouté :

> mémoriser une liste de prénoms affichés pendant quelques secondes,
> puis tenter de les restituer.

Exemple :

```
Hugues – Sandrine – Zoé – Emilie – Capucine – Robert – César – Sophia – Lucas
```

Ce module :

* suivra la même logique que les chiffres
* enregistrera aussi les résultats dans `data/`
* permettra de travailler une mémoire plus **sémantique / verbale**

📌 Pour l’instant, il s’agit d’un **TODO** et n’est pas encore fonctionnel.

---

## 🎯 Objectif du projet

L'idée est de proposer :

* un entraînement court et régulier
* une progression mesurable
* différents types de mémorisation

---

## 🚀 Pistes d’amélioration

* module prénoms ✅ (à venir)
* visualisation graphique
* interface graphique
* difficulté adaptative
* nouveaux types de stimuli

---

## 📜 Licence

Usage personnel libre.

