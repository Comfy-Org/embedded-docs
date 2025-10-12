> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftControls/fr.md)

Crée des contrôles Recraft pour personnaliser la génération Recraft. Ce nœud vous permet de configurer les paramètres de couleur qui seront utilisés pendant le processus de génération d'image Recraft.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `couleurs` | COLOR | Non | - | Paramètres de couleur pour les éléments principaux |
| `couleur_de_fond` | COLOR | Non | - | Paramètre de couleur d'arrière-plan |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `recraft_controls` | CONTROLS | Les contrôles Recraft configurés contenant les paramètres de couleur |
