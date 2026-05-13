> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/fr.md)

Le nœud ModelComputeDtype modifie le type de données de calcul (précision) utilisé par un modèle pendant son traitement. Il crée une copie du modèle d'entrée et applique le réglage de précision sélectionné, ce qui peut aider à optimiser l'utilisation de la mémoire et les performances en fonction de votre matériel. Cela est utile pour le débogage et le test de différentes configurations de précision.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle d'entrée à modifier avec un nouveau type de données de calcul |
| `dtype` | STRING | Oui | "default"<br>"fp32"<br>"fp16"<br>"bf16" | Le type de données de calcul à appliquer au modèle (par défaut : "default") |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Le modèle modifié avec le nouveau type de données de calcul appliqué |

---
**Source fingerprint (SHA-256):** `bc65f1e452d0122ad175a8b95f38a36503253c9908157037c516496e65c828e6`
