> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/fr.md)

Le nœud ModelSamplingAuraFlow applique une configuration d'échantillonnage spécialisée aux modèles de diffusion, spécifiquement conçue pour les architectures de modèles AuraFlow. Il modifie le comportement d'échantillonnage du modèle en appliquant un paramètre de décalage qui ajuste la distribution d'échantillonnage. Ce nœud hérite du framework d'échantillonnage de modèle SD3 et offre un contrôle fin sur le processus d'échantillonnage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle de diffusion auquel appliquer la configuration d'échantillonnage AuraFlow |
| `shift` | FLOAT | Oui | 0.0 - 100.0 | La valeur de décalage à appliquer à la distribution d'échantillonnage (par défaut : 1.73) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec la configuration d'échantillonnage AuraFlow appliquée |