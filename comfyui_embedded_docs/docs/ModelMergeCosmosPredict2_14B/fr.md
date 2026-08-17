# ModelMergeCosmosPredict2_14B

Le nœud `ModelMergeCosmosPredict2_14B` fusionne deux modèles d'IA en mélangeant leurs composants internes. Il offre un contrôle précis sur la mesure dans laquelle chaque partie du second modèle influence le résultat final fusionné, grâce à des valeurs de poids ajustables pour des couches et des composants spécifiques.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le modèle de base à fusionner | MODEL | Oui | - |
| `model2` | Le modèle secondaire à fusionner dans le modèle de base | MODEL | Oui | - |
| `pos_embedder.` | Poids de fusion de l'intégrateur de position (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `x_embedder.` | Poids de fusion de l'intégrateur d'entrée (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids de fusion de l'intégrateur temporel (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedding_norm.` | Poids de fusion de la normalisation de l'intégration temporelle (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.0.` | Poids de fusion du bloc 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.1.` | Poids de fusion du bloc 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.2.` | Poids de fusion du bloc 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.3.` | Poids de fusion du bloc 3 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.4.` | Poids de fusion du bloc 4 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.5.` | Poids de fusion du bloc 5 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.6.` | Poids de fusion du bloc 6 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.7.` | Poids de fusion du bloc 7 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.8.` | Poids de fusion du bloc 8 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.9.` | Poids de fusion du bloc 9 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.10.` | Poids de fusion du bloc 10 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.11.` | Poids de fusion du bloc 11 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.12.` | Poids de fusion du bloc 12 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.13.` | Poids de fusion du bloc 13 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.14.` | Poids de fusion du bloc 14 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.15.` | Poids de fusion du bloc 15 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.16.` | Poids de fusion du bloc 16 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.17.` | Poids de fusion du bloc 17 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.18.` | Poids de fusion du bloc 18 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.19.` | Poids de fusion du bloc 19 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.20.` | Poids de fusion du bloc 20 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.21.` | Poids de fusion du bloc 21 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.22.` | Poids de fusion du bloc 22 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.23.` | Poids de fusion du bloc 23 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.24.` | Poids de fusion du bloc 24 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.25.` | Poids de fusion du bloc 25 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.26.` | Poids de fusion du bloc 26 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.27.` | Poids de fusion du bloc 27 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.28.` | Poids de fusion du bloc 28 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.29.` | Poids de fusion du bloc 29 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.30.` | Poids de fusion du bloc 30 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.31.` | Poids de fusion du bloc 31 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.32.` | Poids de fusion du bloc 32 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.33.` | Poids de fusion du bloc 33 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.34.` | Poids de fusion du bloc 34 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.35.` | Poids de fusion du bloc 35 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_layer.` | Poids de fusion de la couche finale (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

**Remarque :** Tous les paramètres de poids de fusion acceptent des valeurs comprises entre 0.0 et 1.0, où 0.0 signifie aucune contribution de `model2` et 1.0 signifie une contribution complète de `model2` pour ce composant spécifique.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/fr.md)

---
**Source fingerprint (SHA-256):** `a5f34deda62dc03f22613517e43996b908a8673dc5da10d8f1b7f6411ece2f0a`
