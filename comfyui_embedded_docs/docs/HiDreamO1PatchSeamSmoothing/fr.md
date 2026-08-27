# Lissage des coutures de patch HiDream-O1

Ce nœud réduit les coutures visibles dans les images générées par le modèle HiDream-O1 en moyennant la sortie du modèle sur plusieurs positions de grille de patches décalées pendant la dernière partie du processus d'échantillonnage. Il fonctionne en exécutant le modèle plusieurs fois avec des alignements d'image légèrement différents et en fusionnant les résultats, ce qui aide à annuler les artefacts de type grille pouvant apparaître aux frontières des patches.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle HiDream-O1 auquel appliquer le lissage des coutures. | MODEL | Oui | - |
| `pourcentage_début` | La progression de l'échantillonnage (0=début, 1=fin) à laquelle l'effet de lissage s'active (par défaut : 0.8). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `pourcentage_fin` | La progression de l'échantillonnage à laquelle l'effet de lissage se désactive (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `motif` | La disposition des positions de grille décalées. `single_shift` : une passe sur la grille de patches naturelle plus d'autres décalées. `symmetric` : toutes les passes sont hors grille, avec des décalages répartis autour de l'origine (par défaut : `"single_shift"`). | COMBO | Oui | `"single_shift"`<br>`"symmetric"` |
| `passes` | Le nombre de passes (exécutions du modèle) par étape contrôlée. `2` et `4` sont des nombres fixes. `ramp_2_4` et `ramp_2_4_8` augmentent le nombre de passes à mesure que l'échantillonnage approche de la fin, offrant un lissage accru là où les coutures sont les plus visibles (par défaut : `"2"`). | COMBO | Oui | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `mélange` | La méthode utilisée pour combiner les résultats de chaque passe. `average` : moyenne pondérée égale de toutes les passes. `window` : utilise une fenêtre de Hann pour donner plus de poids au centre de chaque passe, réduisant les artefacts de bordure. `median` : prend la médiane par pixel, ce qui peut rejeter les passes aberrantes causées par le repliement (par défaut : `"average"`). | COMBO | Oui | `"average"`<br>`"window"`<br>`"median"` |
| `force` | Contrôle l'interpolation entre la sortie originale du modèle (0.0) et le résultat entièrement lissé (1.0) (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

**Note sur les contraintes des paramètres :**
- L'effet de lissage ne sera pas appliqué si `strength` est inférieur ou égal à 0.0, ou si `end_percent` est inférieur ou égal à `start_percent`. Dans ces cas, le nœud renvoie le modèle inchangé.
- Les options de rampe du paramètre `passes` (`ramp_2_4`, `ramp_2_4_8`) ne sont significatives que lorsque `start_percent` et `end_percent` définissent une plage, car le nombre de passes augmente à mesure que l'échantillonnage progresse dans cette plage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l'enveloppe de lissage des coutures appliquée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/fr.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
