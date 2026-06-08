# Bria Remplacement d'Arrière-plan Vidéo

Ce nœud remplace l'arrière-plan d'une vidéo par une image ou une vidéo fournie via l'API de Bria. La sortie conserve la résolution et la fréquence d'images de la vidéo de premier plan ; un arrière-plan avec un rapport hauteur/largeur différent est étiré pour s'adapter, donc des rapports hauteur/largeur identiques produisent des résultats sans distorsion.

## Entrées

| Paramètre | Description | Type de Données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Vidéo de premier plan dont l'arrière-plan est remplacé. | VIDEO | Oui | - |
| `background_image` | Image d'arrière-plan à composer derrière le premier plan. Fournissez soit une image d'arrière-plan, soit une vidéo d'arrière-plan, pas les deux. | IMAGE | Non | - |
| `background_video` | Vidéo d'arrière-plan à composer derrière le premier plan. Fournissez soit une image d'arrière-plan, soit une vidéo d'arrière-plan, pas les deux. | VIDEO | Non | - |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (valeur par défaut : 0) | INT | Oui | 0 à 2147483647 |

**Remarque :** Vous devez fournir exactement un élément parmi `background_image` ou `background_video` — pas les deux et pas aucun. La vidéo de premier plan doit durer 60 secondes ou moins.

## Sorties

| Nom de Sortie | Description | Type de Données |
|---------------|-------------|-----------------|
| `video` | La vidéo résultante avec l'arrière-plan remplacé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/fr.md)

---
**Source fingerprint (SHA-256):** `4eb9650e5ca88baf2a91a9309b87936b3d18b88e314a56ab4c73d06a9143c645`
