# Guidage spatio-temporel LTXV (STG)

Ce nœud améliore la précision spatiale et la cohérence du mouvement de la génération vidéo LTXV en exécutant une passe supplémentaire à chaque étape d’échantillonnage. Au cours de cette passe, l’auto-attention des blocs de transformateur sélectionnés est dégradée en un passage direct de la valeur, et la génération est guidée à l’écart du résultat dégradé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle de base auquel appliquer la guidance spatio-temporelle. Le modèle est cloné et modifié avec une fonction de guidance post-CFG. | MODEL | Oui | — |
| `échelle` | La force de la guidance appliquée au résultat débruité. Lorsqu’elle est définie sur 0, la guidance n’a aucun effet. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 100.0 (step 0.01) |
| `blocs` | Indices de blocs de transformateur à perturber, séparés par des virgules. Seules les valeurs numériques sont utilisées ; tous les autres caractères sont ignorés. (par défaut : "29") | STRING | Oui | — |
| `pourcentage_début` | La fraction du processus d’échantillonnage à laquelle la guidance commence. Il s’agit d’un paramètre avancé. (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 (step 0.001) |
| `pourcentage_fin` | La fraction du processus d’échantillonnage à laquelle la guidance se termine. Il s’agit d’un paramètre avancé. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (step 0.001) |

Remarque : La guidance n’est appliquée que pendant l’intervalle d’échantillonnage entre `start_percent` et `end_percent`. Si `scale` est défini sur 0 ou si `blocks` ne contient aucune valeur numérique, la passe guidée n’a aucun effet sur le processus d’échantillonnage.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le modèle cloné avec la fonction de guidance spatio-temporelle attachée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
