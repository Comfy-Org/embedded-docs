# Recraft Remove Background

Ce nœud supprime l'arrière-plan des images à l'aide du service API Recraft. Il traite chaque image du lot d'entrée et renvoie à la fois les images traitées avec des arrière-plans transparents et les masques alpha correspondants qui indiquent les zones d'arrière-plan supprimées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Image(s) d'entrée à traiter pour la suppression d'arrière-plan | IMAGE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | Images traitées avec des arrière-plans transparents | IMAGE |
| `mask` | Masques de canal alpha indiquant les zones d'arrière-plan supprimées | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/fr.md)

---
**Source fingerprint (SHA-256):** `9e3f1a0471da3afda6b8de26de3b7e78c1070c49ab49e4fc8b6b79bb10ff77de`
