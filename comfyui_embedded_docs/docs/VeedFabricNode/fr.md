# VEED Fabric 1.0

Transformez une image fixe et une piste vocale en une vidéo parlante avec synchronisation labiale grâce à VEED Fabric. Cela fonctionne avec des photos, des illustrations et des mascottes tant que le visage est clairement visible ; la vidéo conserve le rapport d'aspect de l'image et sa durée correspond à celle de l'audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle à utiliser. La sélection d'un modèle révèle les paramètres qui lui sont propres : `image`, `audio` et `resolution`. | DYNAMIC_COMBO | Oui | `"fabric-1.0"` |
| `image` | Image dont le visage est clairement visible. La vidéo conserve son rapport d'aspect. | IMAGE | Oui | - |
| `audio` | Parole à synchroniser labialement, jusqu'à 300 secondes. Détermine la durée de la vidéo. | AUDIO | Oui | Jusqu'à 300 secondes |
| `resolution` | Classe de taille de sortie : environ 0,4 mégapixel à `"480p"` (864x480 en 16:9) et 0,9 mégapixel à `"720p"` (1312x736 en 16:9). (par défaut : `"720p"`) | COMBO | Oui | `"480p"`<br>`"720p"` |

Le nœud s'arrête avec une erreur lorsque la piste vocale dépasse 300 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `VIDEO` | La vidéo parlante : l'image d'entrée animée pour correspondre à la piste vocale. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedFabricNode/fr.md)

---
**Source fingerprint (SHA-256):** `69cabfa5f03885ce770e8502419305dacee49d7e89a748f31abe3775d682a33a`
