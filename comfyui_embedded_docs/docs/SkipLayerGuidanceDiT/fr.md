> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/fr.md)

Améliore le guidage vers une structure détaillée en utilisant un autre ensemble de négatifs CFG avec des couches ignorées. Cette version générique de SkipLayerGuidance peut être utilisée sur tous les modèles DiT et s'inspire de Perturbed Attention Guidance. L'implémentation expérimentale originale a été créée pour SD3.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel appliquer le guidage par couches ignorées |
| `double_layers` | STRING | Oui | - | Numéros de couches séparés par des virgules pour les blocs doubles à ignorer (par défaut : "7, 8, 9") |
| `single_layers` | STRING | Oui | - | Numéros de couches séparés par des virgules pour les blocs simples à ignorer (par défaut : "7, 8, 9") |
| `scale` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle du guidage (par défaut : 3.0) |
| `start_percent` | FLOAT | Oui | 0.0 - 1.0 | Pourcentage de départ pour l'application du guidage (par défaut : 0.01) |
| `end_percent` | FLOAT | Oui | 0.0 - 1.0 | Pourcentage de fin pour l'application du guidage (par défaut : 0.15) |
| `rescaling_scale` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle de re-dimensionnement (par défaut : 0.0) |

**Note :** Si `double_layers` et `single_layers` sont vides (ne contiennent aucun numéro de couche), le nœud retourne le modèle original sans appliquer de guidage.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec le guidage par couches ignorées appliqué |