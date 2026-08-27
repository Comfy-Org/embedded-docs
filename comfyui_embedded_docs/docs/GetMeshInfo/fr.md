# GetMeshInfo

Get Mesh Info indique le nombre de sommets et de faces d’un maillage, ainsi que les attributs qu’il contient (tels que les UV, les couleurs de sommets, les normales et les textures). Le rapport est affiché sur le nœud et renvoyé sous forme de sortie texte, tandis que le maillage lui-même est transmis tel quel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage à inspecter. Le nœud compte ses sommets et ses faces, détecte les attributs présents et transmet le maillage sans modification. | MESH | Oui | — |

Remarque : lorsque l’entrée contient plusieurs maillages (un lot), le rapport indique les totaux de sommets et de faces pour l’ensemble du lot, ainsi qu’une ventilation par maillage. Pour les lots avec remplissage de zéros, les comptes par élément stockés dans les données du maillage sont utilisés.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage d’origine, transmis sans aucune modification. | MESH |
| `info` | Un rapport textuel sur plusieurs lignes indiquant le nombre de sommets, le nombre de faces et les attributs détectés (uvs, vertex_colors, normals, tangents, texture, metallic_roughness, normal_map). Les grands nombres sont formatés avec des virgules, par exemple « 1,234,567 (1.23M) ». Le même texte est affiché sur le nœud. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetMeshInfo/fr.md)

---
**Source fingerprint (SHA-256):** `cd168a5e69131a4a37f1f47014af2bc2ac2c8aa69e146cf33c2072480b35ebb2`
