Ce nœud fusionne deux modèles d'IA en utilisant une approche par blocs avec un contrôle fin sur différents composants du modèle. Il vous permet de mélanger des modèles en ajustant les poids d'interpolation pour des sections spécifiques, notamment les fréquences positionnelles, les couches d'incorporation (embedding) et les blocs de transformeur individuels. Le processus de fusion combine les architectures et les paramètres des deux modèles d'entrée selon les valeurs de poids spécifiées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle1` | Premier modèle à fusionner | MODEL | Oui | - |
| `modèle2` | Second modèle à fusionner | MODEL | Oui | - |
| `pos_frequencies.` | Poids pour l'interpolation des fréquences positionnelles (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t_embedder.` | Poids pour l'interpolation de l'incorporateur temporel (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t5_y_embedder.` | Poids pour l'interpolation de l'incorporateur T5-Y (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `t5_yproj.` | Poids pour l'interpolation de la projection T5-Y (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.0.` | Poids pour l'interpolation du bloc 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.1.` | Poids pour l'interpolation du bloc 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.2.` | Poids pour l'interpolation du bloc 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.3.` | Poids pour l'interpolation du bloc 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.4.` | Poids pour l'interpolation du bloc 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.5.` | Poids pour l'interpolation du bloc 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.6.` | Poids pour l'interpolation du bloc 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.7.` | Poids pour l'interpolation du bloc 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.8.` | Poids pour l'interpolation du bloc 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.9.` | Poids pour l'interpolation du bloc 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.10.` | Poids pour l'interpolation du bloc 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.11.` | Poids pour l'interpolation du bloc 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.12.` | Poids pour l'interpolation du bloc 12 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.13.` | Poids pour l'interpolation du bloc 13 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.14.` | Poids pour l'interpolation du bloc 14 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.15.` | Poids pour l'interpolation du bloc 15 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.16.` | Poids pour l'interpolation du bloc 16 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.17.` | Poids pour l'interpolation du bloc 17 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.18.` | Poids pour l'interpolation du bloc 18 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.19.` | Poids pour l'interpolation du bloc 19 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.20.` | Poids pour l'interpolation du bloc 20 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.21.` | Poids pour l'interpolation du bloc 21 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.22.` | Poids pour l'interpolation du bloc 22 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.23.` | Poids pour l'interpolation du bloc 23 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.24.` | Poids pour l'interpolation du bloc 24 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.25.` | Poids pour l'interpolation du bloc 25 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.26.` | Poids pour l'interpolation du bloc 26 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.27.` | Poids pour l'interpolation du bloc 27 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.28.` | Poids pour l'interpolation du bloc 28 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.29.` | Poids pour l'interpolation du bloc 29 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.30.` | Poids pour l'interpolation du bloc 30 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.31.` | Poids pour l'interpolation du bloc 31 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.32.` | Poids pour l'interpolation du bloc 32 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.33.` | Poids pour l'interpolation du bloc 33 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.34.` | Poids pour l'interpolation du bloc 34 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.35.` | Poids pour l'interpolation du bloc 35 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.36.` | Poids pour l'interpolation du bloc 36 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.37.` | Poids pour l'interpolation du bloc 37 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.38.` | Poids pour l'interpolation du bloc 38 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.39.` | Poids pour l'interpolation du bloc 39 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.40.` | Poids pour l'interpolation du bloc 40 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.41.` | Poids pour l'interpolation du bloc 41 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.42.` | Poids pour l'interpolation du bloc 42 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.43.` | Poids pour l'interpolation du bloc 43 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.44.` | Poids pour l'interpolation du bloc 44 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.45.` | Poids pour l'interpolation du bloc 45 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.46.` | Poids pour l'interpolation du bloc 46 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `blocks.47.` | Poids pour l'interpolation du bloc 47 (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `final_layer.` | Poids pour l'interpolation de la couche finale (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée selon les poids spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMochiPreview/fr.md)

---
**Source fingerprint (SHA-256):** `aebf536f3f89ca8c81141ac871b1b612082c3bd38a29984168b05eccf0cb57e3`
