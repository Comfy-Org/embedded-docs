# Image Flux.1 Kontext [pro]

Génère ou modifie une image avec Flux.1 Kontext [pro] via l'API BFL, à partir d'un prompt et d'un ratio d'aspect. Lorsque `input_image` est connecté, le prompt décrit la modification ; sans cela, le nœud génère une nouvelle image à partir du prompt seul.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `invite` | Prompt pour la génération d'image. Avec une image d'entrée, précisez ce qu'il faut modifier et comment le modifier. | STRING | Oui | - |
| `rapport_d'aspect` | Ratio d'aspect de l'image ; doit être compris entre 1:4 et 4:1 (valeur par défaut : `"16:9"`). | STRING | Oui | - |
| `guidage` | Force de guidage du processus de génération d'image (valeur par défaut : 3.0). | FLOAT | Oui | 0.1 à 99.0 (pas de 0.1) |
| `étapes` | Nombre d'étapes du processus de génération d'image (valeur par défaut : 50). | INT | Oui | 1 à 150 |
| `graine` | Graine aléatoire utilisée pour créer le bruit (valeur par défaut : 1234). | INT | Oui | 0 à 18446744073709551615 |
| `suréchantillonnage_prompt` | Indique s'il faut effectuer un suréchantillonnage du prompt. Si cette option est active, le prompt est modifié automatiquement pour une génération plus créative, mais les résultats sont non déterministes ; une même graine ne produira donc pas exactement le même résultat (valeur par défaut : `False`). Il s'agit d'un paramètre avancé. | BOOLEAN | Oui | True / False |
| `image_entrée` | Image facultative à modifier. Lorsqu'elle est omise, le prompt est validé pour s'assurer qu'il n'est pas vide. | IMAGE | Non | - |

**Remarque :** Le nœud envoie la requête à BFL et interroge régulièrement le service jusqu'à ce que l'image soit prête. Les requêtes rejetées par la modération du contenu de BFL échouent au lieu de renvoyer une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image générée ou modifiée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextProImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `7a5be7e7859b1aca5130552345c76045ab64be3b4bee588091d147480a9ae1ac`
