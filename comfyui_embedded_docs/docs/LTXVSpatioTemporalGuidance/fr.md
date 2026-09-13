# Guidage spatio-temporel LTXV (STG)

Ce nœud améliore le détail spatial et la cohérence du mouvement de la génération vidéo LTXV en exécutant une passe supplémentaire à chaque étape d'échantillonnage. Durant cette passe, l'auto-attention des blocs Transformer sélectionnés est dégradée en une transmission directe de valeur, et la génération est guidée à l'écart de ce résultat dégradé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle de base auquel appliquer le guidage spatio-temporel. Le modèle est cloné et une fonction de guidage post-CFG est attachée au clone. | MODEL | Oui | — |
| `scale` | La force du guidage appliqué au résultat débruité. Lorsque la valeur est définie à 0, le guidage n'a aucun effet. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 100.0 (pas: 0.01) |
| `blocks` | Indices des blocs Transformer à perturber, séparés par des virgules. Seules les valeurs numériques sont utilisées ; tout autre caractère est ignoré. (par défaut : "29") | STRING | Oui | — |
| `start_percent` | Fraction du processus d'échantillonnage à laquelle le guidage commence. Il s'agit d'un paramètre avancé. (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 (pas: 0.001) |
| `end_percent` | Fraction du processus d'échantillonnage à laquelle le guidage se termine. Il s'agit d'un paramètre avancé. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas: 0.001) |

Remarque : Le guidage n'est appliqué que pendant l'intervalle d'échantillonnage entre `start_percent` et `end_percent`. En dehors de cet intervalle, le résultat débruité d'origine est renvoyé sans modification. Si `scale` vaut 0 ou si `blocks` ne contient aucune valeur numérique, la passe guidée n'a aucun effet sur le processus d'échantillonnage.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le modèle cloné avec la fonction de guidage spatio-temporel attachée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
