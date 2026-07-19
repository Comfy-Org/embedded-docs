# Division CFG MultiGPU

## Vue d'ensemble

Le nœud MultiGPU CFG Split permet de répartir le travail de diffusion sur plusieurs GPU installés dans le même ordinateur. Le gain de vitesse dépend du workflow, mais des accélérations allant jusqu'à 1.95x ont été mesurées sur des workflows courants.

## Détails importants

Le mélange de GPU différents n'est pas pris en charge. Les GPU installés doivent être identiques, par exemple 2x 5090 ou 2x 5080.

ComfyUI détecte automatiquement plusieurs GPU installés au démarrage.

## GPU pris en charge

Toute configuration homogène à deux GPU avec une architecture Ampere ou plus récente, par exemple 2 x 3090 ou 2 x RTX6000 Pro.

## Modèles pris en charge

* LTX-2.3  
* WAN 2.2  
* FLUX.2 Klein - versions de base  
* Z-Image  
* Stable Diffusion 3.5 Large  
* Hunyuan Video  
* Qwen-Image-Edit-2511  
* Hunyuan-3D-v2.1  
* SDXL

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle à préparer pour utiliser MultiGPU CFG Split avant l'échantillonnage. | MODEL | Oui | N/A |
| `max_gpus` | Le nombre maximal de GPU identiques à utiliser pour répartir la charge. Réglez cette valeur sur le nombre de GPU correspondants installés dans votre système. | INT | Oui | Minimum : 1<br>Pas : 1<br>Par défaut : 2 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle préparé pour MultiGPU CFG Split, prêt pour un échantillonnage accéléré. | MODEL |

## Placement du nœud et notes sur le workflow

![image1.png](./asset/image1.png)

Le champ `max_gpus` doit être réglé sur le nombre maximal de GPU identiques installés dans le système.

**Placement du nœud :** MultiGPU CFG Split doit être placé entre le nœud de chargement du modèle et le nœud d'échantillonnage. Si d'autres nœuds sont connectés à la sortie modèle du chargeur, MultiGPU CFG Split doit être le dernier nœud de cette chaîne avant le nœud d'échantillonnage.

![image2.png](./asset/image2.png)

**Exigences du workflow :** Ce nœud découpe le workflow de diffusion au niveau du CFG. Pour cette raison, le CFG du workflow doit être supérieur à 1. Les workflows distillés qui exigent un CFG = 1 ne montreront pas de gain de performance lors de l'utilisation de MultiGPU CFG Split sur plusieurs GPU.

## Vérification de l'utilisation de plusieurs GPU

Lorsque vous exécutez un workflow avec MultiGPU CFG Split activé, vous pouvez ouvrir le Gestionnaire des tâches de Windows et sélectionner la catégorie des performances.

![image3.webp](./asset/image3.webp)  

![image4.png](./asset/image4.webp)

Vous devriez voir de l'activité sur les deux GPU installés pendant que le sampler fonctionne dans le workflow.

## Exemple de workflow multi-GPU : (Wan 2.2 FP8)

[Workflow d'exemple (Wan 2.2 FP8)](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/asset/video_wan2_2_14B_t2v_mGPU.json)

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/fr.md)

---
**Source fingerprint (SHA-256):** `7293ee785e29aea9a1a70a10444b99e89fb23c866505628ec57c209a2b8aaee0`
