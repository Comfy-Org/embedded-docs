> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/fr.md)

Ce nœud effectue une retopologie intelligente sur un modèle 3D, créant automatiquement un nouveau maillage plus propre avec un nombre de polygones optimisé. Il se connecte à une API Tencent Hunyuan 3D pour traiter le modèle, prenant en charge les formats de fichier GLB et OBJ jusqu'à 200 Mo. Le nœud renvoie le modèle traité sous forme de fichier OBJ.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model_3d` | FILE3D | Oui | - | Modèle 3D d'entrée (GLB ou OBJ). Le fichier doit être au format GLB ou OBJ et ne peut pas dépasser 200 Mo. |
| `polygon_type` | STRING | Oui | `"triangle"`<br>`"quadrilateral"` | Type de composition de surface. |
| `face_level` | STRING | Oui | `"medium"`<br>`"high"`<br>`"low"` | Niveau de réduction des polygones. |
| `seed` | INT | Non | 0 à 2147483647 | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes, quelle que soit la graine. (valeur par défaut : 0) |

**Remarque :** Le paramètre `seed` est utilisé pour déclencher une nouvelle exécution du nœud, mais la sortie finale n'est pas garantie d'être identique pour une même valeur de graine.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `OBJ` | FILE3D | Le modèle 3D traité avec une topologie optimisée, renvoyé au format OBJ. |

---
**Source fingerprint (SHA-256):** `13c2dce5f5fbc46a505d0366d8da1c4e762d3a64d11fae1bcceebd510b273f62`
