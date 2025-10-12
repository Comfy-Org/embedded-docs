> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/fr.md)

Le nœud ChromaRadianceOptions vous permet de configurer les paramètres avancés pour le modèle Chroma Radiance. Il encapsule un modèle existant et applique des options spécifiques pendant le processus de débruitage basé sur les valeurs sigma, permettant un contrôle précis de la taille des tuiles NeRF et d'autres paramètres liés à la radiance.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Requis | - | - | Le modèle auquel appliquer les options Chroma Radiance |
| `preserve_wrapper` | BOOLEAN | Optionnel | True | - | Lorsqu'activé, délègue à un wrapper de fonction de modèle existant s'il existe. Doit généralement rester activé. |
| `start_sigma` | FLOAT | Optionnel | 1.0 | 0.0 - 1.0 | Premier sigma pour lequel ces options seront actives. |
| `end_sigma` | FLOAT | Optionnel | 0.0 | 0.0 - 1.0 | Dernier sigma pour lequel ces options seront actives. |
| `nerf_tile_size` | INT | Optionnel | -1 | -1 et plus | Permet de remplacer la taille de tuile NeRF par défaut. -1 signifie utiliser la valeur par défaut (32). 0 signifie utiliser le mode sans tuilage (peut nécessiter beaucoup de VRAM). |

**Note :** Les options Chroma Radiance ne prennent effet que lorsque la valeur sigma actuelle se situe entre `end_sigma` et `start_sigma` (inclus). Le paramètre `nerf_tile_size` n'est appliqué que lorsqu'il est défini sur 0 ou des valeurs supérieures.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec les options Chroma Radiance appliquées |
