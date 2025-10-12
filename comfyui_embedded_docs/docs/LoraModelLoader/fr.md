> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/fr.md)

Le nœud LoraModelLoader applique des poids LoRA (Low-Rank Adaptation) entraînés à un modèle de diffusion. Il modifie le modèle de base en chargeant les poids LoRA d'un modèle LoRA entraîné et en ajustant leur force d'influence. Cela vous permet de personnaliser le comportement des modèles de diffusion sans avoir à les réentraîner depuis le début.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle de diffusion auquel le LoRA sera appliqué. |
| `lora` | LORA_MODEL | Oui | - | Le modèle LoRA à appliquer au modèle de diffusion. |
| `strength_model` | FLOAT | Oui | -100.0 à 100.0 | Force de modification du modèle de diffusion. Cette valeur peut être négative (par défaut : 1.0). |

**Remarque :** Lorsque `strength_model` est défini sur 0, le nœud renvoie le modèle original sans appliquer aucune modification LoRA.

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle de diffusion modifié avec les poids LoRA appliqués. |
