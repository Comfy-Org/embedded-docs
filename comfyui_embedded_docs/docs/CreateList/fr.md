# Créer une liste

Le nœud « Create List » combine plusieurs entrées en une seule liste séquentielle. Il accepte un nombre quelconque d’entrées du même type de données et les concatène dans l’ordre où elles sont connectées. Ce nœud est utile pour préparer des lots de données, comme des images ou du texte, à traiter par d’autres nœuds du flux de travail.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `entrées` | Un nombre variable d’emplacements d’entrée nommés `input`, `input_2`, `input_3`, etc. Chaque emplacement accepte une liste d’éléments du même type de données. Vous pouvez ajouter d’autres emplacements en cliquant sur l’icône plus (+). Tous les emplacements doivent utiliser le même type de données (p. ex. tous de type IMAGE ou tous de type STRING). | Variable | Oui | Nombre d’emplacements illimité ; chaque emplacement accepte un nombre illimité d’éléments |

**Remarque :** Le nœud crée automatiquement de nouveaux emplacements d’entrée lorsque vous connectez des éléments. Toutes les entrées connectées doivent partager le même type de données pour que le nœud fonctionne correctement. Chaque emplacement connecté fournit une liste d’éléments, et le nœud combine les listes dans l’ordre des emplacements (`input`, puis `input_2`, puis `input_3`, ...). Le nœud est également accessible par recherche sous les alias « Image Iterator », « Text Iterator » et « Iterator ».

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `liste` | Une liste unique contenant tous les éléments des entrées connectées, concaténés dans l’ordre où ils ont été fournis. Le type de données de sortie correspond au type de données d’entrée. | Variable |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/fr.md)

---
**Source fingerprint (SHA-256):** `457d17da815ef9cee000d9e8dc8768f19ddfe247feae4b2ff4ce3c6cc0fd564e`
