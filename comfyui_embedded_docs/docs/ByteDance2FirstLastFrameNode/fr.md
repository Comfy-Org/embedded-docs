> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/fr.md)

Ce nœud utilise le modèle Seedance 2.0 de ByteDance pour générer une vidéo. Il crée la vidéo à partir d'une description textuelle et d'une image de première frame obligatoire. Vous pouvez optionnellement fournir une image de dernière frame pour guider la fin de la séquence vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | Le modèle à utiliser pour la génération vidéo. Seedance 2.0 est pour une qualité maximale, tandis que Seedance 2.0 Fast est optimisé pour la vitesse. La sélection d'un modèle révélera des entrées supplémentaires pour `prompt`, `resolution`, `ratio`, `duration`, et `generate_audio`. |
| `first_frame` | IMAGE | Non | - | L'image à utiliser comme première frame de la vidéo. |
| `last_frame` | IMAGE | Non | - | L'image à utiliser comme dernière frame de la vidéo. |
| `first_frame_asset_id` | STRING | Non | - | Un asset_id Seedance à utiliser comme première frame. Ceci ne peut pas être utilisé en même temps que l'entrée d'image `first_frame`. La valeur par défaut est une chaîne vide. |
| `last_frame_asset_id` | STRING | Non | - | Un asset_id Seedance à utiliser comme dernière frame. Ceci ne peut pas être utilisé en même temps que l'entrée d'image `last_frame`. La valeur par défaut est une chaîne vide. |
| `seed` | INT | Non | 0 à 2147483647 | Une valeur de seed. Changer cette seed forcera le nœud à se ré-exécuter, mais les résultats ne sont pas déterministes. La valeur par défaut est 0. |
| `watermark` | BOOLEAN | Non | - | Indique s'il faut ajouter un filigrane à la vidéo générée. La valeur par défaut est Faux. |

**Contraintes des paramètres :**
*   Vous devez fournir **soit** une image `first_frame` **soit** un `first_frame_asset_id`. Fournir les deux provoquera une erreur.
*   Vous ne pouvez pas fournir à la fois une image `last_frame` et un `last_frame_asset_id` pour la même frame.
*   L'entrée `model` est un combo dynamique. Après avoir sélectionné un modèle, vous devez également remplir le champ `prompt` révélé (une description textuelle) et configurer les autres paramètres révélés (`resolution`, `ratio`, `duration`, `generate_audio`).

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée. |