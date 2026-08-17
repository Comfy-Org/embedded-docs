# Lissage des coutures de patch HiDream-O1

## Aperçu

Ce nœud réduit les coutures visibles dans les images générées par le modèle HiDream-O1 en faisant la moyenne de la sortie du modèle sur plusieurs positions décalées de la grille de patchs pendant la dernière partie du processus d’échantillonnage. Il fonctionne en exécutant le modèle plusieurs fois avec des alignements d’image légèrement différents et en fusionnant les résultats, ce qui aide à neutraliser les artefacts de type grille qui peuvent apparaître aux frontières des patchs.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle HiDream-O1 auquel appliquer l’enveloppe de lissage des coutures. | MODEL | Oui | - |
| `start_percent` | Progression de l’échantillonnage (0 = début, 1 = fin) à laquelle la fusion s’active (par défaut : 0.8). | FLOAT | Oui | 0.0 to 1.0 (pas : 0.01) |
| `end_percent` | Progression de l’échantillonnage à laquelle la fusion se désactive (par défaut : 1.0). | FLOAT | Oui | 0.0 to 1.0 (pas : 0.01) |
| `pattern` | Disposition des décalages. `single_shift` : un passage sur la grille de patchs naturelle plus d’autres passages décalés. `symmetric` : tous les passages hors grille, avec des décalages répartis autour de l’origine (par défaut : `"single_shift"`). | COMBO | Oui | `"single_shift"`<br>`"symmetric"` |
| `passes` | Nombre de passages par étape contrôlée. `2`/`4` = fixe. `ramp_*` : le nombre de passages augmente à mesure que l’échantillonnage approche de la fin (davantage de lissage là où les coutures sont les plus visibles) (par défaut : `"2"`). | COMBO | Oui | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `blend` | `average` : moyenne à poids égaux. `window` : pondération par fenêtre de Hann qui privilégie chaque passage loin de ses propres frontières de patch. `median` : médiane par pixel, rejette les passages aberrants dus au rebouclage (wraparound) (par défaut : `"average"`). | COMBO | Oui | `"average"`<br>`"window"`<br>`"median"` |
| `strength` | Interpolation entre la prédiction sur la grille naturelle (0) et le résultat moyenné (1) (par défaut : 1.0). | FLOAT | Oui | 0.0 to 1.0 (pas : 0.01) |

**Remarques sur les contraintes :**

- L’effet de lissage n’est pas appliqué si `strength` vaut 0.0 ou moins, ou si `end_percent` est inférieur ou égal à `start_percent` ; dans ces cas, le nœud renvoie le modèle inchangé.
- Les options progressives de `passes` (`ramp_2_4`, `ramp_2_4_8`) augmentent le nombre de passages à mesure que l’échantillonnage progresse vers `end_percent` dans la plage contrôlée ; elles ne sont donc pertinentes que lorsque `start_percent` et `end_percent` définissent une plage non vide.
- Le résultat moyenné est réinjecté dans la sortie du modèle uniquement loin des bords de l’image : un masque conserve la prédiction d’origine dans la bande de 32 pixels le long de chaque bord (avec un fondu de 4 pixels), évitant ainsi la contamination par rebouclage (wraparound) causée par les passages décalés.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l’enveloppe de lissage des coutures de patch appliquée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/fr.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
