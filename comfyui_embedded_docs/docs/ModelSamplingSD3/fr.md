> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/fr.md)

Le nœud ModelSamplingSD3 applique les paramètres d'échantillonnage de Stable Diffusion 3 à un modèle. Il modifie le comportement d'échantillonnage du modèle en ajustant le paramètre de décalage, qui contrôle les caractéristiques de la distribution d'échantillonnage. Le nœud crée une copie modifiée du modèle d'entrée avec la configuration d'échantillonnage spécifiée appliquée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle d'entrée auquel appliquer les paramètres d'échantillonnage SD3 |
| `décalage` | FLOAT | Oui | 0.0 - 100.0 | Contrôle le paramètre de décalage d'échantillonnage (par défaut : 3.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle modifié avec les paramètres d'échantillonnage SD3 appliqués |
