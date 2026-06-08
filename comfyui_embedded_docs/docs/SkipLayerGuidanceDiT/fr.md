Améliore le guidage vers une structure détaillée en utilisant un autre ensemble de CFG négatif avec des couches ignorées. Cette version générique de SkipLayerGuidance peut être utilisée sur tous les modèles DiT et s'inspire de l'Attention Guidée Perturbée. L'implémentation expérimentale originale a été créée pour SD3.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer le guidage par saut de couche | MODEL | Oui | - |
| `double_couches` | Numéros de couches séparés par des virgules pour les blocs doubles à ignorer (par défaut : "7, 8, 9") | STRING | Oui | - |
| `couches_simples` | Numéros de couches séparés par des virgules pour les blocs simples à ignorer (par défaut : "7, 8, 9") | STRING | Oui | - |
| `échelle` | Facteur d'échelle du guidage (par défaut : 3,0) | FLOAT | Oui | 0,0 - 10,0 |
| `pourcentage_de_départ` | Pourcentage de début pour l'application du guidage (par défaut : 0,01) | FLOAT | Oui | 0,0 - 1,0 |
| `pourcentage_de_fin` | Pourcentage de fin pour l'application du guidage (par défaut : 0,15) | FLOAT | Oui | 0,0 - 1,0 |
| `échelle_de_redimensionnement` | Facteur d'échelle de redimensionnement pour ajuster l'amplitude de la sortie (par défaut : 0,0, ce qui signifie aucun redimensionnement) | FLOAT | Oui | 0,0 - 10,0 |

**Remarque :** Si `double_layers` et `single_layers` sont tous deux vides (ne contiennent aucun numéro de couche), le nœud renvoie le modèle original sans appliquer aucun guidage.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec le guidage par saut de couche appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/fr.md)

---
**Source fingerprint (SHA-256):** `cf494fbeb33e7bc3b3f798e9e9b025623afad4ea6340ef628caa776c7d42ba12`
