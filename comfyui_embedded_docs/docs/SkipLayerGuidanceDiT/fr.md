> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/fr.md)

Améliore le guidage vers une structure détaillée en utilisant un autre ensemble de CFG négatif avec des couches ignorées. Cette version générique de SkipLayerGuidance peut être utilisée sur tous les modèles DiT et s'inspire de l'Attention Guidée Perturbée. L'implémentation expérimentale originale a été créée pour SD3.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel appliquer le guidage par saut de couche |
| `double_layers` | STRING | Oui | - | Numéros de couches séparés par des virgules pour les blocs doubles à ignorer (par défaut : "7, 8, 9") |
| `single_layers` | STRING | Oui | - | Numéros de couches séparés par des virgules pour les blocs simples à ignorer (par défaut : "7, 8, 9") |
| `scale` | FLOAT | Oui | 0,0 - 10,0 | Facteur d'échelle du guidage (par défaut : 3,0) |
| `start_percent` | FLOAT | Oui | 0,0 - 1,0 | Pourcentage de début pour l'application du guidage (par défaut : 0,01) |
| `end_percent` | FLOAT | Oui | 0,0 - 1,0 | Pourcentage de fin pour l'application du guidage (par défaut : 0,15) |
| `rescaling_scale` | FLOAT | Oui | 0,0 - 10,0 | Facteur d'échelle de redimensionnement pour ajuster l'amplitude de la sortie (par défaut : 0,0, ce qui signifie aucun redimensionnement) |

**Remarque :** Si `double_layers` et `single_layers` sont tous deux vides (ne contiennent aucun numéro de couche), le nœud renvoie le modèle original sans appliquer aucun guidage.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `model` | MODEL | Le modèle modifié avec le guidage par saut de couche appliqué |

---
**Source fingerprint (SHA-256):** `cf494fbeb33e7bc3b3f798e9e9b025623afad4ea6340ef628caa776c7d42ba12`
