Voici la traduction en français de la documentation du nœud Image Compare :

Le nœud Image Compare fournit une interface visuelle permettant de comparer deux images côte à côte à l'aide d'un curseur déplaçable. Il est conçu comme un nœud de sortie, ce qui signifie qu'il ne transmet pas de données à d'autres nœuds, mais affiche directement les images dans l'interface utilisateur à des fins d'inspection.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image A` | La première image à comparer. | IMAGE | Non | - |
| `image B` | La seconde image à comparer. | IMAGE | Non | - |
| `vue de comparaison` | Le contrôle qui active la vue de comparaison avec curseur dans l'interface utilisateur. | IMAGECOMPARE | Oui | - |

**Remarque :** Ce nœud est un nœud de sortie. Bien que `image_a` et `image_b` soient optionnels, au moins une image doit être fournie pour que le nœud ait un effet visible. Le nœud affichera une zone vide pour toute entrée d'image qui n'est pas connectée.

## Sorties

Ce nœud est un nœud de sortie et ne produit aucune donnée de sortie utilisable dans d'autres nœuds. Sa fonction est d'afficher les images fournies dans l'interface de ComfyUI.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/fr.md)

---
**Source fingerprint (SHA-256):** `2bc980cd20aad3cf60300868599bbce8eaba1cdb21880d2b3f4cd628108d8139`
