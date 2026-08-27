# Bria Video Remplacer l'arrière-plan

Ce nœud remplace l'arrière-plan d'une vidéo par une image ou une vidéo fournie via l'API de Bria. La sortie conserve la résolution et la fréquence d'images de la vidéo de premier plan ; un arrière-plan avec un format d'image différent est étiré pour s'adapter, donc des formats d'image correspondants produisent des résultats sans distorsion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéo` | Vidéo de premier plan dont l'arrière-plan est remplacé. | VIDEO | Oui | - |
| `image d'arrière-plan` | Image d'arrière-plan à composer derrière le premier plan. Fournissez soit une image d'arrière-plan, soit une vidéo d'arrière-plan, pas les deux. | IMAGE | Non | - |
| `vidéo d'arrière-plan` | Vidéo d'arrière-plan à composer derrière le premier plan. Fournissez soit une image d'arrière-plan, soit une vidéo d'arrière-plan, pas les deux. | VIDEO | Non | - |
| `graine` | La graine (seed) contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (défaut : 0) | INT | Oui | 0 à 2147483647 |

**Remarque :** Vous devez fournir exactement un élément parmi `background_image` ou `background_video` — pas les deux et pas aucun des deux. La vidéo de premier plan et la vidéo d'arrière-plan (si utilisée) doivent chacune durer 60 secondes ou moins. Lorsque `background_image` est utilisé, son canal alpha est supprimé avant le traitement.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo résultante avec l'arrière-plan remplacé, encodée en MP4 (H.264). | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/fr.md)

---
**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`
