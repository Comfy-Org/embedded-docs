> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/fr.md)

Voici la traduction en français de la documentation du nœud RegexReplace :

Le nœud RegexReplace recherche et remplace du texte dans des chaînes de caractères à l'aide de motifs d'expressions régulières. Il vous permet de rechercher des motifs textuels et de les remplacer par un nouveau texte, avec des options pour contrôler le fonctionnement de la correspondance des motifs, notamment la sensibilité à la casse, la correspondance multiligne et la limitation du nombre de remplacements.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `string` | STRING | Oui | - | La chaîne de texte d'entrée dans laquelle rechercher et remplacer |
| `regex_pattern` | STRING | Oui | - | Le motif d'expression régulière à rechercher dans la chaîne d'entrée |
| `replace` | STRING | Oui | - | Le texte de remplacement à substituer aux motifs correspondants |
| `case_insensitive` | BOOLEAN | Non | - | Lorsqu'activé, rend la correspondance des motifs insensible à la casse (par défaut : True) |
| `multiline` | BOOLEAN | Non | - | Lorsqu'activé, modifie le comportement de ^ et $ pour qu'ils correspondent au début/fin de chaque ligne plutôt qu'au début/fin de la chaîne entière (par défaut : False) |
| `dotall` | BOOLEAN | Non | - | Lorsqu'activé, le point (.) correspond à n'importe quel caractère, y compris les sauts de ligne. Lorsque désactivé, les points ne correspondent pas aux sauts de ligne (par défaut : False) |
| `count` | INT | Non | 0-100 | Nombre maximal de remplacements à effectuer. Mettre à 0 pour remplacer toutes les occurrences (par défaut). Mettre à 1 pour remplacer uniquement la première correspondance, 2 pour les deux premières, etc. (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | STRING | La chaîne modifiée avec les remplacements spécifiés appliqués |

---
**Source fingerprint (SHA-256):** `4a4d4b317ee23314a4ac26cf3b58a2cc904bfb8111608f88345c1014b801ea00`
