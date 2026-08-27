# ModelMergeSD1

Le nœud ModelMergeSD1 fusionne deux modèles Stable Diffusion 1.x en ajustant la contribution de chaque composant du modèle au résultat. Il offre un contrôle individuel sur l'intégration temporelle, l'intégration des étiquettes, ainsi que sur chaque bloc d'entrée, intermédiaire et de sortie, permettant une fusion de modèles finement ajustée pour des cas d'utilisation spécifiques.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Le deuxième modèle à fusionner | MODEL | Oui | - |
| `time_embed.` | Poids de mélange de la couche d'intégration temporelle (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `label_emb.` | Poids de mélange de la couche d'intégration des étiquettes (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.0.` | Poids de mélange du bloc d'entrée 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.1.` | Poids de mélange du bloc d'entrée 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.2.` | Poids de mélange du bloc d'entrée 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.3.` | Poids de mélange du bloc d'entrée 3 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.4.` | Poids de mélange du bloc d'entrée 4 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.5.` | Poids de mélange du bloc d'entrée 5 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.6.` | Poids de mélange du bloc d'entrée 6 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.7.` | Poids de mélange du bloc d'entrée 7 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.8.` | Poids de mélange du bloc d'entrée 8 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.9.` | Poids de mélange du bloc d'entrée 9 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.10.` | Poids de mélange du bloc d'entrée 10 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.11.` | Poids de mélange du bloc d'entrée 11 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `middle_block.0.` | Poids de mélange du bloc intermédiaire 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `middle_block.1.` | Poids de mélange du bloc intermédiaire 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `middle_block.2.` | Poids de mélange du bloc intermédiaire 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.0.` | Poids de mélange du bloc de sortie 0 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.1.` | Poids de mélange du bloc de sortie 1 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.2.` | Poids de mélange du bloc de sortie 2 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.3.` | Poids de mélange du bloc de sortie 3 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.4.` | Poids de mélange du bloc de sortie 4 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.5.` | Poids de mélange du bloc de sortie 5 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.6.` | Poids de mélange du bloc de sortie 6 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.7.` | Poids de mélange du bloc de sortie 7 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.8.` | Poids de mélange du bloc de sortie 8 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.9.` | Poids de mélange du bloc de sortie 9 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.10.` | Poids de mélange du bloc de sortie 10 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.11.` | Poids de mélange du bloc de sortie 11 (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |
| `out.` | Poids de mélange de la couche de sortie (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (step: 0.01) |

Tous les poids de mélange acceptent des valeurs de 0.0 à 1.0 et sont définis sur 1.0 par défaut, ce qui signifie que chaque composant du premier modèle est entièrement utilisé sauf ajustement.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle fusionné combinant les caractéristiques des deux modèles d'entrée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/fr.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
