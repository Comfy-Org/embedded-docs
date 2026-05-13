> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/fr.md)

Voici la traduction en français de la documentation du nœud Recraft V4 Text to Vector :

Le nœud Recraft V4 Texte vers Vecteur génère des illustrations vectorielles (SVG) à partir d'une description textuelle. Il se connecte à une API externe pour utiliser le modèle Recraft V4 ou Recraft V4 Pro pour la génération d'images. Le nœud produit une ou plusieurs images SVG en fonction de votre invite.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Invite pour la génération d'image. Maximum 10 000 caractères. |
| `prompt_négatif` | STRING | Non | N/A | Description textuelle facultative des éléments indésirables sur une image. |
| `modèle` | COMBO | Oui | `"recraftv4"`<br>`"recraftv4_pro"` | Le modèle à utiliser pour la génération. La sélection d'un modèle modifie les options `size` disponibles. |
| `size` | COMBO | Oui | Pour `recraftv4` : `"1024x1024"`, `"1152x896"`, `"896x1152"`, `"1216x832"`, `"832x1216"`, `"1344x768"`, `"768x1344"`, `"1536x640"`, `"640x1536"`<br>Pour `recraftv4_pro` : `"2048x2048"`, `"2304x1792"`, `"1792x2304"`, `"2432x1664"`, `"1664x2432"`, `"2688x1536"`, `"1536x2688"`, `"3072x1280"`, `"1280x3072"` | La taille de l'image générée. Les options disponibles dépendent du `modèle` sélectionné. La valeur par défaut est `"1024x1024"` pour `recraftv4` et `"2048x2048"` pour `recraftv4_pro`. |
| `n` | INT | Oui | 1 à 6 | Le nombre d'images à générer (par défaut : 1). |
| `graine` | INT | Oui | 0 à 18446744073709551615 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine. |
| `recraft_controls` | CUSTOM | Non | N/A | Contrôles supplémentaires facultatifs sur la génération via le nœud Contrôles Recraft. |

**Remarque :** Le paramètre `size` est une entrée dynamique dont les options disponibles changent en fonction du `model` sélectionné. La valeur `seed` ne garantit pas des résultats reproductibles depuis l'API externe.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | SVG | La ou les images vectorielles (SVG) générées. |

---
**Source fingerprint (SHA-256):** `ffab67555923cea29b50ae71e3ffaad13340aead4d01973a70244468fae4420d`
