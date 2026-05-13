> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/fr.md)

Voici la traduction en français de la documentation du nœud APG :

Le nœud APG (Guidage Projectif Adaptatif) modifie le processus d'échantillonnage en ajustant la manière dont le guidage est appliqué pendant la diffusion. Il sépare le vecteur de guidage en composantes parallèle et orthogonale par rapport à la sortie conditionnelle, permettant une génération d'image plus contrôlée. Le nœud fournit des paramètres pour mettre à l'échelle le guidage, normaliser sa magnitude et appliquer un momentum pour des transitions plus fluides entre les étapes de diffusion.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle de diffusion auquel appliquer le guidage projectif adaptatif |
| `eta` | FLOAT | Oui | -10.0 à 10.0 | Contrôle l'échelle du vecteur de guidage parallèle. Comportement CFG par défaut à un réglage de 1 (par défaut : 1.0). |
| `norm_threshold` | FLOAT | Oui | 0.0 à 50.0 | Normalise le vecteur de guidage à cette valeur, la normalisation est désactivée à un réglage de 0 (par défaut : 5.0). |
| `momentum` | FLOAT | Oui | -5.0 à 1.0 | Contrôle une moyenne mobile du guidage pendant la diffusion, désactivé à un réglage de 0 (par défaut : 0.0). |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `model` | MODEL | Renvoie le modèle modifié avec le guidage projectif adaptatif appliqué à son processus d'échantillonnage |

---
**Source fingerprint (SHA-256):** `89e2486bf08f750f82608db93c389f0b25ce0be766f62faa8704d19bd7e41654`
