Ce nœud génère des images à partir de descriptions textuelles en utilisant les modèles d'IA Recraft V4 ou V4 Pro. Il envoie votre prompt à une API externe et retourne les images générées. Vous pouvez contrôler le résultat en spécifiant le modèle, la taille de l'image et le nombre d'images à créer.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt pour la génération d'image. Maximum 10 000 caractères. | STRING | Oui | N/A |
| `prompt_négatif` | Description textuelle facultative des éléments indésirables sur une image. | STRING | Non | N/A |
| `modèle` | Le modèle à utiliser pour la génération. La sélection d'un modèle détermine les tailles d'image disponibles. | COMBO | Oui | `"recraftv4"`<br>`"recraftv4_pro"` |
| `size` | La taille de l'image générée. Les options disponibles dépendent du modèle sélectionné. Pour `recraftv4`, la valeur par défaut est "1024x1024". Pour `recraftv4_pro`, la valeur par défaut est "2048x2048". | COMBO | Oui | Varie selon le modèle |
| `n` | Le nombre d'images à générer (par défaut : 1). | INT | Oui | 1 à 6 |
| `graine` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 18446744073709551615 |
| `recraft_controls` | Contrôles supplémentaires facultatifs sur la génération via le nœud Recraft Controls. | CUSTOM | Non | N/A |

**Remarque :** Le paramètre `size` est une entrée dynamique dont les options disponibles changent en fonction du `model` sélectionné. La valeur `seed` ne garantit pas des résultats d'image reproductibles.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | L'image générée ou le lot d'images. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `77d549a43aeee670b6c42069654017fb6b202ed83ca330389573b790bad6ae6e`
