> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/fr.md)

Le nœud Quiver Text to SVG génère une image graphique vectorielle évolutive (SVG) à partir d'une description textuelle en utilisant les modèles de Quiver AI. Vous pouvez éventuellement fournir des images de référence et des instructions de style pour guider le processus de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Description textuelle de la sortie SVG souhaitée. C'est l'instruction principale pour la génération. |
| `instructions` | STRING | Non | N/A | Instructions supplémentaires concernant le style ou le formatage. Il s'agit d'un paramètre avancé facultatif. |
| `reference_images` | IMAGE | Non | N/A | Jusqu'à 4 images de référence pour guider la génération. Il s'agit d'une entrée facultative. |
| `model` | COMBO | Oui | Plusieurs options disponibles | Modèle à utiliser pour la génération SVG. Les options disponibles sont déterminées par l'API Quiver. |
| `seed` | INT | Oui | 0 à 2147483647 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes, quelle que soit la graine. Par défaut : 0. |

**Note :** L'entrée `reference_images` accepte un maximum de 4 images. Si plus d'images sont fournies, le nœud générera une erreur.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `SVG` | SVG | L'image graphique vectorielle évolutive (SVG) générée. |