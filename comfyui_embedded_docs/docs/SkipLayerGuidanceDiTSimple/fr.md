> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/fr.md)

Version simplifiée du nœud SkipLayerGuidanceDiT qui modifie uniquement le passage inconditionnel pendant le processus de débruitage. Ce nœud applique un guidage par saut de couches à des couches spécifiques du transformateur dans les modèles DiT (Diffusion Transformer) en ignorant sélectivement certaines couches lors du passage inconditionnel, en fonction des paramètres de temporisation et de couches spécifiés.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel appliquer le guidage par saut de couches |
| `double_layers` | STRING | Non | - | Liste séparée par des virgules des indices de couches de blocs doubles à ignorer (par défaut : "7, 8, 9") |
| `single_layers` | STRING | Non | - | Liste séparée par des virgules des indices de couches de blocs simples à ignorer (par défaut : "7, 8, 9") |
| `start_percent` | FLOAT | Non | 0,0 - 1,0 | Pourcentage de début du processus de débruitage auquel le guidage par saut de couches commence (par défaut : 0,0) |
| `end_percent` | FLOAT | Non | 0,0 - 1,0 | Pourcentage de fin du processus de débruitage auquel le guidage par saut de couches s'arrête (par défaut : 1,0) |

**Remarque :** Le guidage par saut de couches n'est appliqué que lorsque `double_layers` et `single_layers` contiennent tous deux des indices de couches valides. Si les deux sont vides, le nœud renvoie le modèle original inchangé. Le guidage par saut de couches est actif uniquement lorsque la valeur sigma de l'étape de débruitage actuelle se situe entre `start_percent` et `end_percent` (converties en valeurs sigma en interne).

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Le modèle modifié avec le guidage par saut de couches appliqué aux couches spécifiées |

---
**Source fingerprint (SHA-256):** `6795a67a63d9aa8b2adea3d96e49272d88c21d0642bb507e175a2fcf3a125f98`
