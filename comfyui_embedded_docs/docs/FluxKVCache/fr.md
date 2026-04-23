> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/fr.md)

Le nœud Flux KV Cache applique une optimisation de cache clé-valeur (KV) aux modèles de la famille Flux. Cette optimisation est spécifiquement conçue pour améliorer les performances lors de l'utilisation d'images de référence en mettant en cache certains calculs, ce qui peut accélérer le processus de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | | Le modèle sur lequel appliquer le cache KV. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec le cache KV activé. |