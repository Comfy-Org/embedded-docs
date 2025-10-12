> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/fr.md)

Le nœud ModelMergeQwenImage fusionne deux modèles d'IA en combinant leurs composants avec des poids ajustables. Il vous permet de mélanger des parties spécifiques des modèles d'image Qwen, y compris les blocs transformeurs, les embeddings positionnels et les composants de traitement de texte. Vous pouvez contrôler l'influence de chaque modèle sur différentes sections du résultat fusionné.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Oui | - | Premier modèle à fusionner (par défaut : aucun) |
| `model2` | MODEL | Oui | - | Deuxième modèle à fusionner (par défaut : aucun) |
| `pos_embeds.` | FLOAT | Oui | 0.0 à 1.0 | Poids pour le mélange des embeddings positionnels (par défaut : 1.0) |
| `img_in.` | FLOAT | Oui | 0.0 à 1.0 | Poids pour le mélange du traitement des entrées d'image (par défaut : 1.0) |
| `txt_norm.` | FLOAT | Oui | 0.0 à 1.0 | Poids pour le mélange de la normalisation de texte (par défaut : 1.0) |
| `txt_in.` | FLOAT | Oui | 0.0 à 1.0 | Poids pour le mélange du traitement des entrées de texte (par défaut : 1.0) |
| `time_text_embed.` | FLOAT | Oui | 0.0 à 1.0 | Poids pour le mélange des embeddings de temps et de texte (par défaut : 1.0) |
| `transformer_blocks.0.` à `transformer_blocks.59.` | FLOAT | Oui | 0.0 à 1.0 | Poids pour le mélange de chaque bloc transformeur (par défaut : 1.0) |
| `proj_out.` | FLOAT | Oui | 0.0 à 1.0 | Poids pour le mélange de la projection de sortie (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle fusionné combinant les composants des deux modèles d'entrée avec les poids spécifiés |
