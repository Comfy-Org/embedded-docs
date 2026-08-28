# ClipTextEncodeHunyuanDit

Le nœud `CLIPTextEncodeHunyuanDiT` convertit les descriptions textuelles dans un format que le modèle HunyuanDiT peut comprendre. Il s'agit d'un nœud de conditionnement avancé conçu pour l’architecture à double encodeur de texte de HunyuanDiT, traitant deux entrées de texte distinctes via différents tokenizers et combinant leurs résultats en une seule sortie de conditionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Une instance de modèle CLIP utilisée pour la tokenisation et l’encodage du texte, essentielle à la génération de conditionnements. | CLIP | Oui | - |
| `bert` | Entrée de texte à encoder via le tokenizer BERT. Préfère les phrases et les mots-clés. Prend en charge les invites multilignes et dynamiques. | STRING | Oui | - |
| `mt5xl` | Entrée de texte à encoder via le tokenizer mT5-XL. Prend en charge les invites multilignes et dynamiques (multilingues). Peut utiliser des phrases complètes et des descriptions complexes. | STRING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | La sortie de conditionnement encodée, combinant le texte tokenisé par BERT et mT5-XL, utilisée pour un traitement ultérieur dans les tâches de génération. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncodeHunyuanDit/fr.md)

---
**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`
