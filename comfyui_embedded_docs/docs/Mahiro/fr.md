> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/fr.md)

Le nœud Mahiro modifie la fonction de guidage pour se concentrer davantage sur la direction du prompt positif plutôt que sur la différence entre les prompts positif et négatif. Il crée un modèle modifié qui applique une approche personnalisée de mise à l'échelle du guidage utilisant la similarité cosinus entre les sorties débruitées normalisées conditionnelles et non conditionnelles. Ce nœud expérimental aide à orienter plus fortement la génération vers la direction souhaitée du prompt positif.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | | Le modèle à modifier avec la fonction de guidage adaptée |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Le modèle modifié avec la fonction de guidage Mahiro appliquée |