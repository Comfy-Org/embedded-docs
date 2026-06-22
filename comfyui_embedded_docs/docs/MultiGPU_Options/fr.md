# MultiGPU_Options

Voici la traduction de la documentation du nœud ComfyUI :

## Aperçu

Ce nœud vous permet de spécifier la performance relative de chaque GPU lorsque vous utilisez plusieurs cartes graphiques de vitesses différentes. Il crée un groupe d'options GPU pouvant être utilisé pour répartir le travail entre les périphériques, bien que la répartition réelle de la charge de travail basée sur la vitesse ne soit pas encore implémentée dans la version actuelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `device_index` | Le numéro d'index du périphérique GPU à configurer (par défaut : 0) | INT | Oui | 0 à 64 |
| `relative_speed` | La vitesse relative de ce GPU par rapport aux autres, utilisée pour la répartition de la charge de travail (par défaut : 1.0, pas : 0.01) | FLOAT | Oui | 0.0 à illimité |
| `gpu_options` | Un groupe d'options GPU existant auquel ajouter les options de ce périphérique. Si non fourni, un nouveau groupe est créé | GPU_OPTIONS | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `GPU_OPTIONS` | Un groupe d'options GPU contenant les paramètres configurés du périphérique, pouvant être transmis à d'autres nœuds pour des opérations multi-GPU | GPU_OPTIONS |

**Remarque :** Le paramètre `relative_speed` est défini mais n'est pas encore utilisé par le planificateur interne pour répartir le travail entre les GPU. Dans l'implémentation actuelle, le travail est réparti uniformément entre tous les périphériques, indépendamment de leurs vitesses relatives.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_Options/fr.md)

---
**Source fingerprint (SHA-256):** `8010460560a69c57d4ee0d8c3728a7a5d999e56ef5316b557fba0c660c9f38b0`
