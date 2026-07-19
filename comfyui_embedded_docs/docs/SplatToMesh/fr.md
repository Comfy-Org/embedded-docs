# Extraire un maillage depuis un Splat

Ce nœud convertit un splat gaussien 3D en une surface maillée colorée. Il fonctionne en rastérisant les gaussiens sur une grille de densité, en extrayant une iso-surface à un niveau de densité choisi, puis en appliquant un lissage et un nettoyage optionnels pour produire un maillage triangulaire propre et coloré.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `splat` | Le splat gaussien d’entrée à convertir en maillage | SPLAT | Oui | - |
| `résolution` | Résolution de la grille de densité le long de l’axe le plus long. Des valeurs plus élevées produisent des détails de surface plus fins mais nécessitent plus de VRAM et de temps de traitement (croît en resolution^3). Par défaut : 384 | INT | Oui | 64 - 768 (pas de 16) |
| `noyau` | Demi-largeur maximale du splat en voxels. Chaque gaussien est rastérisé sur une fenêtre dimensionnée à son propre 3-sigma, plafonnée à cette valeur. Les petits surfels restent économiques tandis que les grands ne sont pas tronqués. Augmentez si les splats épars laissent des espaces vides. Par défaut : 5 | INT | Oui | 1 - 8 |
| `lissage` | Itérations de lissage de maillage Taubin. Lisse la surface sans la rétrécir (préservation du volume), contrairement au floutage de la densité. 0 signifie aucun lissage. Par défaut : 0 | INT | Oui | 0 - 60 |
| `niveau` | Niveau de l’iso-surface. Sélectionné automatiquement par seuillage d’Otsu ; cette valeur biaise la sélection automatique (1,0 = automatique, des valeurs plus basses produisent des surfaces plus épaisses/plus connectées, des valeurs plus élevées produisent des surfaces plus fines/plus serrées). Par défaut : 0,4 | FLOAT | Oui | 0,0 - 2,0 (pas de 0,01) |
| `composant_min` | Supprime les composants connectés plus petits que ce nombre de sommets. Élimine les amas flottants détachés et la coque interne des doubles parois. 0 conserve tous les composants. Par défaut : 500 | INT | Oui | 0 - 100000 (pas de 50) |
| `opacité_min` | Ignore les gaussiens plus faibles que cette valeur avant le maillage. Par défaut : 0,02 | FLOAT | Oui | 0,0 - 1,0 (pas de 0,01) |
| `accentuation_couleur` | Affûte la texture des sommets. 1,0 donne un mélange physiquement correct ; des valeurs plus élevées biaisent la couleur de chaque voxel vers sa gaussienne dominante au lieu de faire la moyenne des voisins (dé-étale la texture). Affecte uniquement la couleur, pas la géométrie. Par défaut : 2,0 | FLOAT | Oui | 1,0 - 8,0 (pas de 0,5) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `maillage` | Le maillage coloré extrait avec rendu non éclairé (type émissif) pour correspondre à l’apparence du splat | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToMesh/fr.md)

---
**Source fingerprint (SHA-256):** `5a7060c26252b587ce533e5682abe880a6fcc83f6671232489c3de64b094cd84`
