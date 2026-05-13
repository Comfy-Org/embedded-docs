> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/fr.md)

Voici la traduction en français de la documentation du nœud Quiver Text to SVG :

Le nœud Quiver Text to SVG génère une image vectorielle scalable (SVG) à partir d'une description textuelle en utilisant les modèles d'IA de Quiver. Vous pouvez éventuellement fournir des images de référence et des instructions de style pour guider le processus de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Description textuelle du résultat SVG souhaité. Il s'agit de l'instruction principale pour déterminer ce qui doit être généré. |
| `instructions` | STRING | Non | N/A | Conseils supplémentaires concernant le style ou la mise en forme. Il s'agit d'un paramètre avancé et facultatif. |
| `reference_images` | IMAGE | Non | 0 à 4 images | Jusqu'à 4 images de référence pour guider la génération. Il s'agit d'une entrée facultative. |
| `model` | COMBO | Oui | `"Quiver SVG v1"`<br>`"Quiver SVG v1 Max"`<br>`"Quiver SVG v1 Preview"` | Modèle à utiliser pour la génération SVG. Les options disponibles sont déterminées par l'API Quiver. |
| `seed` | INT | Oui | 0 à 2147483647 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine. Valeur par défaut : 0. |

**Remarque :** L'entrée `reference_images` accepte un maximum de 4 images. Si davantage sont fournies, le nœud générera une erreur.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `SVG` | SVG | L'image vectorielle scalable (SVG) générée. |

---
**Source fingerprint (SHA-256):** `634758797a59e5a409424deee808e1d8b5b5852a86eac4bccd7f2634a19fb743`
