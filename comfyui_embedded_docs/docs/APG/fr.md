# Guidance Adaptatif Projeté

Le nœud APG (Adaptive Projected Guidance) modifie le processus d'échantillonnage en ajustant la manière dont le guidage est appliqué pendant la diffusion. Il sépare le vecteur de guidage en composantes parallèles et orthogonales par rapport à la sortie conditionnelle, permettant une génération d'images plus contrôlée. Le nœud fournit des paramètres pour mettre à l'échelle le guidage, normaliser sa norme et appliquer un momentum pour des transitions plus fluides entre les étapes de diffusion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel appliquer le guidage projeté adaptatif | MODEL | Oui | - |
| `eta` | Contrôle l'échelle du vecteur de guidage parallèle. Comportement CFG par défaut pour un réglage de 1 (par défaut : 1.0). | FLOAT | Oui | -10.0 à 10.0 |
| `norm_threshold` | Normalise le vecteur de guidage à cette valeur, la normalisation est désactivée pour un réglage de 0 (par défaut : 5.0). | FLOAT | Oui | 0.0 à 50.0 |
| `momentum` | Contrôle une moyenne mobile du guidage pendant la diffusion, désactivé pour un réglage de 0 (par défaut : 0.0). | FLOAT | Oui | -5.0 à 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Renvoie le modèle modifié avec le guidage projeté adaptatif appliqué à son processus d'échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/fr.md)

---
**Source fingerprint (SHA-256):** `df0c76aee28479d49c4e471e54d1d32082adc6921a6a50b506675144a79e018a`
