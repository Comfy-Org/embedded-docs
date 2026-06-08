Voici la traduction en français de la documentation du nœud GeminiImage, en respectant vos règles de traduction.

---

Le nœud GeminiImage génère des réponses textuelles et visuelles à partir des modèles d'IA Gemini de Google. Il permet de fournir des entrées multimodales, notamment des invites textuelles, des images et des fichiers, pour créer des sorties textuelles et visuelles cohérentes. Le nœud gère toutes les communications avec l'API et l'analyse des réponses des derniers modèles Gemini.

## Entrées

| Paramètre | Description | Type de données | Type d'entrée | Valeur par défaut | Plage |
| --- | --- | --- | --- | --- | --- |
| `prompt` | Invite textuelle pour la génération | STRING | requis | "" | - |
| `model` | Le modèle Gemini à utiliser pour générer les réponses. | COMBO | requis | gemini_2_5_flash_image_preview | `gemini_2_5_flash_image_preview`<br>`gemini_2_5_pro_exp_03_25`<br>`gemini_2_0_flash_exp_image_generation` |
| `seed` | Lorsque la graine est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. Une sortie déterministe n'est pas garantie. De plus, la modification du modèle ou des paramètres, comme la température, peut entraîner des variations dans la réponse, même en utilisant la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée. | INT | requis | 42 | 0 à 18446744073709551615 |
| `images` | Image(s) optionnelle(s) à utiliser comme contexte pour le modèle. Pour inclure plusieurs images, vous pouvez utiliser le nœud Batch Images. | IMAGE | optionnel | Aucun | - |
| `files` | Fichier(s) optionnel(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | optionnel | Aucun | - |

**Remarque :** Le nœud comprend des paramètres cachés (`auth_token`, `comfy_api_key`, `unique_id`) qui sont automatiquement gérés par le système et ne nécessitent aucune intervention de l'utilisateur.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | La réponse visuelle générée par le modèle Gemini | IMAGE |
| `STRING` | La réponse textuelle générée par le modèle Gemini | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage/fr.md)

---
**Source fingerprint (SHA-256):** `bf55ec4f5a869a6bc5a15366f55f86ad25f9498c14056acc80951d3637bf08f2`
