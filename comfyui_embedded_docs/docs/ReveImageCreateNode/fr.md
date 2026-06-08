Le nœud Reve Image Create génère des images à partir de descriptions textuelles en utilisant le modèle Reve AI. Il envoie une invite textuelle à l'API Reve et retourne l'image générée. Vous pouvez contrôler le rapport hauteur/largeur de l'image et appliquer des effets de post-traitement optionnels comme la mise à l'échelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Description textuelle de l'image souhaitée. Maximum 2560 caractères. | STRING | Oui | N/A |
| `modèle` | Version du modèle et rapport hauteur/largeur à utiliser pour la génération. La première option sélectionne le modèle, et les options suivantes définissent le rapport hauteur/largeur de l'image. | COMBO | Oui | `"reve-create@20250915"`<br>`"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `agrandir` | Active ou désactive l'étape de post-traitement de mise à l'échelle. Lorsqu'elle est activée, vous devez également sélectionner un facteur de mise à l'échelle. | COMBO | Non | `"disabled"`<br>`"enabled"` |
| `upscale_factor` | Facteur par lequel augmenter la résolution de l'image. Ce paramètre n'est actif que lorsque `agrandir` est défini sur `"enabled"`. | COMBO | Non | `2`<br>`3`<br>`4` |
| `supprimer l’arrière-plan` | Lorsqu'il est activé, applique une étape de post-traitement de suppression d'arrière-plan à l'image générée. | BOOLEAN | Non | N/A |
| `graine` | Une valeur de graine qui contrôle si le nœud doit être réexécuté. Remarque : Les résultats sont non déterministes quelle que soit la valeur de la graine. Par défaut : 0. | INT | Non | 0 à 2147483647 |

**Remarque :** Le paramètre `upscale_factor` dépend du paramètre `upscale` défini sur `"enabled"`. Le paramètre `seed` ne garantit pas des sorties déterministes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image générée par le modèle Reve en fonction de l'invite d'entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/fr.md)

---
**Source fingerprint (SHA-256):** `56cb32ad254d39609d9795ca29f1ccba1db2c5a7ac5bb530475298306ec4ea19`
