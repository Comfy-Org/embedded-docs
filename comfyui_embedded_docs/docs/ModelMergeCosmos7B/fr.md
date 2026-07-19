# ModelMergeCosmos7B

Le nœud ModelMergeCosmos7B fusionne deux modèles d'IA en utilisant un mélange pondéré de composants spécifiques. Il permet un contrôle précis sur la façon dont les différentes parties des modèles sont combinées en ajustant des poids individuels pour les plongements de position, les blocs de transformeur et les couches finales.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Deuxième modèle à fusionner | MODEL | Oui | - |
| `pos_embedder.` | Poids pour le composant de plongement de position (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `extra_pos_embedder.` | Poids pour le composant de plongement de position supplémentaire (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `x_embedder.` | Poids pour le composant de plongement x (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids pour le composant de plongement t (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `affline_norm.` | Poids pour le composant de normalisation affine (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block0.` | Poids pour le bloc de transformeur 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block1.` | Poids pour le bloc de transformeur 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block2.` | Poids pour le bloc de transformeur 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block3.` | Poids pour le bloc de transformeur 3 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block4.` | Poids pour le bloc de transformeur 4 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block5.` | Poids pour le bloc de transformeur 5 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block6.` | Poids pour le bloc de transformeur 6 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block7.` | Poids pour le bloc de transformeur 7 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block8.` | Poids pour le bloc de transformeur 8 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block9.` | Poids pour le bloc de transformeur 9 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block10.` | Poids pour le bloc de transformeur 10 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block11.` | Poids pour le bloc de transformeur 11 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block12.` | Poids pour le bloc de transformeur 12 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block13.` | Poids pour le bloc de transformeur 13 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block14.` | Poids pour le bloc de transformeur 14 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block15.` | Poids pour le bloc de transformeur 15 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block16.` | Poids pour le bloc de transformeur 16 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block17.` | Poids pour le bloc de transformeur 17 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block18.` | Poids pour le bloc de transformeur 18 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block19.` | Poids pour le bloc de transformeur 19 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block20.` | Poids pour le bloc de transformeur 20 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block21.` | Poids pour le bloc de transformeur 21 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block22.` | Poids pour le bloc de transformeur 22 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block23.` | Poids pour le bloc de transformeur 23 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block24.` | Poids pour le bloc de transformeur 24 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block25.` | Poids pour le bloc de transformeur 25 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block26.` | Poids pour le bloc de transformeur 26 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block27.` | Poids pour le bloc de transformeur 27 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_layer.` | Poids pour le composant de couche finale (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/fr.md)

---
**Source fingerprint (SHA-256):** `0721b047933179706c76f622efb5b7425aad530d302d8b33ec12dd68513dec0b`
