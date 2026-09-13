# FusionModèleQwenImage

Ce nœud fusionne deux modèles d'image Qwen en mélangeant leurs composants individuels avec des poids ajustables. Chaque poids contrôle dans quelle mesure la partie correspondante du deuxième modèle contribue au résultat fusionné, vous permettant de mélanger séparément les embeddings positionnels, les couches de traitement de texte, les couches d'entrée d'image, les 60 blocs Transformer et la projection de sortie. Le résultat final est un unique MODEL que vous pouvez utiliser partout où un modèle normal est attendu.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Le deuxième modèle à fusionner | MODEL | Oui | - |
| `pos_embeds.` | Poids pour le mélange des embeddings positionnels (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `img_in.` | Poids pour le mélange du traitement d'entrée d'image (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `txt_norm.` | Poids pour le mélange de la normalisation de texte (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `txt_in.` | Poids pour le mélange du traitement d'entrée de texte (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `time_text_embed.` | Poids pour le mélange des embeddings de temps et de texte (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `transformer_blocks.0.` à `transformer_blocks.59.` | Poids pour le mélange de chaque bloc Transformer (par défaut : 1.0). Le nœud expose un poids pour chacun des 60 blocs Transformer. | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `proj_out.` | Poids pour le mélange de la projection de sortie (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

Remarque : toutes les entrées de poids sont obligatoires et partagent les mêmes limites — une valeur par défaut de 1.0 avec une plage valide de 0.0 à 1.0, ajustable par pas de 0.01.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les composants des deux modèles d'entrée avec les poids spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/fr.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
