# Charger le modèle LoRA

Le nœud `LoraModelLoader` applique des poids LoRA (Low-Rank Adaptation) entraînés à un modèle de diffusion. Il modifie le modèle de base en chargeant les poids LoRA depuis un modèle LoRA entraîné et en ajustant leur force d’influence. Cela permet de personnaliser le comportement des modèles de diffusion sans avoir à les réentraîner de zéro.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle de diffusion auquel le LoRA sera appliqué. | MODEL | Oui | - |
| `lora` | Le modèle LoRA à appliquer au modèle de diffusion. | LORA_MODEL | Oui | - |
| `strength_model` | Degré de modification du modèle de diffusion. Cette valeur peut être négative (défaut : 1.0). | FLOAT | Oui | -100.0 à 100.0 |
| `bypass` | Lorsqu’elle est activée, applique le LoRA en mode contournement sans modifier les poids du modèle de base. Utile pour l’entraînement et lorsque les poids du modèle sont déchargés (défaut : False). | BOOLEAN | Oui | True ou False |

**Remarque :** Lorsque `strength_model` est défini sur 0, le nœud renvoie le modèle original sans appliquer aucune modification LoRA.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Le modèle de diffusion modifié. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/fr.md)

---
**Source fingerprint (SHA-256):** `81eb2a9b0376fe7453f6e7e422414472e80a3d1b92bb6874b91df6de8aed0d9a`
