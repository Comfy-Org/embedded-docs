# CLIPSubtract

Le nœud CLIPSubtract effectue une opération de soustraction entre deux modèles CLIP. Il prend le premier modèle CLIP comme base et soustrait les correctifs clés du second modèle CLIP, avec un multiplicateur optionnel pour contrôler l'intensité de la soustraction. Cela permet un mélange fin des modèles en supprimant des caractéristiques spécifiques d'un modèle à l'aide d'un autre.

## Entrées

| Paramètre | Description | Type de données | Type d'entrée | Défaut | Plage |
| --- | --- | --- | --- | --- | --- |
| `clip1` | Le modèle CLIP de base qui sera modifié | CLIP | Requis | - | - |
| `clip2` | Le modèle CLIP dont les correctifs clés seront soustraits du modèle de base | CLIP | Requis | - | - |
| `multiplier` | Contrôle l'intensité de l'opération de soustraction. Les valeurs positives soustraient les caractéristiques de clip2, les valeurs négatives les ajoutent à la place. | FLOAT | Requis | 1.0 | -10.0 à 10.0, pas de 0.01 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CLIP` | Le modèle CLIP résultant après l'opération de soustraction | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/fr.md)

---
**Source fingerprint (SHA-256):** `ea7b6f838d6eb083d2d9bc07891b6ef2f3e625861ab1de9279df351e58f2a2a8`
