> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/fr.md)

Le nœud IdeogramV1 génère des images en utilisant le modèle Ideogram V1 via une API. Il prend des invites textuelles et divers paramètres de génération pour créer une ou plusieurs images basées sur votre saisie. Le nœud prend en charge différents ratios d'aspect et modes de génération pour personnaliser le résultat.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | L'invite pour la génération d'image (par défaut : vide) |
| `turbo` | BOOLEAN | Oui | - | Indique s'il faut utiliser le mode turbo (génération plus rapide, qualité potentiellement inférieure) (par défaut : Faux) |
| `aspect_ratio` | COMBO | Non | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | Le ratio d'aspect pour la génération d'image (par défaut : "1:1") |
| `magic_prompt_option` | COMBO | Non | "AUTO"<br>"ON"<br>"OFF" | Détermine si MagicPrompt doit être utilisé dans la génération (par défaut : "AUTO") |
| `seed` | INT | Non | 0-2147483647 | Valeur de graine aléatoire pour la génération (par défaut : 0) |
| `negative_prompt` | STRING | Non | - | Description de ce qu'il faut exclure de l'image (par défaut : vide) |
| `num_images` | INT | Non | 1-8 | Nombre d'images à générer (par défaut : 1) |

**Note :** Le paramètre `num_images` a une limite maximale de 8 images par requête de génération.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | L'image ou les images générées par le modèle Ideogram V1 |
