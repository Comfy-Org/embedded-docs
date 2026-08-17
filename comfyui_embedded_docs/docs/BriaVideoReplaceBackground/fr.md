# Bria Video Remplacer l'arrière-plan

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Vidéo de premier plan dont l’arrière-plan est remplacé. | VIDEO | Oui | - |
| `background_image` | Image d’arrière-plan à composer derrière le premier plan. Fournissez soit une image d’arrière-plan, soit une vidéo d’arrière-plan, pas les deux. | IMAGE | Non | - |
| `background_video` | Vidéo d’arrière-plan à composer derrière le premier plan. Fournissez soit une image d’arrière-plan, soit une vidéo d’arrière-plan, pas les deux. | VIDEO | Non | - |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) | INT | Oui | 0 to 2147483647 |

**Remarque :** Vous devez fournir exactement l’un des deux paramètres `background_image` ou `background_video` — pas les deux, et pas aucun. Les vidéos de premier plan et d’arrière-plan doivent durer 60 secondes ou moins. Si une image d’arrière-plan est fournie, son canal alpha (transparence) est supprimé avant le téléversement.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo résultante avec l’arrière-plan remplacé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/fr.md)

---
**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`
