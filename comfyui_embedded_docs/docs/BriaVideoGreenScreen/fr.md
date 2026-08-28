# Bria Video Green Screen

Ce nœud remplace l'arrière-plan d'une vidéo par un écran chroma-key unicolore à l'aide de l'API Bria. Il traite la vidéo d'entrée et renvoie une nouvelle vidéo où l'arrière-plan d'origine a été supprimé et remplacé par une couleur d'écran verte ou bleue uniforme.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `vidéo` | La vidéo d'entrée à traiter | VIDEO | Oui | Fichier vidéo |
| `teinte verte` | Teinte chroma-key unicolore appliquée derrière le premier plan : broadcast_green (#00B140), chroma_green (#00FF00) ou blue_screen (#0000FF). | COMBO | Oui | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `graine` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (défaut : 0) | INT | Oui | 0 à 2147483647 |

**Remarque :** La vidéo d'entrée ne doit pas dépasser 60 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `video` | La vidéo traitée (MP4, H.264) avec l'arrière-plan d'origine remplacé par la teinte chroma-key sélectionnée | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/fr.md)

---
**Source fingerprint (SHA-256):** `70d2951d0adbbe7492b2bc97d04be6591b65f040ca4b414754ad6365c5db45cf`
