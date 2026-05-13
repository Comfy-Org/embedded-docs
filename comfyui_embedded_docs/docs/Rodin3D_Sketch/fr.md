> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/fr.md)

Ce nœud génère des actifs 3D à l'aide de l'API Rodin. Il prend des images en entrée et les convertit en modèles 3D via un service externe. Le nœud gère l'ensemble du processus, de la création de la tâche au téléchargement des fichiers de modèles 3D finaux.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `Images` | IMAGE | Oui | - | Images d'entrée à convertir en modèles 3D. Plusieurs images peuvent être fournies. |
| `Seed` | INT | Non | 0-65535 | Valeur de graine aléatoire pour la génération (par défaut : 0). Réglez sur 0 pour une graine aléatoire. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `Chemin du modèle 3D` | STRING | Chemin d'accès au fichier du modèle 3D généré (pour la rétrocompatibilité uniquement) |
| `GLB` | FILE3DGLB | Le modèle 3D généré au format GLB |

---
**Source fingerprint (SHA-256):** `d3bc71e6a44c11cbeff25351d561e99a7f09ed8ce3544d2968a873b6796512da`
