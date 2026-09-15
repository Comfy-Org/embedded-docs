# Créer une liste

Le nœud Create List combine plusieurs entrées en une seule liste séquentielle. Il accepte un nombre quelconque d’emplacements d’entrée partageant le même type de données et concatène leurs éléments dans l’ordre dans lequel les emplacements sont connectés. Le résultat est une liste contenant tous les éléments connectés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `entrées` | Un nombre variable d’emplacements d’entrée nommés `input`, `input_2`, `input_3`, etc. Chaque emplacement accepte une liste d’éléments du même type de données (par exemple, tous IMAGE ou tous STRING). De nouveaux emplacements sont créés automatiquement selon les besoins. Le nœud concatène les listes dans l’ordre des emplacements. | Any | Oui | Nombre quelconque d’emplacements ; chaque emplacement accepte un nombre quelconque d’éléments |

**Remarque :** Toutes les entrées connectées doivent partager le même type de données. Chaque emplacement connecté fournit une liste d’éléments, et le nœud combine les listes dans l’ordre des emplacements (`input`, puis `input_2`, puis `input_3`, ...). Le nœud peut également être recherché via les alias « Image Iterator », « Text Iterator » et « Iterator ».

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `list` | Une seule liste contenant tous les éléments des entrées connectées, concaténés dans l’ordre dans lequel les emplacements ont été fournis. Le type de données de sortie correspond au type de données d’entrée. | Any |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/fr.md)

---
**Source fingerprint (SHA-256):** `4824fa6af46ab08cd3c10b033dbb3e43682b468e1dbd934fffb571349e025b96`
