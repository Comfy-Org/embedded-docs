# GetItemFromList

Ce nœud renvoie un seul élément d'une liste, sélectionné par sa position. Vous fournissez la liste et le numéro d'index de l'élément souhaité, et le nœud produit cet élément. Cela est utile pour choisir un élément spécifique parmi un groupe de valeurs, comme une image particulière dans un lot.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `list` | La liste de valeurs dans laquelle sélectionner. Comme ce nœud est marqué comme prenant une entrée de type liste, la valeur connectée est traitée comme un groupe d'éléments. | Tout type | Oui | Toute liste de valeurs |
| `index` | La position de l'élément à renvoyer. La valeur commence à 0, donc `0` renvoie le premier élément, `1` renvoie le deuxième élément, et ainsi de suite (par défaut : 0). | INT | Oui | Tout index entier |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `OUTPUT` | L'élément unique situé à la position `index` dans la `list` fournie. | Tout type |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetItemFromList/fr.md)

---
**Source fingerprint (SHA-256):** `11c1c90fed0e29f1110b4c1dda64d60797aff38d7f3af69f76b74e94fe94e976`
