> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/fr.md)

Voici la traduction en français de la documentation du nœud RegexExtract :

Le nœud RegexExtract recherche des motifs dans un texte à l'aide d'expressions régulières. Il peut trouver la première correspondance, toutes les correspondances, des groupes spécifiques issus des correspondances, ou tous les groupes parmi plusieurs correspondances. Le nœud prend en charge divers indicateurs regex pour la sensibilité à la casse, la correspondance multiligne et le comportement dotall.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `chaîne` | STRING | Oui | - | Le texte d'entrée dans lequel rechercher des motifs |
| `motif_regex` | STRING | Oui | - | Le motif d'expression régulière à rechercher |
| `mode` | COMBO | Oui | "Première correspondance"<br>"Toutes les correspondances"<br>"Premier groupe"<br>"Tous les groupes" | Le mode d'extraction détermine quelles parties des correspondances sont renvoyées (par défaut : "Première correspondance") |
| `insensible_à_la_casse` | BOOLEAN | Non | - | Indique s'il faut ignorer la casse lors de la correspondance (par défaut : Vrai) |
| `multiligne` | BOOLEAN | Non | - | Indique s'il faut traiter la chaîne comme plusieurs lignes (par défaut : Faux) |
| `dotall` | BOOLEAN | Non | - | Indique si le point (.) correspond aux sauts de ligne (par défaut : Faux) |
| `index_groupe` | INT | Non | 0-100 | L'index du groupe de capture à extraire lors de l'utilisation des modes de groupe (par défaut : 1) |

**Remarque :** Lors de l'utilisation des modes "Premier groupe" ou "Tous les groupes", le paramètre `group_index` spécifie le groupe de capture à extraire. Le groupe 0 représente la correspondance entière, tandis que les groupes 1+ représentent les groupes de capture numérotés dans votre motif regex.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | STRING | Le texte extrait en fonction du mode et des paramètres sélectionnés |

---
**Source fingerprint (SHA-256):** `38e365d21bea966ed65bc78c184766330924fe75392cdb88c6978052037f5d5f`
