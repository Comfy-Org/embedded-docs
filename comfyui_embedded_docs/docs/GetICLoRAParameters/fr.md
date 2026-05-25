> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/fr.md)

Voici la traduction de la documentation en français, conformément à vos règles :

## Aperçu

Ce nœud extrait les paramètres IC-LoRA à partir des métadonnées d’un modèle chargé avec un LoRA. Il lit les métadonnées du fichier safetensors pour trouver des valeurs telles que le facteur de sous-échantillonnage de référence et les produit sous forme d’un objet paramètre structuré, qui peut être connecté au nœud LTXVAddGuide pour une gestion spéciale des guides.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `iclora_model` | MODEL | Oui | N/A | Sortie directe d’un chargeur LoRA pour le IC-LoRA spécifique dont les métadonnées doivent être extraites. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `iclora_parameters` | IC_LORA_PARAMETERS | Paramètres IC-LoRA extraits des métadonnées du LoRA (par exemple, reference_downscale_factor). Connectez à LTXVAddGuide si le LoRA nécessite une gestion spéciale des guides. |

---
**Source fingerprint (SHA-256):** `44673f0b06cb258014efd77f734c076865d59338ddf825598d85592f000aca50`
