Voici la traduction en français de la documentation du nœud ComfyUI **Krea 2 Style Reference** :

## Aperçu

Le nœud Krea 2 Style Reference vous permet d'ajouter une image de référence pour influencer le style d'une génération d'image Krea 2. Vous pouvez chaîner plusieurs références de style ensemble (jusqu'à 10 au total) et transmettre le résultat combiné à un nœud Krea 2 Image. Chaque image que vous fournissez est téléchargée vers le stockage ComfyAPI et transmise sous forme d'URL.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Image de référence dont le style influence la génération. | IMAGE | Oui | - |
| `force` | Force de la référence ; les valeurs négatives inversent l'influence du style (par défaut : 1,0). | FLOAT | Oui | -2,0 à 2,0 (pas : 0,05) |
| `style_reference` | Chaîne de références de style entrante facultative ; ce nœud en ajoute une supplémentaire. | STYLE_REF | Non | - |

**Remarque sur les contraintes :** Vous pouvez chaîner un maximum de 10 références de style au total. Si vous tentez d'ajouter une 11e référence, le nœud générera une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `style_reference` | Une liste d'entrées de référence de style, chacune contenant une URL et une valeur de force. Transmettez cette sortie à un nœud Krea 2 Image. | STYLE_REF |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2StyleReferenceNode/fr.md)

---
**Source fingerprint (SHA-256):** `7f87568a1cd5038571f3188cfb1d71e15533ea19eee01d7826fe574a1a4dc88d`
