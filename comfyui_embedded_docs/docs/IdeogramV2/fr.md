Le nœud Ideogram V2 génère des images à l'aide du modèle d'IA Ideogram V2. Il prend des invites textuelles et divers paramètres de génération pour créer des images via un service API. Le nœud prend en charge différents ratios d'aspect, résolutions et options de style pour personnaliser les images de sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Invite pour la génération d'image (par défaut : chaîne vide) | STRING | Oui | - |
| `turbo` | Indique s'il faut utiliser le mode turbo (génération plus rapide, qualité potentiellement inférieure) (par défaut : False) | BOOLEAN | Non | - |
| `aspect_ratio` | Le ratio d'aspect pour la génération d'image. Ignoré si la résolution n'est pas définie sur AUTO. (par défaut : "1:1") | COMBO | Non | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" |
| `resolution` | La résolution pour la génération d'image. Si elle n'est pas définie sur AUTO, elle remplace le paramètre `aspect_ratio`. (par défaut : "Auto") | COMBO | Non | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `magic_prompt_option` | Détermine si MagicPrompt doit être utilisé lors de la génération (par défaut : "AUTO") | COMBO | Non | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Graine aléatoire pour la génération (par défaut : 0) | INT | Non | 0-2147483647 |
| `style_type` | Type de style pour la génération (V2 uniquement) (par défaut : "NONE") | COMBO | Non | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" |
| `negative_prompt` | Description de ce qui doit être exclu de l'image (par défaut : chaîne vide) | STRING | Non | - |
| `num_images` | Nombre d'images à générer (par défaut : 1) | INT | Non | 1-8 |

**Remarque :** Lorsque `resolution` n'est pas défini sur "Auto", il remplace le paramètre `aspect_ratio`. Le paramètre `num_images` a une limite maximale de 8 images par génération.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La ou les images générées par le modèle Ideogram V2 | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/fr.md)

---
**Source fingerprint (SHA-256):** `c0ba21cb62ad75212c960e2bf6730a39c6479c7389a58c50968c66cc8964f5e3`
