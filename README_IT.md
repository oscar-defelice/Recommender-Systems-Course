<a href="https://oscar-defelice.github.io" target="_blank"><img src="https://user-images.githubusercontent.com/49638680/98257151-9f5e5800-1f7f-11eb-9f42-479a4fc6cf24.png" height="125" align="right" /></a>

# Recommender Systems

Questo è il repository del corso Recommender Systems.

<p align="center">
  <img width="776" alt="image" src="https://user-images.githubusercontent.com/49638680/204351915-373011d3-75ac-4e21-a6df-99cd1c552f2c.png">
</p>

## Introduzione

I sistemi di raccomandazione (_recommender systems_ o _recommender engines_ in inglese) sono un insieme di algoritmi che hanno in comune l'idea di _suggerire_ ad un utente un "prodotto".

È difficile stabilire quando quest'idea antichissima è stata trasferita all'ambito informatico, ma sappiamo che ha profondamente cambiato il nostro modo di rapportarci al mondo digitale. Basti pensare a Google, ad Amazon, Netflix, YouTube, etc., tutte queste compagnie fondano i loro successi su particolari sistemi di raccomandazione particolarmente efficienti.

L'uso esteso di questi sistemi ha contribuito in modo determinante all'affermarsi del fenomeno noto come delle " bolle di informazione"[[1]](#1).
Infatti, la sempre più massiccia presenza delle persone sui social network, e la loro tendenza ad informarsi tramite questi canali ha prodotto importanti effetti sociali e politici, come si mostra ad esempio in [[2]](#2) o [[3]](#3).

Altre problematiche nell'uso dei recommender systems sono emerse quando si è constatato come questi sistemi possano portare ad aumentare i livelli di ansia e depressione in soggetti predisposti [[4]](#4) e rovinare in generale l'esperienza online, oppure come rendano molto più semplice il diffondersi di notizie false [[5]](#5) e teorie cospiratorie [[6]](#6).

Ovviamente, non ci sono solo conseguenze negative dell'uso di questi sistemi.
Molte aziende hanno potuto publicizzarsi online in maniera più efficace (essendo le pubblicità mirate agli utenti "giusti") e contemporaneamente l'utente medio durante la sua presenza online ha potuto vedere solo prodotti di suo interesse.

Sono in corso studi sulla possibilità di costruire terapie personalizzate per ogni paziente, con risultati decisamente promettenti [[7]](#7).

In conclusione, i recommender systems sono probabilmente tra le applicazioni del machine learning il cui studio è più utile non solo al professionista, ma anche al semplice cittadino, data la loro enorme influenza nel plasmare la società odierna.
Per queste ragioni, comprendere e studiare il funzionamento di questi sistemi è importante ed interessante.

Rimandiamo ai vari moduli e all'indice delle lezioni (si veda più in basso) per dettagli puntuali, nel frattempo, vi _raccomandiamo_ buon apprendimento e buon lavoro!

---

## Installazione

Consiglio fortemente di creare un ambiente virtuale per isolare le dipendenze dei pacchetti.
A seconda del sistema operativo esistono varie guide e tutorial su come fare. [Qui](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) ne indico una multipiattaforma.

La versione di Python consigliata è la `3.7` (o superiore).

Una volta configurato il proprio ambiente, nel vostro prompt di comandi preferito, eseguire

```bash
pip install -r requirements.txt
```

questo installera i pacchetti e le librerie necessarie al corso nelle versioni opportune.

## Interagire con i notebook online

Il servizio gratuito _Binder_, permette di accedere ad un ambiente già configurato ed eseguire i notebook. Basta cliccare sul badge qui sotto per avviare l'ambiente.

<p align="center">
<a href = "https://mybinder.org/v2/gh/DeepLearningItalia/Recommender-Systems-Course/HEAD?urlpath=lab" target="_blank"> <img src="https://mybinder.org/badge_logo.svg"> </a>
</p>

## Indice delle lezioni

[Qui](src/README.md) puoi trovare un indice più dettagliato dei vari moduli.

---

## Docente

### [Oscar de Felice](https://oscar-defelice.github.io/)

<a href="https://oscar-defelice.github.io/" target="_blank" rel="that's me!">![Oscar](https://oscar-defelice.github.io/images/OscarAboutMe.png)</a>

Sono un fisico teorico e appassionato di programmazione e IA.

Scrivo articoli su Medium (molto poco sistematicamente), puoi leggerli [qui](https://oscar-defelice.medium.com/).
Ho anche un [profilo github](https://github.com/oscar-defelice) dove metto i miei progetti personali ed open-source.

📫 [Contattami!](mailto:oscar.defelice@gmail.com)

[![github](https://img.shields.io/badge/GitHub-100000?style=plastic&logo=github&logoColor=white)](https://github.com/oscar-defelice)
[![Website](https://img.shields.io/badge/oscar--defelice-oscar-orange?style=plastic&logo=netlify&logoColor=informational&link=oscar-defelice.github.io)](https://oscar-defelice.github.io)
[![Twitter Badge](https://img.shields.io/badge/-@OscardeFelice-1ca0f1?style=plastic&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/oscardefelice)](https://twitter.com/OscardeFelice)
[![Linkedin Badge](https://img.shields.io/badge/-oscardefelice-blue?style=plastic&logo=Linkedin&logoColor=white&link=https://linkedin.com/in/oscar-de-felice-5ab72383/)](https://linkedin.com/in/oscar-de-felice-5ab72383/)

## Altri corsi

Qui puoi trovare i materiali di altri miei corsi su argomenti di Machine Learning.

1. [Introduction to Data Science](https://oscar-defelice.github.io/DSAcademy-lectures) 🧮
2. [Statistical Learning](https://oscar-defelice.github.io/ML-lectures) 📈
3. [Deep Learning](https://oscar-defelice.github.io/DeepLearning-lectures) 🦾
4. [Time Series](https://oscar-defelice.github.io/TimeSeries-lectures) ⌛
5. [Computer Vision Hands-On](https://oscar-defelice.github.io/Computer-Vision-Hands-on) 👀️

## Referenze

<a id="1">[1]</a>
Van Alstyne, Marshall; Brynjolfsson, Erik (March 1997).
["Electronic Communities: Global Village or Cyberbalkans?"](http://web.mit.edu/marshall/www/papers/CyberBalkans.pdf)

<a id="2">[2]</a>
Hern (2017).
["How social media filter bubbles and algorithms influence the election"](https://www.theguardian.com/technology/2017/may/22/social-media-election-facebook-filter-bubbles)

<a id="3">[3]</a>
Baer, Drake (2017).
["The ‘Filter Bubble’ Explains Why Trump Won and You Didn’t See It Coming"](http://nymag.com/scienceofus/2016/11/how-facebook-and-the-filter-bubble-pushed-trump-to-victory.html)

<a id="4">[4]</a>
Lazar, Shira (June 1, 2011).
["Algorithms and the Filter Bubble Ruining Your Online Experience?"](http://www.huffingtonpost.com/shira-lazar/algorithms-and-the-filter_b_869473.html)

<a id="5">[5]</a>
Meredith, Sam (10 April 2018).
["Facebook-Cambridge Analytica: A timeline of the data hijacking scandal"](https://www.cnbc.com/2018/04/10/facebook-cambridge-analytica-a-timeline-of-the-data-hijacking-scandal.html)

<a id="6">[6]</a>
Catalina Albeanu (17 November 2016).
["Bursting the filter bubble after the US election: Is the media doomed to fail?"](https://www.journalism.co.uk/news/bursting-the-filter-bubble-after-the-us-election/s2/a692918/)

<a id="7">[7]</a>
Felix Gräßer, Stefanie Beckert, Denise Küster, Jochen Schmitt, Susanne Abraham, Hagen Malberg, and Sebastian Zaunseder (2017).
["Therapy Decision Support Based on Recommender System Methods"](https://www.hindawi.com/journals/jhe/2017/8659460/)
