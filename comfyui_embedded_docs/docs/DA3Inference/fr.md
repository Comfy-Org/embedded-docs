# Exécuter Depth Anything 3

Ce nœud exécute le modèle Depth Anything 3 sur une image pour estimer les informations de profondeur et de géométrie. En mode multi-vue, plusieurs images sont traitées ensemble comme des vues séparées d'une même scène pour produire des cartes de profondeur géométriquement cohérentes et des poses de caméra.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `da3_model` | Le modèle Depth Anything 3 à utiliser pour l'inférence | DA3_MODEL | Oui | - |
| `image` | Image ou images d'entrée à traiter | IMAGE | Oui | - |
| `resolution` | Résolution à laquelle le modèle fonctionne (côté le plus long, multiple de 14). Les valeurs plus faibles sont plus rapides et utilisent moins de VRAM. Les valeurs plus élevées produisent plus de détails. La sortie est suréchantillonnée à la taille d'origine (par défaut : 504) | INT | Oui | 140 à 2520 (pas : 14) |
| `resize_method` | upper_bound_resize : redimensionne pour que le côté le plus long soit égal à la résolution (limite la mémoire, par défaut). lower_bound_resize : redimensionne pour que le côté le plus court soit égal à la résolution (préserve plus de détails sur les images hautes/larges, utilise plus de mémoire) | COMBO | Oui | `"upper_bound_resize"`<br>`"lower_bound_resize"` |
| `mode` | mono : traitement d'image en vue unique (fonctionne avec toutes les variantes de modèle). multiview : toutes les images sont traitées ensemble pour la cohérence géométrique et l'estimation de pose de caméra (pour les modèles Small et Base uniquement) | COMBO | Oui | `"mono"`<br>`"multiview"` |
| `ref_view_strategy` | Quelle vue sert d'ancrage géométrique en mode multi-vue. saddle_balanced : la vue la plus moyenne par rapport à toutes les autres (meilleur choix général). saddle_sim_range : la vue la plus visuellement distincte des autres. first / middle : sélections positionnelles fixes | COMBO | Non (conditionnel) | `"saddle_balanced"`<br>`"saddle_sim_range"`<br>`"first"`<br>`"middle"` |
| `pose_method` | Comment le champ de vision de la caméra est estimé (pour les modèles Small et Base uniquement). cam_dec : appris à partir des caractéristiques de l'image. ray_pose : dérivé géométriquement de la sortie de rayons 3D du modèle. Affecte la correction de perspective de la sortie 3D | COMBO | Non (conditionnel) | `"cam_dec"`<br>`"ray_pose"` |

**Remarques sur les contraintes des paramètres :**
- Les paramètres `ref_view_strategy` et `pose_method` sont disponibles uniquement lorsque `mode` est défini sur `"multiview"`
- Le mode multi-vue nécessite une variante de modèle Small ou Base. Les modèles avec d'autres types de tête (comme Metric ou Mono) ne prennent pas en charge l'attention inter-vues ou l'estimation de pose de caméra
- Lorsque `pose_method` est défini sur `"cam_dec"`, le modèle doit disposer d'un décodeur de caméra. S'il est défini sur `"ray_pose"`, le modèle doit avoir une tête DualDPT
- Si le `pose_method` sélectionné n'est pas compatible avec le modèle chargé, une erreur sera générée

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `da3_geometry` | Dictionnaire de tenseurs non normalisés. Contient toujours les clés : depth, image, mode. Les clés optionnelles incluent : sky (pour les modèles Mono/Metric), confidence (pour les modèles Small/Base), extrinsics et intrinsics (pour le mode multi-vue) | DA3_GEOMETRY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Inference/fr.md)

---
**Source fingerprint (SHA-256):** `e91dd47e6a01719cdd6b6ce8a9bcc45933cac72c5e147ac42906d2f83ab7c250`
