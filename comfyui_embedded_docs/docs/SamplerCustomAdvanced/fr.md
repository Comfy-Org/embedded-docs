# ÉchantillonneurPersonnaliséAvancé

Le nœud SamplerCustomAdvanced effectue un échantillonnage avancé dans l'espace latent en utilisant des configurations personnalisées de bruit, de guidage et d'échantillonnage. Il traite une image latente via un processus d'échantillonnage guidé avec des générations de bruit et des échéanciers sigma personnalisables, produisant à la fois le résultat final échantillonné et une version débruitée lorsqu'elle est disponible.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `bruit` | Le générateur de bruit qui fournit le motif de bruit initial et la graine pour le processus d'échantillonnage | NOISE | Oui | - |
| `guide` | Le modèle de guidage qui oriente le processus d'échantillonnage vers les résultats souhaités | GUIDER | Oui | - |
| `échantillonneur` | L'algorithme d'échantillonnage qui définit la manière dont l'espace latent est parcouru pendant la génération | SAMPLER | Oui | - |
| `sigmas` | L'échéancier sigma qui contrôle les niveaux de bruit tout au long des étapes d'échantillonnage | SIGMAS | Oui | - |
| `image_latente` | La représentation latente initiale qui sert de point de départ à l'échantillonnage | LATENT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sortie` | La représentation latente finale échantillonnée après avoir terminé le processus d'échantillonnage | LATENT |
| `sortie_débruitée` | Une version débruitée de la sortie lorsqu'elle est disponible, sinon renvoie la même valeur que la sortie | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `bf711ecc0684ad04babe5c63a246195f358204d203e836587a90feff742929a3`
