> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/fr.md)

Voici la traduction en français de la documentation du nœud OpenAIGPTImageNodeV2 :

## Aperçu

Ce nœud génère des images à l'aide de l'API GPT Image d'OpenAI. Il prend en charge plusieurs modèles, vous permet de fournir des images d'entrée pour l'édition et peut utiliser un masque pour spécifier les parties de l'image à modifier.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Invite textuelle pour GPT Image (par défaut : ""). |
| `modèle` | COMBO | Oui | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` | Le modèle GPT Image OpenAI à utiliser. La sélection d'un modèle révèle des paramètres supplémentaires spécifiques à ce modèle. |
| `model.size` | COMBO | Oui | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Personnalisé"` | Taille de l'image. Sélectionnez 'Personnalisé' pour utiliser la largeur et la hauteur personnalisées (par défaut : "auto"). Disponible uniquement pour `gpt-image-2`. |
| `model.custom_width` | INT | Non | 1024 à 3840 | Utilisé uniquement lorsque `size` est 'Personnalisé'. Doit être un multiple de 16 (par défaut : 1024). Disponible uniquement pour `gpt-image-2`. |
| `model.custom_height` | INT | Non | 1024 à 3840 | Utilisé uniquement lorsque `size` est 'Personnalisé'. Doit être un multiple de 16 (par défaut : 1024). Disponible uniquement pour `gpt-image-2`. |
| `model.background` | COMBO | Oui | `"auto"`<br>`"opaque"` | Renvoie l'image avec ou sans arrière-plan (par défaut : "auto"). Disponible uniquement pour `gpt-image-2`. |
| `model.quality` | COMBO | Oui | `"standard"`<br>`"hd"` | La qualité de l'image générée. Disponible uniquement pour `gpt-image-2`. |
| `model.images` | IMAGE | Non | N/A | Images d'entrée pour l'édition. Disponible uniquement pour `gpt-image-2`. |
| `model.mask` | MASK | Non | N/A | Un masque pour spécifier les parties de l'image d'entrée à modifier. Disponible uniquement pour `gpt-image-2`. |
| `n` | INT | Oui | 1 à 8 | Nombre d'images à générer (par défaut : 1). |
| `graine` | INT | Oui | 0 à 2147483647 | Graine pour la reproductibilité (par défaut : 0). Remarque : pas encore implémentée dans le backend. |

**Contraintes et limitations des paramètres :**

- Lors de l'utilisation de `gpt-image-2` avec un `model.size` défini sur "Personnalisé", les `custom_width` et `custom_height` doivent être des multiples de 16, le bord maximum doit être <= 3840, le rapport hauteur/largeur ne doit pas dépasser 3:1, et le nombre total de pixels doit être compris entre 655 360 et 8 294 400.
- Si un `mask` est fourni, une image d'entrée (`model.images`) est requise. Un masque ne peut pas être utilisé sans image d'entrée.
- Un masque ne peut pas être utilisé avec plusieurs images d'entrée.
- Lorsqu'un masque est fourni, ses dimensions doivent correspondre à celles de l'image d'entrée.
- Le paramètre `seed` n'est actuellement pas fonctionnel.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | L'image ou les images générées. |

---
**Source fingerprint (SHA-256):** `a757208cf6cc151594599b35b0ef73f2caf7274189e948799211c0714a6a8f89`
