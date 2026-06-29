# LumaRay32KeyframesToVideoNode

Ce nœud génère une vidéo interpolant une séquence d'images guides, chacune ancrée à une position spécifique sur la timeline, en utilisant Luma Ray 3.2. Construisez la séquence d'images clés à l'aide des nœuds Luma Ray 3.2 Keyframe, en connectant au moins 2 images clés pour définir l'animation.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Texte d'invite pour la génération vidéo. | STRING | Oui | 1 à 6000 caractères |
| `résolution` | La résolution de sortie de la vidéo générée (par défaut : "720p"). | COMBO | Oui | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `durée` | La durée de la vidéo générée (par défaut : "5s"). | COMBO | Oui | `"5s"`<br>`"10s"` |
| `seed` | Graine pour la génération de nombres aléatoires afin de contrôler la reproductibilité. | INT | Oui | 0 à 4294967295 |
| `images clés` | Séquence d'images clés provenant des nœuds Luma Ray 3.2 Keyframe (au moins 2). | LUMA_RAY32_KEYFRAME | Oui | 2 à 64 images clés |

**Remarque :** La séquence d'images clés doit contenir au moins 2 images clés et au maximum 64 images clés. Chaque image clé doit avoir une position distincte sur la timeline. Les positions des images clés sont résolues en indices d'images de sortie en fonction de la durée sélectionnée (120 images pour 5s, 240 images pour 10s). Les positions des images clés en mode secondes ne doivent pas dépasser la durée totale de la vidéo.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `identifiant_génération` | La vidéo générée en sortie. | VIDEO |
| `generation_id` | L'identifiant unique de la demande de génération. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframesToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `28099e5990942860a20e23cfd5c71a36b23a6264b44097ca617f8bdd06e7857a`
