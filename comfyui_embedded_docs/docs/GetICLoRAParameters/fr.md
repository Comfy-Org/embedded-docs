# Obtenir les paramètres IC-LoRA

**Aperçu**

Ce nœud extrait les paramètres IC-LoRA à partir des métadonnées d'un modèle chargé avec LoRA. Il lit les métadonnées safetensors pour trouver des valeurs telles que le facteur de sous-échantillonnage de référence et les affiche sous forme d'objet de paramètres structuré, qui peut être connecté au nœud LTXVAddGuide pour une gestion spéciale des guides. Si les métadonnées sont manquantes ou si le facteur de sous-échantillonnage de référence ne peut pas être lu, la valeur par défaut est 1 ; lorsqu'il est trouvé, la valeur est arrondie et limitée à un minimum de 1.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `iclora_model` | Sortie directe d'un chargeur LoRA pour l'IC-LoRA spécifique dont on souhaite extraire les métadonnées. | MODEL | Oui | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `iclora_parameters` | Paramètres IC-LoRA extraits des métadonnées LoRA (par exemple, `reference_downscale_factor`). Connectez à LTXVAddGuide si le LoRA nécessite un traitement spécial des guides. | IC_LORA_PARAMETERS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/fr.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
