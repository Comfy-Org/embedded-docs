# Bria Video Green Screen

Ce nœud remplace l'arrière-plan d'une vidéo par un écran de fond vert unicolore à l'aide de l'API Bria. Il traite la vidéo d'entrée et renvoie une nouvelle vidéo dont l'arrière-plan d'origine a été supprimé et remplacé par une couleur de fond vert ou bleu uniforme.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéo` | La vidéo d'entrée à traiter | VIDEO | Oui | Fichier vidéo |
| `teinte verte` | Teinte de fond vert unicolore appliquée derrière le premier plan : broadcast_green (#00B140), chroma_green (#00FF00) ou blue_screen (#0000FF) | STRING | Oui | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `graine` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine (valeur par défaut : 0) | INT | Oui | 0 à 2147483647 |

**Remarque :** La vidéo d'entrée ne doit pas dépasser 60 secondes de durée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `vidéo` | La vidéo traitée dont l'arrière-plan d'origine a été remplacé par la teinte de fond vert unicolore sélectionnée | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/fr.md)

---
**Source fingerprint (SHA-256):** `663b41bf51bd8d871a59e756f226e4bf6244bb616ebcd2e8ccfa426137f2a05b`
