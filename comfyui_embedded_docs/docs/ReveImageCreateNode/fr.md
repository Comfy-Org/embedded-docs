> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/fr.md)

Le nœud Reve Image Create génère des images à partir de descriptions textuelles en utilisant le modèle Reve AI. Il envoie une requête textuelle à l'API Reve et retourne l'image générée. Vous pouvez contrôler le format de l'image et appliquer des effets de post-traitement optionnels comme le suréchantillonnage (upscaling).

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Description textuelle de l'image souhaitée. Maximum 2560 caractères. |
| `model` | COMBO | Oui | `"reve-create@20250915"`<br>`"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | Version du modèle et format d'image à utiliser pour la génération. La première option sélectionne le modèle, et les options suivantes définissent le format de l'image. |
| `upscale` | COMBO | Non | `"disabled"`<br>`"enabled"` | Active ou désactive l'étape de post-traitement de suréchantillonnage. Lorsqu'elle est activée, vous devez également sélectionner un facteur de suréchantillonnage. |
| `upscale_factor` | COMBO | Non | `2`<br>`3`<br>`4` | Facteur par lequel augmenter la résolution de l'image. Ce paramètre n'est actif que lorsque `upscale` est défini sur `"enabled"`. |
| `remove_background` | BOOLEAN | Non | N/A | Lorsqu'activé, applique une étape de post-traitement de suppression de l'arrière-plan à l'image générée. |
| `seed` | INT | Non | 0 à 2147483647 | Une valeur de seed qui contrôle si le nœud doit être réexécuté. Remarque : Les résultats ne sont pas déterministes, quelle que soit la valeur du seed. Par défaut : 0. |

**Remarque :** Le paramètre `upscale_factor` dépend du paramètre `upscale` défini sur `"enabled"`. Le paramètre `seed` ne garantit pas des sorties déterministes.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image générée par le modèle Reve en fonction de la requête textuelle d'entrée. |