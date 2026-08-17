# Bria Video Green Screen

Ce nœud remplace l'arrière-plan d'une vidéo par un écran unicolore de chroma-key à l'aide de l'API Bria. Il traite la vidéo d'entrée et renvoie une nouvelle vidéo dont l'arrière-plan d'origine a été supprimé et remplacé par une couleur d'écran vert ou bleu uniforme.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `video` | La vidéo d'entrée à traiter. | VIDEO | Oui | Fichier vidéo |
| `green_shade` | Teinte unie de chroma-key appliquée derrière le premier plan : broadcast_green (#00B140), chroma_green (#00FF00) ou blue_screen (#0000FF). | COMBO | Oui | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | Le paramètre `seed` contrôle si le nœud doit s'exécuter à nouveau ; les résultats sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 2147483647 |

**Remarque :** La vidéo d'entrée ne doit pas dépasser 60 secondes de durée.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `video` | La vidéo traitée avec l'arrière-plan d'origine remplacé par la teinte chroma-key sélectionnée, renvoyée sous forme de vidéo MP4 (H.264). | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/fr.md)

---
**Source fingerprint (SHA-256):** `70d2951d0adbbe7492b2bc97d04be6591b65f040ca4b414754ad6365c5db45cf`
