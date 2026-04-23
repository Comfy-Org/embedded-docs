> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/fr.md)

Ce nœud effectue une retopologie intelligente sur un modèle 3D, c'est-à-dire le processus de création automatique d'un nouveau maillage plus propre avec un nombre de polygones réduit. Il se connecte à une API Tencent Hunyuan 3D pour traiter le modèle, prenant en charge les formats de fichiers GLB et OBJ. Le nœud renvoie le modèle traité sous forme de fichier OBJ.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Oui | - | Modèle 3D d'entrée (GLB ou OBJ). Le fichier doit être au format GLB ou OBJ et ne peut pas dépasser 200 Mo. |
| `polygon_type` | STRING | Oui | `"triangle"`<br>`"quadrilateral"` | Type de composition de la surface. |
| `face_level` | STRING | Oui | `"medium"`<br>`"high"`<br>`"low"` | Niveau de réduction des polygones. |
| `seed` | INT | Non | 0 à 2147483647 | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) |

**Note :** Le paramètre `seed` est utilisé pour déclencher une ré-exécution du nœud, mais le résultat final n'est pas garanti d'être identique pour une même valeur de graine.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | Le modèle 3D traité avec une topologie optimisée, renvoyé au format OBJ. |