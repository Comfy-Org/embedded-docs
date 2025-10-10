> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV3/fr.md)

Le nœud Ideogram V3 génère des images en utilisant le modèle Ideogram V3. Il prend en charge à la fois la génération d'images régulières à partir de prompts texte et l'édition d'images lorsqu'une image et un masque sont fournis. Le nœud offre divers contrôles pour le format d'image, la résolution, la vitesse de génération et des images de référence de caractères optionnelles.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Prompt pour la génération ou l'édition d'image (par défaut : vide) |
| `image` | IMAGE | Non | - | Image de référence optionnelle pour l'édition d'image |
| `mask` | MASK | Non | - | Masque optionnel pour l'inpainting (les zones blanches seront remplacées) |
| `aspect_ratio` | COMBO | Non | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | Le format d'image pour la génération. Ignoré si la résolution n'est pas définie sur Auto (par défaut : "1:1") |
| `resolution` | COMBO | Non | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | La résolution pour la génération d'image. Si elle n'est pas définie sur Auto, cela remplace le paramètre aspect_ratio (par défaut : "Auto") |
| `magic_prompt_option` | COMBO | Non | "AUTO"<br>"ON"<br>"OFF" | Détermine si MagicPrompt doit être utilisé dans la génération (par défaut : "AUTO") |
| `seed` | INT | Non | 0-2147483647 | Graine aléatoire pour la génération (par défaut : 0) |
| `num_images` | INT | Non | 1-8 | Nombre d'images à générer (par défaut : 1) |
| `rendering_speed` | COMBO | Non | "DEFAULT"<br>"TURBO"<br>"QUALITY" | Contrôle le compromis entre la vitesse de génération et la qualité (par défaut : "DEFAULT") |
| `character_image` | IMAGE | Non | - | Image à utiliser comme référence de caractère |
| `character_mask` | MASK | Non | - | Masque optionnel pour l'image de référence de caractère |

**Contraintes des paramètres :**
- Lorsque `image` et `mask` sont tous deux fournis, le nœud passe en mode édition
- Si seulement l'un des deux paramètres `image` ou `mask` est fourni, une erreur se produira
- `character_mask` nécessite que `character_image` soit présent
- Le paramètre `aspect_ratio` est ignoré lorsque `resolution` n'est pas défini sur "Auto"
- Les zones blanches du masque seront remplacées pendant l'inpainting
- Le masque de caractère et l'image de caractère doivent avoir la même taille

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | L'image ou les images générées ou éditées |