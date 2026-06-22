# ByteDance Seedance 2.0 Première-Dernière-Image vers Vidéo

Ce nœud utilise le modèle Seedance 2.0 de ByteDance pour générer une vidéo. Il crée la vidéo à partir d'une invite textuelle et d'une image de première image obligatoire. Vous pouvez éventuellement fournir une image de dernière image pour guider la fin de la séquence vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à utiliser pour la génération vidéo. Seedance 2.0 est destiné à une qualité maximale, tandis que Seedance 2.0 Fast est optimisé pour la vitesse. La sélection d'un modèle révèlera des entrées supplémentaires pour `prompt`, `resolution`, `ratio`, `duration` et `generate_audio`. | COMBO | Oui | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` |
| `première image` | L'image à utiliser comme première image de la vidéo. | IMAGE | Non | - |
| `dernière image` | L'image à utiliser comme dernière image de la vidéo. | IMAGE | Non | - |
| `first_frame_asset_id` | Un asset_id Seedance à utiliser comme première image. Ne peut pas être utilisé en même temps que l'entrée d'image `première image`. La valeur par défaut est une chaîne vide. | STRING | Non | - |
| `last_frame_asset_id` | Un asset_id Seedance à utiliser comme dernière image. Ne peut pas être utilisé en même temps que l'entrée d'image `dernière image`. La valeur par défaut est une chaîne vide. | STRING | Non | - |
| `seed` | Une valeur de graine. La modification de cette graine entraînera la réexécution du nœud, mais les résultats sont non déterministes. La valeur par défaut est 0. | INT | Non | 0 à 2147483647 |
| `filigrane` | Indique s'il faut ajouter un filigrane à la vidéo générée. La valeur par défaut est Faux. | BOOLEAN | Non | - |

**Contraintes des paramètres :**
*   Vous devez fournir **soit** une image `first_frame` **soit** un `first_frame_asset_id`. Fournir les deux provoquera une erreur.
*   Vous ne pouvez pas fournir à la fois une image `last_frame` et un `last_frame_asset_id` pour la même image.
*   L'entrée `model` est une liste déroulante dynamique. Après avoir sélectionné un modèle, vous devez également remplir le champ `prompt` révélé (une description textuelle) et configurer les autres paramètres révélés (`resolution`, `ratio`, `duration`, `generate_audio`).

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `2c9c1fe8fddd0c3e1c356d2b93a06a07f83db8f7a0380e94629a91ce1ff1e29a`
