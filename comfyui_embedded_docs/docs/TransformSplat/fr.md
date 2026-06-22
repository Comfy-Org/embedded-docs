# Transformer Splat

Le nœud Transform Splat applique des transformations de translation, rotation et mise à l'échelle à un splat gaussien. Il déplace, fait pivoter et redimensionne l'ensemble du splat comme un objet unique. Lorsqu'une mise à l'échelle non uniforme est appliquée, il remodèle également chaque splat gaussien individuel pour des résultats précis.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `splat` | Le splat gaussien à transformer | SPLAT | Oui | - |
| `translation_x` | Translation le long de l'axe X (par défaut : 0.0) | FLOAT | Oui | -100.0 à 100.0 |
| `translation_y` | Translation le long de l'axe Y (par défaut : 0.0) | FLOAT | Oui | -100.0 à 100.0 |
| `translation_z` | Translation le long de l'axe Z (par défaut : 0.0) | FLOAT | Oui | -100.0 à 100.0 |
| `rotation_x` | Rotation autour de l'axe X en degrés (par défaut : 0.0) | FLOAT | Oui | -360.0 à 360.0 |
| `rotation_y` | Rotation autour de l'axe Y en degrés (par défaut : 0.0) | FLOAT | Oui | -360.0 à 360.0 |
| `rotation_z` | Rotation autour de l'axe Z en degrés (par défaut : 0.0) | FLOAT | Oui | -360.0 à 360.0 |
| `échelle_x` | Facteur d'échelle le long de l'axe X (par défaut : 1.0) | FLOAT | Oui | 0.01 à 100.0 |
| `échelle_y` | Facteur d'échelle le long de l'axe Y (par défaut : 1.0) | FLOAT | Oui | 0.01 à 100.0 |
| `échelle_z` | Facteur d'échelle le long de l'axe Z (par défaut : 1.0) | FLOAT | Oui | 0.01 à 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `splat` | Le splat gaussien transformé avec positions, échelles et rotations mises à jour | SPLAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TransformSplat/fr.md)

---
**Source fingerprint (SHA-256):** `19e6a7da7b4f0d8c9674ead2d35d742df460576b01c4ab4108dd59a2d08dfcb0`
