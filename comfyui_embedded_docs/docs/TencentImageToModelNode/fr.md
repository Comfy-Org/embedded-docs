Ce nœud utilise l'API Tencent Hunyuan3D Pro pour générer un modèle 3D à partir d'une ou plusieurs images d'entrée. Il traite les images, les envoie à l'API et renvoie les fichiers du modèle 3D généré aux formats GLB et OBJ, ainsi que des cartes de texture optionnelles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | La version du modèle Hunyuan3D à utiliser. L'option LowPoly n'est pas disponible pour le modèle `3.1`. | COMBO | Oui | `"3.0"`<br>`"3.1"` |
| `image` | L'image d'entrée principale utilisée pour générer le modèle 3D. Doit faire au moins 128x128 pixels. | IMAGE | Oui | - |
| `image gauche` | Une image optionnelle du côté gauche de l'objet pour une génération multi-vue. Doit faire au moins 128x128 pixels. | IMAGE | Non | - |
| `image droite` | Une image optionnelle du côté droit de l'objet pour une génération multi-vue. Doit faire au moins 128x128 pixels. | IMAGE | Non | - |
| `image arrière` | Une image optionnelle de l'arrière de l'objet pour une génération multi-vue. Doit faire au moins 128x128 pixels. | IMAGE | Non | - |
| `nombre de faces` | Le nombre cible de faces pour le modèle 3D généré (par défaut : 500000). | INT | Oui | 3000 - 1500000 |
| `type de génération` | Le type de modèle 3D à générer. La sélection d'une option révèle des paramètres supplémentaires associés. | DYNAMICCOMBO | Oui | `"Normal"`<br>`"LowPoly"`<br>`"Geometry"` |
| `generate_type.pbr` | Active la génération de matériaux basée sur le rendu physique (PBR). Ce paramètre n'est visible que lorsque `type de génération` est défini sur "Normal" ou "LowPoly" (par défaut : False). | BOOLEAN | Non | - |
| `generate_type.polygon_type` | Le type de polygone à utiliser pour le maillage. Ce paramètre n'est visible que lorsque `type de génération` est défini sur "LowPoly". | COMBO | Non | `"triangle"`<br>`"quadrilateral"` |
| `graine` | Une valeur de graine pour le processus de génération. La graine détermine si le nœud doit être réexécuté ; les résultats ne sont pas déterministes, quelle que soit la graine (par défaut : 0). | INT | Oui | 0 - 2147483647 |

**Remarque :** Toutes les images d'entrée doivent avoir une largeur et une hauteur minimales de 128 pixels. Les images sont automatiquement réduites si elles dépassent 4900 pixels sur leur côté le plus long.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `fichier_modèle` | Une sortie héritée pour la rétrocompatibilité. | STRING |
| `GLB` | Le modèle 3D généré au format de fichier GLB (Binary GL Transmission Format). | FILE3DGLB |
| `OBJ` | Le modèle 3D généré au format de fichier OBJ (Wavefront). | FILE3DOBJ |
| `texture_image` | L'image de texture pour le modèle 3D généré. | IMAGE |
| `optionnel_metallic` | La carte de métallisation pour les matériaux PBR. Renvoie une image noire si elle n'est pas disponible. | IMAGE |
| `optionnel_normal` | La carte de normales pour les matériaux PBR. Renvoie une image noire si elle n'est pas disponible. | IMAGE |
| `optionnel_roughness` | La carte de rugosité pour les matériaux PBR. Renvoie une image noire si elle n'est pas disponible. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `56ac9e55bd9bb3a5c7c46c2de1ea06921cf41c0971471f6d0b64166722705e4d`
