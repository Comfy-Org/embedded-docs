> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/fr.md)

Le nœud RegexExtract recherche des motifs dans du texte en utilisant des expressions régulières. Il peut trouver la première correspondance, toutes les correspondances, des groupes spécifiques parmi les correspondances, ou tous les groupes à travers plusieurs correspondances. Le nœud prend en charge divers drapeaux d'expressions régulières pour la sensibilité à la casse, la recherche multiligne et le comportement dotall.

## Entrées

| Paramètre | Type de Données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Oui | - | Le texte d'entrée dans lequel rechercher des motifs |
| `regex_pattern` | STRING | Oui | - | Le motif d'expression régulière à rechercher |
| `mode` | COMBO | Oui | "First Match"<br>"All Matches"<br>"First Group"<br>"All Groups" | Le mode d'extraction détermine quelles parties des correspondances sont renvoyées |
| `case_insensitive` | BOOLEAN | Non | - | Indique s'il faut ignorer la casse lors de la correspondance (par défaut : True) |
| `multiline` | BOOLEAN | Non | - | Indique s'il faut traiter la chaîne comme multiple lignes (par défaut : False) |
| `dotall` | BOOLEAN | Non | - | Indique si le point (.) correspond aux sauts de ligne (par défaut : False) |
| `group_index` | INT | Non | 0-100 | L'index du groupe de capture à extraire lors de l'utilisation des modes de groupe (par défaut : 1) |

**Note :** Lors de l'utilisation des modes "First Group" ou "All Groups", le paramètre `group_index` spécifie quel groupe de capture extraire. Le groupe 0 représente la correspondance entière, tandis que les groupes 1+ représentent les groupes de capture numérotés dans votre motif d'expression régulière.

## Sorties

| Nom de Sortie | Type de Données | Description |
|-------------|-----------|-------------|
| `output` | STRING | Le texte extrait basé sur le mode sélectionné et les paramètres |
