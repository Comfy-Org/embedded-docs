# FusionModèleQwenImage

Le nœud **ModelMergeQwenImage** fusionne deux modèles d'IA en combinant leurs composants avec des poids ajustables. Il vous permet de mélanger des parties spécifiques des modèles d'image Qwen, notamment les blocs de transformeur, les plongements positionnels et les composants de traitement de texte. Vous pouvez contrôler le degré d'influence de chaque modèle sur les différentes sections du résultat fusionné.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le premier modèle à fusionner (défaut : aucun) | MODEL | Oui | - |
| `model2` | Le deuxième modèle à fusionner (défaut : aucun) | MODEL | Oui | - |
| `pos_embeds.` | Poids pour le mélange des plongements positionnels (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `img_in.` | Poids pour le mélange du traitement d'entrée d'image (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `txt_norm.` | Poids pour le mélange de la normalisation de texte (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `txt_in.` | Poids pour le mélange du traitement d'entrée de texte (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `time_text_embed.` | Poids pour le mélange des plongements de temps et de texte (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `transformer_blocks.0.` à `transformer_blocks.59.` | Poids pour le mélange de chaque bloc de transformeur (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `proj_out.` | Poids pour le mélange de la projection de sortie (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |

Remarque : Il y a 60 entrées de poids individuelles pour les blocs de transformeur (`transformer_blocks.0.` à `transformer_blocks.59.`), une pour chaque bloc de transformeur du modèle.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les composants des deux modèles d'entrée avec les poids spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/fr.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
