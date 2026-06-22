# ModelMergeFlux1

Le nœud ModelMergeFlux1 fusionne deux modèles de diffusion en mélangeant leurs composants par interpolation pondérée. Il permet un contrôle précis sur la façon dont les différentes parties des modèles sont combinées, notamment les blocs de traitement d'image, les couches d'intégration temporelle, les mécanismes de guidage, les entrées vectorielles, les encodeurs de texte et divers blocs de transformeurs. Cela permet de créer des modèles hybrides aux caractéristiques personnalisées à partir de deux modèles sources.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Premier modèle source à fusionner | MODEL | Oui | - |
| `model2` | Deuxième modèle source à fusionner | MODEL | Oui | - |
| `img_in.` | Poids d'interpolation de l'entrée image (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `time_in.` | Poids d'interpolation de l'intégration temporelle (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `guidance_in` | Poids d'interpolation du mécanisme de guidage (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `vector_in.` | Poids d'interpolation de l'entrée vectorielle (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `txt_in.` | Poids d'interpolation de l'encodeur de texte (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.0.` | Poids d'interpolation du bloc double 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.1.` | Poids d'interpolation du bloc double 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.2.` | Poids d'interpolation du bloc double 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.3.` | Poids d'interpolation du bloc double 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.4.` | Poids d'interpolation du bloc double 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.5.` | Poids d'interpolation du bloc double 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.6.` | Poids d'interpolation du bloc double 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.7.` | Poids d'interpolation du bloc double 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.8.` | Poids d'interpolation du bloc double 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.9.` | Poids d'interpolation du bloc double 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.10.` | Poids d'interpolation du bloc double 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.11.` | Poids d'interpolation du bloc double 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.12.` | Poids d'interpolation du bloc double 12 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.13.` | Poids d'interpolation du bloc double 13 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.14.` | Poids d'interpolation du bloc double 14 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.15.` | Poids d'interpolation du bloc double 15 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.16.` | Poids d'interpolation du bloc double 16 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.17.` | Poids d'interpolation du bloc double 17 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `double_blocks.18.` | Poids d'interpolation du bloc double 18 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.0.` | Poids d'interpolation du bloc simple 0 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.1.` | Poids d'interpolation du bloc simple 1 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.2.` | Poids d'interpolation du bloc simple 2 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.3.` | Poids d'interpolation du bloc simple 3 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.4.` | Poids d'interpolation du bloc simple 4 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.5.` | Poids d'interpolation du bloc simple 5 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.6.` | Poids d'interpolation du bloc simple 6 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.7.` | Poids d'interpolation du bloc simple 7 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.8.` | Poids d'interpolation du bloc simple 8 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.9.` | Poids d'interpolation du bloc simple 9 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.10.` | Poids d'interpolation du bloc simple 10 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.11.` | Poids d'interpolation du bloc simple 11 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.12.` | Poids d'interpolation du bloc simple 12 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.13.` | Poids d'interpolation du bloc simple 13 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.14.` | Poids d'interpolation du bloc simple 14 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.15.` | Poids d'interpolation du bloc simple 15 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.16.` | Poids d'interpolation du bloc simple 16 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.17.` | Poids d'interpolation du bloc simple 17 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.18.` | Poids d'interpolation du bloc simple 18 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.19.` | Poids d'interpolation du bloc simple 19 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.20.` | Poids d'interpolation du bloc simple 20 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.21.` | Poids d'interpolation du bloc simple 21 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.22.` | Poids d'interpolation du bloc simple 22 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.23.` | Poids d'interpolation du bloc simple 23 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.24.` | Poids d'interpolation du bloc simple 24 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.25.` | Poids d'interpolation du bloc simple 25 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.26.` | Poids d'interpolation du bloc simple 26 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.27.` | Poids d'interpolation du bloc simple 27 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.28.` | Poids d'interpolation du bloc simple 28 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.29.` | Poids d'interpolation du bloc simple 29 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.30.` | Poids d'interpolation du bloc simple 30 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.31.` | Poids d'interpolation du bloc simple 31 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.32.` | Poids d'interpolation du bloc simple 32 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.33.` | Poids d'interpolation du bloc simple 33 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.34.` | Poids d'interpolation du bloc simple 34 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.35.` | Poids d'interpolation du bloc simple 35 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.36.` | Poids d'interpolation du bloc simple 36 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `single_blocks.37.` | Poids d'interpolation du bloc simple 37 (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `final_layer.` | Poids d'interpolation de la couche finale (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeFlux1/fr.md)

---
**Source fingerprint (SHA-256):** `a632133b5d4bc7c5a4e1be5f6f779e424a491fffb8ef7702346adc4acf6f23bc`
