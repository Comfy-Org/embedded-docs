# ÉchantillonneurPersonnaliséAvancé

Le nœud SamplerCustomAdvanced effectue un échantillonnage avancé de l'espace latent à l'aide de configurations personnalisées de bruit, de guidage et d'échantillonnage. Il traite une image latente via un processus d'échantillonnage guidé avec des générations de bruit et des programmes de sigmas personnalisables, produisant à la fois la sortie échantillonnée finale et une version débruitée lorsque disponible.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `bruit` | Le générateur de bruit qui fournit le motif de bruit initial et la seed pour le processus d'échantillonnage | NOISE | Oui | - |
| `guide` | Le modèle de guidage qui oriente le processus d'échantillonnage vers les sorties souhaitées | GUIDER | Oui | - |
| `échantillonneur` | L'algorithme d'échantillonnage qui définit la manière dont l'espace latent est parcouru pendant la génération | SAMPLER | Oui | - |
| `sigmas` | Le programme de sigmas qui contrôle les niveaux de bruit tout au long des étapes d'échantillonnage | SIGMAS | Oui | - |
| `image_latente` | La représentation latente initiale qui sert de point de départ pour l'échantillonnage. Prend en charge un `noise_mask` facultatif pour un débruitage sélectif, ainsi que des clés facultatives `downscale_ratio_spacial` et `downscale_ratio_temporal` pour la gestion avancée des latents | LATENT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sortie` | La représentation latente échantillonnée finale après l'achèvement du processus d'échantillonnage. Les clés `downscale_ratio_spacial` ou `downscale_ratio_temporal` provenant du latent d'entrée sont supprimées de cette sortie | LATENT |
| `sortie_débruitée` | Une version débruitée de la sortie lorsque le processus d'échantillonnage produit une prédiction propre intermédiaire (x0), sinon renvoie la même chose que la sortie. Lorsqu'elle est disponible, elle représente la meilleure estimation du modèle pour le latent propre à chaque étape | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
