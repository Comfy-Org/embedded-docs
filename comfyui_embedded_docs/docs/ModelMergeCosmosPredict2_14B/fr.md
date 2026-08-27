# ModelMergeCosmosPredict2_14B

Le nœud ModelMergeCosmosPredict2_14B fusionne deux modèles d'IA en mélangeant leurs composants internes. Il vous offre un contrôle précis sur la mesure dans laquelle chaque partie du second modèle influence le résultat fusionné final, en utilisant des valeurs de poids réglables pour des couches et composants spécifiques.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle1` | Le modèle de base à fusionner | MODEL | Oui | - |
| `modèle2` | Le modèle secondaire à fusionner dans le modèle de base | MODEL | Oui | - |
| `pos_embedder.` | Poids de mélange de l'embedder de position (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `x_embedder.` | Poids de mélange de l'embedder d'entrée (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids de mélange de l'embedder temporel (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedding_norm.` | Poids de mélange de la normalisation de l'embedding temporel (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.0.` | Poids de mélange du bloc 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.1.` | Poids de mélange du bloc 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.2.` | Poids de mélange du bloc 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.3.` | Poids de mélange du bloc 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.4.` | Poids de mélange du bloc 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.5.` | Poids de mélange du bloc 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.6.` | Poids de mélange du bloc 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.7.` | Poids de mélange du bloc 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.8.` | Poids de mélange du bloc 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.9.` | Poids de mélange du bloc 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.10.` | Poids de mélange du bloc 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.11.` | Poids de mélange du bloc 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.12.` | Poids de mélange du bloc 12 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.13.` | Poids de mélange du bloc 13 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.14.` | Poids de mélange du bloc 14 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.15.` | Poids de mélange du bloc 15 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.16.` | Poids de mélange du bloc 16 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.17.` | Poids de mélange du bloc 17 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.18.` | Poids de mélange du bloc 18 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.19.` | Poids de mélange du bloc 19 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.20.` | Poids de mélange du bloc 20 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.21.` | Poids de mélange du bloc 21 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.22.` | Poids de mélange du bloc 22 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.23.` | Poids de mélange du bloc 23 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.24.` | Poids de mélange du bloc 24 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.25.` | Poids de mélange du bloc 25 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.26.` | Poids de mélange du bloc 26 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.27.` | Poids de mélange du bloc 27 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.28.` | Poids de mélange du bloc 28 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.29.` | Poids de mélange du bloc 29 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.30.` | Poids de mélange du bloc 30 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.31.` | Poids de mélange du bloc 31 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.32.` | Poids de mélange du bloc 32 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.33.` | Poids de mélange du bloc 33 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.34.` | Poids de mélange du bloc 34 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocs.35.` | Poids de mélange du bloc 35 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_layer.` | Poids de mélange de la couche finale (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

**Remarque :** Tous les paramètres de poids de mélange acceptent des valeurs comprises entre 0.0 et 1.0 par pas de 0.01, où 0.0 signifie aucune contribution de model2 et 1.0 signifie une contribution complète de model2 pour ce composant spécifique.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/fr.md)

---
**Source fingerprint (SHA-256):** `a5f34deda62dc03f22613517e43996b908a8673dc5da10d8f1b7f6411ece2f0a`
