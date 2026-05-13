> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/fr.md)

Ce nœud utilise l'API Tencent Hunyuan3D pour analyser automatiquement un modèle 3D et générer ou identifier ses composants en fonction de sa structure. Il traite le modèle et renvoie un nouveau fichier FBX.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle_3d` | FILE3D | Oui | FBX, Tous | Le modèle 3D à traiter. Le modèle doit être au format FBX et comporter moins de 30 000 faces. |
| `graine` | INT | Non | 0 à 2147483647 | Une valeur de graine pour contrôler si le nœud doit être réexécuté. Les résultats sont non déterministes, quelle que soit la valeur de la graine. (par défaut : 0) |

**Remarque :** L'entrée `model_3d` ne prend en charge que les fichiers au format FBX. Si un autre format de fichier 3D est fourni, le nœud générera une erreur.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `FBX` | FILE3DFBX | Le modèle 3D traité, renvoyé sous forme de fichier FBX. |

---
**Source fingerprint (SHA-256):** `eae7d0197d4391af1f5f24f120c64f1045649182108affad10b9a00f329310fe`
