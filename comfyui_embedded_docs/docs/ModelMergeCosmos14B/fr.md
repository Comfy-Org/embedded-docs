> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/fr.md)

Le nœud **ModelMergeCosmos14B** fusionne deux modèles d'IA en utilisant une approche par blocs spécialement conçue pour l'architecture du modèle Cosmos 14B. Il permet de mélanger différents composants des modèles en ajustant les valeurs de poids entre 0.0 et 1.0 pour chaque bloc de modèle et couche d'incorporation.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle1` | MODEL | Oui | - | Premier modèle à fusionner |
| `modèle2` | MODEL | Oui | - | Second modèle à fusionner |
| `pos_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant d'incorporation de position (par défaut : 1.0) |
| `extra_pos_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant d'incorporation de position supplémentaire (par défaut : 1.0) |
| `x_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant d'incorporation x (par défaut : 1.0) |
| `t_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant d'incorporation t (par défaut : 1.0) |
| `affline_norm.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le composant de normalisation affine (par défaut : 1.0) |
| `blocks.block0.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 0 (par défaut : 1.0) |
| `blocks.block1.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 1 (par défaut : 1.0) |
| `blocks.block2.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 2 (par défaut : 1.0) |
| `blocks.block3.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 3 (par défaut : 1.0) |
| `blocks.block4.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 4 (par défaut : 1.0) |
| `blocks.block5.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 5 (par défaut : 1.0) |
| `blocks.block6.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 6 (par défaut : 1.0) |
| `blocks.block7.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 7 (par défaut : 1.0) |
| `blocks.block8.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 8 (par défaut : 1.0) |
| `blocks.block9.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 9 (par défaut : 1.0) |
| `blocks.block10.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 10 (par défaut : 1.0) |
| `blocks.block11.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 11 (par défaut : 1.0) |
| `blocks.block12.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 12 (par défaut : 1.0) |
| `blocks.block13.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 13 (par défaut : 1.0) |
| `blocks.block14.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 14 (par défaut : 1.0) |
| `blocks.block15.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 15 (par défaut : 1.0) |
| `blocks.block16.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 16 (par défaut : 1.0) |
| `blocks.block17.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 17 (par défaut : 1.0) |
| `blocks.block18.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 18 (par défaut : 1.0) |
| `blocks.block19.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 19 (par défaut : 1.0) |
| `blocks.block20.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 20 (par défaut : 1.0) |
| `blocks.block21.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 21 (par défaut : 1.0) |
| `blocks.block22.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 22 (par défaut : 1.0) |
| `blocks.block23.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 23 (par défaut : 1.0) |
| `blocks.block24.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 24 (par défaut : 1.0) |
| `blocks.block25.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 25 (par défaut : 1.0) |
| `blocks.block26.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 26 (par défaut : 1.0) |
| `blocks.block27.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 27 (par défaut : 1.0) |
| `blocks.block28.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 28 (par défaut : 1.0) |
| `blocks.block29.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 29 (par défaut : 1.0) |
| `blocks.block30.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 30 (par défaut : 1.0) |
| `blocks.block31.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 31 (par défaut : 1.0) |
| `blocks.block32.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 32 (par défaut : 1.0) |
| `blocks.block33.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 33 (par défaut : 1.0) |
| `blocks.block34.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 34 (par défaut : 1.0) |
| `blocks.block35.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour le bloc 35 (par défaut : 1.0) |
| `final_layer.` | FLOAT | Oui | 0.0 - 1.0 | Poids pour la couche finale (par défaut : 1.0) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `model` | MODEL | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée |

---
**Source fingerprint (SHA-256):** `6fcb4fefe7738d0addef49d386c0d3d22cda4c68f0e49ad003d1df595cf0e9d9`
