> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentImageToModelNode/fr.md)

Ce nœud utilise l'API Tencent Hunyuan3D Pro pour générer un modèle 3D à partir d'une ou plusieurs images d'entrée. Il traite les images, les envoie à l'API et renvoie les fichiers du modèle 3D généré aux formats GLB et OBJ, ainsi que des cartes de texture optionnelles.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | COMBO | Oui | `"3.0"`<br>`"3.1"` | La version du modèle Hunyuan3D à utiliser. L'option LowPoly n'est pas disponible pour le modèle `3.1`. |
| `image` | IMAGE | Oui | - | L'image d'entrée principale utilisée pour générer le modèle 3D. Doit faire au moins 128x128 pixels. |
| `image_left` | IMAGE | Non | - | Une image optionnelle du côté gauche de l'objet pour une génération multi-vue. Doit faire au moins 128x128 pixels. |
| `image_right` | IMAGE | Non | - | Une image optionnelle du côté droit de l'objet pour une génération multi-vue. Doit faire au moins 128x128 pixels. |
| `image_back` | IMAGE | Non | - | Une image optionnelle de l'arrière de l'objet pour une génération multi-vue. Doit faire au moins 128x128 pixels. |
| `face_count` | INT | Oui | 3000 - 1500000 | Le nombre cible de faces pour le modèle 3D généré (par défaut : 500000). |
| `generate_type` | DYNAMICCOMBO | Oui | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` | Le type de modèle 3D à générer. La sélection d'une option révèle des paramètres supplémentaires associés. |
| `generate_type.pbr` | BOOLEAN | Non | - | Active la génération de matériaux basée sur le rendu physique (PBR). Ce paramètre n'est visible que lorsque `generate_type` est défini sur "Normal" ou "LowPoly" (par défaut : False). |
| `generate_type.polygon_type` | COMBO | Non | `"triangle"`<br>`"quadrilateral"` | Le type de polygone à utiliser pour le maillage. Ce paramètre n'est visible que lorsque `generate_type` est défini sur "LowPoly". |
| `seed` | INT | Oui | 0 - 2147483647 | Une valeur de graine pour le processus de génération. La graine détermine si le nœud doit être réexécuté ; les résultats ne sont pas déterministes, quelle que soit la graine (par défaut : 0). |

**Remarque :** Toutes les images d'entrée doivent avoir une largeur et une hauteur minimales de 128 pixels. Les images sont automatiquement réduites si elles dépassent 4900 pixels sur leur côté le plus long.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `model_file` | STRING | Une sortie héritée pour la rétrocompatibilité. |
| `GLB` | FILE3DGLB | Le modèle 3D généré au format de fichier GLB (Binary GL Transmission Format). |
| `OBJ` | FILE3DOBJ | Le modèle 3D généré au format de fichier OBJ (Wavefront). |
| `texture_image` | IMAGE | L'image de texture pour le modèle 3D généré. |
| `optional_metallic` | IMAGE | La carte de métallisation pour les matériaux PBR. Renvoie une image noire si elle n'est pas disponible. |
| `optional_normal` | IMAGE | La carte de normales pour les matériaux PBR. Renvoie une image noire si elle n'est pas disponible. |
| `optional_roughness` | IMAGE | La carte de rugosité pour les matériaux PBR. Renvoie une image noire si elle n'est pas disponible. |

---
**Source fingerprint (SHA-256):** `56ac9e55bd9bb3a5c7c46c2de1ea06921cf41c0971471f6d0b64166722705e4d`
