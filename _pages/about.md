---
layout: page
title: About Me
permalink: /about/
references:
  - name: Nadia Wallace
    title: Senior Engineering Manager @ Synthego
    linkedin: https://www.linkedin.com/in/wallacenadia
    photo: https://i.imgur.com/e9qHcbp.jpg
    reference: >
      Adithya quickly made an impact on our team at Synthego. I was immediately
      impressed with his ability to dive into multiple large codebases of
      varying technologies (React, Django, gRPC) and quickly get up to speed.
      Over the course of the summer, he delivered production-ready softwares
      features to increase efficiencies in our laboratories. Adithya was
      especially dedicated to not only helping internal users go faster, but to
      making developers' lives easier as well. He was self-motivated and took
      the initiative to modernize our Python tooling and implemented pre-commit
      hooks, auto-formatting using Black, and auto-documentation using Sphinx.
      It was an absolute pleasure having Adithya on our team!
  - name: Madalin Mihailescu
    title: Head of R&D @ Georgian
    linkedin: https://www.linkedin.com/in/madalinmihailescu
    photo: https://pbs.twimg.com/profile_images/1286297982527102977/awlAnsTl_400x400.jpg
    reference: >
      Adithya has been a member of our Impact team for the past year. He came
      highly recommended by Carl Ryden, CEO at PrecisionLender, one of our
      portfolio companies. Smart, ambitious, hard-working, resourceful, Adithya
      hit the ground running when he joined us, quickly became an integral
      member of our team, and has exceeded the high expectations set by Carl.
      He's been driving our efforts in the area of AutoML, by doing market
      research, writing technical reports, blog posts, and giving presentations
      on the topic, and by being a core engineer on Foreshadow, our AutoML
      software platform. He's a pleasure to work with.
  - name: Carl Ryden
    title: CEO @ PrecisionLender
    linkedin: https://www.linkedin.com/in/caryden
    photo: https://pbs.twimg.com/profile_images/1383769110/20aacb3_400x400.jpg
    reference: >
      I first met Adithya though the Entrepreneurship class that I teach at
      NCSSM. Adithya was a student in that class and was truly a joy to teach. I
      also had the pleasure of watching him lead the FIRST Robotics Competition
      team 900 all the way to the World Championships in Houston. I asked
      Adithya to join us as an intern here at PrecisionLender. He was nothing
      short of amazing. He helped us prototype a natural language processing
      microservice in Azure Service Fabric that is currently in our production
      environment today.
---

## Bio

![](https://i.imgur.com/m5cwmQy.png){:style="float: left; margin-right: 1.5em"
height="30%" width="30%"}

I went to grad school at [Carnegie Mellon University][CMU] and received a
[Computer Science][CSD] Master's Degree. In undergrad, I double majored in
[Electrical Engineering and Computer Engineering][ECE]
at [NC State University][NCSU].

I've previously worked as a Software Engineering Intern for [Microsoft] on their
Quantum System team, [Synthego][SYNTH] as a Software Engineering Intern through
the [8vc fellowship][8VC], for
[Georgian Partners][GP] as a Data Science Intern, for the
[Oklahoma City Thunder][OKC] as a Data Science Intern, for the
[NC State CS Department][NCSUCS] as a Research Assistant, for
[Precision Lender][PL] as a Software Engineering Intern.

## References

[comment]: <> (Box is from: https://primer.style/css/)
<details>
    <summary class="pb-3">Show References</summary>
    {% for ref in page.references %}
    <div class="mb-2">
    <div class="Box box-shadow-medium rounded-3 col-12">
        {%- if ref.photo -%}
        <div class="col-4 col-sm-2 d-table-cell v-align-middle p-3">
            <img class="ref-image" src="{{ ref.photo }}" />
          </div>
        {%- endif -%}
        <div class="col-8 col-sm-10 d-table-cell pb-3 pr-3">
            <h3>
              <a class="post-link" href="{{ ref.linkedin }}">
                {{ ref.name }}
              </a>
            </h3>
            <p class="ref-job-title">{{ ref.title }}</p>
            <p class="ref-description">{{ ref.reference }}</p>
          </div>
    </div>
    </div>
    {% endfor %}
</details>

<!-- Links -->

[CMU]: https://www.cmu.edu/ "Carnegie Mellon University"

[CSD]: https://www.csd.cs.cmu.edu/ "CS Department @ CMU"

[NCSU]: https://www.ncsu.edu/ "NC State University"

[ECE]: https://www.ece.ncsu.edu/ "ECE Department @ NC State"

[Microsoft]: https://azure.microsoft.com/en-us/solutions/quantum-computing/ "Microsoft Quantum"

[SYNTH]: https://www.synthego.com "Synthego"

[8VC]: https://8vc.com/ "8VC"

[GP]: https://www.georgianpartners.com "Georgian Partners"

[OKC]: https://www.nba.com/thunder/ "OKC Thunder"

[NCSUCS]: https://www.csc.ncsu.edu/ "CS Department @ NC State"

[PL]: https://precisionlender.com/ "Precision Lender"
