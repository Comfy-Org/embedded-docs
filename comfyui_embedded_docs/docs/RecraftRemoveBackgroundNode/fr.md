# Recraft Remove Background

Ce nœud supprime l’arrière-plan des images à l’aide du service API Recraft. Il traite chaque image du lot d’entrée et renvoie à la fois les images traitées avec des arrière-plans transparents et les masques alpha correspondants qui indiquent les zones d’arrière-plan supprimées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image ou les images d’entrée à traiter pour la suppression d’arrière-plan. Chaque image du lot est traitée individuellement. | IMAGE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | Images traitées avec arrière-plans transparents (format RGBA) | IMAGE |
| `mask` | Masques de canal alpha indiquant les zones d’arrière-plan supprimées, au format B,H,W | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/fr.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`
