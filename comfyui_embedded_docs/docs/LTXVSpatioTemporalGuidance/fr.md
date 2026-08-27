# LTXVSpatioTemporalGuidance

Ce nœud améliore le détail spatial et la cohérence du mouvement de la génération vidéo LTXV en effectuant une passe supplémentaire à chaque étape d'échantillonnage. Au cours de cette passe, l'auto-attention des blocs de transformateur sélectionnés est dégradée en un passage direct des valeurs, et la génération est guidée à l'écart du résultat dégradé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle de base auquel appliquer le guidage spatio-temporel. Le modèle est cloné et modifié avec une fonction de guidage post-CFG. | MODEL | Oui | — |
| `échelle` | La force du guidage appliqué au résultat débruité. Lorsqu'elle est définie à 0, le guidage n'a aucun effet. (défaut : 1.0) | FLOAT | Oui | 0.0 à 100.0 (pas 0.01) |
| `blocs` | Indices de blocs de transformateur séparés par des virgules à perturber. Seules les valeurs numériques sont utilisées ; tous les autres caractères sont ignorés. (défaut : "29") | STRING | Oui | — |
| `pourcentage_début` | La fraction du processus d'échantillonnage à laquelle le guidage commence. (défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 (pas 0.001) |
| `pourcentage_fin` | La fraction du processus d'échantillonnage à laquelle le guidage se termine. (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas 0.001) |

Remarque : Le guidage n'est appliqué que pendant l'intervalle d'échantillonnage entre `start_percent` et `end_percent`. Si `scale` est 0 ou si `blocks` ne contient aucune valeur numérique, la passe guidée n'a aucun effet sur le processus d'échantillonnage.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le modèle cloné avec la fonction de guidage spatio-temporel attachée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
