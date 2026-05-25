> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMask/fr.md)

Voici la traduction en français de la documentation du nœud MediaPipeFaceMask :

## Aperçu

Ce nœud crée un masque binaire (une image en noir et blanc) basé sur les points de repère faciaux détectés par MediaPipe. Il dessine des formes polygonales remplies pour chaque région faciale détectée, produisant un masque par image dans un lot. Lorsque plusieurs visages sont détectés dans la même image, leurs masques sont combinés en un seul masque.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `face_landmarks` | FACE_LANDMARKS | Oui | - | Les données de points de repère faciaux provenant d'un nœud de détection faciale MediaPipe. |
| `regions` | COMBO | Oui | `"all"`<br>`"custom"` | Sélectionne les régions faciales à inclure dans le masque. `"all"` crée un masque à partir de l'union de toutes les régions faciales (ovale du visage, lèvres, yeux, iris). `"custom"` permet d'activer ou désactiver chaque région individuellement. Par défaut : `"all"` |

Lorsque `regions` est défini sur `"custom"`, les paramètres booléens supplémentaires suivants deviennent disponibles :

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `face_oval` | BOOLEAN | Non | Vrai/Faux | Inclure la région de l'ovale du visage dans le masque. Par défaut : Vrai |
| `lips` | BOOLEAN | Non | Vrai/Faux | Inclure la région des lèvres dans le masque. Par défaut : Vrai |
| `eyes` | BOOLEAN | Non | Vrai/Faux | Inclure la région des yeux dans le masque. Par défaut : Vrai |
| `irises` | BOOLEAN | Non | Vrai/Faux | Inclure la région des iris dans le masque. Par défaut : Vrai |

**Remarque :** En mode `"all"`, le masque inclut toutes les régions combinées. Étant donné que l'ovale du visage englobe les autres régions, sélectionner `"all"` produit effectivement le même résultat que de sélectionner uniquement l'ovale du visage.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `MASK` | MASK | Un tenseur de masque binaire où les régions faciales sont blanches (valeur 1.0) et l'arrière-plan est noir (valeur 0.0). Le masque a les mêmes dimensions que l'image d'entrée et contient un masque par image dans le lot. |

---
**Source fingerprint (SHA-256):** `92270002a42ed59bc75e676a6881e1899186d3c8a1bb4dd4c0d39b3762b5bb66`
