> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/fr.md)

Ce nœud définit le latent de référence pour un modèle d'édition. Il prend des données de conditionnement et une entrée latente optionnelle, puis modifie le conditionnement pour inclure les informations du latent de référence. Si le modèle le supporte, vous pouvez chaîner plusieurs nœuds ReferenceLatent pour définir plusieurs images de référence.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Oui | - | Les données de conditionnement à modifier avec les informations du latent de référence |
| `latent` | LATENT | Non | - | Données latentes optionnelles à utiliser comme référence pour le modèle d'édition |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | CONDITIONING | Les données de conditionnement modifiées contenant les informations du latent de référence |