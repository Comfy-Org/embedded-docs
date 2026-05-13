> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentTextToModelNode/fr.md)

Ce nœud utilise l'API Hunyuan3D Pro de Tencent pour générer un modèle 3D à partir d'une description textuelle. Il envoie une requête pour créer une tâche de génération, interroge le résultat et télécharge les fichiers finaux du modèle aux formats GLB et OBJ.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | `"3.0"`<br>`"3.1"` | La version du modèle Hunyuan3D à utiliser. L'option LowPoly n'est pas disponible pour le modèle `3.1`. |
| `invite` | STRING | Oui | - | La description textuelle du modèle 3D à générer. Prend en charge jusqu'à 1024 caractères. |
| `nombre de faces` | INT | Oui | 3000 - 1500000 | Le nombre cible de faces pour le modèle 3D généré. Valeur par défaut : 500000. |
| `type de génération` | DYNAMICCOMBO | Oui | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` | Le type de modèle 3D à générer. Les options disponibles et leurs paramètres associés sont :<br>- **Normal** : Génère un modèle standard. Inclut un paramètre `pbr` (par défaut : `False`).<br>- **LowPoly** : Génère un modèle à faible nombre de polygones. Inclut les paramètres `polygon_type` (`"triangle"` ou `"quadrilateral"`) et `pbr` (par défaut : `False`).<br>- **Geometry** : Génère un modèle géométrique uniquement. |
| `graine` | INT | Non | 0 - 2147483647 | Une valeur de graine pour la génération. Les résultats ne sont pas déterministes quelle que soit la graine. Définir une nouvelle graine contrôle si le nœud doit être réexécuté. Valeur par défaut : 0. |

**Remarque :** Le paramètre `generate_type` est dynamique. La sélection de `"LowPoly"` révèlera des entrées supplémentaires pour `polygon_type` et `pbr`. La sélection de `"Normal"` révèlera une entrée pour `pbr`. La sélection de `"Geometry"` ne révélera aucune entrée supplémentaire.

**Contrainte :** Le type de génération `"LowPoly"` ne peut pas être utilisé avec le modèle `"3.1"`.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `GLB` | STRING | Une sortie héritée pour la rétrocompatibilité. |
| `OBJ` | FILE3DGLB | Le modèle 3D généré au format de fichier GLB. |
| `texture_image` | FILE3DOBJ | Le modèle 3D généré au format de fichier OBJ. |
| `texture_image` | IMAGE | L'image de texture extraite du fichier OBJ généré, si disponible. |

---
**Source fingerprint (SHA-256):** `e35f5165941cc7761639dd72e78141326d37d5e169be9a0e326afcbcdc572b7d`
