# Comparaison d’images

Le nœud Image Compare fournit une interface visuelle permettant de comparer deux images côte à côte à l'aide d'un curseur déplaçable. Il est conçu comme un nœud de sortie, ce qui signifie qu'il ne transmet pas de données à d'autres nœuds, mais affiche directement les images dans l'interface utilisateur pour inspection.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image A` | La première image à comparer. | IMAGE | Non | - |
| `image B` | La deuxième image à comparer. | IMAGE | Non | - |
| `vue de comparaison` | Le contrôle qui active la vue de comparaison par curseur dans l'interface utilisateur. | IMAGECOMPARE | Oui | - |

**Remarque :** Ce nœud est un nœud de sortie. Bien que `image_a` et `image_b` soient optionnels, au moins une image doit être fournie pour que le nœud ait un effet visible. Le nœud affichera une zone vide pour toute entrée d'image non connectée.

## Sorties

Ce nœud est un nœud de sortie et ne produit aucune donnée de sortie utilisable par d'autres nœuds. Sa fonction est d'afficher les images fournies dans l'interface ComfyUI.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/fr.md)

---
**Source fingerprint (SHA-256):** `bc065572c5631ed80c0590aabae775c51d0f607895a87cb2cca78037ab9a6638`
