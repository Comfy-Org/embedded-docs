# FusionModèleQwenImage

ModelMergeQwenImage fusionne deux modèles d'IA en combinant leurs composants avec des poids réglables. Il permet de mélanger des parties spécifiques des modèles d'image Qwen, notamment les blocs transformer, les plongements positionnels et les composants de traitement de texte. Vous pouvez contrôler le degré d'influence de chaque modèle sur les différentes sections du résultat fusionné.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle1` | Le premier modèle à fusionner | MODEL | Oui | - |
| `modèle2` | Le deuxième modèle à fusionner | MODEL | Oui | - |
| `pos_embeds.` | Poids pour la fusion des plongements positionnels (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (step: 0.01) |
| `img_in.` | Poids pour la fusion du traitement des entrées d'image (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (step: 0.01) |
| `txt_norm.` | Poids pour la fusion de la normalisation de texte (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (step: 0.01) |
| `txt_in.` | Poids pour la fusion du traitement des entrées de texte (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (step: 0.01) |
| `time_text_embed.` | Poids pour la fusion des plongements temporels et textuels (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (step: 0.01) |
| `transformer_blocks.0.` à `transformer_blocks.59.` | Poids pour la fusion de chaque bloc transformer (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (step: 0.01) |
| `proj_out.` | Poids pour la fusion de la projection de sortie (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (step: 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les composants des deux modèles d'entrée avec les poids spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/fr.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
