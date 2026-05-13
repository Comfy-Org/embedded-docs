> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI **Kling Dual Character Video Effect Node** :

Le nœud d'effet vidéo à double personnage Kling crée des vidéos avec des effets spéciaux basés sur la scène sélectionnée. Il prend deux images et positionne la première image sur le côté gauche et la seconde image sur le côté droit de la vidéo composite. Différents effets visuels sont appliqués en fonction de la scène d'effet choisie.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image_left` | IMAGE | Oui | - | Image du côté gauche |
| `image_right` | IMAGE | Oui | - | Image du côté droit |
| `effect_scene` | COMBO | Oui | `"chat"`<br>`"dance"`<br>`"hug"`<br>`"kill"`<br>`"kiss"`<br>`"pat"`<br>`"punch"`<br>`"shrug"`<br>`"slap"`<br>`"tickle"` | Le type de scène d'effet spécial à appliquer à la génération vidéo |
| `model_name` | COMBO | Non | `"kling-v1"`<br>`"kling-v1-5"`<br>`"kling-v1-6"` | Le modèle à utiliser pour les effets de personnage (par défaut : "kling-v1") |
| `mode` | COMBO | Non | `"std"`<br>`"pro"` | Le mode de génération vidéo (par défaut : "std") |
| `duration` | COMBO | Oui | `"5"`<br>`"10"` | La durée de la vidéo générée en secondes |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | VIDEO | La vidéo générée avec les effets à double personnage |
| `duration` | STRING | Les informations de durée de la vidéo générée |

---
**Source fingerprint (SHA-256):** `4ee0c3cd834e1c70e41b40b66ac98d15a8b88993e7dc9d9df9fb4fadb868f079`
