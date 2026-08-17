# Bria Image Edit

Le nœud Bria FIBO Image Edit vous permet de modifier une image existante à l'aide d'une instruction texte. Il envoie l'image et votre prompt à l'API Bria, qui utilise le modèle FIBO pour créer une version modifiée de l'image. Vous pouvez également fournir un masque pour limiter les modifications à une zone spécifique.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | La version du modèle à utiliser pour la modification d'image. | COMBO | Oui | `"FIBO"` |
| `image` | L'image d'entrée que vous souhaitez modifier. | IMAGE | Oui | - |
| `prompt` | Instruction pour modifier l'image (défaut : vide). | STRING | Oui | - |
| `negative_prompt` | Texte décrivant ce que vous ne voulez pas voir apparaître dans l'image modifiée (défaut : vide). | STRING | Oui | - |
| `structured_prompt` | Chaîne contenant le prompt de modification structuré au format JSON. Utilisez-la à la place du prompt habituel pour un contrôle précis et programmatique (défaut : vide). | STRING | Oui | - |
| `seed` | Nombre utilisé pour initialiser la génération aléatoire, garantissant des résultats reproductibles (défaut : 1). | INT | Oui | 1 à 2147483647 |
| `guidance_scale` | Une valeur plus élevée fait que l'image suit le prompt plus fidèlement (défaut : 3). | FLOAT | Oui | 3.0 à 5.0 |
| `steps` | Le nombre d'étapes de débruitage effectuées par le modèle (défaut : 50). | INT | Oui | 20 à 50 |
| `moderation` | Paramètres de modération. La sélection de `"true"` révèle des options de modération supplémentaires. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |
| `mask` | S'il est omis, la modification s'applique à l'image entière. | MASK | Non | - |

### Entrées de modération

Lorsque `moderation` est défini sur `"true"`, ces entrées supplémentaires deviennent disponibles :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt_content_moderation` | Indique si le texte du prompt doit être modéré pour détecter un contenu inapproprié (défaut : false). | BOOLEAN | Non | `true`<br>`false` |
| `visual_input_moderation` | Indique si l'image d'entrée doit être modérée pour détecter un contenu inapproprié (défaut : false). | BOOLEAN | Non | `true`<br>`false` |
| `visual_output_moderation` | Indique si l'image de sortie modifiée doit être modérée pour détecter un contenu inapproprié (défaut : true). | BOOLEAN | Non | `true`<br>`false` |

**Contraintes importantes :**

- Au moins un des deux paramètres `prompt` ou `structured_prompt` doit être non vide. Si les deux sont vides, le nœud génère une erreur.
- Lorsque `moderation` est défini sur `"true"`, les trois entrées de modération ci-dessus sont affichées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image modifiée renvoyée par l'API Bria. | IMAGE |
| `structured_prompt` | Le prompt structuré utilisé ou généré lors du processus de modification. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
