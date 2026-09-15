# LoopIteration

Ce nœud fournit des métadonnées d’itération pour les workflows de type boucle. Il reçoit des entrées sous forme de listes et transmet le premier élément de chaque liste, afin qu’une boucle puisse suivre l’index courant, savoir s’il s’agit de la première ou de la dernière étape, l’élément de liste courant et toute valeur d’itération en cours. Le comportement du cache est contrôlé par l’indicateur `reuse_cache`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `iteration_index` | L’index de l’itération courante, fourni sous forme de liste. Le premier élément est transmis à la sortie. | INT | Oui | - |
| `is_first` | Indique si l’itération courante est la première, fourni sous forme de liste. Le premier élément est transmis à la sortie. | BOOLEAN | Oui | - |
| `is_last` | Indique si l’itération courante est la dernière, fourni sous forme de liste. Le premier élément est transmis à la sortie. | BOOLEAN | Oui | - |
| `list_item` | L’élément extrait de la liste pour cette itération. Facultatif ; le premier élément est transmis à la sortie lorsqu’il est fourni, sinon None est renvoyé. | ANY | Non | - |
| `current_iteration_value` | La valeur portée par l’itération courante. Facultatif ; le premier élément est transmis à la sortie lorsqu’il est fourni, sinon None est renvoyé. | ANY | Non | - |
| `reuse_cache` | Contrôle si le résultat peut être réutilisé depuis le cache. Lorsqu’il est activé, le nœud conserve une empreinte stable afin que les résultats mis en cache puissent être réutilisés. Lorsqu’il est désactivé, une empreinte non correspondante est produite afin que le nœud s’exécute à nouveau à chaque itération. | BOOLEAN | Oui | - |

Remarque : ce nœud est compatible avec les entrées de type liste, ce qui signifie que chaque entrée est censée arriver sous forme de liste et que le nœud ne produit que le premier élément de chaque liste. Il accepte également des entrées supplémentaires au-delà de celles listées ici.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `iteration_index` | L’index de l’itération courante. | INT |
| `is_first` | Indique si l’itération courante est la première. | BOOLEAN |
| `is_last` | Indique si l’itération courante est la dernière. | BOOLEAN |
| `list_item` | L’élément extrait de la liste pour cette itération, ou None lorsqu’aucun élément n’a été fourni. | ANY |
| `current_iteration_value` | La valeur portée par l’itération courante, ou None lorsqu’aucune valeur n’a été fournie. | ANY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopIteration/fr.md)

---
**Source fingerprint (SHA-256):** `1d167860b89de0f7b435a3715f6d543cad7602648abb58575b572c0406631cda`
