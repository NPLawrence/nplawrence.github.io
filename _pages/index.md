---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true

---

I'm co-organizing an open invited track at the IFAC world congress 2026 on learning interpretable control policies. Find details and submission code [here](https://nplawrence.com/assets/misc/ifac2026_oit.pdf)!

I'm a postdoc in the [Mesbah Lab](https://www.mesbahlab.com) at UC Berkeley.
My work is driven by the need for safe algorithms and architectures for automatic decision-making. 
My recent work develops a complementary framework inspired by deep reinforcement learning and model predictive control.
These two areas are often viewed as opposites, but really they have a common core in dynamic programming and Markov decision processes.
Essentially, RL represents one branch that solves decision-making tasks through trial and error and function approximators, while MPC is another branch that is based on dynamics, constraints, and optimization.
RL has proved to be incredibly versatile but is not necessarily safe by-design; MPC puts safety and robustness at the forefront, but it can be difficult to design toward high performance.
A more unified perspective of these two areas would make RL more appealing for real-world applications while also making MPC more flexible and scalable under general learning algorithms.
Please see my recent works on RL and MPC and don't hesitate to [get in touch](mailto:{{site.author.short_name}} <{{site.author.email}}>).


{% comment %}
News
======

Upper Bound 2024 MPC tutorial: Slides and code [here](https://nplawrence.com/RL-MPC-tutorial/)

I recently completed my PhD!

We are organizing a half-day workshop at AdCONIP 2022 on reinforcement learning to be held on August 7th 2022. Further details on the [conference webpage](https://adconip2022.org/workshops/#workshop-2-making-reinforcement-learning-a-practical-technology-for-industrial-control).
{% endcomment %}

Publications
======

Most of my papers are linked to arXiv or a DOI. {% if site.author.googlescholar %} You can also find my articles on my [Google Scholar profile]({{site.author.googlescholar}}).
{% endif %}

{% include pub_list.html %}
