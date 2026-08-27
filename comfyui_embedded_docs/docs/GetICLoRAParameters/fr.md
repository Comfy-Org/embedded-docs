# Obtenir les paramètres IC-LoRA

Ce nœud lit les métadonnées d'un modèle chargé via LoRA afin d'extraire les paramètres IC-LoRA, tels que le facteur de réduction de référence. Il produit ces paramètres sous forme d'objet structuré pouvant être connecté au nœud `LTXVAddGuide` lorsqu'une LoRA nécessite une gestion spéciale des guides.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `iclora_model` | Sortie directe d'un chargeur LoRA pour l'IC-LoRA spécifique dont il faut extraire les métadonnées. | MODEL | Oui | N/A |

Remarque : Si les métadonnées de la LoRA sont manquantes ou ne contiennent pas d'entrée `reference_downscale_factor`, le nœud renvoie une valeur par défaut de 1. Lorsqu'elle est présente, le facteur est arrondi et défini à un minimum de 1.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `iclora_parameters` | Paramètres IC-LoRA extraits des métadonnées de la LoRA (p. ex. `reference_downscale_factor`). Connecter à `LTXVAddGuide` si la LoRA nécessite une gestion spéciale des guides. | IC_LORA_PARAMETERS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/fr.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
