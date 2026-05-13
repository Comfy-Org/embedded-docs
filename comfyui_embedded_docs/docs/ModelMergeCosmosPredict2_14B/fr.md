> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/fr.md)

Le nœud `ModelMergeCosmosPredict2_14B` fusionne deux modèles d'IA en mélangeant leurs composants internes. Il offre un contrôle précis sur l'influence de chaque partie du second modèle dans le résultat final fusionné, grâce à des valeurs de pondération ajustables pour des couches et composants spécifiques.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle1` | MODEL | Oui | - | Le modèle de base à fusionner |
| `modèle2` | MODEL | Oui | - | Le modèle secondaire à fusionner dans le modèle de base |
| `pos_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion de l'intégrateur de position (par défaut : 1.0) |
| `x_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion de l'intégrateur d'entrée (par défaut : 1.0) |
| `t_embedder.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion de l'intégrateur temporel (par défaut : 1.0) |
| `t_embedding_norm.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion de la normalisation de l'intégration temporelle (par défaut : 1.0) |
| `blocks.0.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 0 (par défaut : 1.0) |
| `blocks.1.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 1 (par défaut : 1.0) |
| `blocks.2.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 2 (par défaut : 1.0) |
| `blocks.3.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 3 (par défaut : 1.0) |
| `blocks.4.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 4 (par défaut : 1.0) |
| `blocks.5.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 5 (par défaut : 1.0) |
| `blocks.6.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 6 (par défaut : 1.0) |
| `blocks.7.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 7 (par défaut : 1.0) |
| `blocks.8.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 8 (par défaut : 1.0) |
| `blocks.9.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 9 (par défaut : 1.0) |
| `blocks.10.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 10 (par défaut : 1.0) |
| `blocks.11.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 11 (par défaut : 1.0) |
| `blocks.12.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 12 (par défaut : 1.0) |
| `blocks.13.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 13 (par défaut : 1.0) |
| `blocks.14.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 14 (par défaut : 1.0) |
| `blocks.15.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 15 (par défaut : 1.0) |
| `blocks.16.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 16 (par défaut : 1.0) |
| `blocks.17.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 17 (par défaut : 1.0) |
| `blocks.18.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 18 (par défaut : 1.0) |
| `blocks.19.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 19 (par défaut : 1.0) |
| `blocks.20.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 20 (par défaut : 1.0) |
| `blocks.21.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 21 (par défaut : 1.0) |
| `blocks.22.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 22 (par défaut : 1.0) |
| `blocks.23.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 23 (par défaut : 1.0) |
| `blocks.24.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 24 (par défaut : 1.0) |
| `blocks.25.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 25 (par défaut : 1.0) |
| `blocks.26.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 26 (par défaut : 1.0) |
| `blocks.27.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 27 (par défaut : 1.0) |
| `blocks.28.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 28 (par défaut : 1.0) |
| `blocks.29.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 29 (par défaut : 1.0) |
| `blocks.30.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 30 (par défaut : 1.0) |
| `blocks.31.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 31 (par défaut : 1.0) |
| `blocks.32.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 32 (par défaut : 1.0) |
| `blocks.33.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 33 (par défaut : 1.0) |
| `blocks.34.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 34 (par défaut : 1.0) |
| `blocks.35.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion du bloc 35 (par défaut : 1.0) |
| `final_layer.` | FLOAT | Oui | 0.0 - 1.0 | Poids de fusion de la couche finale (par défaut : 1.0) |

**Remarque :** Tous les paramètres de poids de fusion acceptent des valeurs comprises entre 0.0 et 1.0, où 0.0 signifie aucune contribution de `model2` et 1.0 signifie une contribution totale de `model2` pour ce composant spécifique.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `model` | MODEL | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée |

---
**Source fingerprint (SHA-256):** `5e72608391bc47c2610c93fda19e6e12a1695f95f6135a08efe97e3d400acf84`
