> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/fr.md)

Le nœud Kling Dual Character Video Effect crée des vidéos avec des effets spéciaux basés sur la scène sélectionnée. Il prend deux images et positionne la première image sur le côté gauche et la deuxième image sur le côté droit de la vidéo composite. Différents effets visuels sont appliqués en fonction de la scène d'effet choisie.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image_left` | IMAGE | Oui | - | Image côté gauche |
| `image_right` | IMAGE | Oui | - | Image côté droit |
| `effect_scene` | COMBO | Oui | Plusieurs options disponibles | Le type de scène d'effet spécial à appliquer à la génération de vidéo |
| `model_name` | COMBO | Non | Plusieurs options disponibles | Le modèle à utiliser pour les effets de personnage (par défaut : "kling-v1") |
| `mode` | COMBO | Non | Plusieurs options disponibles | Le mode de génération de vidéo (par défaut : "std") |
| `duration` | COMBO | Oui | Plusieurs options disponibles | La durée de la vidéo générée |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `duration` | VIDEO | La vidéo générée avec des effets à double personnage |
| `duration` | STRING | Les informations de durée de la vidéo générée |
