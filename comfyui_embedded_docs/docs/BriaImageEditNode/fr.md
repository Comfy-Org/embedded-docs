# Bria Image Edit

Le nœud Bria FIBO Image Edit modifie une image existante à l'aide d'une instruction textuelle. Il envoie l'image et votre prompt à l'API Bria, où le modèle FIBO crée une version modifiée. Un masque optionnel peut limiter les modifications à une zone spécifique.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | La version du modèle à utiliser pour l'édition d'image. | COMBO | Oui | `"FIBO"` |
| `image` | L'image d'entrée que vous souhaitez modifier. | IMAGE | Oui | - |
| `invite` | Instruction pour modifier l'image (par défaut : vide). | STRING | Oui | - |
| `invite négative` | Texte décrivant ce que vous ne voulez pas voir apparaître dans l'image modifiée (par défaut : vide). | STRING | Oui | - |
| `invite structurée` | Chaîne contenant le prompt d'édition structuré au format JSON. Utilisez-la à la place du prompt habituel pour un contrôle précis et programmatique (par défaut : vide). | STRING | Oui | - |
| `graine` | Nombre utilisé pour initialiser la génération aléatoire, garantissant des résultats reproductibles (par défaut : 1). | INT | Oui | 1 à 2147483647 |
| `échelle de guidage` | Une valeur plus élevée fait suivre l'image plus fidèlement au prompt (par défaut : 3). | FLOAT | Oui | 3.0 à 5.0 |
| `étapes` | Le nombre d'étapes de débruitage effectuées par le modèle (par défaut : 50). | INT | Oui | 20 à 50 |
| `modération` | Paramètres de modération. Sélectionner `"true"` affiche des options de modération supplémentaires. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |
| `masque` | S'il est omis, la modification s'applique à l'image entière. | MASK | Non | - |

### Entrées de modération

Lorsque `moderation` est réglé sur `"true"`, ces entrées supplémentaires deviennent disponibles :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt_content_moderation` | Indique s'il faut modérer le texte du prompt pour détecter un contenu inapproprié (par défaut : false). | BOOLEAN | Non | `true`<br>`false` |
| `visual_input_moderation` | Indique s'il faut modérer l'image d'entrée pour détecter un contenu inapproprié (par défaut : false). | BOOLEAN | Non | `true`<br>`false` |
| `visual_output_moderation` | Indique s'il faut modérer l'image de sortie modifiée pour détecter un contenu inapproprié (par défaut : true). | BOOLEAN | Non | `true`<br>`false` |

**Contraintes importantes :**

- Au moins l'un des deux `prompt` ou `structured_prompt` doit être non vide. Si les deux sont vides, le nœud génère une erreur.
- Lorsque `moderation` est réglé sur `"true"`, les trois entrées de modération ci-dessus sont affichées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image modifiée renvoyée par l'API Bria. | IMAGE |
| `invite structurée` | Le prompt structuré utilisé ou généré pendant le processus d'édition. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
