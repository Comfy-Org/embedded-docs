# Hunyuan3D : Partie 3D

Ce nœud utilise l'API Tencent Hunyuan3D pour identifier et générer automatiquement les composants d'un modèle 3D en fonction de sa structure. Il accepte un modèle FBX, le traite et renvoie un nouveau fichier FBX.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle_3d` | Modèle 3D au format FBX. Le modèle doit comporter moins de 30 000 faces. | FILE3D | Oui | FBX, Any |
| `graine` | Le seed contrôle si le nœud doit se relancer ; les résultats sont non déterministes quel que soit le seed. (par défaut : 0) | INT | Non | 0 à 2147483647 |

**Remarque :** L'entrée `model_3d` ne prend en charge que les fichiers au format FBX. Si un autre format de fichier 3D est fourni, le nœud générera une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `FBX` | Le modèle 3D traité, renvoyé sous forme de fichier FBX. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/fr.md)

---
**Source fingerprint (SHA-256):** `827b42559f4b2c341f08c58f53778d27c1c6afce607c36c8d1eae7c208c6a738`
