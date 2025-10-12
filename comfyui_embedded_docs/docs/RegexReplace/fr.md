> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/fr.md)

Le nœud RegexReplace recherche et remplace du texte dans des chaînes de caractères en utilisant des motifs d'expressions régulières. Il vous permet de rechercher des motifs de texte et de les remplacer par un nouveau texte, avec des options pour contrôler le fonctionnement de la correspondance des motifs, y compris la sensibilité à la casse, la correspondance multiligne et la limitation du nombre de remplacements.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Oui | - | La chaîne de texte d'entrée dans laquelle effectuer la recherche et le remplacement |
| `regex_pattern` | STRING | Oui | - | Le motif d'expression régulière à rechercher dans la chaîne d'entrée |
| `replace` | STRING | Oui | - | Le texte de remplacement à substituer aux motifs correspondants |
| `case_insensitive` | BOOLEAN | Non | - | Lorsqu'activé, rend la correspondance de motifs insensible à la casse (par défaut : True) |
| `multiline` | BOOLEAN | Non | - | Lorsqu'activé, modifie le comportement de ^ et $ pour qu'ils correspondent au début/fin de chaque ligne plutôt qu'au début/fin de la chaîne entière (par défaut : False) |
| `dotall` | BOOLEAN | Non | - | Lorsqu'activé, le point (.) correspondra à n'importe quel caractère, y compris les caractères de nouvelle ligne. Lorsque désactivé, les points ne correspondront pas aux nouvelles lignes (par défaut : False) |
| `count` | INT | Non | 0-100 | Nombre maximum de remplacements à effectuer. Mettre à 0 pour remplacer toutes les occurrences (par défaut). Mettre à 1 pour remplacer uniquement la première correspondance, 2 pour les deux premières correspondances, etc. (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | STRING | La chaîne modifiée avec les remplacements spécifiés appliqués |