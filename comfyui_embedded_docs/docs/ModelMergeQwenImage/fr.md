Le nœud ModelMergeQwenImage fusionne deux modèles d'IA en combinant leurs composants avec des poids ajustables. Il vous permet de mélanger des parties spécifiques des modèles d'images Qwen, notamment les blocs de transformeurs, les embeddings positionnels et les composants de traitement de texte. Vous pouvez contrôler le degré d'influence de chaque modèle sur les différentes sections du résultat fusionné.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle1` | Premier modèle à fusionner (par défaut : aucun) | MODEL | Oui | - |
| `modèle2` | Deuxième modèle à fusionner (par défaut : aucun) | MODEL | Oui | - |
| `pos_embeds.` | Poids pour le mélange des embeddings positionnels (par défaut : 1,0) | FLOAT | Oui | 0,0 à 1,0 |
| `img_in.` | Poids pour le mélange du traitement d'entrée d'image (par défaut : 1,0) | FLOAT | Oui | 0,0 à 1,0 |
| `txt_norm.` | Poids pour le mélange de la normalisation de texte (par défaut : 1,0) | FLOAT | Oui | 0,0 à 1,0 |
| `txt_in.` | Poids pour le mélange du traitement d'entrée de texte (par défaut : 1,0) | FLOAT | Oui | 0,0 à 1,0 |
| `time_text_embed.` | Poids pour le mélange des embeddings temporels et textuels (par défaut : 1,0) | FLOAT | Oui | 0,0 à 1,0 |
| `transformer_blocks.0.` à `transformer_blocks.59.` | Poids pour le mélange de chaque bloc de transformeur (par défaut : 1,0) | FLOAT | Oui | 0,0 à 1,0 |
| `proj_out.` | Poids pour le mélange de la projection de sortie (par défaut : 1,0) | FLOAT | Oui | 0,0 à 1,0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les composants des deux modèles d'entrée avec les poids spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/fr.md)

---
**Source fingerprint (SHA-256):** `a0424a3f4d4ffe170471ba463350d741f67ff1b1f5a8a016ad844c111033f97c`
