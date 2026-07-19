# Obtenir les paramètres IC-LoRA

Voici la traduction de la documentation en français, conformément à vos règles :

## Aperçu

Ce nœud extrait les paramètres IC-LoRA à partir des métadonnées d’un modèle chargé avec un LoRA. Il lit les métadonnées du fichier safetensors pour trouver des valeurs telles que le facteur de sous-échantillonnage de référence et les produit sous forme d’un objet paramètre structuré, qui peut être connecté au nœud LTXVAddGuide pour une gestion spéciale des guides.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `iclora_model` | Sortie directe d’un chargeur LoRA pour le IC-LoRA spécifique dont les métadonnées doivent être extraites. | MODEL | Oui | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `iclora_parameters` | Paramètres IC-LoRA extraits des métadonnées du LoRA (par exemple, reference_downscale_factor). Connectez à LTXVAddGuide si le LoRA nécessite une gestion spéciale des guides. | IC_LORA_PARAMETERS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/fr.md)

---
**Source fingerprint (SHA-256):** `44673f0b06cb258014efd77f734c076865d59338ddf825598d85592f000aca50`
