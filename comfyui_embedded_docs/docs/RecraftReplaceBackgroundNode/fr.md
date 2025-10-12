> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/fr.md)

Remplacer l'arrière-plan d'une image en fonction de l'inspiration fournie. Ce nœud utilise l'API Recraft pour générer de nouveaux arrière-plans pour vos images selon votre description textuelle, vous permettant de transformer complètement l'arrière-plan tout en conservant le sujet principal intact.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à traiter |
| `invite` | STRING | Oui | - | Inspiration pour la génération d'image (par défaut : vide) |
| `n` | INT | Oui | 1-6 | Le nombre d'images à générer (par défaut : 1) |
| `graine` | INT | Oui | 0-18446744073709551615 | Graine pour déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) |
| `recraft_style` | STYLEV3 | Non | - | Sélection de style optionnelle pour l'arrière-plan généré |
| `invite négative` | STRING | Non | - | Une description textuelle optionnelle des éléments indésirables sur une image (par défaut : vide) |

**Note :** Le paramètre `seed` contrôle quand le nœud se réexécute mais ne garantit pas des résultats déterministes en raison de la nature de l'API externe.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | L'image ou les images générées avec l'arrière-plan remplacé |
