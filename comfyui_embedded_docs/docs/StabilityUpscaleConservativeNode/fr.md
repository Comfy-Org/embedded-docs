> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleConservativeNode/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à suréchantillonner |
| `prompt` | STRING | Oui | - | Ce que vous souhaitez voir dans l'image de sortie. Un prompt fort et descriptif qui définit clairement les éléments, les couleurs et les sujets donnera de meilleurs résultats. (par défaut : chaîne vide) |
| `creativity` | FLOAT | Oui | 0.2-0.5 | Contrôle la probabilité de créer des détails supplémentaires non fortement conditionnés par l'image initiale. (par défaut : 0.35) |
| `seed` | INT | Oui | 0-4294967294 | La graine aléatoire utilisée pour créer le bruit. (par défaut : 0) |
| `negative_prompt` | STRING | Non | - | Mots-clés de ce que vous ne souhaitez pas voir dans l'image de sortie. Il s'agit d'une fonctionnalité avancée. (par défaut : chaîne vide) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image suréchantillonnée en résolution 4K |