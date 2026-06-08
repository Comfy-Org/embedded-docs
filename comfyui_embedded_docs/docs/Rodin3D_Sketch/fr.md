Ce nœud génère des actifs 3D à l'aide de l'API Rodin. Il prend des images en entrée et les convertit en modèles 3D via un service externe. Le nœud gère l'ensemble du processus, de la création de la tâche au téléchargement des fichiers de modèles 3D finaux.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `Images` | Images d'entrée à convertir en modèles 3D. Plusieurs images peuvent être fournies. | IMAGE | Oui | - |
| `Graine` | Valeur de graine aléatoire pour la génération (par défaut : 0). Réglez sur 0 pour une graine aléatoire. | INT | Non | 0-65535 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `GLB` | Chemin d'accès au fichier du modèle 3D généré (pour la rétrocompatibilité uniquement) | STRING |
| `GLB` | Le modèle 3D généré au format GLB | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/fr.md)

---
**Source fingerprint (SHA-256):** `d3bc71e6a44c11cbeff25351d561e99a7f09ed8ce3544d2968a873b6796512da`
