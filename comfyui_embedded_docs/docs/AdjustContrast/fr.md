# Ajuster le contraste

Le nœud Ajuster le Contraste modifie le niveau de contraste d'une image d'entrée. Il fonctionne en ajustant la différence entre les zones claires et sombres de l'image. Un facteur de 1,0 laisse l'image inchangée, les valeurs inférieures à 1,0 réduisent le contraste et les valeurs supérieures à 1,0 l'augmentent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée dont le contraste doit être ajusté. | IMAGE | Oui | - |
| `facteur` | Facteur de contraste. 1,0 = aucun changement, <1,0 = moins de contraste, >1,0 = plus de contraste. (par défaut : 1,0) | FLOAT | Non | 0,0 - 2,0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image résultante avec le contraste ajusté. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/fr.md)

---
**Source fingerprint (SHA-256):** `01148cdd9d951e78c712c1c3159c5562a680a5147bd4a76e33d91543d5245854`
