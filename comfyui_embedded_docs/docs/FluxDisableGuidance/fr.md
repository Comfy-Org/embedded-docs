> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/fr.md)

Ce nœud désactive complètement la fonctionnalité d'intégration de guidage pour Flux et les modèles similaires. Il prend des données de conditionnement en entrée et supprime le composant de guidage en le définissant sur None, désactivant ainsi efficacement le conditionnement basé sur le guidage pour le processus de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `conditionnement` | CONDITIONING | Oui | - | Les données de conditionnement à traiter et dont il faut supprimer le guidage |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `conditionnement` | CONDITIONING | Les données de conditionnement modifiées avec le guidage désactivé |
