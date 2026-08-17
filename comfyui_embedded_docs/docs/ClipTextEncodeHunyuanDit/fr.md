# CLIPTextEncodeHunyuanDiT

Le nœud `CLIPTextEncodeHunyuanDiT` convertit les descriptions textuelles dans un format compréhensible par le modèle HunyuanDiT. Il s'agit d'un nœud de conditionnement avancé conçu pour l'architecture à double encodeur de texte de HunyuanDiT, qui traite deux entrées de texte séparées via différents tokeniseurs et les combine en une seule sortie de conditionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Une instance de modèle CLIP utilisée pour la tokenisation et l'encodage du texte, essentielle à la génération des conditions. | CLIP | Oui | - |
| `bert` | Entrée de texte à encoder via le tokeniseur BERT. Préfère les phrases et mots-clés. Prend en charge le multiligne et les prompts dynamiques. | STRING | Oui | - |
| `mt5xl` | Entrée de texte à encoder via le tokeniseur mT5-XL. Prend en charge le multiligne et les prompts dynamiques (multilingues). Peut utiliser des phrases complètes et des descriptions complexes. | STRING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | La sortie de conditionnement encodée, combinant les textes tokenisés de BERT et de mT5-XL, utilisée pour le traitement ultérieur dans les tâches de génération. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/fr.md)

---
**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`
