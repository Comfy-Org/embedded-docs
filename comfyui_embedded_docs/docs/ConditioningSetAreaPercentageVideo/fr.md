# Pourcentage de la zone de conditionnement vidéo

Le nœud `ConditioningSetAreaPercentageVideo` modifie les données de conditionnement en définissant une zone spécifique et une région temporelle pour la génération vidéo. Il utilise des valeurs en pourcentage relatives aux dimensions globales pour définir la position, la taille et la durée de la zone où le conditionnement est appliqué. Cela est utile pour concentrer la génération sur des parties spécifiques d'une séquence vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `conditionnement` | Les données de conditionnement à modifier | CONDITIONING | Oui | - |
| `largeur` | La largeur de la zone en pourcentage de la largeur totale (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas de 0.01) |
| `hauteur` | La hauteur de la zone en pourcentage de la hauteur totale (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas de 0.01) |
| `temporel` | La durée temporelle de la zone en pourcentage de la longueur totale de la vidéo (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas de 0.01) |
| `x` | La position de départ horizontale de la zone en pourcentage (par défaut : 0.0) | FLOAT | Oui | 0.0 - 1.0 (pas de 0.01) |
| `y` | La position de départ verticale de la zone en pourcentage (par défaut : 0.0) | FLOAT | Oui | 0.0 - 1.0 (pas de 0.01) |
| `z` | La position de départ temporelle de la zone en pourcentage de la timeline vidéo (par défaut : 0.0) | FLOAT | Oui | 0.0 - 1.0 (pas de 0.01) |
| `force` | Le multiplicateur de force appliqué au conditionnement dans la zone définie (par défaut : 1.0) | FLOAT | Oui | 0.0 - 10.0 (pas de 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `conditioning` | Les données de conditionnement modifiées avec la zone spécifiée et les réglages de force appliqués | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/fr.md)

---
**Source fingerprint (SHA-256):** `9c5ddae6a2b1da5907fb52ef625eefb12b0b228fd3bd52c3033b5c4226d76150`
