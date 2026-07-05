# Lissage des coutures de patch HiDream-O1

Voici la traduction en français de la documentation, en respectant toutes les règles fournies :

## Aperçu

Ce nœud réduit les coutures visibles dans les images générées par le modèle HiDream-O1 en faisant la moyenne de la sortie du modèle sur plusieurs positions décalées de la grille de patchs pendant la dernière partie du processus d'échantillonnage. Il fonctionne en exécutant le modèle plusieurs fois avec des alignements d'image légèrement différents et en fusionnant les résultats, ce qui permet d'atténuer les artefacts en forme de grille pouvant apparaître aux limites des patchs.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle HiDream-O1 auquel appliquer le lissage des coutures. | MODEL | Oui | - |
| `pourcentage_début` | La progression de l'échantillonnage (0=début, 1=fin) à laquelle l'effet de lissage s'ACTIVE (par défaut : 0,8). | FLOAT | Oui | 0,0 à 1,0 (pas : 0,01) |
| `pourcentage_fin` | La progression de l'échantillonnage à laquelle l'effet de lissage se DÉSACTIVE (par défaut : 1,0). | FLOAT | Oui | 0,0 à 1,0 (pas : 0,01) |
| `motif` | La disposition des positions décalées de la grille. `single_shift` : un passage sur la grille de patchs naturelle plus d'autres décalés. `symmetric` : tous les passages sont hors grille, avec des décalages répartis autour de l'origine (par défaut : `"single_shift"`). | COMBO | Oui | `"single_shift"`<br>`"symmetric"` |
| `passes` | Le nombre de passages (exécutions du modèle) par étape contrôlée. `2` ou `4` sont des nombres fixes. `ramp_2_4` et `ramp_2_4_8` augmentent le nombre de passages à mesure que l'échantillonnage approche de la fin, offrant plus de lissage là où les coutures sont les plus visibles (par défaut : `"2"`). | COMBO | Oui | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `mélange` | La méthode utilisée pour combiner les résultats de chaque passage. `average` : moyenne pondérée égale de tous les passages. `window` : utilise une fenêtre de Hann pour donner plus de poids au centre de chaque passage, réduisant les artefacts de bordure. `median` : prend la médiane par pixel, ce qui peut rejeter les passages aberrants causés par le repliement (par défaut : `"average"`). | COMBO | Oui | `"average"`<br>`"window"`<br>`"median"` |
| `force` | Contrôle l'interpolation entre la sortie originale du modèle (0,0) et le résultat entièrement lissé (1,0) (par défaut : 1,0). | FLOAT | Oui | 0,0 à 1,0 (pas : 0,01) |

**Remarque sur les contraintes des paramètres :**
- L'effet de lissage ne sera pas appliqué si `strength` est égal ou inférieur à 0,0, ou si `end_percent` est inférieur ou égal à `start_percent`.
- Les options de rampe du paramètre `passes` (`ramp_2_4`, `ramp_2_4_8`) ne sont significatives que lorsque `start_percent` et `end_percent` définissent une plage, car le nombre de passages augmente à mesure que l'échantillonnage progresse dans cette plage.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec l'adaptateur de lissage des coutures appliqué. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/fr.md)

---
**Source fingerprint (SHA-256):** `f4d1a617d88f880dcae3afda25699333df023d7b4ec13a22a73512713d6ef18c`
