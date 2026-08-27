# ModelMergeWAN2_1

Le nœud ModelMergeWAN2_1 fusionne deux modèles WAN2.1 en mélangeant leurs composants à l'aide de moyennes pondérées. Il prend en charge différentes tailles de modèles, notamment les modèles 1.3B avec 30 blocs et les modèles 14B avec 40 blocs, avec un traitement spécial pour les modèles image-vers-vidéo qui incluent un composant d'incorporation d'image supplémentaire. Chaque composant peut être pondéré individuellement pour contrôler le rapport de mélange entre les deux modèles d'entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Deuxième modèle à fusionner | MODEL | Oui | - |
| `patch_embedding.` | Poids du composant de plongement de patch (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `time_embedding.` | Poids du composant de plongement temporel (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `time_projection.` | Poids du composant de projection temporelle (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `text_embedding.` | Poids du composant de plongement textuel (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `img_emb.` | Poids du composant de plongement d'image, utilisé dans les modèles image-vers-vidéo (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.0.` | Poids du bloc 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.1.` | Poids du bloc 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.2.` | Poids du bloc 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.3.` | Poids du bloc 3 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.4.` | Poids du bloc 4 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.5.` | Poids du bloc 5 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.6.` | Poids du bloc 6 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.7.` | Poids du bloc 7 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.8.` | Poids du bloc 8 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.9.` | Poids du bloc 9 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.10.` | Poids du bloc 10 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.11.` | Poids du bloc 11 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.12.` | Poids du bloc 12 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.13.` | Poids du bloc 13 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.14.` | Poids du bloc 14 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.15.` | Poids du bloc 15 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.16.` | Poids du bloc 16 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.17.` | Poids du bloc 17 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.18.` | Poids du bloc 18 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.19.` | Poids du bloc 19 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.20.` | Poids du bloc 20 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.21.` | Poids du bloc 21 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.22.` | Poids du bloc 22 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.23.` | Poids du bloc 23 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.24.` | Poids du bloc 24 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.25.` | Poids du bloc 25 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.26.` | Poids du bloc 26 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.27.` | Poids du bloc 27 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.28.` | Poids du bloc 28 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.29.` | Poids du bloc 29 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.30.` | Poids du bloc 30 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.31.` | Poids du bloc 31 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.32.` | Poids du bloc 32 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.33.` | Poids du bloc 33 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.34.` | Poids du bloc 34 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.35.` | Poids du bloc 35 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.36.` | Poids du bloc 36 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.37.` | Poids du bloc 37 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.38.` | Poids du bloc 38 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.39.` | Poids du bloc 39 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `head.` | Poids du composant de tête (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

**Remarque :** Tous les paramètres de poids utilisent une plage de 0.0 à 1.0 avec des incréments de 0.01. Le nœud fournit jusqu'à 40 entrées de poids de blocs pour s'adapter aux différentes tailles de modèles : les modèles 1.3B utilisent 30 blocs (`blocks.0.` à `blocks.29.`), tandis que les modèles 14B utilisent 40 blocs (`blocks.0.` à `blocks.39.`). Le paramètre `img_emb.` est utilisé par les modèles image-vers-vidéo.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les composants des deux modèles d'entrée selon les poids spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeWAN2_1/fr.md)

---
**Source fingerprint (SHA-256):** `6a17defa25b1ef045b85af4a73e00d3a64c1948c0c47f355d1d488a75b09f224`
