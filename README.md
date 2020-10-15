# pspgamer

**This is an early-stage ongoing project**

Allow patients with partial [Locked-in syndrome](https://en.wikipedia.org/wiki/Locked-in_syndrome) to communicate. The current implementation is being developed for patients affected by the [Progressive supranuclear palsy](https://en.wikipedia.org/wiki/Progressive_supranuclear_palsy)

# Functionalities
## Pre-defined text-to-speech
The caregiver can define a set of pre-defined sentences, like "yes/no", "I need to go to the bathroom" or "Thanks for supporting me", and map those sentences to a simple to use input device to allow the affected person to quickly give a voice-based feedback to the caregiver.

## Entertainment Plugins
A plugin-based system allows the patient to control entertainment devices, like smart tv or audio providers. 

|Platform|Support Status|Notes|
|:---| :----: |------|
|Samsung Smart TV| ongoing| Tizen only, models from 2016
|Spotify| in progress | Only podcasts 
  

# Hardware
The current required hardware is 
* A raspberry Pi 4, 4GB ram
* INPUT: a [3 pedal keyboard](https://www.amazon.it/gp/product/B00WS2GZU2/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1) 
* INPUT: ["buttons"](https://www.amazon.it/gp/product/B01N78D6HB/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)   

# Licensing
PSPGamer software kit is licensed under the ZeroTier BSL, which allows source code access and free use for all with the exception of selling for  commercial purposes or embedding the software source code in a commercial hardware. You can use ZeroTier controllers and nodes for free if you use it for non-commercial purposes. Please contact us to learn more.

The BSL is based on the Business Source License (BSL) version 1.1 developed by MariaDB. This license has been adopted by other commercial open source projects like CockroachDB.

The BSL also carries an expiration date (“change date”) after which the licensed work reverts to a more permissive license of the author’s choice (Apache License 2.0 in our case). Each major release can carry an updated change date, allowing the author to extend the BSL’s coverage into the future for new releases. The existence of a change date means that should the original project’s author(s) abandon the project it will eventually fall into a more permissive open source license and can be taken over by the community.
