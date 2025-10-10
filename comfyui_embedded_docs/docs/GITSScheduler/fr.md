> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/fr.md)

Le nœud GITSScheduler génère des plannings de bruit sigmas pour la méthode d'échantillonnage GITS (Generative Iterative Time Steps). Il calcule les valeurs sigma basées sur un paramètre de coefficient et un nombre d'étapes, avec un facteur de débruitage optionnel qui peut réduire le nombre total d'étapes utilisées. Le nœud utilise des niveaux de bruit prédéfinis et une interpolation pour créer le planning sigma final.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `coeff` | FLOAT | Oui | 0.80 - 1.50 | La valeur du coefficient qui contrôle la courbe du planning de bruit (par défaut : 1.20) |
| `steps` | INT | Oui | 2 - 1000 | Le nombre total d'étapes d'échantillonnage pour lesquelles générer les sigmas (par défaut : 10) |
| `denoise` | FLOAT | Oui | 0.0 - 1.0 | Facteur de débruitage qui réduit le nombre d'étapes utilisées (par défaut : 1.0) |

**Note :** Lorsque `denoise` est défini sur 0.0, le nœud retourne un tenseur vide. Lorsque `denoise` est inférieur à 1.0, le nombre réel d'étapes utilisées est calculé comme `round(steps * denoise)`.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Les valeurs sigma générées pour le planning de bruit |