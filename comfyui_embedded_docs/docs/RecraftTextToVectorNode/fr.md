> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToVectorNode/fr.md)

Génère un SVG de manière synchrone en fonction de l'invite et de la résolution. Ce nœud crée des illustrations vectorielles en envoyant des invites textuelles à l'API Recraft et renvoie le contenu SVG généré.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite pour la génération d'image. (par défaut : "") |
| `sous-style` | COMBO | Oui | Options multiples disponibles | Le style d'illustration spécifique à utiliser pour la génération. Les options sont déterminées par les sous-styles d'illustration vectorielle disponibles dans RecraftStyleV3. |
| `taille` | COMBO | Oui | Options multiples disponibles | La taille de l'image générée. (par défaut : 1024x1024) |
| `n` | INT | Oui | 1-6 | Le nombre d'images à générer. (par défaut : 1, min : 1, max : 6) |
| `seed` | INT | Oui | 0-18446744073709551615 | Graine pour déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine. (par défaut : 0, min : 0, max : 18446744073709551615) |
| `prompt négatif` | STRING | Non | - | Une description textuelle facultative des éléments indésirables sur une image. (par défaut : "") |
| `recraft_controls` | CONTROLS | Non | - | Contrôles supplémentaires facultatifs sur la génération via le nœud Recraft Controls. |

**Note :** Le paramètre `seed` contrôle uniquement quand le nœud se réexécute mais ne rend pas les résultats de génération déterministes.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `SVG` | SVG | L'illustration vectorielle générée au format SVG |
