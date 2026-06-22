# Référence Luma

Ce nœud contient une image et une valeur de poids destinées à être utilisées avec le nœud Luma Generate Image. Il crée une chaîne de référence pouvant être transmise à d'autres nœuds Luma pour influencer la génération d'images. Le nœud peut soit démarrer une nouvelle chaîne de référence, soit s'ajouter à une chaîne existante.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Image à utiliser comme référence. | IMAGE | Oui | - |
| `poids` | Poids de la référence d'image (par défaut : 1.0). | FLOAT | Oui | 0.0 - 1.0 |
| `luma_ref` | Chaîne de référence Luma existante facultative à laquelle s'ajouter. | LUMA_REF | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `luma_ref` | La chaîne de référence Luma contenant l'image et le poids. | LUMA_REF |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/fr.md)

---
**Source fingerprint (SHA-256):** `1ad653f0ad7c56702f607ebc3c3d117196295e4e3b044a2c6f1aa3db18869a40`
