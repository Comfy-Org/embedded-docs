# ModelMergeCosmos14B

Le nœud **ModelMergeCosmos14B** fusionne deux modèles d'IA en utilisant une approche par blocs spécialement conçue pour l'architecture du modèle Cosmos 14B. Il permet de mélanger différents composants des modèles en ajustant les valeurs de poids entre 0.0 et 1.0 pour chaque bloc de modèle et couche d'incorporation.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle1` | Premier modèle à fusionner | MODEL | Oui | - |
| `modèle2` | Second modèle à fusionner | MODEL | Oui | - |
| `pos_embedder.` | Poids pour le composant d'incorporation de position (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `extra_pos_embedder.` | Poids pour le composant d'incorporation de position supplémentaire (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `x_embedder.` | Poids pour le composant d'incorporation x (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids pour le composant d'incorporation t (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `affline_norm.` | Poids pour le composant de normalisation affine (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block0.` | Poids pour le bloc 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block1.` | Poids pour le bloc 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block2.` | Poids pour le bloc 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block3.` | Poids pour le bloc 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block4.` | Poids pour le bloc 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block5.` | Poids pour le bloc 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block6.` | Poids pour le bloc 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block7.` | Poids pour le bloc 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block8.` | Poids pour le bloc 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block9.` | Poids pour le bloc 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block10.` | Poids pour le bloc 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block11.` | Poids pour le bloc 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block12.` | Poids pour le bloc 12 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block13.` | Poids pour le bloc 13 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block14.` | Poids pour le bloc 14 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block15.` | Poids pour le bloc 15 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block16.` | Poids pour le bloc 16 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block17.` | Poids pour le bloc 17 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block18.` | Poids pour le bloc 18 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block19.` | Poids pour le bloc 19 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block20.` | Poids pour le bloc 20 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block21.` | Poids pour le bloc 21 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block22.` | Poids pour le bloc 22 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block23.` | Poids pour le bloc 23 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block24.` | Poids pour le bloc 24 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block25.` | Poids pour le bloc 25 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block26.` | Poids pour le bloc 26 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block27.` | Poids pour le bloc 27 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block28.` | Poids pour le bloc 28 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block29.` | Poids pour le bloc 29 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block30.` | Poids pour le bloc 30 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block31.` | Poids pour le bloc 31 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block32.` | Poids pour le bloc 32 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block33.` | Poids pour le bloc 33 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block34.` | Poids pour le bloc 34 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.block35.` | Poids pour le bloc 35 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_layer.` | Poids pour la couche finale (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/fr.md)

---
**Source fingerprint (SHA-256):** `6fcb4fefe7738d0addef49d386c0d3d22cda4c68f0e49ad003d1df595cf0e9d9`
