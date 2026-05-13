> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/fr.md)

Voici la traduction en français de la documentation du nœud Bria FIBO Image Edit :

Le nœud Bria FIBO Image Edit vous permet de modifier une image existante à l'aide d'une instruction textuelle. Il envoie l'image et votre invite à l'API Bria, qui utilise le modèle FIBO pour générer une nouvelle version modifiée de l'image en fonction de votre demande. Vous pouvez également fournir un masque pour limiter les modifications à une zone spécifique.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | `"FIBO"` | La version du modèle à utiliser pour l'édition d'image. |
| `image` | IMAGE | Oui | - | L'image d'entrée que vous souhaitez modifier. |
| `invite` | STRING | Non | - | L'instruction textuelle décrivant comment modifier l'image (par défaut : vide). |
| `invite négative` | STRING | Non | - | Texte décrivant ce que vous ne souhaitez pas voir apparaître dans l'image modifiée (par défaut : vide). |
| `invite structurée` | STRING | Non | - | Une chaîne contenant l'invite d'édition structurée au format JSON. Utilisez-la à la place de l'invite habituelle pour un contrôle précis et programmatique (par défaut : vide). |
| `graine` | INT | Oui | 1 à 2147483647 | Un nombre utilisé pour initialiser la génération aléatoire, garantissant des résultats reproductibles (par défaut : 1). |
| `échelle de guidage` | FLOAT | Oui | 3,0 à 5,0 | Contrôle à quel point l'image générée suit l'invite. Une valeur plus élevée entraîne une adhérence plus forte (par défaut : 3,0). |
| `étapes` | INT | Oui | 20 à 50 | Le nombre d'étapes de débruitage que le modèle effectuera (par défaut : 50). |
| `modération` | DYNAMICCOMBO | Oui | `"false"`<br>`"true"` | Active ou désactive la modération du contenu. La sélection de `"true"` révèle des options de modération supplémentaires pour le contenu de l'invite, l'entrée visuelle et la sortie visuelle. |
| `masque` | MASK | Non | - | Une image de masque optionnelle. Si fournie, les modifications ne seront appliquées qu'aux zones masquées de l'image. |

**Contraintes importantes :**

* Vous devez fournir au moins l'une des entrées `prompt` ou `structured_prompt`. Elles ne peuvent pas être toutes les deux vides.
* Une seule entrée `image` est requise.
* Lorsque le paramètre `moderation` est défini sur `"true"`, trois entrées booléennes supplémentaires deviennent disponibles : `prompt_content_moderation` (par défaut : false), `visual_input_moderation` (par défaut : false) et `visual_output_moderation` (par défaut : true).

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `invite structurée` | IMAGE | L'image modifiée renvoyée par l'API Bria. |
| `invite structurée` | STRING | L'invite structurée qui a été utilisée ou générée pendant le processus d'édition. |

---
**Source fingerprint (SHA-256):** `30148261f43f5bfd14339f5ff1ec250381a615cc05c67eee21b0a2423ebe349d`
