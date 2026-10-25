# Branch

Branch sélectionne l’une de plusieurs entrées connectées par nom et la transmet à la sortie. Il fonctionne comme un commutateur paresseux : seule la branche sélectionnée est évaluée, de sorte que les autres branches peuvent rester non connectées ou contenir des sorties que vous ne souhaitez pas calculer. Chaque nouvelle connexion ajoute une nouvelle entrée de branche, les entrées peuvent être renommées en double-cliquant dessus, et la branche active est choisie dans le sélecteur `branch`.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `autogrow` | Les branches connectées. Chaque connexion ajoute une nouvelle entrée de branche, jusqu’à 32 ; toutes les branches doivent utiliser le même type de données, qui devient le type de sortie. | AUTOGROW | Oui | 1 à 32 branches |
| `branch` | Nom de la branche transmise à la sortie. Les options sont les noms des entrées de branches connectées, et une entrée peut être renommée en double-cliquant dessus. | STRING | Oui | Noms des branches connectées |
| `branch_names` | Liste interne des noms des branches connectées, maintenue synchronisée par le frontend. Elle associe le nom sélectionné à sa branche et n’est pas destinée à être modifiée manuellement. | ARRAY | Oui | - |

**Remarque :** Seule la branche sélectionnée est demandée, les autres branches ne sont donc pas évaluées. Le nœud génère une erreur lorsque le nom sélectionné n’est pas connecté.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La valeur de la branche sélectionnée, transmise sans modification. | MATCH_TYPE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BranchNode/fr.md)

---
**Source fingerprint (SHA-256):** `2b4dca360c1b459a9f05eb54fedb7cdea6842fb0c606ee6f937ed00f715ee23a`
