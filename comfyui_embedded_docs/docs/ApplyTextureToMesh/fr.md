# ApplyTextureToMesh

Ce nœud attache les images de texture cuites à la disposition UV d’un maillage afin qu’elles puissent être exportées avec le maillage par le nœud SaveGLB. Connectez le même maillage déplié en UV que celui utilisé pour le baking, ainsi que les cartes d’images cuites. Les cartes optionnelles de métallicité, de rugosité et d’occlusion sont regroupées dans une seule texture ORM, et la fourniture d’une carte de normales stocke également les normales lisses et les tangentes nécessaires à un ombrage correct.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage déplié en UV auquel les textures cuites seront attachées. Doit être le même maillage que celui utilisé pendant le baking ; une erreur est levée si le maillage n’a pas d’UV. | MESH | Oui | — |
| `base_color` | L’image de couleur de base cuite. Stockée comme texture du maillage et limitée à la plage 0-1. | IMAGE | Oui | — |
| `metallic` | La carte de métallicité cuite. Utilisée comme canal bleu de la texture ORM combinée ; par défaut à 0 lorsqu’elle n’est pas fournie. | IMAGE | Non | — |
| `roughness` | La carte de rugosité cuite. Utilisée comme canal vert de la texture ORM combinée ; par défaut à 1 lorsqu’elle n’est pas fournie. | IMAGE | Non | — |
| `occlusion` | La carte d’occlusion ambiante cuite. Utilisée comme canal rouge de la texture ORM combinée ; par défaut à 1 lorsqu’elle n’est pas fournie. Lorsqu’elle est fournie, la texture ORM est également marquée comme texture d’occlusion pour SaveGLB. | IMAGE | Non | — |
| `normal_map` | La carte de normales tangentes cuite. Lorsqu’elle est fournie, le nœud recalcule la base tangente par sommet et exporte des normales de sommet lisses afin que la carte de normales soit ombrée correctement. | IMAGE | Non | — |

Remarque : lorsque l’une des cartes `metallic`, `roughness` ou `occlusion` est connectée, les trois sont regroupées dans une seule texture ORM glTF avec les canaux R = occlusion, G = rugosité, B = métallicité. Les cartes manquantes sont remplies avec des valeurs par défaut (occlusion 1, rugosité 1, métallicité 0), et les cartes de résolutions différentes sont redimensionnées à la largeur et à la hauteur maximales. Lorsque `normal_map` est connectée, les normales du maillage sont remplacées par des normales de sommet lisses calculées et une base tangente est ajoutée. Les coordonnées UV qui tombent hors de la plage [0,1] sont uniformément mises à l’échelle dans [0,1] tout en préservant le rapport d’aspect.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage d’entrée avec les images de texture attachées à sa disposition UV, prêt à être enregistré par SaveGLB. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/fr.md)

---
**Source fingerprint (SHA-256):** `f91985ef686beddccc41a72614b3d263b4e0d9f1a156db6017d620de26d7b6cf`
