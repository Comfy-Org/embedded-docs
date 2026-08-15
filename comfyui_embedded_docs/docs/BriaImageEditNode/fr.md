# Bria Image Edit

Le nœud Bria FIBO Image Edit vous permet de modifier une image existante à l'aide d'une instruction textuelle. Il envoie l'image et votre invite à l'API Bria, qui utilise le modèle FIBO pour générer une nouvelle version modifiée de l'image en fonction de votre demande. Vous pouvez également fournir un masque pour limiter les modifications à une zone spécifique.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | La version du modèle à utiliser pour l'édition d'image. | COMBO | Oui | `"FIBO"` |
| `image` | L'image d'entrée que vous souhaitez modifier. | IMAGE | Oui | - |
| `prompt` | Instruction pour modifier l'image (par défaut : vide). | STRING | Oui | - |
| `negative_prompt` | Texte décrivant ce que vous ne voulez pas voir apparaître dans l'image modifiée (par défaut : vide). | STRING | Oui | - |
| `structured_prompt` | Chaîne contenant l'invite de modification structurée au format JSON. Utilisez-la à la place de l'invite habituelle pour un contrôle précis et programmatique (par défaut : vide). | STRING | Oui | - |
| `seed` | Un nombre utilisé pour initialiser la génération aléatoire, garantissant des résultats reproductibles (par défaut : 1). | INT | Oui | 1 à 2147483647 |
| `guidance_scale` | Une valeur plus élevée fait que l'image suit l'invite plus fidèlement (par défaut : 3.0). | FLOAT | Oui | 3.0 à 5.0 |
| `steps` | Le nombre d'étapes de débruitage que le modèle effectuera (par défaut : 50). | INT | Oui | 20 à 50 |
| `moderation` | Paramètres de modération. La sélection de `"true"` révèle des options de modération supplémentaires pour le contenu de l'invite, l'entrée visuelle et la sortie visuelle. | DYNAMICCOMBO | Oui | `"false"`<br>`"true"` |
| `mask` | S'il est omis, la modification s'applique à l'image entière. | MASK | Non | - |

**Contraintes importantes :**

- Vous devez fournir au moins l'une des entrées `prompt` ou `structured_prompt`. Elles ne peuvent pas être toutes deux vides.
- Lorsque le paramètre `moderation` est défini sur `"true"`, trois entrées booléennes supplémentaires deviennent disponibles : `prompt_content_moderation` (par défaut : false), `visual_input_moderation` (par défaut : false), et `visual_output_moderation` (par défaut : true).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image modifiée renvoyée par l'API Bria. | IMAGE |
| `structured_prompt` | L'invite structurée qui a été utilisée ou générée pendant le processus de modification. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
