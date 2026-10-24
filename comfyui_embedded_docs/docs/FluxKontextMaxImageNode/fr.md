# Image Flux.1 Kontext [max]

Génère ou modifie une image avec Flux.1 Kontext [max] via l'API BFL, à partir d'un prompt et d'un ratio d'aspect. Lorsque `input_image` est connecté, le prompt décrit la modification ; sans celui-ci, le nœud génère une nouvelle image à partir du prompt seul. Il expose les mêmes entrées que Flux.1 Kontext [pro] Image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `invite` | Prompt pour la génération de l'image. Avec une image d'entrée, précisez quoi et comment modifier. | STRING | Oui | - |
| `rapport_d'aspect` | Ratio d'aspect de l'image ; doit être compris entre 1:4 et 4:1 (par défaut : `"16:9"`). | STRING | Oui | - |
| `guidage` | Force de guidage pour le processus de génération de l'image (par défaut : 3.0). | FLOAT | Oui | 0.1 à 99.0 (pas de 0.1) |
| `étapes` | Nombre d'étapes pour le processus de génération de l'image (par défaut : 50). | INT | Oui | 1 à 150 |
| `graine` | La graine aléatoire utilisée pour créer le bruit (par défaut : 1234). | INT | Oui | 0 à 18446744073709551615 |
| `suréchantillonnage_d'invite` | Indique s'il faut effectuer un suréchantillonnage (upsampling) du prompt. Si activé, le prompt est modifié automatiquement pour une génération plus créative, mais les résultats sont non déterministes, de sorte que la même graine ne produira pas exactement le même résultat (par défaut : `False`). Il s'agit d'un paramètre avancé. | BOOLEAN | Oui | True / False |
| `image_d'entrée` | Image optionnelle à modifier. Lorsqu'elle est omise, le prompt est validé pour s'assurer qu'il n'est pas vide. | IMAGE | Non | - |

**Note :** Le nœud envoie la requête à BFL et interroge jusqu'à ce que l'image soit prête. Les requêtes rejetées par la modération de contenu de BFL échouent au lieu de renvoyer une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image générée ou modifiée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMaxImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `557f9e69de37ee89e161dffdaef7458ed026b884298594f2046454b6b8d3c415`
