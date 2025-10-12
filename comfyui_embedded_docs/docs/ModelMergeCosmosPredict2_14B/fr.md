> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/fr.md)

Le nœud ModelMergeCosmosPredict2_14B vous permet de fusionner deux modèles d'IA en ajustant l'influence des différents composants du modèle. Il offre un contrôle précis sur la contribution de chaque partie du second modèle au modèle fusionné final, en utilisant des poids de mélange pour des couches et composants spécifiques du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Oui | - | Le modèle de base à fusionner |
| `model2` | MODEL | Oui | - | Le modèle secondaire à fusionner dans le modèle de base |
| `pos_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange de l'encodeur de position (par défaut : 1.0) |
| `x_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange de l'encodeur d'entrée (par défaut : 1.0) |
| `t_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange de l'encodeur temporel (par défaut : 1.0) |
| `t_embedding_norm.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange de la normalisation de l'embedding temporel (par défaut : 1.0) |
| `blocks.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 0 (par défaut : 1.0) |
| `blocks.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 1 (par défaut : 1.0) |
| `blocks.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 2 (par défaut : 1.0) |
| `blocks.3.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 3 (par défaut : 1.0) |
| `blocks.4.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 4 (par défaut : 1.0) |
| `blocks.5.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 5 (par défaut : 1.0) |
| `blocks.6.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 6 (par défaut : 1.0) |
| `blocks.7.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 7 (par défaut : 1.0) |
| `blocks.8.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 8 (par défaut : 1.0) |
| `blocks.9.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 9 (par défaut : 1.0) |
| `blocks.10.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 10 (par défaut : 1.0) |
| `blocks.11.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 11 (par défaut : 1.0) |
| `blocks.12.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 12 (par défaut : 1.0) |
| `blocks.13.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 13 (par défaut : 1.0) |
| `blocks.14.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 14 (par défaut : 1.0) |
| `blocks.15.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 15 (par défaut : 1.0) |
| `blocks.16.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 16 (par défaut : 1.0) |
| `blocks.17.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 17 (par défaut : 1.0) |
| `blocks.18.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 18 (par défaut : 1.0) |
| `blocks.19.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 19 (par défaut : 1.0) |
| `blocks.20.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 20 (par défaut : 1.0) |
| `blocks.21.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 21 (par défaut : 1.0) |
| `blocks.22.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 22 (par défaut : 1.0) |
| `blocks.23.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 23 (par défaut : 1.0) |
| `blocks.24.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 24 (par défaut : 1.0) |
| `blocks.25.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 25 (par défaut : 1.0) |
| `blocks.26.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 26 (par défaut : 1.0) |
| `blocks.27.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 27 (par défaut : 1.0) |
| `blocks.28.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 28 (par défaut : 1.0) |
| `blocks.29.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 29 (par défaut : 1.0) |
| `blocks.30.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 30 (par défaut : 1.0) |
| `blocks.31.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 31 (par défaut : 1.0) |
| `blocks.32.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 32 (par défaut : 1.0) |
| `blocks.33.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 33 (par défaut : 1.0) |
| `blocks.34.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 34 (par défaut : 1.0) |
| `blocks.35.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange du bloc 35 (par défaut : 1.0) |
| `final_layer.` | FLOAT | Oui | 0.0 - 1.0 | Poids de mélange de la couche finale (par défaut : 1.0) |

**Note :** Tous les paramètres de poids de mélange acceptent des valeurs entre 0.0 et 1.0, où 0.0 signifie aucune contribution du modèle2 et 1.0 signifie une contribution complète du modèle2 pour ce composant spécifique.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée |