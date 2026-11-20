# Model Merge MiniMax H3

Fusionnez deux modèles MiniMax H3 compatibles par composant, avec un ratio distinct pour chaque partie de l'architecture. Augmenter un ratio prélève davantage de ce composant depuis `model2`, ce qui vous permet de conserver les projections de patch et les blocs de raffinement d'un modèle tout en remplaçant les blocs Transformer par ceux d'un autre.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model1` | Premier modèle MiniMax H3, la base à partir de laquelle chaque composant est pris (le poids par défaut s'applique là où `model2` n'est pas utilisé). | MODEL | Oui | - |
| `model2` | Second modèle MiniMax H3 qui fournit les composants que vous mélangez. | MODEL | Oui | - |
| `video_patch_proj.` | Part de `model2` pour la projection de patch vidéo (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `audio_patch_proj.` | Part de `model2` pour la projection de patch audio (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `condition_proj.` | Part de `model2` pour la projection de conditionnement (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `time_embedder.` | Part de `model2` pour l'intégrateur temporel (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `token_refiner.blocks.0.` | Part de `model2` pour le premier bloc de raffinement de tokens (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `token_refiner.blocks.1.` | Part de `model2` pour le second bloc de raffinement de tokens (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `token_refiner.final_norm.` | Part de `model2` pour la normalisation finale du raffineur de tokens (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `blocks.0.` à `blocks.49.` | Part de `model2` pour chacun des 50 blocs Transformer, un widget par bloc (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `final_layer.norm.` | Part de `model2` pour la normalisation de la couche finale (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `final_layer.adaln_proj.` | Part de `model2` pour la projection de normalisation adaptative finale (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `final_layer.video_out.` | Part de `model2` pour la couche de sortie vidéo (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `final_layer.audio_out.` | Part de `model2` pour la couche de sortie audio (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

Un ratio de 0.0 fait que ce composant provient entièrement de `model1`, et 1.0 qu'il provient entièrement de `model2` ; les valeurs intermédiaires mélangent les deux. Les tenseurs sans ratio, comme les statistiques de normalisation, proviennent toujours de `model1`. Les deux entrées doivent être des modèles MiniMax H3 de même architecture ; sinon, la fusion produit un modèle qui ne fonctionnera pas.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le modèle MiniMax H3 fusionné. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMiniMaxH3/fr.md)

---
**Source fingerprint (SHA-256):** `4fea4e588d16a8396c68aa071a59e671a2a0c645734606be6d7e221986ba88bd`
