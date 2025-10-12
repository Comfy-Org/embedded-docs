> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/fr.md)

Version simplifiée du nœud SkipLayerGuidanceDiT qui modifie uniquement la passe inconditionnelle pendant le processus de débruitage. Ce nœud applique le guidage par saut de couche à des couches spécifiques du transformateur dans les modèles DiT (Diffusion Transformer) en ignorant sélectivement certaines couches pendant la passe inconditionnelle en fonction des paramètres de timing et de couche spécifiés.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel appliquer le guidage par saut de couche |
| `double_layers` | STRING | Oui | - | Liste séparée par des virgules des indices de couches à double bloc à ignorer (par défaut : "7, 8, 9") |
| `single_layers` | STRING | Oui | - | Liste séparée par des virgules des indices de couches à simple bloc à ignorer (par défaut : "7, 8, 9") |
| `start_percent` | FLOAT | Oui | 0.0 - 1.0 | Le pourcentage de départ du processus de débruitage lorsque le guidage par saut de couche commence (par défaut : 0.0) |
| `end_percent` | FLOAT | Oui | 0.0 - 1.0 | Le pourcentage de fin du processus de débruitage lorsque le guidage par saut de couche s'arrête (par défaut : 1.0) |

**Note :** Le guidage par saut de couche n'est appliqué que lorsque `double_layers` et `single_layers` contiennent tous deux des indices de couches valides. Si les deux sont vides, le nœud retourne le modèle original inchangé.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec le guidage par saut de couche appliqué aux couches spécifiées |