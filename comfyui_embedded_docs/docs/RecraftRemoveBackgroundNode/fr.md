> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/fr.md)

Ce nœud supprime l'arrière-plan des images à l'aide du service API Recraft. Il traite chaque image du lot d'entrée et renvoie à la fois les images traitées avec des arrière-plans transparents et les masques alpha correspondants qui indiquent les zones d'arrière-plan supprimées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | Image(s) d'entrée à traiter pour la suppression d'arrière-plan |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `image` | IMAGE | Images traitées avec des arrière-plans transparents |
| `mask` | MASK | Masques de canal alpha indiquant les zones d'arrière-plan supprimées |

---
**Source fingerprint (SHA-256):** `9e3f1a0471da3afda6b8de26de3b7e78c1070c49ab49e4fc8b6b79bb10ff77de`
