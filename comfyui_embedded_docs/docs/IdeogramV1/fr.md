> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/fr.md)

Le nœud IdeogramV1 génère des images en utilisant le modèle Ideogram V1 via une API. Il prend en entrée des invites textuelles et divers paramètres de génération pour créer une ou plusieurs images selon vos instructions. Le nœud prend en charge différents formats d'image et modes de génération pour personnaliser le résultat.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite pour la génération d'image (par défaut : vide) |
| `turbo` | BOOLEAN | Oui | - | Indique si le mode turbo doit être utilisé (génération plus rapide, qualité potentiellement inférieure) (par défaut : False) |
| `aspect_ratio` | COMBO | Non | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | Le format d'image pour la génération (par défaut : "1:1") |
| `magic_prompt_option` | COMBO | Non | "AUTO"<br>"ON"<br>"OFF" | Détermine si MagicPrompt doit être utilisé lors de la génération (par défaut : "AUTO") |
| `seed` | INT | Non | 0-2147483647 | Valeur de graine aléatoire pour la génération (par défaut : 0) |
| `negative_prompt` | STRING | Non | - | Description de ce qui doit être exclu de l'image (par défaut : vide) |
| `num_images` | INT | Non | 1-8 | Nombre d'images à générer (par défaut : 1) |

**Remarque :** Le paramètre `num_images` a une limite maximale de 8 images par requête de génération.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | IMAGE | La ou les images générées par le modèle Ideogram V1 |

---
**Source fingerprint (SHA-256):** `7e453cd54b5db48588ed899b0754e0d06fdcfbaed248d13fb74b7049f0f25b8f`
