Le nœud `CLIPTextEncodeHunyuanDiT` convertit des descriptions textuelles dans un format compréhensible par le modèle HunyuanDiT. Il s'agit d'un nœud de conditionnement avancé conçu pour l'architecture à double encodeur de texte de HunyuanDiT, traitant deux entrées textuelles distinctes via des tokenizers différents.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Instance du modèle CLIP utilisée pour la tokenisation et l'encodage du texte, essentielle à la génération des conditions. | CLIP | Oui | - |
| `bert` | Texte à encoder via le tokenizer BERT. Privilégie les phrases et mots-clés. Prend en charge le multiligne et les invites dynamiques. | STRING | Oui | - |
| `mt5xl` | Texte à encoder via le tokenizer mT5-XL. Prend en charge le multiligne et les invites dynamiques (multilingue). Peut utiliser des phrases complètes et des descriptions complexes. | STRING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Sortie de conditionnement encodée, combinant le texte tokenisé par BERT et mT5-XL, utilisée pour un traitement ultérieur dans les tâches de génération. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/fr.md)

---
**Source fingerprint (SHA-256):** `6a8d649708b315c42b7933b52fad7e0b45aa34c168616f18a2178041148eeea1`
