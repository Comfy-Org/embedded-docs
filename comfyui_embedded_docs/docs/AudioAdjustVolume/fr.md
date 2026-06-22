# Ajuster le Volume Audio

Voici la traduction en français de la documentation du nœud AudioAdjustVolume :

Le nœud AudioAdjustVolume modifie le volume sonore d'un fichier audio en appliquant des ajustements de gain en décibels (dB). Il prend une entrée audio et applique un facteur de gain basé sur le niveau de volume spécifié, où les valeurs positives augmentent le volume et les valeurs négatives le diminuent. Le nœud renvoie l'audio modifié avec la même fréquence d'échantillonnage que l'original.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | L'entrée audio à traiter | AUDIO | Oui | - |
| `volume` | Ajustement du volume en décibels (dB). 0 = aucun changement, +6 = double, -6 = moitié, etc. (valeur par défaut : 1) | INT | Oui | -100 à 100 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | L'audio traité avec le niveau de volume ajusté | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/fr.md)

---
**Source fingerprint (SHA-256):** `0436765680671551239f7a89b575cdfb22590fbe662bdfe5da01bd1cd5c496ed`
