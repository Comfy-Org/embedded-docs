> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/fr.md)

Le nœud ModelMergeCosmos7B fusionne deux modèles d'IA en utilisant un mélange pondéré de composants spécifiques. Il permet un contrôle précis de la manière dont les différentes parties des modèles sont combinées en ajustant les poids individuels pour les embeddings de position, les blocs de transformation et les couches finales.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Oui | - | Premier modèle à fusionner |
| `model2` | MODEL | Oui | - | Second modèle à fusionner |
| `pos_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant d'embedding de position (par défaut : 1.0) |
| `extra_pos_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant d'embedding de position supplémentaire (par défaut : 1.0) |
| `x_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant d'embedding X (par défaut : 1.0) |
| `t_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant d'embedding T (par défaut : 1.0) |
| `affline_norm.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant de normalisation affine (par défaut : 1.0) |
| `blocks.block0.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 0 (par défaut : 1.0) |
| `blocks.block1.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 1 (par défaut : 1.0) |
| `blocks.block2.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 2 (par défaut : 1.0) |
| `blocks.block3.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 3 (par défaut : 1.0) |
| `blocks.block4.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 4 (par défaut : 1.0) |
| `blocks.block5.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 5 (par défaut : 1.0) |
| `blocks.block6.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 6 (par défaut : 1.0) |
| `blocks.block7.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 7 (par défaut : 1.0) |
| `blocks.block8.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 8 (par défaut : 1.0) |
| `blocks.block9.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 9 (par défaut : 1.0) |
| `blocks.block10.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 10 (par défaut : 1.0) |
| `blocks.block11.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 11 (par défaut : 1.0) |
| `blocks.block12.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 12 (par défaut : 1.0) |
| `blocks.block13.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 13 (par défaut : 1.0) |
| `blocks.block14.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 14 (par défaut : 1.0) |
| `blocks.block15.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 15 (par défaut : 1.0) |
| `blocks.block16.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 16 (par défaut : 1.0) |
| `blocks.block17.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 17 (par défaut : 1.0) |
| `blocks.block18.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 18 (par défaut : 1.0) |
| `blocks.block19.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 19 (par défaut : 1.0) |
| `blocks.block20.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 20 (par défaut : 1.0) |
| `blocks.block21.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 21 (par défaut : 1.0) |
| `blocks.block22.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 22 (par défaut : 1.0) |
| `blocks.block23.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 23 (par défaut : 1.0) |
| `blocks.block24.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 24 (par défaut : 1.0) |
| `blocks.block25.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 25 (par défaut : 1.0) |
| `blocks.block26.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 26 (par défaut : 1.0) |
| `blocks.block27.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc de transformation 27 (par défaut : 1.0) |
| `final_layer.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant de couche finale (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée |
