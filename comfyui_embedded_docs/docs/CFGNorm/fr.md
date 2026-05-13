> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/fr.md)

Le nœud CFGNorm applique une technique de normalisation au processus de guidage sans classifieur (CFG) dans les modèles de diffusion. Il ajuste l'échelle de la prédiction débruitée en comparant les normes des sorties conditionnelles et inconditionnelles, puis applique un multiplicateur d'intensité pour contrôler l'effet. Cela permet de stabiliser le processus de génération en empêchant les valeurs extrêmes dans la mise à l'échelle du guidage.

## Entrées

| Paramètre | Type de données | Type d'entrée | Valeur par défaut | Plage | Description |
|-----------|-----------------|---------------|-------------------|-------|-------------|
| `model` | MODEL | requis | - | - | Le modèle de diffusion auquel appliquer la normalisation CFG |
| `strength` | FLOAT | requis | 1.0 | 0.0 - 100.0 | Contrôle l'intensité de l'effet de normalisation appliqué à la mise à l'échelle CFG |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `patched_model` | MODEL | Renvoie le modèle modifié avec la normalisation CFG appliquée à son processus d'échantillonnage |

---
**Source fingerprint (SHA-256):** `af9e5f965500b959ff46f781e9329524fc0a4b94af2ce6d74116fe27b0e9005e`
