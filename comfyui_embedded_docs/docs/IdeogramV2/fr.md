> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/fr.md)

Le nœud Ideogram V2 génère des images en utilisant le modèle d'IA Ideogram V2. Il prend des invites textuelles et divers paramètres de génération pour créer des images via un service API. Le nœud prend en charge différents ratios d'aspect, résolutions et options de style pour personnaliser les images générées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite pour la génération d'image (par défaut : chaîne vide) |
| `turbo` | BOOLEAN | Non | - | Active le mode turbo (génération plus rapide, qualité potentiellement inférieure) (par défaut : False) |
| `aspect_ratio` | COMBO | Non | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | Le ratio d'aspect pour la génération d'image. Ignoré si la résolution n'est pas définie sur AUTO. (par défaut : "1:1") |
| `resolution` | COMBO | Non | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | La résolution pour la génération d'image. Si elle n'est pas définie sur AUTO, cela remplace le paramètre aspect_ratio. (par défaut : "Auto") |
| `magic_prompt_option` | COMBO | Non | "AUTO"<br>"ON"<br>"OFF" | Détermine si MagicPrompt doit être utilisé dans la génération (par défaut : "AUTO") |
| `seed` | INT | Non | 0-2147483647 | Graine aléatoire pour la génération (par défaut : 0) |
| `style_type` | COMBO | Non | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" | Type de style pour la génération (V2 uniquement) (par défaut : "NONE") |
| `negative_prompt` | STRING | Non | - | Description de ce qu'il faut exclure de l'image (par défaut : chaîne vide) |
| `num_images` | INT | Non | 1-8 | Nombre d'images à générer (par défaut : 1) |

**Note :** Lorsque `resolution` n'est pas définie sur "Auto", elle remplace le paramètre `aspect_ratio`. Le paramètre `num_images` a une limite maximale de 8 images par génération.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | L'image ou les images générées par le modèle Ideogram V2 |
