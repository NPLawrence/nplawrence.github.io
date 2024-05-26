---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true

---
{% assign sup1 = site.author.supervisors[0] %}
{% assign sup2 = site.author.supervisors[1] %}

Upper bound tutorial: Slides and code [here](https://nplawrence.com/RL-MPC-tutorial/)


I'm a postdoc at {{ site.author.employer_short }}.


The broad goal of my work is to unify machine learning and control theory.
More specifically, I am keen on alleviating the tension between deep reinforcement learning and model predictive control.
A more unified perspective of these two areas would make RL more appealing for real-world applications while also making MPC more flexible and scalable under general learning algorithms.
Ultimately, I want to create safe decision-making technologies that "just work" in response to high-level commands.


My PhD is in {{ site.author.discipline }} from UBC where I worked with [{{ sup1.name}}]({{ sup1.url }}) and [{{ sup2.name }}]({{ sup2.url }}).
Here you can find my thesis on [Deep reinforcement learning agents for industrial control system design](https://open.library.ubc.ca/collections/24/items/1.0430547).
The first part of my thesis focuses on the practical implementation of RL and meta-RL for PID tuning in the context of industrial process control.
I later developed a general method for synthesizing stabilizing controllers with any RL algorithm using input-output data.


{% comment %}
News
======

I recently completed my PhD!

We are organizing a half-day workshop at AdCONIP 2022 on reinforcement learning to be held on August 7th 2022. Further details on the [conference webpage](https://adconip2022.org/workshops/#workshop-2-making-reinforcement-learning-a-practical-technology-for-industrial-control).
{% endcomment %}

Publications
======

Most of my papers are linked to arXiv or a DOI. If you can't find one, feel free to [get in touch](mailto:{{site.author.short_name}} <{{site.author.email}}>). {% if site.author.googlescholar %} You can also find my articles on my [Google Scholar profile]({{site.author.googlescholar}}).
{% endif %}

{% include pub_list.html %}
