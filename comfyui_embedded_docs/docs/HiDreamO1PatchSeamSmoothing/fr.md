# Lissage des coutures de patch HiDream-O1

Ce nœud réduit les coutures visibles dans les images générées par le modèle HiDream-O1 en moyennant la sortie du modèle sur plusieurs positions décalées de la grille de patchs pendant la dernière partie du processus d'échantillonnage. Il exécute le modèle plusieurs fois avec de légers décalages d'alignement de l'image et mélange les résultats, ce qui aide à annuler les artefacts de type grille pouvant apparaître aux limites des patchs.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel appliquer le lissage des coutures. | MODEL | Oui | - |
| `start_percent` | Progression de l'échantillonnage (0=début, 1=fin) à laquelle le mélange s'active. par défaut : 0.8 | FLOAT | Oui | 0.0 à 1.0 (step: 0.01) |
| `end_percent` | Progression de l'échantillonnage à laquelle le mélange se désactive. par défaut : 1.0 | FLOAT | Oui | 0.0 à 1.0 (step: 0.01) |
| `pattern` | Disposition des décalages. `single_shift` : une passe sur la grille de patchs naturelle + les autres décalées. `symmetric` : toutes les passes hors grille, les décalages répartis autour de l'origine. par défaut : "single_shift" | COMBO | Oui | `"single_shift"`<br>`"symmetric"` |
| `passes` | Nombre de passes par étape conditionnée. `2`/`4` = fixe. `ramp_*` : le nombre de passes augmente à mesure que l'échantillonnage approche de la fin (davantage de lissage là où les coutures sont les plus visibles). par défaut : "2" | COMBO | Oui | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `blend` | `average` : moyenne à poids égaux. `window` : pondération par fenêtre de Hann favorisant chaque passe à distance de ses limites de patchs. `median` : médiane par pixel, rejette les passes aberrantes de type repliement. par défaut : "average" | COMBO | Oui | `"average"`<br>`"window"`<br>`"median"` |
| `strength` | Interpolation entre la prédiction sur grille naturelle (0) et le résultat moyenné (1). par défaut : 1.0 | FLOAT | Oui | 0.0 à 1.0 (step: 0.01) |

**Remarque sur les contraintes des paramètres :**
- L'effet de lissage n'est pas appliqué si `strength` vaut 0.0 ou moins, ou si `end_percent` est inférieur ou égal à `start_percent`. Dans ces cas, le nœud renvoie le modèle inchangé.
- Les options de rampe du paramètre `passes` (`ramp_2_4`, `ramp_2_4_8`) n'ont de sens que lorsque `end_percent` est supérieur à `start_percent`, car le nombre de passes augmente à mesure que l'échantillonnage progresse dans cette plage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le wrapper de lissage des coutures appliqué. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/fr.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
