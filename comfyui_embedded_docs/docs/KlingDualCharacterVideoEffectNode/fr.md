# Effets vidéo à deux personnages Kling

Voici la traduction en français de la documentation du nœud ComfyUI **Kling Dual Character Video Effect Node** :

Le nœud d'effet vidéo à double personnage Kling crée des vidéos avec des effets spéciaux basés sur la scène sélectionnée. Il prend deux images et positionne la première image sur le côté gauche et la seconde image sur le côté droit de la vidéo composite. Différents effets visuels sont appliqués en fonction de la scène d'effet choisie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image_left` | Image du côté gauche | IMAGE | Oui | - |
| `image_right` | Image du côté droit | IMAGE | Oui | - |
| `effect_scene` | Le type de scène d'effet spécial à appliquer à la génération vidéo | COMBO | Oui | `"chat"`<br>`"dance"`<br>`"hug"`<br>`"kill"`<br>`"kiss"`<br>`"pat"`<br>`"punch"`<br>`"shrug"`<br>`"slap"`<br>`"tickle"` |
| `model_name` | Le modèle à utiliser pour les effets de personnage (par défaut : "kling-v1") | COMBO | Non | `"kling-v1"`<br>`"kling-v1-5"`<br>`"kling-v1-6"` |
| `mode` | Le mode de génération vidéo (par défaut : "std") | COMBO | Non | `"std"`<br>`"pro"` |
| `duration` | La durée de la vidéo générée en secondes | COMBO | Oui | `"5"`<br>`"10"` |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `duration` | La vidéo générée avec les effets à double personnage | VIDEO |
| `duration` | Les informations de durée de la vidéo générée | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/fr.md)

---
**Source fingerprint (SHA-256):** `4ee0c3cd834e1c70e41b40b66ac98d15a8b88993e7dc9d9df9fb4fadb868f079`
