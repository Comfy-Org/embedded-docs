> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/fr.md)

Le nœud AudioAdjustVolume modifie l'intensité sonore d'un audio en appliquant des ajustements de volume en décibels. Il prend une entrée audio et applique un facteur de gain basé sur le niveau de volume spécifié, où les valeurs positives augmentent le volume et les valeurs négatives le diminuent. Le nœud retourne l'audio modifié avec la même fréquence d'échantillonnage que l'original.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `audio` | AUDIO | requis | - | - | L'entrée audio à traiter |
| `volume` | INT | requis | 1.0 | -100 à 100 | Ajustement du volume en décibels (dB). 0 = pas de changement, +6 = double, -6 = moitié, etc |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `audio` | AUDIO | L'audio traité avec le niveau de volume ajusté |