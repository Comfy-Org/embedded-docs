> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/fr.md)

Ce nœud génère des images à partir de descriptions textuelles en utilisant les modèles d'IA Recraft V4 ou V4 Pro. Il envoie votre prompt à une API externe et renvoie les images générées. Vous pouvez contrôler le résultat en spécifiant le modèle, la taille de l'image et le nombre d'images à créer.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Prompt pour la génération d'image. Maximum 10 000 caractères. |
| `negative_prompt` | STRING | Non | N/A | Une description textuelle facultative des éléments indésirables sur une image. |
| `model` | COMBO | Oui | `"recraftv4"`<br>`"recraftv4_pro"` | Le modèle à utiliser pour la génération. La sélection d'un modèle détermine les tailles d'image disponibles. |
| `size` | COMBO | Oui | Varie selon le modèle | La taille de l'image générée. Les options disponibles dépendent du modèle sélectionné. Pour `recraftv4`, la valeur par défaut est "1024x1024". Pour `recraftv4_pro`, la valeur par défaut est "2048x2048". |
| `n` | INT | Oui | 1 à 6 | Le nombre d'images à générer (par défaut : 1). |
| `seed` | INT | Oui | 0 à 18446744073709551615 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). |
| `recraft_controls` | CUSTOM | Non | N/A | Contrôles additionnels facultatifs sur la génération via le nœud Recraft Controls. |

**Note :** Le paramètre `size` est une entrée dynamique dont les options disponibles changent en fonction du `model` sélectionné. La valeur de `seed` ne garantit pas des sorties d'image reproductibles.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | L'image ou le lot d'images généré. |
