# Meshy: Image to Relief

Ce nœud transforme une photo en modèle de bas-relief ainsi qu'en carte de profondeur 16 bits pour l'impression 3D, la gravure laser et le fraisage CNC. Les motifs sombres sur fond clair sont mis en relief et les zones claires restent basses. Seules les sorties que vous connectez sont générées et téléchargées ; ainsi, sans sortie de modèle connectée, la tâche renvoie uniquement la carte de profondeur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Photo à convertir en relief. Les motifs sombres sur fond clair sont mis en relief. La transparence est supprimée avant le téléversement ; aplatissez donc d'abord un logo transparent sur un fond blanc. | IMAGE | Oui | Image unique |
| `relief_type` | Préréglage de gravure. `"low"` correspond à une gravure peu profonde pour la gravure laser, le travail CNC et les plaques ; `"high"` est plus profonde pour les pièces imprimées en 3D. Le préréglage sélectionne la valeur de `carving_depth_mm`. | DYNAMIC_COMBO | Oui | `"low"`<br>`"high"` |
| `carving_depth_mm` | Profondeur de la gravure en millimètres. Disponible lorsque `relief_type` est défini (par défaut : 3.0 pour `"low"`, 6.0 pour `"high"`). | FLOAT | Oui | 0.1 à 60.0 (pas : 0.1) |
| `size_mm` | Longueur du côté le plus long de la photo sur le modèle, en millimètres, mesurée à plat avant toute courbure (par défaut : 60.0). | FLOAT | Oui | 20.0 à 250.0 (pas : 1.0) |
| `carving_mode` | `"emboss"` met en relief les parties les plus proches de la photo, `"engrave"` les grave en creux. | COMBO | Oui | `"emboss"`<br>`"engrave"` |
| `base` | `"plate"` conserve une plaque de base sous le relief, `"none"` découpe l'arrière-plan et ne construit aucune plaque. La sélection d'une option révèle son paramètre. | DYNAMIC_COMBO | Oui | `"plate"`<br>`"none"` |
| `base_thickness_mm` | Épaisseur de la plaque de base en millimètres. Disponible lorsque `base` est `"plate"` (par défaut : 1.0). | FLOAT | Oui | 0.1 à 10.0 (pas : 0.1) |
| `removal_threshold` | Profondeur en dessous de laquelle l'arrière-plan est découpé, sur la carte de profondeur de 0 à 1. 0.3 garde un buste entier, 0.8 le fragmente. Disponible lorsque `base` est `"none"` (par défaut : 0.01). | FLOAT | Oui | 0.01 à 1.0 (pas : 0.01) |
| `bend` | `"convex"` bombe l'avant vers l'extérieur, `"concave"` le courbe vers l'intérieur, `"off"` garde le relief plat. La sélection d'une courbure révèle `bend_axis` et `bend_angle`. | DYNAMIC_COMBO | Oui | `"off"`<br>`"convex"`<br>`"concave"` |
| `bend_axis` | `"xz"` enroule les bords gauche et droit, `"yz"` les bords supérieur et inférieur. Disponible lorsque `bend` est `"convex"` ou `"concave"`. | COMBO | Oui | `"xz"`<br>`"yz"` |
| `bend_angle` | Angle de l'arc couvert par la courbure, en degrés ; 360 referme le relief en cylindre. Disponible lorsque `bend` est `"convex"` ou `"concave"` (par défaut : 60.0). | FLOAT | Oui | 1.0 à 360.0 (pas : 1.0) |
| `seed` | Graine qui contrôle si le nœud s'exécute à nouveau ; le résultat est non déterministe quelle que soit la graine. Modifiez-la pour demander une sortie qui a été connectée après la dernière exécution (par défaut : 42). | INT | Oui | 0 à 2147483647 |
| `mesh_resolution` | Points du maillage le long du côté le plus long de la photo. À 1024, le GLB fait environ 50 Mo et le STL environ 105 Mo ; à 2048, environ 200 Mo et 420 Mo ; une courbure les double. (par défaut : 1024 ; option avancée) | INT | Oui | 512 à 2048 |
| `color_mapping` | Colorise les fichiers GLB, OBJ, FBX et USDZ avec la photo. Les fichiers STL et 3MF restent blancs. (par défaut : False ; option avancée) | BOOLEAN | Oui | True ou False |

**Remarque :** Un format de modèle n'est généré et téléchargé que lorsque sa sortie est connectée. Sans sortie de modèle connectée, la tâche renvoie uniquement la carte de profondeur, et `preview` seul fait tout de même générer le modèle pour la vignette, mais ne renvoie aucun fichier de modèle. `depth_map` conserve toute la plage 16 bits ; Save Image (Advanced) l'écrit en PNG 16 bits.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `GLB` | Le modèle de relief téléchargé au format GLB. | FILE3DGLB |
| `STL` | Le modèle de relief téléchargé au format STL. | FILE3DSTL |
| `OBJ` | Le modèle de relief téléchargé au format OBJ. | FILE3DOBJ |
| `FBX` | Le modèle de relief téléchargé au format FBX. | FILE3DFBX |
| `USDZ` | Le modèle de relief téléchargé au format USDZ. | FILE3DUSDZ |
| `3MF` | Le modèle de relief téléchargé au format 3MF. | FILE3D |
| `depth_map` | Carte de profondeur avec toute la plage 16 bits ; Save Image (Advanced) l'écrit en PNG 16 bits. | IMAGE |
| `preview` | Vignette rendue par Meshy pour le relief terminé. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToReliefNode/fr.md)

---
**Source fingerprint (SHA-256):** `6f2f0eb49074281b99d7ee10daf3bcc5616c6596c1c4d8491c72739550395f52`
