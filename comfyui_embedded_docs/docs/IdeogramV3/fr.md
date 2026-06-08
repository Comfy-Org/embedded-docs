Voici la traduction en français de la documentation du nœud Ideogram V3 :

Le nœud Ideogram V3 génère des images à l'aide du modèle Ideogram V3. Il prend en charge à la fois la génération d'images standard à partir de descriptions textuelles et l'édition d'images lorsqu'une image et un masque sont fournis. Le nœud offre divers contrôles pour le rapport hauteur/largeur, la résolution, la vitesse de génération et les images de référence de personnage optionnelles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Description textuelle pour la génération ou l'édition d'image (par défaut : vide) | STRING | Oui | - |
| `image` | Image de référence optionnelle pour l'édition d'image | IMAGE | Non | - |
| `mask` | Masque optionnel pour l'incrustation (les zones blanches seront remplacées) | MASK | Non | - |
| `aspect_ratio` | Le rapport hauteur/largeur pour la génération d'image. Ignoré si la résolution n'est pas définie sur Auto (par défaut : "1:1") | COMBO | Non | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" |
| `resolution` | La résolution pour la génération d'image. Si elle n'est pas définie sur Auto, elle remplace le paramètre aspect_ratio (par défaut : "Auto") | COMBO | Non | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `magic_prompt_option` | Détermine si MagicPrompt doit être utilisé lors de la génération (par défaut : "AUTO") | COMBO | Non | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Graine aléatoire pour la génération (par défaut : 0) | INT | Non | 0-2147483647 |
| `num_images` | Nombre d'images à générer (par défaut : 1) | INT | Non | 1-8 |
| `rendering_speed` | Contrôle le compromis entre la vitesse de génération et la qualité (par défaut : "DEFAULT") | COMBO | Non | "DEFAULT"<br>"TURBO"<br>"QUALITY" |
| `image_du_personnage` | Image à utiliser comme référence de personnage | IMAGE | Non | - |
| `masque_du_personnage` | Masque optionnel pour l'image de référence de personnage | MASK | Non | - |

**Contraintes des paramètres :**

- Lorsque `image` et `mask` sont tous deux fournis, le nœud passe en mode édition
- Si un seul des deux paramètres `image` ou `mask` est fourni, une erreur se produira
- `character_mask` nécessite que `character_image` soit présent
- Le paramètre `aspect_ratio` est ignoré lorsque `resolution` n'est pas défini sur "Auto"
- Les zones blanches du masque seront remplacées lors de l'incrustation
- Le masque de personnage et l'image de personnage doivent avoir la même taille

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La ou les images générées ou éditées | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV3/fr.md)

---
**Source fingerprint (SHA-256):** `0d0058cc8483c453100d8d9dfcb9a31ae5e686f38ced77ed7e472cd083c3464b`
