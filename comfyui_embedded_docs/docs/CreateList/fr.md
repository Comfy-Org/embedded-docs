# Créer une liste

Le nœud Create List combine plusieurs entrées en une liste unique et séquentielle. Il accepte un nombre quelconque d’entrées du même type de données et les concatène dans l’ordre où elles sont connectées. Ce nœud est utile pour préparer des lots de données, telles que des images ou du texte, à traiter par d’autres nœuds dans un workflow.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `inputs` | Un ensemble extensible d’emplacements d’entrée. Ajoutez plus d’emplacements en cliquant sur l’icône plus (+), ou connectez des éléments et de nouveaux emplacements sont créés automatiquement. Chaque emplacement accepte un ou plusieurs éléments, et tous les emplacements doivent partager le même type de données (par exemple, tous IMAGE ou tous STRING). | Varie (correspond au type de données connecté) | Oui | Nombre illimité d’emplacements ; chaque emplacement accepte un ou plusieurs éléments |

**Remarque :** Le nœud crée automatiquement de nouveaux emplacements d’entrée lorsque vous connectez des éléments. Toutes les entrées connectées doivent partager le même type de données pour que le nœud fonctionne correctement, et la liste de sortie adopte ce même type.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `list` | Une liste unique contenant tous les éléments des emplacements d’entrée connectés, concaténés dans l’ordre où les emplacements sont connectés. Le type de données de sortie correspond au type de données d’entrée. | Varie (correspond au type de données d’entrée) |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/fr.md)

---
**Source fingerprint (SHA-256):** `457d17da815ef9cee000d9e8dc8768f19ddfe247feae4b2ff4ce3c6cc0fd564e`
