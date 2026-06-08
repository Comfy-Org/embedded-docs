Le nœud CFGZeroStar applique une technique de mise à l'échelle spécialisée du guidage aux modèles de diffusion. Il modifie le processus de guidage sans classifieur en calculant un facteur d'échelle optimisé basé sur la différence entre les prédictions conditionnelles et inconditionnelles. Cette approche ajuste la sortie finale pour offrir un contrôle accru sur le processus de génération tout en maintenant la stabilité du modèle.

## Entrées

| Paramètre | Description | Type de données | Type d'entrée | Défaut | Plage |
| --- | --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion à modifier avec la technique de mise à l'échelle du guidage CFGZeroStar | MODEL | requis | - | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `patched_model` | Le modèle modifié avec la mise à l'échelle du guidage CFGZeroStar appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/fr.md)

---
**Source fingerprint (SHA-256):** `1f5fcd1377c64609e28d85e453aaaa0bcc8f3ac322b7b7240f34f71aa113562a`
