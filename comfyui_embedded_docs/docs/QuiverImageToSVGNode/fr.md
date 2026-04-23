> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/fr.md)

Ce nœud convertit une image matricielle en un graphique vectoriel évolutif (SVG) en utilisant les modèles de vectorisation de Quiver AI. Il envoie l'image à une API externe qui la traite et renvoie le résultat vectorisé.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | N/A | Image d'entrée à vectoriser. |
| `auto_crop` | BOOLEAN | Non | `True`<br>`False` | Recadrage automatique sur le sujet principal. Il s'agit d'un paramètre avancé (par défaut : `False`). |
| `model` | DYNAMICCOMBO | Oui | Plusieurs options disponibles | Modèle à utiliser pour la vectorisation SVG. La sélection d'un modèle révèle des paramètres supplémentaires spécifiques à ce modèle : `target_size` (taille cible de redimensionnement carré en pixels, par défaut : 1024, plage : 128-4096), `temperature`, `top_p`, et `presence_penalty`. |
| `seed` | INT | Non | 0 à 2147483647 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la valeur de la graine. Ce paramètre dispose de la fonctionnalité "control after generate" (par défaut : 0). |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `SVG` | SVG | Le résultat SVG vectorisé. |